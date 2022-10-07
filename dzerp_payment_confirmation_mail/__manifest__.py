# -*- coding: utf-8 -*-
{
    'name': "Dzerp Payment Confirmation Mail",

    'summary': "Payment Confirmation",

    'description': """
        Payment Confirmation Mail
    """,

    'author': "DzERP",
    'sequence': 45,

    'website': "https://www.fiverr.com/users/ilyastensai",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '15.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account', 'website_sale', 'sale', 'mail'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
