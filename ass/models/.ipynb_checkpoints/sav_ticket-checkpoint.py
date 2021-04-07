# -*- coding: utf-8 -*-

from odoo import models, fields , api


class ctr(models.Model):
    _inherit = 'helpdesk.ticket'
    sequence = fields.Char(string="N° ticket", readonly=True, required=True, copy=False, default='New')
    reference=fields.Char(string="Réference")
    #objet_reclamation=fields.Char(string="Objet de la reclamation")
    #date_reclamation=fields.Date(string="Date de raclamation")
    cust=fields.Many2one(comodel_name="res.partner",string="Partenaire")
    phone = fields.Char(related="cust.mobile",string="Téléphone")
    applicant_name = fields.Many2one(comodel_name="res.partner",string="Demandeur")
    applicant_phone = fields.Char(related="applicant_name.mobile",string="Téléphone")
    dealer_name =  fields.Many2one(comodel_name="res.partner",string="Revendeur")
    dealer_phone = fields.Char(related="dealer_name.mobile",string="Téléphone")
    product = fields.Many2one(comodel_name="product.product",string="Produit")
    mark = fields.Many2one(comodel_name="product.category",string="Marque")
    product_model = fields.Char(string="Modèle Produit")
    product_serial = fields.Char(string="Numéro de serie")
   

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sav.ticket')
        return super(ctr, self).create(vals)
