{
    'name': 'External Freight Cosal',
    'version': '1.0',
    'author':'ANFEPI: Roberto Requejo Fernández',
    'depends': ['stock_picking_batch', 'stock_fleet', 'fleet'],
    'description': """
    """,
    'data': [
        'views/stock_picking_batch_view.xml',
        'report/report_picking_batch.xml',
        'views/fleet_vehicle_view.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    "license": "AGPL-3",
}