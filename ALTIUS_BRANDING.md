# Altius ERP branding

This fork of Odoo Community (LGPL-3) is the product **Altius ERP**, offered by
[Altius Solutions](https://altiusol.com). CRM is a module inside that product.
The Odoo copyright headers and the repository `LICENSE` file stay in place;
the LGPL still applies.

Branding lives in addon modules under `altius_addons/`, not in copied core
screens, so an upstream merge of Odoo `20.0` mostly touches the two hooks
listed at the bottom.

## Modules

| Module | Installs when | What it changes |
| --- | --- | --- |
| `altius_branding` | Automatically with the web client | Browser title and favicon, login page, navbar wordmark, indigo theme, user menu (Documentation and Support → altiusol.com, My Subscription removed), settings “About” text, PWA name and icons, default company logo, Apps list Enterprise “Upgrade” links, theme-store and odoo.com app-store menus |
| `altius_branding_mail` | Automatically with Discuss (mail) | “Powered by” line on notification emails, email button color `#4F46E5` |
| `altius_branding_portal` | Automatically with the customer portal | Portal record sidebar footer |
| `altius_branding_website` | Automatically with Website | Removes the “Create a free website” link to odoo.com; website loader wordmark |
| `altius_branding_digest` | Automatically with KPI Digests | Digest email footer |
| `altius_branding_crm` | Automatically with CRM | Drops the IAP “Lead Sourcing” and Odoo mail-plugin items from the pipeline Generate menu |

`altius_branding` is `auto_install`. A new database that loads the web client
gets the brand without a separate install click. Installing CRM also pulls
in the mail, portal, digest, and CRM pieces.

The database manager (`/web/database/manager`) is branded even when no
database is selected. That page is rendered from files on disk. See the core
hooks below.

## Run it

From the repository root, with PostgreSQL running:

```bash
python3 odoo-bin -d altius --addons-path=addons,odoo/addons,altius_addons \
    -i crm,altius_branding --without-demo=False
```

You do not have to pass `--addons-path` if you start Odoo from this checkout.
`odoo/modules/module.py` adds a sibling `altius_addons` directory when it
exists. Passing the path explicitly is still the right setting for a
packaged deploy (systemd, Docker) whose working directory is not the repo.

Log in as `admin` / `admin` on a database created by that command. The web
client, login page, and `/web/database/manager` should show Altius, not Odoo.

## Colors and logo

Palette, taken from altiusol.com:

| Role | Hex |
| --- | --- |
| Primary (buttons, links, active) | `#4F46E5` |
| Hover / pressed | `#4338CA` |
| Navy (navbar, “ALTIUS”) | `#1E1B4B` |
| Accent (“SOLUTIONS”, icon family) | `#6366F1` |
| Soft background | `#EEF2FF` |
| Slate text / muted | `#0F172A` / `#64748B` |

Change them in:

- `altius_addons/altius_branding/static/src/scss/primary_variables.scss` (set before Odoo’s `!default` values)
- `altius_addons/altius_branding/static/src/scss/brand_overrides.scss` (wins over later modules such as portal, which otherwise restores the Odoo purple)
- `altius_addons/altius_branding/static/src/scss/login.scss` and `backend.scss` for the login wash and navbar

There is no logo file from the company site. The mark is a wordmark:
**ALTIUS** in navy, **SOLUTIONS** in `#6366F1`, plus a square indigo “A” icon.
On the navy navbar, ALTIUS is white and SOLUTIONS is `#C7D2FE` so it stays readable.

Regenerate the SVG, PNG, and favicon after a color or lettering change:

```bash
python3 altius_addons/tools/render_brand_assets.py
```

Files:

- `altius_branding/static/src/img/wordmark.svg` — login, database manager, light surfaces
- `altius_branding/static/src/img/wordmark-on-navy.svg` — backend navbar
- `altius_branding/static/src/img/icon.svg` — favicon and navbar mark
- `altius_branding/static/src/img/company_logo.png` — default company logo stored on `res.company`
- `altius_branding/static/src/img/favicon.ico`, `icon-180.png`, `icon-192.png`, `icon-512.png` — browser and PWA icons

After replacing `company_logo.png`, update each company that still uses the
previous default (Settings → Companies, or reinstall the module on a fresh
database). The install hook only replaces the upstream “Your logo” placeholder
and empty logos, so a logo a customer uploaded is left alone.

The user menu Documentation and Support entries, in-app documentation icons,
and the Enterprise-feature dialog all open https://altiusol.com. Change that
URL in `static/src/js/user_menu.js`, `documentation.js`, and `enterprise.js`
if the destination moves.

## Pulling upstream Odoo

1. Fetch the upstream `20.0` branch and merge it into this branch.
2. Expect conflicts, if any, only in:
   - `odoo/modules/module.py` — `initialize_sys_path` appends `altius_addons`
   - `addons/web/controllers/database.py` — `_render_template` prefers
     `altius_branding/static/src/public/database_manager.qweb.html` when that
     file is on the addons path, then falls back to the upstream template
3. Re-read those two functions and keep the Altius fallback. Both are no-ops
   when `altius_addons` is not present, so the same core revision still runs
   as stock Odoo.
4. Restart Odoo and upgrade the branding modules: `-u altius_branding`.
   Asset bundles rebuild on the next page load. If colors look cached, update
   the `web` module once (`-u web`) or bump the branding module version.

Do not delete `LICENSE`, `COPYRIGHT`, or the `# Part of Odoo` headers in
upstream files. Those notices are required by the LGPL. The settings About
block names Altius ERP and still credits Odoo S.A. and the GNU LGPL.

## Core edits

These are the only upstream files this branding changes, because there is no
addon hook for them:

1. **`odoo/modules/module.py` (`initialize_sys_path`)** — adds
   `<repo>/altius_addons` to the addons path when the directory exists, so
   the modules load without a custom config. A deploy that already passes
   `--addons-path` can drop this hunk and include the directory in that option.

2. **`addons/web/controllers/database.py` (`_render_template`)** — the
   database manager is a set of QWeb files read from disk with no database,
   so a normal view inherit cannot replace them. The reader tries the Altius
   copy first.

Everything else (login, layout title, favicon, SCSS variables, navbar,
user menu, settings, emails, portal, website, digest, CRM generate menu,
PWA manifest) is an addon override.

## Still upstream, on purpose

A few Odoo marks remain because changing them would mean editing dozens of
localized or app-specific templates for surfaces this product does not lead
with, or because the LGPL requires the notice:

- Point of Sale receipts and the attendance kiosk still say “Powered by Odoo”
  until a POS or attendance bridge module is added the same way as
  `altius_branding_portal`.
- Some accounting and recruitment email templates hard-code an Odoo logo or
  the old `#875A7B` purple in the message body. Notification layouts used by
  most outgoing mail are branded.
- Developer errors, test fixtures, and comments still say Odoo. They are not
  shown to a business user.
- The “no logo” placeholder file `addons/web/static/img/nologo.png` is still
  the upstream image. Companies created here receive the Altius wordmark, so
  that file is not what the login page or navbar shows.
- Odoo S.A. copyright and the LGPL link stay in Settings → General Settings,
  and in the source headers.
