{
    'search': '', 
    'category': product.public.category(), 
    'attrib_values': [],
    'attrib_set': set(),
    'pager': {
        'page_count': 6, 
        'offset': 0, 
        'page': {'url': '/shop?ppg=2', 'num': 1},
        'page_first': {'url': '/shop?ppg=2', 'num': 1},
        'page_start': {'url': '/shop?ppg=2', 'num': 1},
        'page_previous': {'url': '/shop?ppg=2', 'num': 1},
        'page_next': {'url': '/shop/page/2?ppg=2', 'num': 2},
        'page_end': {'url': '/shop/page/6?ppg=2', 'num': 6},
        'page_last': {'url': '/shop/page/6?ppg=2', 'num': 6},
        'pages': [
            {'url': '/shop?ppg=2', 'num': 1},
            {'url': '/shop/page/2?ppg=2', 'num': 2},
            {'url': '/shop/page/3?ppg=2', 'num': 3},
            {'url': '/shop/page/4?ppg=2', 'num': 4},
            {'url': '/shop/page/5?ppg=2', 'num': 5},
            {'url': '/shop/page/6?ppg=2', 'num': 6}
        ]
    },
    'pricelist': product.pricelist(1,), 
    'add_qty': 1,
    'products': product.template(4, 7, 3, 5, 6, 8, 9, 10, 11, 12, 13), 
    'search_count': 11, 
    'bins': [
        [
            {'product': product.template(4,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(7,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(3,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(5,), 'x': 1, 'y': 1, 'class': ''
            }
        ],
        [
            {'product': product.template(6,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(8,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(9,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(10,), 'x': 1, 'y': 1, 'class': ''
            }
        ],
        [
            {'product': product.template(11,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(12,), 'x': 1, 'y': 1, 'class': ''
            },
            {'product': product.template(13,), 'x': 1, 'y': 1, 'class': ''
            }
        ]
    ], 'ppg': 2, 'ppr': 4, 'categories': product.public.category(1,), 'attributes': product.attribute(), 'keep': <odoo.addons.website.controllers.main.QueryURL object at 0x7f9c46844048>, 'search_categories_ids': [], 'layout_mode': 'grid'
}

===========================================
CART
===========================================

URL: /shop/cart/update
Fields: product_id, add_qty=1 (default), set_qty=0 (default)
Method: GET/POST

==========================================
MINI CART
==========================================

URL: /dkaroma/shop/get-cart
APPLICATION-TYPE: HTTP
RESPONSE FORMAT: [{"product_id": 4, "product_name": "1X-JST-XH-255", "quantity": 1.0, "price": 10.0, "sub_total": 10.0, "total": 50.0}, {"product_id": 7, "product_name": "BMG-MDD-HW", "quantity": 4.0, "price": 10.0, "sub_total": 40.0, "total": 50.0}]


=============================================
HOME PAGE
=============================================

Odoo object name: home_page
Fields available:
    name = fields.Char("Name")
    banner_text_small_1 = fields.Char()
    banner_text_small_2 = fields.Char()
    banner_image_1 = fields.Binary()
    banner_image_2 = fields.Binary()
    
    header_text_big = fields.Char()
    header_text_small = fields.Char()
    
    card_1_text_big = fields.Char()
    card_1_text_small = fields.Char()
    card_1_image = fields.Binary()

    card_2_text_big = fields.Char()
    card_2_text_small = fields.Char()
    card_2_image = fields.Binary()

    scroll_products_1_text_big = fields.Char()
    scroll_products_1_text_small = fields.Char()
    scroll_products_1 = fields.Many2many("product.template", "scroll_products_1_rel")

    card_3_text_big = fields.Char()
    card_3_text_small = fields.Char()
    card_3_image = fields.Binary()

    card_4_text_big = fields.Char()
    card_4_text_small = fields.Char()
    card_4_image = fields.Binary()

    card_5_text_big = fields.Char()
    card_5_text_small = fields.Char()
    card_5_image = fields.Binary()

    card_6_text_big = fields.Char()
    card_6_text_small = fields.Char()
    card_6_image = fields.Binary()

    scroll_products_2_text_big = fields.Char()
    scroll_products_2_text_small = fields.Char()
    scroll_products_2 = fields.Many2many("product.template", "scroll_products_2_rel")