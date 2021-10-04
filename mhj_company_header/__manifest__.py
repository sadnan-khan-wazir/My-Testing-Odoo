# -*- coding: utf-8 -*-
{
    'name': "Company header/footer",

    'summary': """
       Allows you to add header and footer image on company and use it on printed sales & invoices""",

    'description': """
        Allows you to add header and footer image on company and use it on printed sales sales & invoice.
    """,
    'version': '12.0.2.0',
    'category': 'Accounting',
    'license': 'AGPL-3',
    'author': 'HAJJAJ.PRO',
    'website': 'http://hajjaj.pro/',
    'depends': ['sale_management','account'],
    'data': [
        'views/base_templates.xml',
        'views/views.xml',
        'views/sale_report.xml',
        'views/invoice_report.xml',
    ],
    "images": [
        'static/description/banner.png'
    ],
}
