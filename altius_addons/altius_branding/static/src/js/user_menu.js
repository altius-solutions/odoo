import { browser } from "@web/core/browser/browser";
import { _t } from "@web/core/l10n/translation";
import { registry } from "@web/core/registry";

const ALTIUS_URL = "https://altiusol.com";
const userMenu = registry.category("user_menuitems");

function externalItem(id, description, sequence) {
    return {
        type: "item",
        id,
        description,
        href: ALTIUS_URL,
        callback: () => browser.open(ALTIUS_URL, "_blank"),
        sequence,
    };
}

// Community "Help" opens the Odoo Enterprise purchase page.
userMenu.add("support", () => externalItem("support", _t("Support"), 20), { force: true });
userMenu.add("altius_docs", () => externalItem("altius_docs", _t("Documentation"), 15));

// "My Subscription" is the Odoo account / Enterprise plan screen.
if (userMenu.contains("mysubscription_user_menu")) {
    userMenu.remove("mysubscription_user_menu");
}
