-*- coding: utf-8 -*-

from odoo import models, fields, api

class stock(models.Model):
    _name = 'library.stock'
    

    id_libro = fields.Char(string="ID Libro", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    titulo = fields.Char(string="Título", required=True)
    precio = fields.Float(string="Precio", required=True)

    # Relacion N:1 con Tienda
    tienda_id = fields.Many2one('library.tienda', string="Tienda")

    #  N:M con Compra 
    compra_ids = fields.Many2many(
        'library.compra', string="Compras")
    
