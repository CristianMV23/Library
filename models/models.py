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


class libro(models.Model):

    _name = 'library.libro'
    
    titulo = fields.Char(string="Título", required=True)
    autor = fields.Char(string="Autor", required=True)
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)

    ejemplares=fields.One2many(
        'library.ejemplar', 'libro', string="Ejemplares")
        
class ejemplar(models.Model):

    _name = 'library.ejemplar'
    
    numeroRegistro = fields.Integer(string="Número de registro", required=True)

    libro=fields.Many2one('biblary.libro', string="Libro")
    #related field to show "titulo" in "Prestamos" tab in user's view
    titulo = fields.Char(related="libro.titulo",store=True)
    prestatario=fields.Many2one('res.users', string="Prestatario")

class Categoria(models.Model):

    _name = 'library.categoria'
    
    
    name = fields.Char(string="Nombre de la categoría", required=True)
    descripcion = fields.Text(string="Descripción")
    
    # Relación inversa One2many hacia los libros
    libro_ids = fields.One2many(
        'library.libro', 'categoria_id', string="Libros")       

class user(models.Model):

    _name = 'res.users'
    _inherit = 'res.users'
    
    prestamos=fields.One2many(
        'library.ejemplar', 'prestatario', string="Préstamos")    