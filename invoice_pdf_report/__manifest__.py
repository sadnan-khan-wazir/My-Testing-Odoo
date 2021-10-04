# -*- coding: utf-8 -*-
{
    'name': "Sale Invoice PDF Report",
    'summary': """This Module Designed For Sale And Invoice Report""",
    'description': """This Module Designed For Sale And Invoice Report""",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'res_comapny', 'account', 'sale_management', 'purchase', 'hr_expense','bran_company'],
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report.xml',
        'reports/sale_order_temp.xml',
        'reports/journal_entries.xml',
        'reports/po_order_temp.xml',
        'reports/report_temp.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
