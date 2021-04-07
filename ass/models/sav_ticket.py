# -*- coding: utf-8 -*-

from odoo import models, fields , api


class ctr(models.Model):
    _inherit = 'helpdesk.ticket'
    sequence = fields.Char(string="N° ticket", readonly=True, required=True, copy=False, default='New')
    cust=fields.Many2one(comodel_name="res.partner",string="Partenaire")
    phone = fields.Char(related="cust.mobile",string="Téléphone")
    product = fields.Many2one(comodel_name="product.product",string="Produit")
    mark = fields.Many2one(comodel_name="product.category",string="Marque")
    reference=fields.Char(string="Réference")
    objet_reclamation=fields.Char(string="Objet de la reclamation")
    date_reclamation=fields.Date(string="Date de raclamation")
    date_proch_action=fields.Date(string="Date de prochain action")

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sav.ticket')
        return super(ctr, self).create(vals)

""" class product(models.Model):
    _inherit= 'helpdesk.ticket'
    code_produit=fields.Char(string='Code')
    libelle_produit=fields.Char(string='Produit')

class marque(models.Model):
    _inherit= 'helpdesk.ticket'
    code_marque=fields.Char(string='Code')
    libelle_marque=fields.Char(string='Marque') """