-*- coding: utf-8 -*-

from odoo import models, fields, api

class compra(models.Model):
    _name = 'library.compra'
    

    id_compra = fields.Char(string="ID Compra", required=True)
    fecha = fields.Char(string="Fecha", required=True)  # Recomendado: fields.Date
    total = fields.Float(string="Total")
    descuento = fields.Char(string="Descuento")  # Recomendado: fields.Float

    #  N:1 con Cliente y Tienda
    cliente_id = fields.Many2one('library.cliente', string="Cliente", required=True)
    tienda_id = fields.Many2one('library.tienda', string="Tienda", required=True)

    #  N:M con Libro
    libro_ids = fields.Many2many(
        'library.stock', string="Libros" )
    