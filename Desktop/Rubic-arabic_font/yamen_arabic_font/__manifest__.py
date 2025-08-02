 # -*- coding: utf-8 -*-
{
    'name': "Yamen arabic font",

    'summary': """
        change defult font to rubic arabic font""",

    'description': """
        Change the defult arabic font of the all interfaces with a beautiful one preferred by the Arabic user
 ,
    """,
    'author': "Husam Ragab",
    'website': "http://swvt.com",
    'category': 'Localization',
    'version': '1.10',
    'depends': ['web'],
    'qweb': [],

    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'auto_install': True,
    'installable': True,
    'live_test_url': 'https://youtu.be/aR3ZmDu8OjI',

'assets': {
    'web.assets_backend': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
        'yamen_arabic_font/static/src/css/web_style.css',
    ],
    'web.assets_frontend': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
        'yamen_arabic_font/static/src/css/web_style.css',
    ],
    'web.report_assets_common': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
    ],
    'web._assets_primary_variables': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
    ],
    'web._assets_bootstrap': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
    ],
    'web.assets_common': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
    ],
    'point_of_sale.assets': [
        'yamen_arabic_font/static/src/scss/rubikfont.scss',
        'yamen_arabic_font/static/src/css/pos_style.css',
    ],
},


}