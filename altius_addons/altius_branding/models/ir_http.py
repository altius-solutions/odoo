# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from odoo import models

ALTIUS_URL = "https://altiusol.com"


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super().session_info()
        # Community uses this for the user-menu Help item, and the default
        # target is the Odoo Enterprise purchase page.
        result['support_url'] = ALTIUS_URL
        return result
