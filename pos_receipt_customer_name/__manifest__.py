# -*- coding: utf-8 -*-
{
    'name': "pos_receipt_customer_name",

    'summary': """
        include customer's name in the point of sale receipt""",

    'description': """
        This module should be used with the point of sale module 
        to have the customer's name in the receipt
    """,

    'author': "AKOREDE FODILU OLAWALE",
    'website': "https://www.ehiotech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/pos_receipt_customer_name.xml',
    ],
    'installable': True,
	'auto_install': False,
	'application': True,
}
