# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test_module(models.Model):
    _inherit = 'helpdesk.ticket'
    _name = 'test_module.test_module'
    _description = 'test_module.test_module'

    ticket_number = fields.Char(string="N° de Ticket", required=True)
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
