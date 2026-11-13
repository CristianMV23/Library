# -- coding: utf-8 --

from odoo import models, fields, api
 class library(models.Model):
    _name = 'library.library'
    _description = 'library.library'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

   