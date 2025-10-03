"""Deutsche Post Internetmarke REST API client.

Deutsche Post released its `Internetmarke REST API`_ in September, 2024, as a successor to its
Internetmarke `SOAP API`_, which it deprecated in August, 2024 and announced to
turn it off at the end of 2025.

.. _SOAP API: https://developer.dhl.com/sites/default/files/2023-08/quick-Guide%20INTERNETMARKE.pdf

For sending postage requests to Deutsche Post a :class:`Session` object is required.
The body parameter that is necessary for some requests can be constructed with the
``mk_*`` functions.

For the actual checkout the total price need to be supplied and the checkout only succeeds
if your local computation matches the remote one. See also the :func:`calc_total` and :func:`compute_total` helper functions.

Example
-------

The following snippets buys a registered mail postage PDF label that can be directly printed to a C6 envelope::

    import inema.rest as ir

    im   = ir.Session('some client id', 'some client secret',
               'some portokasse user', 'some portokasse password')
    oid  = im.create_order()
    p    = ir.mk_pdf_pos(1002,
               sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
               receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    t    = ir.calc_total(p)
    body = ir.mk_pdf_req(oid, 5, p, t)
    d    = im.checkout_pdf(body, 'postage.pdf')

Alternatively, it's also possible to check out a list of label positions, e.g.
to create multiple pages or when printing multiple labels in columns and rows to one page.


Note
----

The new `Internetmarke REST API`_ is structured quite similarly to the previous SOAP API.
On the one hand this might simplify migration, because the workflow
is basically the same, but on the other hand the REST API aguably is non-idiomatic
and contains too many surprises such that it's harder to adopt than necessary.

Hint
----
    This package contains default Deutsche Post prices, but some customers may have discounts in place.

Important
---------
   A fresh 'Portokasse' needs to allow-list the 'application' that is identified by the client id.
   This can be accomplished most easily by a first session login attempt that will fail,
   but also trigger an authorization request that can be acknowledged in the 'Portokasse' account web UI,
   after the fact.

Error
-----

This module uses the requests package for all HTTP requests.
Consequently, REST API HTTP error status codes are reported via raised
``requests.exceptions.HTTPError`` exceptions.
When caught, the remote error may be obtained like this::

    try:
        Session im(client, secret, user, password)
        // some requests, checkout, whatever ...
    except requests.exceptions.HTTPError as e:
        d = e.response.json()
        print(f'Remote errror: {d}')

Examples of such an error::

    {'statusCode': '400',
     'title': 'Bad Request',
     'description': 'positions[4].position.labelX: must be greater than or equal to 1',
     'instance': 'PCF-A1033'}

Another error example::

    {'statusCode': '400',
     'title': 'invalidTotalAmount',
     'description': 'The total amount of the order is invalid! Reason: The total cost of the shopping cart is invalid! PPL-total: 415, Cart: 1',
     'instance': 'PCF-A1031'}


.. _Internetmarke REST API:
   https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany

"""


# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: © 2025 Georg Sauthoff <mail@gms.tf>


import enum
from decimal import Decimal
import io
import requests

from .data import products as default_products



class Layout(enum.StrEnum):
    ADDRESS_ZONE  = 'ADDRESS_ZONE'
    FRANKING_ZONE = 'FRANKING_ZONE'



def mk_addr(name, line, postcode, city, country='DEU', header=None, line2=None):
    """Create address for postage label position object.

    The result of this function can be used to supply the sender and receivers parameters
    of the :func:`mk_pdf_pos` and :func:`mk_png_pos` functions.

    .. _ISO 3166-1 alpha-3:
       https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3

    Parameters
    ----------
    name : str
        First name and last name, company name or something like that.
    line : str
        Street and housenumber or postbox.
        NB: It's required to be non-empty even though there are some real world postal addresses
        where only name, postcode and city are specified.
    postcode : str
        Postleitzahl
    country : str, default: 'DEU'
        `ISO 3166-1 alpha-3`_ three-letter country code.
        NB: when the DEU default is used the remote service leaves the country line blank.
    header : str, optional
        Another line above the name field, e.g. put company here and department or person in the name field then.
    line2 : str, optional
        Another line below the line field.

    Returns
    -------
    dict
        Dictionary that conforms to the inema Address schema.
    """
    d = {
        'name'         : name,
        'addressLine1' : line,
        'postalCode'   : str(postcode),
        'city'         : city,
        'country'      : country
    }
    if header is not None:
        d['additionalName'] = header
    if line2  is not None:
        d['addressLine2']   = line2
    return d


def mk_pdf_pos(product_code, column=1, row=1, page=1, layout='ADDRESS_ZONE', sender=None, receiver=None):
    """Create a postage PDF label position.

    The result (or a list of such results) can be used as a parameter of a :func:`mk_png_req` call.

    Address information is optional, but if supplied both sender and receiver need to be supplied.

    Parameters
    ----------
    product_code: int
        Product identifier from the Deutsche Post price list.
        See also :attr:`inema.data.products` or `data/products.json` or the Deutsche Post products webservice.
    column : int, default: 1
        when buying multiple positions and the format has multiple columns.
        one-based indexing
    row : int, default: 1
        when buying multiple positions and the format has multiple rows.
        one-based indexing
    page : int, default: 1
        when buying multiple positions and not all fit on one page.
        one-based indexing
    layout: { 'ADDRESS_ZONE', 'FRANKING_ZONE' }, default: 'ADDRESS_ZONE'
        use the default when you supply sender and receiver and FRANKING_ZONE when not.
        The default layout also works without sender and receiver,
        but FRANKING_ZONE is less crammed then.
    sender: dict
        Sender address information, created by :func:`mk_addr`.
    receiver: dict
        Receiver address information, created by :func:`mk_addr`.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPDFPosition schema.

    Raises
    ------
    ValueError
        In case a parameter violates the schema in an obvious way.
    KeyError
        Invalid layout parameter.
    """
    layout = str(Layout[layout])
    d = {
        'positionType'  : 'AppShoppingCartPDFPosition',
        'position': {
            'labelX'    : int(column),
            'labelY'    : int(row),
            'page'      : int(page)
        },
        'productCode'   : int(product_code),
        'voucherLayout' : layout
    }
    if sender is not None:
        if receiver is None:
            raise ValueError('incomplete address')
        d['address'] = {
            'sender'   : sender,
            'receiver' : receiver
        }
    elif sender is None and receiver is not None:
        raise ValueError('incomplete address')
    if column < 1 or row < 1 or page < 1:
        raise ValueError('value violated one-based indexing')
    return d


def mk_png_pos(product_code, layout='ADDRESS_ZONE', sender=None, receiver=None):
    """Create a postage PNG label position.

    The result (or a list of such results) can be used as a parameter of a :func:`mk_png_req` call.

    Address information is optional, but if supplied both sender and receiver need to be supplied.

    Parameters
    ----------
    product_code: int
        Product identifier from the Deutsche Post price list.
        See also :attr:`inema.data.products` or `data/products.json` or the Deutsche Post products webservice.
    layout: { 'ADDRESS_ZONE', 'FRANKING_ZONE' }, default: 'ADDRESS_ZONE'
        use the default when you supply sender and receiver and FRANKING_ZONE when not.
        The default layout also works without sender and receiver,
        but FRANKING_ZONE is less crammed then.
    sender: dict
        Sender address information, created by :func:`mk_addr`.
    receiver: dict
        Receiver address information, created by :func:`mk_addr`.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPosition schema.

    Raises
    ------
    ValueError
        In case a parameter violates the schema in an obvious way.
    KeyError
        Invalid layout parameter.
    """
    layout = str(Layout[layout])
    d = {
        'positionType'  : 'AppShoppingCartPosition',
        'productCode'   : product_code,
        'voucherLayout' : layout
    }
    if sender is not None:
        if receiver is None:
            raise ValueError('incomplete address')
        d['address'] = {
            'sender'   : sender,
            'receiver' : receiver
        }
    return d


def mk_pdf_req(order_id, format_id, positions, total, manifest=False):
    """
    Create PDF checkout request.

    The result can be used as body parameter of a :meth:`Session.checkout_pdf` call.

    Parameters
    ----------
    order_id : str
        Order ID returned by a previous :meth:`Session.create_order` call.
        Each request requires a fresh order ID.
    format_id: int
        Page format ID.
        See also :attr:`inema.data.formats` or `data/formats.json`
    positions: list or object
        Value or list of values created by :func:`mk_pdf_pos`.
    total: integer
        Total monetary amount of all positions. See also :func:`calc_total` and :func:`compute_total`
        for a helper.
    manifest: bool, default: False
        Also request manifest link.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPDFRequest schema.

    Raises
    ------
    ValueError
        In case a parameter violates the schema in an obvious way.
    """
    if type(positions) is not list:
        positions = [ positions ]
    for p in positions:
        if p['positionType'] != 'AppShoppingCartPDFPosition':
            raise ValueError('pdf request only allows pdf positions')
    d = {
        'type'         : 'AppShoppingCartPDFRequest',
        'shopOrderId'  : str(order_id),
        'pageFormatId' : int(format_id),
        'positions'    : positions,
        'total'        : int(total)
    }
    if manifest:
        d['createManifest'] = True
    return d


def mk_png_req(order_id, positions, total, manifest=False):
    """
    Create PNG checkout request.

    The result can be used as body parameter of a :meth:`Session.checkout_png` call.

    Parameters
    ----------
    order_id : str
        Order ID returned by a previous :meth:`Session.create_order` call.
    positions: list or object
        Value or list of values created by :func:`mk_pdf_pos`.
    total: integer
        Total monetary amount of all positions. See also :func:`calc_total` and :func:`compute_total`
        for a helper.
    manifest: bool, default: False
        Also request manifest link.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPNGRequest schema.

    Raises
    ------
    ValueError
        In case a parameter violates the schema in an obvious way.
    """
    if type(positions) is not list:
        positions = [ positions ]
    for p in positions:
        if p['positionType'] != 'AppShoppingCartPosition':
            raise ValueError('pdf request only allows pdf positions')
    d = {
        'type'        : 'AppShoppingCartPNGRequest',
        'shopOrderId' : str(order_id),
        'positions'   : positions,
        'total'       : int(total)
    }
    if manifest:
        d['createManifest'] = True
    return d


def mk_cancel_req(order_id=None, vouchers=None):
    """Create postage cancellation request.

    Parameters
    ----------
    order_id: str, optional
        Order ID used in a previous :meth:`Session.checkout_pdf` or :meth:`Session.checkout_png` call.
    vouchers: list, optional
        List of voucher ID prevously returned by :meth:`Session.checkout_pdf` or :meth:`Session.checkout_png` call
        or as read from the labels.
        Alternatively, list of pairs of voucher and tracking IDs.

    Returns
    -------
    dict
        Dictionary that conforms to the inema RetoureVouchersRequest schema.

    Raises
    ------
    ValueError
        In case a parameter violates the schema in an obvious way.
    """
    if order_id is None and vouchers is None:
        raise ValueError('you have to specify at least one order id or voucher')
    d = {
        'shoppingCart': { }
    }
    if order_id is not None:
        d['shoppingCart']['shopOrderId'] = str(order_id)

    def f(v):
        match v:
            case a, b:
                return { 'voucherId': a, 'trackId': b }
            case a:
                return { 'voucherId': a }

    if vouchers is not None:
        if type(vouchers) is not list:
            vouchers = [ vouchers ]
        d['shoppingCart']['voucherList'] = [ f(v) for v in vouchers ]
    if 'voucherList' in d['shoppingCart'] and len(d['shoppingCart']['voucherList']) == 0:
        raise ValueError('voucher list must not be empty')
    return d


def mk_pdf_preview_req(format_id, product_code, layout='ADDRESS_ZONE'):
    """Create PDF preview label request.

    The result can be used as body parameter to a :meth:`Session.preview_pdf` call.

    Note that the preview doesn't include any address information and thus is only
    useful for checking the placement of the QR code.

    Parameters
    ----------
    format_id : int
        Page format ID.
        See also :attr:`inema.data.formats` or `data/formats.json`
    product_code: int
        Product identifier from the Deutsche Post price list.
        See also :attr:`inema.data.products` or `data/products.json` or the Deutsche Post products webservice.
    layout: { 'ADDRESS_ZONE', 'FRANKING_ZONE' }, default: 'ADDRESS_ZONE'
        use the default when you supply sender and receiver and FRANKING_ZONE when not.
        The default layout also works without sender and receiver,
        but FRANKING_ZONE is less crammed then.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPreviewPDFRequest schema.

    Raises
    ------
    KeyError
        Invalid layout parameter.
    """
    layout = str(Layout[layout])
    d = {
        'type'          : 'AppShoppingCartPreviewPDFRequest',
        'pageFormatId'  : int(format_id),
        'productCode'   : int(product_code),
        'voucherLayout' : layout
    }
    return d


def mk_png_preview_req(product_code, layout='ADDRESS_ZONE'):
    """Create PNG preview label request.

    The result can be used as body parameter to a :meth:`Session.preview_png` call.

    Note that the preview doesn't include any address information and thus is only
    useful for checking the placement of the QR code.

    Parameters
    ----------
    product_code: int
        Product identifier from the Deutsche Post price list.
        See also :attr:`inema.data.products` or `data/products.json` or the Deutsche Post products webservice.
    layout: { 'ADDRESS_ZONE', 'FRANKING_ZONE' }, default: 'ADDRESS_ZONE'
        use the default when you supply sender and receiver and FRANKING_ZONE when not.
        The default layout also works without sender and receiver,
        but FRANKING_ZONE is less crammed then.

    Returns
    -------
    dict
        Dictionary that conforms to the inema AppShoppingCartPreviewPDFRequest schema.

    Raises
    ------
    KeyError
        Invalid layout parameter.
    """
    layout = str(Layout[layout])
    d = {
        'type'          : 'AppShoppingCartPreviewPNGRequest',
        'productCode'   : int(product_code),
        'voucherLayout' : layout
    }
    return d



def check_health(api_base = 'https://api-eu.dhl.com/post/de/shipping/im/v1/'):
    """Check the availability and version of the Deutsche Post INTERNETMARKE REST API endpoint.

    NB: doesn't require a session login.

    Example
    -------
    >>> check_health()
    {'name'    : 'pp-post-internetmarke',
     'version' : 'v1.1.18',
     'rev'     : '35',
     'env'     : 'prod-eu'}
    """
    r = requests.get(api_base)
    r.raise_for_status()
    d = r.json()
    return d['amp']



class Session:
    """Internetmarke REST API Connection class.

    An object of this class primarily wraps the requests http session (`ses`),
    the bearer token obtained after authorization (`token`) and the current
    balance of the user's Portokasse wallet (`balance`).

    The constructor authorises to Internetmarke REST API endpoint.

    Parameters
    ----------
    client : str
        Client ID, a.k.a. the API key credential of your 'Post DE
        Internetmarke (Post & Parcel Germany)' API application that is
        registered in your developer.dhl.com user account.
    secret : str
        Client secret, a.k.a. the API Secret credential of yoru 'Post DE
        Internetmarke (Post & Parcel Germany)' API application that is
        registered in your developer.dhl.com user account.
    user: str
        username of your portokasse.deutschepost.de Portokasse account
    password: str
        password of your portokasse.deutschepost.de Portokasse account

    Raises
    ------
    requests.exceptions.HTTPError
        In case API endpoint responds with an error.

    Example
    -------
    >>> im = Session im(client, secret, user, password)
    >>> im.auth_resp
    {'userToken'              : 'seCreTbeArer=',
     'access_token'           : 'seCreTbeArer=',
     'walletBalance'          : 3285,
     'showTermsAndConditions' : False,
     'infoMessage'            : '',
     'issued_at'              : 'Sun, 14 Sep 2025 14:15:18 GMT',
     'expires_in'             : 86400,
     'token_type'             : 'BearerToken',
     'external_customer_id'   : 'juser-0815',
     'authenticated_user'     : 'myportokasse@example.org'}
    >>> im.balance
    3285
    >>> im.api_base
    'https://api-eu.dhl.com/post/de/shipping/im/v1/'
    >>> type(im.ses)
    requests.sessions.Session
    """


    def __init__(self, client, secret, user, password, api_base = 'https://api-eu.dhl.com/post/de/shipping/im/v1/'):
        ses = requests.Session()
        ses.headers.update({'User-Agent': 'python-requests/python-inema'})
        r = ses.post(api_base + 'user',
                 data={
                     'grant_type'   : 'client_credentials',
                     'client_id'    : client,
                     'client_secret': secret,
                     'username'     : user,
                     'password'     : password,
                     }
                )
        r.raise_for_status()
        d     = r.json()
        token = d['access_token']
        ses.headers.update({ 'Authorization': f'Bearer {token}' })
        self.api_base  = api_base
        self.ses       = ses
        self.auth_resp = d
        self.balance   = d['walletBalance']


    def profile(self):
        """Request your Portokasse profile fields.

        Example
        -------
        >>> im.profile()
        {'ekp'              : None,
         'company'          : 'ACME Inc',
         'title'            : 'Dr.',
         'invoiceType'      : 'PAPER',
         'invoiceFrequency' : 'DECADE',
         'mail'             : 'myportokasse@example.org',
         'firstname'        : 'Erika',
         'lastname'         : 'Mustermann',
         'street'           : 'Heidestr.',
         'houseNo'          : '17',
         'zip'              : '51147',
         'city'             : 'Köln',
         'country'          : 'DEU',
         'phone'            : None,
         'pobox'            : None,
         'poboxZip'         : None,
         'poboxCity'        : None}

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.
        """
        r = self.ses.get(self.api_base + 'user/profile')
        r.raise_for_status()
        d = r.json()
        return d


    def create_order(self):
        """Initialize new order.

        Returns new order ID that is required e.g. for building the body
        of :meth:`checkout_pdf` or :meth:`checkout_png`.

        Returns
        -------
        str
            New order ID

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.
        """
        r = self.ses.post(self.api_base + 'app/shoppingcart')
        r.raise_for_status()
        d = r.json()
        order_id = d['shopOrderId']
        return order_id


    def list_order(self, order_id):
        """Request a checked out order.

        Parameters
        ----------
        order_id: str
            Order ID used in a previous :meth:`checkout_pdf` or :meth:`checkout_png` call.

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.
            Example: When order ID wasn't used to checkout something, yet.

        Example
        -------
        >>> im.list_order(123456)
        {'type'           : 'CheckoutShoppingCartAppResponse',
         'link'           : 'https: //internetmarke.deutschepost.de/PcfExtensionWeb/document?keyphase=1&data=blAHblAh%3D',
         'manifestLink'   : None,
         'shoppingCart'   : {'shopOrderId': '123456',
          'voucherList'   : [{'voucherId': 'A00002300A0000000815', 'trackId': None}]},
         'walletBallance' : None}
        """
        r = self.ses.get(self.api_base + f'app/shoppingcart/{order_id}')
        r.raise_for_status()
        d = r.json()
        return d


    def download(self, src, filename):
        """Download convenience function.

        Downloads through the wrapped requests session,
        while not wasting too much memory in case the downloaded file is very large.

        Parameters
        ----------
        src: str
            source URL
        filename: str or path_like
            target filename

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.
        """
        with self.ses.get(src, stream=True) as x:
            x.raise_for_status()
            with open(filename, 'wb') as f:
                for bs in x.iter_content(chunk_size=128 * 1024):
                    f.write(bs)


    def checkout_pdf(self, body, filename=None):
        """Buy PDF labels.

        Parameters
        ----------
        body: dict
            Request body, usually created with :func:`mk_pdf_req`.
        filename: str or path_like, optional
            Filename for convenience.
            If not specified, the PDF can alternatively be retrieved from the URL
            returned in the 'link' field, e.g. using the requests session available
            via the `ses` object property.

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        Example
        -------
        >>> im.checkout_pdf(body_with_4_positions, 'labels.pdf')
        {'type': 'CheckoutShoppingCartAppResponse',
         'link': 'https://internetmarke.deutschepost.de/PcfExtensionWeb/document?keyphase=1&data=rANdOMdaTaString%3D',
         'manifestLink': None,
         'shoppingCart': {'shopOrderId': '123456789',
             'voucherList': [{'voucherId': 'A00002300A0000000123', 'trackId': None},
                 {'voucherId': 'A00002300A0000000122', 'trackId': None},
                 {'voucherId': 'A00002300A0000000121', 'trackId': None},
                 {'voucherId': 'A00002300A0000000120', 'trackId': None}]},
         'walletBallance': 4205}
        """
        r = self.ses.post(self.api_base + 'app/shoppingcart/pdf', json=body)
        r.raise_for_status()
        d = r.json()
        if 'walletBallance' in d:
            self.balance = d['walletBallance']
        if filename is not None:
            self.download(d['link'], filename)
        return d


    def checkout_png(self, body, filename=None):
        """Buy PNG labels.

        Parameters
        ----------
        body: dict
            Request body, usually created with :func:`mk_png_req`.
        filename: str or path_like, optional
            Filename for convenience.
            NB: The Internetmarke API endpoint always returns PNG labels as ZIP archive,
            i.e. even when just requesting a single label.
            If not specified, the ZIP result can alternatively be retrieved from the URL
            returned in the 'link' field, e.g. using the requests session available
            via the `ses` object property.

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        """
        r = self.ses.post(self.api_base + 'app/shoppingcart/png', json=body)
        r.raise_for_status()
        d = r.json()
        if 'walletBallance' in d:
            self.balance = d['walletBallance']
        if filename is not None:
            self.download(d['link'], filename)
        return d


    def cancel(self, body):
        """Request cancellation of previously checked out postage.

        Parameters
        ----------
        body: dict
            Request body, usually created with :func:`mk_cancel_req`.

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        Example
        -------
        >>> im.cancel(mk_cancel_req(oid))
        { 'shopRetoureId': '123456789', 'retoureTransactionId': '23230815' }
        """
        r = self.ses.post(self.api_base + f'app/retoure', json=body)
        r.raise_for_status()
        d = r.json()
        return d


    def list_cancel(self, retoure_id=None, transaction_id=None, start=None, end=None):
        """Request status of previously requested cancellations.

        Parameters
        ----------
        retoure_id: str, optional
            shopRetoureId field previously returned by a :meth:`cancel` call
        transaction_id: int, optional
            retoureTransactionId field previously returned by a :meth:`cancel` call
        start: str, optional
            start of query period in ISO 8601 datetime format with ``T`` delimiter and without timezone
        end: str, optional
            end of query period in ISO 8601 datetime format with ``T`` delimiter and without timezone

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        Example
        -------
        >>> im.list_cancel(start='2025-09-13T23:45:00')
        [{'retoureTransactionId' : 1234,
          'shopRetoureId'        : '5678',
          'totalCount'           : 1,
          'countStillOpen'       : 0,
          'retourePrice'         : 415,
          'creationDate'         : '14092025-143423',
          'serialnumber'         : 'A00230007A',
          'refundedVouchers'     : [{'voucherId': 'A00230007A000000042C', 'trackId': None}],
          'notRefundedVouchers'  : []},
         {'retoureTransactionId' : 1233,
          'shopRetoureId'        : '5677',
          'totalCount'           : 1,
          'countStillOpen'       : 0,
          'retourePrice'         : 215,
          'creationDate'         : '14092025-142407',
          'serialnumber'         : 'A00230009A',
          'refundedVouchers'     : [{'voucherId': 'A00230009A000000023F', 'trackId': None}],
          'notRefundedVouchers'  : []}]
        """
        ps = {}
        if retoure_id is not None:
            ps['shopRetoureId'] = str(retoure_id)
        if transaction_id is not None:
            ps['retoureTransactionId'] = int(transaction_id)
        if start is not None:
            ps['startDate'] = start
        if end is not None:
            ps['endDate'] = end
        r = self.ses.get(self.api_base + f'app/retoure', params=ps)
        r.raise_for_status()
        d = r.json()
        d = d['RetrieveRetoureStateResponse']
        return d


    def preview_pdf(self, body, filename=None):
        """Request preview PDF.

        Note that Deutsche Post doesn't support previews with addresses.
        Thus, such previews are only got for testing the QR code placement.

        Parameters
        ----------
        body: dict
            Request body, usually created with :func:`mk_pdf_preview_req`
        filename: str or path_like, optional
            Filename for convenience.
            If not specified, the PDF can alternatively be retrieved from the URL
            returned in the 'link' field, e.g. using the requests session available
            via the `ses` object property.

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        Example
        -------
        >>> im.preview_pdf(mk_pdf_preview_req(5, 1), 'letter.pdf')
        {'link': 'https://internetmarke.deutschepost.de/PcfExtensionWeb/preview?keyphase=1&data=ranDodmsTringDaTA'}
        """
        r = self.ses.post(self.api_base + 'app/shoppingcart/pdf', params={ 'validate': True }, json=body)
        r.raise_for_status()
        d = r.json()
        if filename is not None:
            self.download(d['link'], filename)
        return d


    def preview_png(self, body, filename=None):
        """Request preview PNG.

        Note that Deutsche Post doesn't support previews with addresses.
        Thus, such previews are only got for testing the QR code placement.

        NB: In contrast to :meth:`checkout_png` the API endpoint returns
        the preview directly as PNG and _not_ inside a ZIP archive.

        Parameters
        ----------
        body: dict
            Request body, usually created with :func:`mk_png_preview_req`
        filename: str or path_like, optional
            Filename for convenience.
            If not specified, the PNG can alternatively be retrieved from the URL
            returned in the 'link' field, e.g. using the requests session available
            via the `ses` object property.

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.
        """
        r = self.ses.post(self.api_base + 'app/shoppingcart/png', params={ 'validate': True }, json=body)
        r.raise_for_status()
        d = r.json()
        if filename is not None:
            self.download(d['link'], filename)
        return d


    def charge(self, cent):
        """Top up the Portokasse.

        Parameters
        ----------
        cent: int
            monetary amount to transfer to your 'Portokasse' in euro cent units

        Returns
        -------
        dict
            Response fields

        Raises
        ------
        requests.exceptions.HTTPError
            In case API endpoint responds with an error.

        Example
        -------
        Top up the wallet (Portokasse) with 7 €, at a balance of 85.05 €:

        >>> im.charge(700)
        {'shopOrderId': '123456', 'walletBalance': 9205}
        >>> im.balance
        9205

        """
        r = self.ses.put(self.api_base + 'app/wallet', params={ 'amount': int(cent) })
        r.raise_for_status()
        d = r.json()
        self.balance = d['walletBalance']
        return d


    def get_formats(self):
        """Query format catalogue.

        See Also
        --------
        :attr:`inema.data.formats` : or `data/formats.json` for a cached version of that data.
        :func:`formats2json` : helper to write the result as json
        :func:`formats2json` : write result in a more compact and normalized CSV format

        See also :func:`

        Returns
        -------
        list
            List of format dictionaries.

        Example
        -------
        >>> xs = im.get_formats()
        >>> xs[0]
        {'id'                : 1,
         'isAddressPossible' : True,
         'isImagePossible'   : False,
         'name'              : 'DIN A4 Normalpapier',
         'description'       : None,
         'pageType'          : 'REGULARPAGE',
         'pageLayout'        : {'size': {'x': 210, 'y': 297},
             'orientation'   : 'PORTRAIT',
             'labelSpacing'  : {'x': 0, 'y': 0},
             'labelCount'    : {'labelX': 2, 'labelY': 5},
             'margin'        : {'top': 31, 'bottom': 31, 'left': 15, 'right': 15}}}
        """
        r = self.ses.get(self.api_base + 'app/catalog', params={ 'types': 'PAGE_FORMATS'} )
        r.raise_for_status()
        def f(x):
            if x.endswith('.0'):
                return int(x[:-2])
            else:
                raise ValueError('unexpected real float')
        d = r.json(parse_float=f)
        fs = d['pageFormats']
        fs.sort(key=lambda f : f['id'])
        return fs



def compute_total(positions, im, pid2price=None):
    """Compute total of a positions based on prices available online.

    NB: This function requires and imports the pdfminer package.

    Parameters
    ----------
    positions : list or dict or int
       Single product code or list of them, either as raw int or dictonary with ``productCode`` key.
    im : Session
       :class:`Session` object for querying the prices.
    pid2price : dict, optional
       Dictionary to cache product prices for the current and future invocations.

    Returns
    -------
    int
        The monetary sum of all positions in euro cent.
    """
    import pdfminer.high_level
    if type(positions) is not list:
        positions = [ positions ]
    if pid2price is None:
        h = {}
    else:
        h = pid2price
    total = 0
    for p in positions:
        if type(p) is dict:
            pc = p['productCode']
        else:
            pc = p
        if  pc in h:
            total += h[pc]
            continue
        d = im.preview_pdf(mk_pdf_preview_req(5, pc))
        r = im.ses.get(d['link'])
        r.raise_for_status()
        f = io.BytesIO(r.content)
        s = pdfminer.high_level.extract_text(f)
        l = next(l for l in s.splitlines() if l.startswith('IM'))
        xs = l.split()
        t = xs[-1]
        if ',' not in t:
                raise ValueError('cannot find comma')
        t = t.replace(',', '.')
        c = Decimal(t) * Decimal('100')
        total += int(c)
        h[pc]  = int(c)
    return total


def calc_total(positions, products=default_products):
    """Compute total of a positions based on a price dictionary.

    Parameters
    ----------
    positions : list or dict or int
       Single product code or list of them, either as raw int or dictonary with ``productCode`` key.
    products : dict
       Dictionary that maps product code strings to dictionaries that contain the price at the `cost_price` key.
       See :attr:`data.products` for the default prices.

    Returns
    -------
    int
        The monetary sum of all positions in euro cent.
    """
    if type(positions) is not list:
        positions = [ positions ]
    total = 0
    for p in positions:
        if type(p) is dict:
            pc = p['productCode']
        else:
            pc = p
        t = products[str(pc)]['cost_price']
        c = Decimal(t) * Decimal('100')
        total += int(c)
    return total


def formats2json(formats, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(formats, f, ensure_ascii=False, indent=2)


def formats2csv(formats, filename):
    import pandas as pd
    df = pd.json_normalize(fs)
    df.set_index('id', inplace=True)
    df.rename(columns={
        'isAddressPossible'            : 'addr_space',
        'isImagePossible'              : 'img_space',
        'pageType'                     : 'ptype',
        'pageLayout.size.x'            : 'width',
        'pageLayout.size.y'            : 'height',
        'pageLayout.orientation'       : 'orientation',
        'pageLayout.labelSpacing.x'    : 'hpadding',
        'pageLayout.labelSpacing.y'    : 'vpadding',
        'pageLayout.labelCount.labelX' : 'hcount',
        'pageLayout.labelCount.labelY' : 'vcount',
        'pageLayout.margin.top'        : 'tmargin',
        'pageLayout.margin.bottom'     : 'bmargin',
        'pageLayout.margin.left'       : 'lmargin',
        'pageLayout.margin.right'      : 'rmargin',
    }, inplace=True)
    df.to_csv(filename)


