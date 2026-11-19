# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from . import models
from .models.res_partner import brand_discuss_bot


def post_init_hook(env):
    companies = env['res.company'].with_context(active_test=False).search([])
    for company in companies:
        color = (company.email_secondary_color or '').lower()
        if color in ('', '#875a7b', '#714b67', '#71639e'):
            company.email_secondary_color = '#4F46E5'
    brand_discuss_bot(env)
