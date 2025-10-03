#!/usr/bin/env python3


# SPDX-License-Identifier: LGPL-3.0-or-later
# SPDX-FileCopyrightText: © 2025 Georg Sauthoff <mail@gms.tf>


import pytest

import json
import jsonschema
import referencing

import inema.rest as ir


# json schema files can be extracted out of the Internetmarke OpenAPI specification,
# e.g. with https://github.com/instrumenta/openapi2jsonschema (o2js)
#     
# as of 2025, o2js output needs case fixing of references:
#
#     sed '/"\$ref":/s/.*/\L&/' path/to/*.json -i
#
# cf. https://github.com/instrumenta/openapi2jsonschema/issues/63
schema_base = 'schema/rest'


def json_lookup(s):
    assert s.endswith('.json')
    assert '/' not in s
    # does not auto detect schema ...
    # return referencing.Resource.from_contents(json.load(open(f'{schema_base}/{s}')))
    schema = json.load(open(f'{schema_base}/{s}'))
    jsonschema.Draft202012Validator.check_schema(schema)
    return referencing.jsonschema.DRAFT202012.create_resource(schema)


@pytest.fixture(scope='session')
def reg():
    r = referencing.Registry(retrieve=json_lookup)
    return r


def test_addr(reg):
    schema = json_lookup('address.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    d = ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln')
    v.validate(d)

def test_pdf_pos(reg):
    schema = json_lookup('appshoppingcartpdfposition.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    d = ir.mk_pdf_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    v.validate(d)

def test_png_pos(reg):
    schema = json_lookup('appshoppingcartposition.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    d = ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    v.validate(d)

def test_pdf_req(reg):
    schema = json_lookup('appshoppingcartpdfrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    p = ir.mk_pdf_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    oid = 42
    t = 23
    d = ir.mk_pdf_req(oid, 5, p, t)
    v.validate(d)

def test_pdf_req_multi(reg):
    schema = json_lookup('appshoppingcartpdfrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
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
    oid = 42
    t = 23
    d = ir.mk_pdf_req(oid, 1, ps, t)
    v.validate(d)

def test_png_req(reg):
    schema = json_lookup('appshoppingcartpngrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    p = ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')   )
    oid = 42
    t = 23
    d = ir.mk_png_req(oid, p, t)
    v.validate(d)

def test_png_req_multi(reg):
    schema = json_lookup('appshoppingcartpngrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    ps = [
        ir.mk_png_pos(1022,
            sender=ir.mk_addr('Erika Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Bernd Müller', 'Nußhäherstraße 10', '12345', 'München')),
        ir.mk_png_pos(1002,
            sender=ir.mk_addr('Peter Mustermann', 'Heidestr. 17', '51147', 'Köln'),
            receiver=ir.mk_addr('Petra Müller', 'Nußhäherstraße 10', '12345', 'München')),
    ]
    oid = 42
    t = 23
    d = ir.mk_png_req(oid, ps, t)
    v.validate(d)

def test_cancel_req(reg):
    schema = json_lookup('retourevouchersrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    oid = 42
    d = ir.mk_cancel_req(order_id=oid)
    v.validate(d)

def test_pdf_preview_req(reg):
    schema = json_lookup('appshoppingcartpreviewpdfrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    d = ir.mk_pdf_preview_req(5, 31)
    v.validate(d)

def test_png_preview_req(reg):
    schema = json_lookup('appshoppingcartpreviewpngrequest.json').contents
    v = jsonschema.Draft202012Validator(schema, registry=reg)
    d = ir.mk_png_preview_req(290)
    v.validate(d)


