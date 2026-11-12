# -*- coding: utf-8 -*-

from odoo import models, fields, api
# class library(models.Model):
#     _name = 'library.library'
#     _description = 'library.library'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class Cliente(models.Model):
    _name = 'library.cliente'
    
    identificacion = fields.Char(string="ID", required=True)
    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email")
    telefono = fields.Integer(string="Teléfono")

    #  1:N con Compra
    compra_ids = fields.One2many(
        'library.compra', 'cliente_id', string="Compras"
    )


class Tienda(models.Model):
    _name = 'library.tienda'
    

    id_tienda = fields.Char(string="ID Tienda", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    direccion = fields.Char(string="Dirección")
    numero_telf = fields.Integer(string="Número de teléfono")

    #  1:N hacia Stock (Libros) y Compras
    stock_libro_ids = fields.One2many(
        'library.libro', 'tienda_id', string="Stock de Libros"
    )
    compra_ids = fields.One2many(
        'library.compra', 'tienda_id', string="Compras"
    )


class Libro(models.Model):
    _name = 'library.libro'
    

    id_libro = fields.Char(string="ID Libro", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    titulo = fields.Char(string="Título", required=True)
    precio = fields.Float(string="Precio", required=True)

    # Relación N:1 con Tienda
    tienda_id = fields.Many2one('library.tienda', string="Tienda")

    #  N:M con Compra 
    compra_ids = fields.Many2many(
        'library.compra', string="Compras")
    


class Compra(models.Model):
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
        'library.libro', string="Libros" )
    

class DetalleCompra(models.Model):
    _name = 'library.detalle.compra'
    
    
    libro_id = fields.Many2one('library.libro', string="Libro", required=True)
    compra_id = fields.Many2one('library.compra', string="Compra", required=True)

    # Atributos propios de la relación
    cantidad = fields.Integer(string="Cantidad", default=1)
    subtotal = fields.Float(string="Subtotal")

#class user(models.Model):
 #   _name = 'res.users'
  #  _inherit = 'res.users'
   
  #  compra_ids=fields.One2many(

   #     'library.compra', 'cliente_id', string="Compras")