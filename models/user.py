-*- coding: utf-8 -*-

from odoo import models, fields, api

class User(models.Model):
    _name = 'library.user'
    
    identificacion = fields.Char(string="ID", required=True)
    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    telefono = fields.Integer(string="Teléfono")

    #  1:N con Compra
    compra_ids = fields.One2many(
        'library.compra', 'user_id', string="Compras"
    )