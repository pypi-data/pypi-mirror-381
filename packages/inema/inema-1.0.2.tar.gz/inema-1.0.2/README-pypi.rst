python-inema is a Python package that implements the "Internetmarke" web API for
interacing with HTTP endpoints of the German postal company `Deutsche Post`_, in
order to buy printable letter postage, online.

The Internetmarke web API is offered by `Deutsche Post`_ and allows you to buy online
franking for national and international postal products like post cards and
letters of all weight classes and service classes (normal, registered, ...).

Supported APIs:

- Internetmarke REST API (released 2024), cf. ``inema.rest``
- Internetmarke SOAP API (V3, aka 1C4A Webservice API), end of life end of 2025, cf. ``inema.inema``
- Product Webservice SOAP API (ProdWS), cf. ``inema.inema.ProductInformation``
- Warenpost International REST API (released 2020), cf. ``inema.wpint``

.. _Deutsche Post: https://en.wikipedia.org/wiki/Deutsche_Post_(disambiguation)

Continue reading:

- `python-inema git repository <https://gitea.sysmocom.de/odoo/python-inema.git>`_
- `python-inema Codeberg git mirror <https://codeberg.org/gms/python-inema>`_
- `python-inema readthedocs documentation <https://inema.readthedocs.io/en/latest/>`_
