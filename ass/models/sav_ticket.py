# -*- coding: utf-8 -*-

from odoo import models, fields , api
    
class ctr(models.Model):
    #_name='helpdesk.ticket'
    _inherit = 'helpdesk.ticket'
    sequence = fields.Char(string="N° ticket", readonly=True, required=True, copy=False, default='New')
    reference=fields.Char(string="Réference")
    client_phone = fields.Char(related="partner_id.phone",string="Téléphone")
    client_street = fields.Char(related="partner_id.street",string="Adresse")
    #objet_reclamation=fields.Char(string="Objet de la reclamation")
    #date_reclamation=fields.Date(string="Date de raclamation")
    cust=fields.Many2one(comodel_name="res.partner",string="Partenaire")
    phone = fields.Char(related="cust.phone",string="Téléphone")
    applicant_name = fields.Many2one(comodel_name="res.partner",string="Demandeur")
    applicant_phone = fields.Char(related="applicant_name.phone",string="Téléphone")
    dealer_name =  fields.Many2one(comodel_name="res.partner",string="Revendeur")
    dealer_phone = fields.Char(related="dealer_name.phone",string="Téléphone")
    product = fields.Many2one(comodel_name="product.product",string="Produit")
    mark = fields.Many2one(comodel_name="product.category",string="Marque")
    product_model = fields.Char(string="Modèle Produit")
    product_serial = fields.Char(string="Numéro de serie")
    follow_ids = fields.One2many('helpdesk.ticket','follow_relation')
   

    @api.model
    def create(self, vals):
        vals['sequence'] = self.env['ir.sequence'].next_by_code('sav.ticket')
        return super(ctr, self).create(vals)

class follow_ticket(models.Model):
    #_name = 'follow.ticket'
    _inherit = 'helpdesk.ticket'
    follow_date = fields.Date(string="Date")
    follow_description = fields.Text(string="Description")
    follow_relation = fields.Many2one(comodel_name="helpdesk.ticket")
    

