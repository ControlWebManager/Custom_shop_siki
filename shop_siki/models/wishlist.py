# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
import logging

from openerp import models, api, fields
from openerp.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class ViewStatus(models.Model):
    _inherit = 'website'

    #value_field_active_view = fields.Boolean(compute='_compute_active_view', store=False)

    @api.model
    def _compute_website_view(self):
        self.ensure_one()
        self.env.cr.execute("SELECT active FROM ir_ui_view WHERE key='website_sale.products_list_view'")
        value = self.env.cr.fetchone()[0]
        # self.value_field_active_view = value
        return value

    @api.multi
    def _list_add_cart(self):
        #value = self._compute_website_view()
        if value == 'top_right':
            return 'float: right;margin-top: 5px;margin-right:2%; z-index: 999;position: relative;'
        if value == 'list_add_cart':
            return 'float: right;clear: both;'