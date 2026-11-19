# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.tools import BinaryBytes, file_open


class ResCompany(models.Model):
    _inherit = 'res.company'

    def _get_logo(self):
        with file_open('altius_branding/static/src/img/company_logo.png', 'rb') as logo_file:
            return BinaryBytes(logo_file.read(), filename='logo.png')
