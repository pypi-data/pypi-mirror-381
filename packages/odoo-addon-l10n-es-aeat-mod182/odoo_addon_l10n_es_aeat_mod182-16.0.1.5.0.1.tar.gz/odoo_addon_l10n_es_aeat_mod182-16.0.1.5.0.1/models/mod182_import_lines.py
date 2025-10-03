# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class L10nEsAeatMod182ImportLines(models.Model):
    _name = "l10n.es.aeat.mod182.import.lines"
    _description = "AEAT 182 Import Lines"

    type = fields.Char()
    model = fields.Char()
    year = fields.Char()
    company_vat = fields.Char(string="Company VAT")
    partner_vat = fields.Char(string="Partner VAT")
    representative_vat = fields.Char(string="Representative VAT")
    name = fields.Char()
    partner_state_code = fields.Char()
    operation_key = fields.Char()
    deduction_percentage = fields.Float(string="Deduction Percentage (%)")
    donation_amount = fields.Float(string="Donation Amount (€)")
    donation_or_contribution_in_kind = fields.Char(
        string="Donation or Contribution in Kind"
    )
    regional_community_deduction_id = fields.Char()
    regional_deduction_percentage = fields.Char()
    declared_nature = fields.Char()
    revocation = fields.Char()
    year_of_revoked_donation = fields.Char(string="Year of Revoked Donation")
    kind_of_good = fields.Char(string="Kind of Good")
    item_identification = fields.Char()
    donation_recurrence = fields.Char()
    protected_patrimony_holder_nif = fields.Char(
        string="Protected Patrimony Holder NIF"
    )
    protected_patrimony_holder_name = fields.Char()
