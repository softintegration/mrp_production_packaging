# -*- coding: utf-8 -*- 


{
    'name': 'Manufacturing order with packaging',
    'author': 'Soft-integration',
    'application': True,
    'installable': True,
    'auto_install': False,
    'qweb': [],
    'description': False,
    'images': [],
    'version': '1.0.1',
    'category': 'Manufacturing',
    'demo': [],
    'depends': ['mrp','product'],
    'data': [
        'views/mrp_production_views.xml',
        'views/product_packaging_views.xml'
    ],
    'license': 'LGPL-3',
}
