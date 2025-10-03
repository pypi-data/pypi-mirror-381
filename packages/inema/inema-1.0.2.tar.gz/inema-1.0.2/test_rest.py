#!/usr/bin/env python3


# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: © 2025 Georg Sauthoff <mail@gms.tf>


from decimal import Decimal
import magic
import pdfminer.high_level as pmhl
import pytest
import requests
import tomllib
import zipfile


import inema.rest as ir


@pytest.fixture(scope='session')
def im():
    with open('test.toml', 'rb') as f:
        d = tomllib.load(f)
    a = d['account']
    im = ir.Session(a['client_id'], a['client_secret'], a['user'], a['password'])
    return im


def test_health():
    d = ir.check_health()
    assert d['name'] == 'pp-post-internetmarke'
    assert d['version'][0] == 'v'
    assert 'rev' in d
    assert 'env' in d


def test_get_formats(im):
    fs = im.get_formats()
    assert len(fs) > 100
    xs = [ x for x in fs if x['id'] == 5 ]
    assert len(xs) == 1
    x = xs[0]
    assert x['name'] == 'Brief C6 114 x 162'
    assert x['pageLayout']['size']['x'] == 162


def test_user_profile(im):
    d = im.profile()
    assert 'company' in d
    assert 'firstname' in d
    assert 'lastname' in d


def test_charge(im):
    old_balance = im.balance
    d = im.charge(3000)
    assert d['walletBalance'] == im.balance
    assert old_balance + 3000 == im.balance


def test_buy_pdf(im, tmp_path):
    old_balance = im.balance

    oid = im.create_order()
    p = ir.mk_pdf_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    t = ir.compute_total(p, im)

    body = ir.mk_pdf_req(oid, 5, p, t)
    fn   = tmp_path / 'postage.pdf'
    d    = im.checkout_pdf(body, fn)

    assert d['shoppingCart']['shopOrderId'] == oid
    assert im.balance != old_balance

    s = pmhl.extract_text(fn)

    xs = s.strip().splitlines()
    assert xs[0] == 'Erika Mustermann, Heidestr. 17, 51147 Köln'
    assert xs[4].strip() == 'REINSCHREIBEN  EINWURF'
    assert xs[-3] == 'Bernd Müller'
    assert xs[-2] == 'Nußhäherstraße 10'
    assert xs[-1] == '12345 München'

    x = [ x for x in xs if x.startswith('IM ') ][0].split()[-1].replace(',', '.')
    d = int(Decimal(x) * Decimal('100'))
    assert d == old_balance - im.balance



def test_cancel(im):
    old_balance = im.balance

    oid = im.create_order()
    p = ir.mk_pdf_pos(1, layout='FRANKING_ZONE')
    t = ir.compute_total(p, im)

    body = ir.mk_pdf_req(oid, 5, [p], t)
    d    = im.checkout_pdf(body)

    delta = old_balance - im.balance
    vid = d['shoppingCart']['voucherList'][0]['voucherId']

    assert im.balance != old_balance

    assert len(d['link']) > 0

    b = im.ses.get(d['link']).content

    d = im.cancel(ir.mk_cancel_req(order_id=oid))
    rid = d['shopRetoureId']
    tid = d['retoureTransactionId']

    d = im.list_cancel(retoure_id=rid)
    assert len(d) == 1
    d = d[0]

    assert d['totalCount'] == 1
    assert d['countStillOpen'] == 0
    assert d['retourePrice'] == delta
    assert len(d['refundedVouchers']) == 1
    assert d['refundedVouchers'][0]['voucherId'] == vid



def test_buy_pdf_multi(im, tmp_path):
    old_balance = im.balance

    oid = im.create_order()
    ps = [
        ir.mk_pdf_pos(11, 1, 1, 1,
            sender=ir.mk_addr('Max Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Brot', 'Nußhäherstraße 10', '12345', 'München') ),
        ir.mk_pdf_pos(1, 2, 1, 1,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernadine Müller', 'Nußhäherstraße 10', '12345', 'München') ),
        ir.mk_pdf_pos(31, 2, 2, 1),
        ir.mk_pdf_pos(290, 1, 2, 1,
            sender=ir.mk_addr('Joe Doe', 'Heideweg 23', '12345', 'Köln'),
            receiver=ir.mk_addr('Wolfgang Göthe', 'Nußhäherstraße 10', '12345', 'München') ),
    ]
    t = ir.compute_total(ps, im)

    body = ir.mk_pdf_req(oid, 1, ps, t)
    fn   = tmp_path / 'postage.pdf'
    d    = im.checkout_pdf(body, fn)

    assert d['shoppingCart']['shopOrderId'] == oid
    # http has referer and Internetmarke has Ballance [sic] ...
    assert im.balance == d['walletBallance']
    assert im.balance != old_balance
    assert im.balance + t == old_balance
    assert len(d['shoppingCart']['voucherList']) == 4
    old_link = d['link']
    old_vl = d['shoppingCart']['voucherList']

    d = im.list_order(oid)

    assert d['shoppingCart']['shopOrderId'] == oid
    assert len(d['shoppingCart']['voucherList']) == 4
    assert d['shoppingCart']['voucherList'] == old_vl
    assert len(d['link']) > 0
    # usually new link, but same postage, wouldn't need to be different, though ...
    # assert d['link] != old_link


def test_buy_png(im, tmp_path):
    old_balance = im.balance

    oid = im.create_order()
    p = ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    t = ir.calc_total(p)

    body = ir.mk_png_req(oid, p, t)
    fn   = tmp_path / 'postage-png.zip'
    d    = im.checkout_png(body, fn)

    assert d['shoppingCart']['shopOrderId'] == oid
    assert im.balance != old_balance
    assert im.balance + t == old_balance

    m = magic.detect_from_filename(fn)
    assert m.mime_type == 'application/zip'

    z = zipfile.ZipFile(fn)
    xs = [ x.filename for x in z.infolist() ]
    assert xs == [ '0.png' ]


def test_buy_png_multi(im, tmp_path):
    old_balance = im.balance

    oid = im.create_order()
    ps = [
        ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')),
        ir.mk_png_pos(1002,
            sender=ir.mk_addr('Peter Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Petra Müller', 'Nußhäherstraße 10', '12345', 'München')),
    ]
    h = {}
    t = ir.compute_total(ps, im, h)

    assert len(h) == 2
    assert 1022 in h
    assert 1002 in h

    body = ir.mk_png_req(oid, ps, t)
    fn   = tmp_path / 'postage-png.zip'
    d    = im.checkout_png(body, fn)

    assert d['shoppingCart']['shopOrderId'] == oid
    assert im.balance != old_balance
    assert im.balance + t == old_balance

    m = magic.detect_from_filename(fn)
    assert m.mime_type == 'application/zip'

    z = zipfile.ZipFile(fn)
    xs = [ x.filename for x in z.infolist() ]
    assert xs == [ '0.png', '1.png' ]


def test_preview_png(im, tmp_path):
    fn   = tmp_path / 'postage.png'

    d = im.preview_png(ir.mk_png_preview_req(10001), fn)
    m = magic.detect_from_filename(fn)
    assert m.mime_type == 'image/png'


def test_remote_price_error(im):
    old_balance = im.balance
    oid = im.create_order()
    p = ir.mk_pdf_pos(1,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )

    total = 1
    body = ir.mk_pdf_req(oid, 1, p, total)

    with pytest.raises(requests.exceptions.HTTPError) as e:
        im.checkout_pdf(body)

    d = e.value.response.json()
    assert d['statusCode'] == '400'
    assert d['title'] == 'invalidTotalAmount'
    assert d['description'].startswith('The total amount of the order is invalid!')
    xs = d['description'].split()
    assert xs[-4] == 'PPL-total:'
    assert xs[-3] == '95,'
    assert xs[-2] == 'Cart:'
    assert xs[-1] == '1'
    assert im.balance == old_balance



def test_remote_format_error(im):
    old_balance = im.balance
    oid = im.create_order()
    p = ir.mk_pdf_pos(1,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    p['position']['labelX'] = 0

    # NB: as of 2025-09, web service doesn't check for colum/row overflow ...

    t = ir.compute_total(p, im)
    body = ir.mk_pdf_req(oid, 1, p, t)

    with pytest.raises(requests.exceptions.HTTPError) as e:
        im.checkout_pdf(body)

    d = e.value.response.json()
    assert d['statusCode'] == '400'
    assert d['title'] == 'Bad Request'
    assert im.balance == old_balance



