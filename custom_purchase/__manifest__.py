{
    'name': 'Custom Purchase',
    'version': '17.0.1.0.0',
    'category': 'Purchase',
    'summary': 'Custom Purchase with Multiple Vendors and Bidding',
    'description': """
        Custom purchase module with:
        - Multiple vendor assignment for RFQs
        - Bidding system
        - Purchase requests
    """,
    'depends': ['purchase', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_request_views.xml',
        'views/purchase_rfq_views.xml',
        'data/purchase_request_sequence.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
