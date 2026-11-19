# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from markupsafe import Markup

from odoo import models


class ResUsers(models.Model):
    _inherit = 'res.users'

    def _init_odoobot(self):
        self.ensure_one()
        bot_id = self.env['ir.model.data']._xmlid_to_res_id("base.partner_root")
        channel = self.env['discuss.channel']._get_or_create_chat([bot_id, self.partner_id.id])
        message = Markup("%s<br/>%s<br/><b>%s</b>") % (
            self.env._("Hello 👋"),
            self.env._("Altius ERP helps your team collaborate. I'm here to help you explore it."),
            self.env._("Go ahead - Try sending me an emoji 😊"),
        )
        channel.sudo().message_post(
            author_id=bot_id,
            body=message,
            message_type="comment",
            silent=True,
            subtype_xmlid="mail.mt_comment",
        )
        self.sudo().odoobot_state = 'onboarding_emoji'
        return channel
