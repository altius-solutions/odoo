# Part of Altius ERP. See LICENSE file for full copyright and licensing details.

from urllib.parse import unquote, urlencode

from odoo import http
from odoo.http import request

from odoo.addons.web.controllers.webmanifest import WebManifest


class WebManifest(WebManifest):

    def _get_webmanifest(self):
        manifest = super()._get_webmanifest()
        name = request.env['ir.config_parameter'].sudo().get_str('web.web_app_name') or 'Altius ERP'
        manifest.update({
            'name': name,
            'short_name': 'Altius ERP',
            'background_color': '#1E1B4B',
            'theme_color': '#4F46E5',
            'icons': [
                {
                    'src': '/altius_branding/static/src/img/icon-192.png',
                    'sizes': '192x192',
                    'type': 'image/png',
                },
                {
                    'src': '/altius_branding/static/src/img/icon-512.png',
                    'sizes': '512x512',
                    'type': 'image/png',
                },
            ],
        })
        return manifest

    def _icon_path(self):
        return 'altius_branding/static/src/img/icon-192.png'

    @http.route()
    def scoped_app(self, app_id, path='', app_name=''):
        app_name = unquote(app_name) if app_name else self._get_scoped_app_name(app_id)
        path = f"/{unquote(path)}"
        return request.render('web.webclient_scoped_app', {
            'app_id': app_id,
            'apple_touch_icon': '/altius_branding/static/src/img/icon-180.png',
            'app_name': app_name,
            'path': path,
            'safe_manifest_url': "/web/manifest.scoped_app_manifest?" + urlencode({
                'app_id': app_id,
                'path': path,
                'app_name': app_name,
            }),
        })

    @http.route()
    def scoped_app_manifest(self, app_id, path, app_name=''):
        path = unquote(path)
        app_name = unquote(app_name) if app_name else self._get_scoped_app_name(app_id)
        return request.make_json_response({
            'icons': self._get_scoped_app_icons(app_id),
            'name': app_name,
            'scope': path,
            'start_url': path,
            'display': 'standalone',
            'background_color': '#1E1B4B',
            'theme_color': '#4F46E5',
            'prefer_related_applications': False,
            'shortcuts': self._get_scoped_app_shortcuts(app_id),
        }, {'Content-Type': 'application/manifest+json'})
