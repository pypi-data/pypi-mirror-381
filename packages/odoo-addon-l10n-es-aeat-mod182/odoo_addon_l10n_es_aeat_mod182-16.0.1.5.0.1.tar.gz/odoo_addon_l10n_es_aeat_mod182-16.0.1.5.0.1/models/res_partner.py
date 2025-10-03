# Copyright 2018 PESOL - Angel Moya <info@pesol.es>
# Copyright 2019 Tecnativa - Pedro M. Baeza
# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    not_in_mod182 = fields.Boolean(
        string="Not included in 182 report",
        help="If you mark this field, this partner will not be included "
        "in any AEAT 182 model report, independently from the total "
        "amount of its operations.",
        default=False,
    )

    @api.model
    def _commercial_fields(self):
        res = super(ResPartner, self)._commercial_fields()
        res += ["not_in_mod182"]
        return res
