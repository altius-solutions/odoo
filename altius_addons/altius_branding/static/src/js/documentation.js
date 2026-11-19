import { patch } from "@web/core/utils/patch";
import { DocumentationLink } from "@web/views/widgets/documentation_link/documentation_link";

patch(DocumentationLink.prototype, {
    get url() {
        return "https://altiusol.com";
    },
});
