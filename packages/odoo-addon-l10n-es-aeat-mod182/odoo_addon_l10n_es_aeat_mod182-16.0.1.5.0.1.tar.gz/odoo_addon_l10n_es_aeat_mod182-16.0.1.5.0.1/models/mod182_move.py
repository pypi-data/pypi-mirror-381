# Copyright 2004-2011 Pexego Sistemas Informáticos. (http://pexego.es)
# Copyright 2012 NaN·Tic  (http://www.nan-tic.com)
# Copyright 2013 Acysos (http://www.acysos.com)
# Copyright 2013 Joaquín Pedrosa Gutierrez (http://gutierrezweb.es)
# Copyright 2016 Tecnativa - Antonio Espinosa
# Copyright 2016 Tecnativa - Angel Moya <odoo@tecnativa.com>
# Copyright 2018 PESOL - Angel Moya <info@pesol.es>
# Copyright 2019 Tecnativa - Carlos Dauden
# Copyright 2014-2022 Tecnativa - Pedro M. Baeza
# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class L10nEsAeatMod182MoveRecord(models.Model):
    _name = "l10n.es.aeat.mod182.move.record"
    _description = "Move Record"

    @api.model
    def _default_partner_record(self):
        return self.env.context.get("partner_record_id", False)

    partner_record_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod182.partner_record",
        string="Partner record",
        required=True,
        ondelete="cascade",
        index=True,
        default=_default_partner_record,
    )
    move_id = fields.Many2one(
        comodel_name="account.move",
        string="Invoice / Journal entry",
        ondelete="restrict",
    )
    date = fields.Date(
        string="Date",
        related="move_id.date",
        store=True,
        readonly=True,
    )
    amount = fields.Float(
        readonly=True,
    )
