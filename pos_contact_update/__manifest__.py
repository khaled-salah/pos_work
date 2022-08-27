# -*- coding: utf-8 -*-
{
    'name': "Pos Student Customize",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'PoS',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'school_updates'],

    # always loaded
    'data': [
        'views/views.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_contact_update/static/src/js/customer_filter_pos.js',
            'pos_contact_update/static/src/js/customer_filter.js',
            'pos_contact_update/static/src/js/QrCode.js',
            'web/static/lib/zxing-library/zxing-library.js',
        ],
        'web.assets_qweb': [
            'pos_contact_update/static/src/xml/**/*',
        ],

    },

}
