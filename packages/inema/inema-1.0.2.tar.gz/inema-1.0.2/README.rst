.. image:: https://readthedocs.org/projects/inema/badge/?version=latest
    :target: https://inema.readthedocs.io/en/latest/?badge=latest
    :alt: inema Documentation Status

.. image:: https://img.shields.io/pypi/v/inema.svg
    :target: https://pypi.org/project/inema/
    :alt: inema PyPI Project

.. image:: https://img.shields.io/badge/license-LGPL--3-blue.svg
    :target: https://www.gnu.org/licenses/lgpl-3.0.en.html
    :alt: LGPL-3.0-or-later

python-inema
============

python-inema is a Python package that implements the "Internetmarke" web API for
interacing with HTTP endpoints of the German postal company `Deutsche Post`_, in
order to buy printable letter postage, online.

The Internetmarke web API is offered by `Deutsche Post`_ and allows you to buy online
franking for national and international postal products like post cards and
letters of all weight classes and service classes (normal, registered, ...).

Supported APIs:

- Internetmarke REST API (released 2024), cf. :mod:`inema.rest`
- Internetmarke SOAP API (V3, aka 1C4A Webservice API), end of life end of 2025, cf. :mod:`inema.inema`
- Product Webservice SOAP API (ProdWS), cf. :class:`inema.inema.ProductInformation`
- Warenpost International REST API (released 2020), cf. :mod:`inema.wpint`


.. note:: As of 2025, AFAICS, Deutsche Post publishes *only* the documentation of it's server-side web APIs, i.e. it does **not** publish client libraries for any programming language.


.. _Deutsche Post: https://en.wikipedia.org/wiki/Deutsche_Post_(disambiguation)



API Credentials
---------------

As of 2025, Deutsche Post offers access to its APIs only to *business* customers.
That means to use it you either have to have some kind of registered business ('Gewerbe')
or self-employment ('selbständige Erwerbstätigkeit').

The registration workflow differs between the various APIs:

- Internetmarke REST API: register at the Deutsche Post `DHL API Developer Portal`_ (cf. `Internetmarke Get Started`_ Section)
- Product Webservice SOAP API: basically, you need to write to pcf-1click@deutschepost.de (cf. `ProdWS`_ documentation)
- Warenpost International API: you need to contact your `Deutsche Post sales representative`_ (cf. `Deutsche Post International`_ documentation)


.. warning:: FWIW, Deutsche Post refers its private customers to its online shop that doesn't provide any API access.


.. _DHL API Developer Portal: https://developer.dhl.com/user/register?destination=/user
.. _Internetmarke Get Started: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-paket-deutschland#get-started-section/
.. _ProdWS: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany?language_content_entity=de#additional-information-section/informationen-zum-einbinden-des-produkt-webservice-_28prodws_29
.. _Deutsche Post sales representative: https://www.deutschepost.com/en/business-customers/contact.html
.. _Deutsche Post International: https://developer.dhl.com/api-reference/deutsche-post-international-post-parcel-germany?language_content_entity=en#get-started-section/overview--using-the-api


Portokasse
----------

Futhermore, for actually purchasing postage via the API, you need a special
wallet: a '`Portokasse`_'.

That means you need to register separately a `Portokasse`_ account and link it to your API account.

.. note:: The Portokasse web portal username/password credentials are the same that are required for an Internet API session. That means the Portokasse doesn't have a concept API keys or similar.

See also:

- `Internetmarke Overview`_ Section in the Deutsche Post API documentation for general Portokasse integration notes
- `Internetmarke Portokasse`_ Section in the Deutsche Post API documentation that describes how to get a special Portokasse for testing purposes ('Entwickler-Portokasse').



.. tip::  A Entwickler-Portokasse is recommended for first steps and especially so for running the `test_rest.py` test suite that is port of the python-inema repository.


.. _Portokasse: https://portokasse.deutschepost.de/portokasse/
.. _Internetmarke Overview: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-parcel-germany?lang=en#get-started-section/overview
.. _Internetmarke Portokasse: https://developer.dhl.com/api-reference/deutsche-post-internetmarke-post-paket-deutschland?lang=de#additional-information-section/erl_e4uterungen-zur-nutzung-der-api-mit-einer-portokasse


Internetmarke API SOAP Migration
---------------------------------

See the :mod:`inema.soapfree` module for comments and hints.


Sources
-------

The python-inema source code is available from the following official locations:

- https://gitea.sysmocom.de/odoo/python-inema.git
- https://codeberg.org/gms/python-inema
- https://pypi.org/project/inema/
- https://inema.readthedocs.io/en/latest/




Authors / History
-----------------

In 2016, `Harald Welte <https://laforge.gnumonks.org/work/>`_ started developing python-inema
for internal use at his company `sysmocom`_, in order to provide franking
from the Odoo based logistics system. Like most other software at sysmocom,
it was released as open source software under a strong network copyleft
license.

Shortly after the initial release, `Georg Sauthoff <https://gms.tf>`_ joined
the development and improved and extended the code im various ways. He
also added the command-line ``frank.py``.
In 2025 he added support for the new Internetmarke REST API.


.. _sysmocom: https://sysmocom.de/


License
-------

The python-inema software package is licensed under the LGPL-3.0-or-later license.
