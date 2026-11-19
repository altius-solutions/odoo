import { patch } from "@web/core/utils/patch";
import { UpgradeDialog } from "@web/webclient/settings_form_view/fields/upgrade_dialog";
import { FormLabelHighlightText } from "@web/webclient/settings_form_view/highlight_text/form_label_highlight_text";

const ALTIUS_URL = "https://altiusol.com";

patch(UpgradeDialog.prototype, {
    async _confirmUpgrade() {
        window.open(ALTIUS_URL, "_blank");
        this.props.close();
    },
});

patch(FormLabelHighlightText.prototype, {
    setup() {
        super.setup();
        // Hide the "Enterprise" badge that advertises paid-only settings.
        this.upgradeEnterprise = false;
    },
});
