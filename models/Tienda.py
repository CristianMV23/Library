-*- coding: utf-8 -*-

from odoo import models, fields, api

class tienda(models.Model):
    _name = 'library.tienda'
    

    id_tienda = fields.Char(string="ID Tienda", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    direccion = fields.Char(string="Dirección")
    numero_telf = fields.Integer(string="Número de teléfono")

    #  1:N hacia Stock (Libros) y Compras
    stock_libro_ids = fields.One2many(
        'library.stock', 'tienda_id', string="Stock de Libros"
    )
    compra_ids = fields.One2many(
        'library.compra', 'tienda_id', string="Compras"
    )