{
    'name': 'Blue cloudy sky for web',
    'version': '1.91',
    'summary': 'Adds a realistic blue sky with drifting clouds background to your website',
    'category': 'Website',
    'author': 'Abdulrahman Fahim',
    'website': 'https://abdulrahmanfahim.github.io',
    'license': 'OPL-3',
    'depends': ['website'],
    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            # If you had any JS/CSS files, they'd go here. But we use inline style.
        ],
    },
    'images': [
        'static/description/cloud.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
