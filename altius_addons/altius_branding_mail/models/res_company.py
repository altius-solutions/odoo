# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    email_secondary_color = fields.Char(default="#4F46E5")
