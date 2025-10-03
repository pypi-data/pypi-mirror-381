# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, exceptions, _
import base64


class L10nEsAeatMod182ImportWizard(models.TransientModel):
    _name = "l10n.es.aeat.mod182.import.wizard"
    _description = "AEAT 182 Import Wizard"

    file = fields.Binary("File", required=True)
    file_name = fields.Char("File Name", readonly=True)

    def action_import_txt(self):
        self.ensure_one()

        if not self.file:
            return

        decoded_bytes = base64.b64decode(self.file)
        decoded_string = decoded_bytes.decode("latin-1")

        lines = [
            decoded_string[i * 250 : (i + 1) * 250]
            for i in range(len(decoded_string) // 250)
        ]
        if not lines:
            return exceptions.ValidationError(_("Lines not found in the file!"))
        elif lines[0][0] != "1":
            return exceptions.ValidationError(_("First line is not type '1'!"))
        elif lines[0][1:4] != "182":
            raise exceptions.ValidationError(_("Import model should be 182!"))
        elif lines[0][4:8] not in ["2022", "2023"]:
            raise exceptions.ValidationError(_("Import year should be 2022 or 2023!"))

        def transform_string(s):
            # Remove leading zeros
            stripped_zeros = s.lstrip("0")
            # Return the string if it has content after stripping whitespace
            return stripped_zeros if stripped_zeros.strip() else False

        lines_to_create = [
            {
                "type": transform_string(line[0]),
                "model": transform_string(line[1:4]),
                "year": transform_string(line[4:8]),
                "company_vat": transform_string(line[8:17]),
                "partner_vat": transform_string(line[17:26]),
                "representative_vat": transform_string(line[26:35]),
                "name": transform_string(line[35:75]),
                "partner_state_code": transform_string(line[75:77]),
                "operation_key": transform_string(line[77]),
                "deduction_percentage": float(transform_string(line[78:83])) / 100,
                "donation_amount": float(transform_string(line[83:96])) / 100,
                "donation_or_contribution_in_kind": transform_string(line[96]),
                "regional_community_deduction_id": transform_string(line[97:99]),
                "regional_deduction_percentage": transform_string(line[99:104]),
                "declared_nature": transform_string(line[104]),
                "revocation": transform_string(line[105]),
                "year_of_revoked_donation": transform_string(line[106:110]),
                "kind_of_good": transform_string(line[110]),
                "item_identification": transform_string(line[111:131]),
                "donation_recurrence": transform_string(line[131]),
                "protected_patrimony_holder_nif": transform_string(line[132:141]),
                "protected_patrimony_holder_name": transform_string(line[141:181]),
            }
            for line in lines[1:]
        ]

        def transform_to_domain(line):
            domain = []
            for key, value in line.items():
                domain.append((key, "=", value))
            return domain

        domains = [transform_to_domain(line) for line in lines_to_create]
        for domain in domains:
            duplicated_line = self.env["l10n.es.aeat.mod182.import.lines"].search(
                domain
            )
            if duplicated_line:
                raise exceptions.ValidationError(
                    _("Duplicated line in VAT '%s'!", duplicated_line.partner_vat)
                )

        return self.env["l10n.es.aeat.mod182.import.lines"].create(lines_to_create)
