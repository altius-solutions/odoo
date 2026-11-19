import { LeadGenerationDropdown } from "@crm/components/lead_generation_dropdown/lead_generation_dropdown";
import { patch } from "@web/core/utils/patch";

// Lead Sourcing is an Odoo IAP purchase. Mail plugins open a dialog that
// installs the Odoo inbox add-in from odoo.com.
const HIDDEN = new Set(["crm_iap_mine", "Mail Plugins"]);

patch(LeadGenerationDropdown.prototype, {
    // Filter at read time. crm_iap_mine patches setup() and looks the IAP
    // entry up; removing it earlier makes that patch crash the pipeline.
    get sortedDropdownContentElements() {
        return super.sortedDropdownContentElements.filter(
            (element) => !HIDDEN.has(element.moduleName)
        );
    },
});
