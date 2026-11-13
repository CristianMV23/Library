-*- coding: utf-8 -*-

from odoo import models, fields, api

class DetalleCompra(models.Model):
    _name = 'library.detallecompra'
    
    
    libro_id = fields.Many2one('library.stock', string="stock", required=True)
    compra_id = fields.Many2one('library.compra', string="Compra", required=True)

    # Atributos propios de la relación
    cantidad = fields.Integer(string="Cantidad", default=1)
    subtotal = fields.Float(string="Subtotal")

