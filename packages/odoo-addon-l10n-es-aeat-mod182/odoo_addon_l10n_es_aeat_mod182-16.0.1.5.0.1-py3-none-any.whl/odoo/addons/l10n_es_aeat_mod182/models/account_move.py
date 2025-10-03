# Copyright 2018 PESOL - Angel Moya <info@pesol.es>
# Copyright 2019 Tecnativa - Pedro M. Baeza
# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    not_in_mod182 = fields.Boolean(
        string="Force not included in 182 report",
        help="If you mark this field, this invoice will not be included in "
        "any AEAT 182 model report.",
        default=False,
    )
