#!/usr/bin/env python3


# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: © 2025 Georg Sauthoff <mail@gms.tf>


# This test suite validates REST requests constructed by inema.rest.Session
# against the Internetmarke Openapi specification published by Deutsche Post.
#
# It doesn't require internet access, just a copy of that spec file.
#
# See also the Downloads Section in the Internetmarke documentation:
# https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany#downloads-section


import pytest

import openapi_core
import openapi_core.contrib.requests
import requests
import responses
import yaml


import inema.rest as ir



inema_openapi_filename = 'pp-post-internetmarke-latest.yaml'
inema_url = 'http://localhost:6666/v1/'

# otherwise, openapi runs into discriminator property based referencing errors,
# during validation ...
#
# NB: an allOf-adjacent discriminator object isn't covered by the openapi spec
def fix_bogus_discrimi(y):
    for k, v in y['components']['schemas'].items():
        if 'allOf' in v and 'discriminator' in v:
            v.pop('discriminator')


@pytest.fixture(scope='session')
def oa():
    with open(inema_openapi_filename) as f:
        y = yaml.safe_load(f)
        fix_bogus_discrimi(y)
        y['servers'][0]['url'] = inema_url[:-1]
        oa = openapi_core.OpenAPI.from_dict(y)
        return oa


class Early_Exit(Exception):
    pass

class Fake_Session:
    def __init__(self, headers):
        self.headers = headers
        self.req = None

    def post(self, *xs, **kw):
        kw['headers'] = self.headers
        self.req = requests.Request('POST', *xs, **kw)
        return self

    def get(self, *xs, **kw):
        kw['headers'] = self.headers
        self.req = requests.Request('GET', *xs, **kw)
        return self

    def put(self, *xs, **kw):
        kw['headers'] = self.headers
        self.req = requests.Request('PUT', *xs, **kw)
        return self

    def raise_for_status(self):
        raise Early_Exit()

    def clear(self):
        self.req = None


@pytest.fixture(scope='session')
def im():
    with responses.RequestsMock() as r:
        base = inema_url
        r.add(responses.POST,
              base + 'user',
              body='{"access_token": "0815","walletBalance":230}',
              status=200,
              content_type='application/json',
              )
        s = ir.Session('client', 'geheim', 'juser', 'einsfueralles', api_base=base)
        s.ses = Fake_Session(s.ses.headers)
        return s


def test_user_profile(im, oa):
    im.ses.clear()
    try:
        im.profile()
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_get_format(im, oa):
    im.ses.clear()
    try:
        im.get_formats()
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_charge(im, oa):
    im.ses.clear()
    try:
        im.charge(3000)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_create_order(im, oa):
    im.ses.clear()
    try:
        im.create_order()
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_buy_pdf(im, oa):
    im.ses.clear()
    oid = 123
    p = ir.mk_pdf_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    t = 100
    body = ir.mk_pdf_req(oid, 5, p, t)
    try:
        im.checkout_pdf(body)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_cancel(im, oa):
    im.ses.clear()
    oid = 123
    d = ir.mk_cancel_req(order_id=oid)
    try:
        im.cancel(d)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_list_cancel(im, oa):
    im.ses.clear()
    rid = 123
    try:
        im.list_cancel(retoure_id=rid)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_buy_pdf_multi(im, oa):
    im.ses.clear()
    oid = 123
    t = 100
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
    body = ir.mk_pdf_req(oid, 1, ps, t)
    try:
        im.checkout_pdf(body)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_buy_png(im, oa):
    im.ses.clear()
    oid = 123
    p = ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    t = 100
    body = ir.mk_png_req(oid, p, t)
    try:
        im.checkout_png(body)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_buy_png_multi(im, oa):
    im.ses.clear()
    oid = 123
    ps = [
        ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')),
        ir.mk_png_pos(1002,
            sender=ir.mk_addr('Peter Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Petra Müller', 'Nußhäherstraße 10', '12345', 'München')),
    ]
    t = 100
    body = ir.mk_png_req(oid, ps, t)
    try:
        im.checkout_png(body)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_preview_png(im, oa):
    im.ses.clear()
    d = ir.mk_png_preview_req(10001)
    try:
        im.preview_png(d)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


def test_preview_pdf(im, oa):
    im.ses.clear()
    d = ir.mk_pdf_preview_req(5, 1017)
    try:
        im.preview_pdf(d)
    except Early_Exit:
        pass
    r = im.ses.req
    ro = openapi_core.contrib.requests.RequestsOpenAPIRequest(r)
    oa.validate_request(ro)


