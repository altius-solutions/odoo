import { TitlePlugin } from "@web/core/browser/title_plugin";
import { patch } from "@web/core/utils/patch";

const BRAND = "Altius ERP";

patch(TitlePlugin.prototype, {
    setup() {
        super.setup();
        this.defaultTitle = BRAND;
    },
    setParts(parts) {
        super.setParts(parts);
        if (this.titleParts().brand !== BRAND) {
            super.setParts({ brand: BRAND });
        }
    },
});
