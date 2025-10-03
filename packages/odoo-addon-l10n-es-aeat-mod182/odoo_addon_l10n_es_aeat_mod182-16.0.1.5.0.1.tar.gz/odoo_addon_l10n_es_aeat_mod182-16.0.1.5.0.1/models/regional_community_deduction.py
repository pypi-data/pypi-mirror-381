# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

import re


class RegionalCommunityDeduction(models.Model):
    _name = "regional.community.deduction"
    _description = "Regional Community Deduction"

    code = fields.Char(required=True, readonly=True, copy=False)
    name = fields.Char(required=True, readonly=True, copy=False)
    deduction = fields.Float(required=False, copy=False)

    @api.constrains("code")
    def _check_code(self):
        for record in self:
            if not re.match(r"^\d{2}$", record.code):
                raise ValidationError(_("The code must be exactly 2 digits."))

    @api.constrains("deduction")
    def _check_deduction(self):
        for record in self:
            if record.deduction < 0 or record.deduction > 100:
                raise ValidationError(
                    _("The deduction must be a positive percentage between 0 and 100.")
                )
