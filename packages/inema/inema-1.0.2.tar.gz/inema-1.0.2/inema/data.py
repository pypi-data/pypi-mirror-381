
import json

import importlib.resources




def load_products():
    """Load bundled products dictionary.

    Read the most recent inema/data/products-YYYY-MM-DD.json where YYYY-MM-DD is
    not more recent than today. Fall back to inema/data/products.json.
    This allows to ship multiple products.json files for announced future price/product
    changes.

    Returns
    -------
    dict
        Mapping of product code string to product information dictionary that provides cost_price and other fields.

    Warning
    -------
    The `cost_price` field is in euro while all price amounts in the Internetmarke REST API are in euro cent.
    """
    ps = [ e for e in (x.name for x in (importlib.resources.files(__package__) / 'data').iterdir())
            if e.startswith('products-') and e.endswith('.json')
            and e <= 'products-{}.json'.format(date.today().isoformat()) ]
    ps.sort()
    ps.insert(0, 'products.json')
    x = importlib.resources.files('inema') / 'data' / ps[-1]
    t = x.read_text(encoding='utf-8')
    products = json.loads(t)
    return products

products = load_products()
"""Default product dictionary.

Initialized with the result of :func:`load_products`.

Example
-------
>>> inema.data.products['1']
{'cost_price': '0.95',
 'international': False,
 'max_weight': '20',
 'name': 'Standardbrief'}

:meta hide-value:
"""


def load_formats():
    """Load bundled format list.

    Returns
    -------
    list
        List of format dictionaries.

    """
    x = importlib.resources.files(__package__) / 'data' / 'formats.json'
    t = x.read_text(encoding='utf-8')
    formats = json.loads(t)
    return formats

formats = load_formats()
"""Default format list.

Initialized with the result of :func:`load_formats`.

Example
-------
>>> inema.data.formats[0]
Out[2]:
{'id': 1,
 'isAddressPossible': True,
 'isImagePossible': False,
 'name': 'DIN A4 Normalpapier',
 'description': None,
 'pageType': 'REGULARPAGE',
 'pageLayout': {'size': {'x': 210, 'y': 297},
  'orientation': 'PORTRAIT',
  'labelSpacing': {'x': 0, 'y': 0},
  'labelCount': {'labelX': 2, 'labelY': 5},
  'margin': {'top': 31, 'bottom': 31, 'left': 15, 'right': 15}}}

:meta hide-value:
"""

