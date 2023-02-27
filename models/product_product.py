# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from datetime import timedelta, time
from odoo import fields, models, _, api
from odoo.tools.float_utils import float_round



class ProductPackaging(models.Model):
    _inherit = 'product.packaging'

    manufacturing = fields.Boolean("Manufacturing", default=True, help="If true, the packaging can be used for manufacturing orders")
