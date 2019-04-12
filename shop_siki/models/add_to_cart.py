# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
from openerp import models, api, fields

class ViewStatusAddToCArt(models.Model):
    _inherit = 'website'

    #value_field_active_view = fields.Boolean(compute='_compute_active_view', store=False)

    @api.multi
    def _compute_website_view_form(self):
        recordset = self.env['ir.ui.view']
        form_List = recordset.search([('key', '=', 'website_sale.products_list_view')])
        for record in form_List:
            if record.active == True:
                value = record.active
                self.ensure_one()
                #print('add_to_cart=',value)
                return value

    @api.multi
    def _compute_website_view(self):

        recordset = self.env['ir.ui.view']
        form_List = recordset.search([('key', '=', 'website_sale.products_list_view')])

        Productsitem = recordset.search([('key', '=', 'website_sale.products_item')])

        # AddtoCart inherit Productsitem
        AddtoCart = recordset.search([('key', '=', 'website_sale.products_add_to_cart')])

        # Extension
        AddtoCartwithEase = recordset.search([('key', '=', 'add_to_cart.products_item_inherited')])

        AddtoWishlistFromList = recordset.search([('key', '=', 'website_sale_wishlist.products_add_to_wishlist')])

        if AddtoWishlistFromList.active != True:
            #print('llego aqui', AddtoWishlistFromList.active)
            AddtoCartwithEase.active = True
            AddtoCartwithEase.customize_show = True
            self.ensure_one()

        for record in AddtoWishlistFromList:

            if record.active == True:
                #print('Con info', AddtoWishlistFromList.id)
                AddtoCartwithEase.active = True
                #AddtoCartwithEase.customize_show = False

                self.ensure_one()


        return True