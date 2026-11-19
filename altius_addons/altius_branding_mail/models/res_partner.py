# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from odoo import models
from odoo.tools import BinaryBytes, file_open


def brand_discuss_bot(env):
    """Rename the built-in assistant so Discuss does not say OdooBot."""
    bot = env.ref('base.partner_root', raise_if_not_found=False)
    if not bot:
        return
    if bot.name == 'OdooBot':
        bot.name = 'Altius'
        with file_open('altius_branding/static/src/img/icon-192.png', 'rb') as icon:
            bot.image_1920 = BinaryBytes(icon.read(), filename='altius.png')
    messages = env['mail.message'].sudo().search([
        ('author_id', '=', bot.id),
        ('body', 'ilike', 'Odoo'),
    ])
    replacements = (
        (
            "Odoo's Discuss application helps employees collaborate efficiently. I'm here to help you explore its features.",
            "Altius ERP helps your team collaborate. I'm here to help you explore it.",
        ),
        ('@OdooBot', '@Altius'),
        ('OdooBot', 'Altius'),
    )
    for message in messages:
        body = str(message.body or '')
        updated = body
        for old, new in replacements:
            updated = updated.replace(old, new)
        if updated != body:
            message.body = updated


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def _register_hook(self):
        super()._register_hook()
        brand_discuss_bot(self.env)
