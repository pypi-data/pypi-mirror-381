"""Compatibility wrapper that translates Internermarke SOAP API calls to REST ones.

Use case: You have existing software that interfaces with the Deutsche Post
Internetmarke SOAP API via the :class:`inema.inema.Internetmarke` class, you
need to upgrade to the new Deutsche Post Internetmarke REST API (because the
SOAP endpoints are announced to be turned off at the end of 2025) and you want
to change your existing software as little as possible.

In the best case you just need to register for the new REST API, link your
Portokasse in Deutsche Post Web UI, update your credentials configuration and
adjust your import like this::

    from inema import Internetmarke

to something like this::

    from inema.soapfree import Internetmarke

See also `frank.py` in the python-inema repository (around 2025-09-21) for a
real world example.


Of course, depending on your existing usage, directly migrating to the new REST
API via :mod:`inema.rest` likely isn't that complicated, either.

"""

# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: © 2025 Georg Sauthoff <mail@gms.tf>


from .rest import Session, mk_addr, mk_pdf_pos, mk_png_pos, mk_pdf_req, mk_pdf_preview_req, mk_png_preview_req
from .data import products as default_products

import collections
import decimal
import io
import logging
import zipfile


log = logging.getLogger(__name__)


def translate_layout(layout):
    match layout:
        case 'AddressZone':
            layout = 'ADDRESS_ZONE'
        case 'FrankingZone':
            layout = 'FRANKING_ZONE'
    return layout


class Internetmarke:

    def __init__(self, partner_id, key, key_phase="1", products=None):
        self.partner_id = partner_id
        self.key = key
        self.positions = []
        if products is None:
            self.products = default_products
        else:
            self.products = products

    def authenticate(self, username, password):
        self.im = Session(self.partner_id, self.key, username, password)
        self.user_token =  self.im.auth_resp['access_token']
        self.wallet_balance = self.im.balance
        log.debug(f'balance: {self.wallet_balance}')

    def build_addr(self, street, house, zipcode, city, country, additional = None):
        line = f'{street} {house}'
        return (line, zipcode, city, country, additional)


    def build_pers_addr(self, first, last, address, salutation = None, title = None):
        ns = []
        if salutation is not None:
            ns.append(salutation)
        if title is not None:
            ns.append(title)
        ns.append(first)
        ns.append(last)
        name = ' '.join(ns)
        line, zipcode, city, country, additional = address
        a = mk_addr(name, line, zipcode, city, country, line2=additional)
        return a

    def build_comp_addr(self, company, address, person = None):
        if person is None:
            header = None
            name = company
        else:
            header = company
            name = person
        line, zipcode, city, country, additional = address
        a = mk_addr(name, line, zipcode, city, country, header=header, line2=additional)
        return a


    def build_position(self, product, sender=None, receiver=None, layout="AddressZone", pdf=False, x=1, y=1, page=1):
        layout = translate_layout(layout)
        if pdf:
            return mk_pdf_pos(product, x, y, page, layout=layout, sender=sender, receiver=receiver)
        else:
            return mk_png_pos(product, layout=layout, sender=sender, receiver=receiver)

    def add_position(self, position):
        self.positions.append(position)

    def clear_positions(self):
        self.positions = []

    def compute_total(self):
        total = 0
        for p in self.positions:
            total += self.get_product_price_by_id(p['productCode'])
        return total

    def get_product_price_by_id(self, ext_prod_id):
        price_str = self.products[str(ext_prod_id)]['cost_price']
        return int(decimal.Decimal(price_str) * 100)


    def checkoutPDF(self, page_format):
        oid = self.im.create_order()
        log.debug(f'new order id: {oid}')
        t = self.compute_total()
        b = mk_pdf_req(oid, page_format, self.positions, t, manifest=True)
        d = self.im.checkout_pdf(b)
        h = {}
        if d.get('link'):
            h['pdf_bin'] = self.im.ses.get(d['link']).content
        if d.get('manifestLink'):
            h['manifest_pdf_bin'] = self.im.ses.get(d['manifestLink']).content
        Tuple = collections.namedtuple('Checkout', h)
        r = Tuple(**h)
        return r

    def retrievePNGs(self, link):
        r = self.im.ses.get(link)
        z = zipfile.ZipFile(io.BytesIO(r.content))
        return [ z.read(f.filename) for f in z.infolist() ]

    def checkoutPNG(self, page_format):
        oid = self.im.create_order()
        log.debug(f'new order id: {oid}')
        t = self.compute_total()
        b = mk_png_req(oid, self.positions, t, manifest=True)
        d = self.im.checkout_png(b)
        h = {}
        w = {}
        if d.get('link'):
            pngs = self.retrievePNGs(d['link'])
            vs = []
            for png in pngs:
                w['png_bin'] = png
                Tuple = collections.namedtuple('Png', w)
                vs.append(Tuple(**w))
            w = { 'voucher': vs }
            Tuple = collections.namedtuple('Voucher', w)
            v = Tuple(**w)
            w = { 'voucherList': v }
            Tuple = collections.namedtuple('VoucherList', w)
            v = Tuple(**w)
            h['shoppingCart'] = v
        if d.get('manifestLink'):
            h['manifest_pdf_bin'] = self.im.ses.get(d['manifestLink']).content
        Tuple = collections.namedtuple('Checkout', h)
        r = Tuple(**h)
        return r

    def retrievePreviewPDF(self, prod_code, page_format, layout = "AddressZone"):
        layout = translate_layout(layout)
        d = self.im.preview_pdf(mk_pdf_preview_req(page_format, prod_code, layout=layout))
        return d['link']

    def retrievePreviewPNG(self, prod_code, layout = "AddressZone"):
        layout = translate_layout(layout)
        d = self.im.preview_png(mk_png_preview_req(prod_code, layout=layout))
        return d['link']

    def retrievePageFormats(self):
        return self.im.get_formats()



