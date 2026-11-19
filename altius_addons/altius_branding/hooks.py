# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

import logging

from odoo.tools import file_open

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Replace the upstream placeholder company logo on existing companies."""
    with file_open('base/static/img/res_company_logo.png', 'rb') as original:
        placeholder = original.read()
    new_logo = env['res.company']._get_logo()
    companies = env['res.company'].with_context(active_test=False).search([])
    for company in companies:
        current = company.logo.content if company.logo else b''
        if not current or current == placeholder:
            company.logo = new_logo
            _logger.info("Applied the Altius company logo to %s", company.display_name)
