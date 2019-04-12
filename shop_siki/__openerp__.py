# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Custom Module Shop ',
    'summary': 'Hibrid Module - Parent add_to_cart, wishlist ',
    'version': '1.0',
    'author' : 'SIKI SAS, Developer Ing Henry Vivas',
	'website' : 'www.sikisoftware.com',
    "support": "controlwebmanager@gmail.com",
    'category': 'Website',
    'description': """
This module extend App Add to Cart and Whislist.
========================================================================

List of modifications:
-------------------
    * V.-1.0 ( Req. 1061 ) Position icon Add to Cart Bottom - Right 
    * V.-1.1 ( Req. 1060 ) Position icon wishlist Top - Right
    * V.-1.2 Desing View list, button Published see
    * V.-1.3 Best structu Code Python in Model and Xml, More eficcient
    * V.-2.0 Implement the widget Javascript and call mthod python for select app in menu Customize Odoo
    * V.-3.0 ( Req. 1064 ) Position Icon Wishlist , Position input quantity
    

*Required
   This module to work needs the installation of the Add to cart and website_sale_wishlist module

 """,
    'depends': [
        'add_to_cart',
        'website_sale_wishlist',
        'website',
        'sale',
        'website_sale',
        'payment',
    ],
    'data': [
        'views/add_to_cart_template_view.xml',
        'views/shop.xml',

    ],
    'installable': True,
    'application': False,
}