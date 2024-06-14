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
    'version': '1.0.1.5',
    'category': 'Manufacturing/Manufacturing',
    'demo': [],
    'depends': ['mrp_production_fix_replan','product'],
    'data': [
        'views/mrp_production_views.xml',
        'views/product_packaging_views.xml',
        #'report/mrp_report_views_main.xml',
        #'report/mrp_production_templates.xml'
    ],
    'license': 'LGPL-3',
}
