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

from odoo import models, fields, api, exceptions, _

KEY_TAX_MAPPING = {
    "A": "l10n_es_aeat_mod182.aeat_mod182_map_a",
    "B": "l10n_es_aeat_mod182.aeat_mod182_map_b",
}


class L10nEsAeatMod182Report(models.Model):
    _inherit = "l10n.es.aeat.report"
    _name = "l10n.es.aeat.mod182.report"
    _description = "AEAT 182 Report"
    _period_yearly = True
    _period_quarterly = False
    _period_monthly = False
    _aeat_number = "182"

    @api.depends(
        "partner_record_ids",
        "partner_record_ids.amount",
    )
    def _compute_totals(self):
        """Calculates the total_* fields from the line values."""
        for record in self:
            record.total_partner_records = len(record.partner_record_ids)
            record.total_amount = sum(record.mapped("partner_record_ids.amount"))

    number = fields.Char(default="182")

    # --- Persones Físiques (IRPF) ---

    under_limit_percentage = fields.Float(
        string="Under Limit (€)",
        digits="Account",
        default=150.00,
        copy=True,
        help="The limit under € for individual taxpayers.",
    )
    under_limit_value = fields.Float(
        string="Under Limit Percentage (%)",
        digits="Account",
        default=80.00,
        copy=True,
        help="The value for individual taxpayers under limit.",
    )
    rest_3_years_old_value = fields.Float(
        string="Rest 3 Years Old Percentage (%)",
        digits="Account",
        default=40.00,
        copy=True,
        help="The value for individual taxpayers with 3 years of antiquity.",
    )
    rest_percentage_value = fields.Float(
        string="Rest Percentage (%)",
        digits="Account",
        default=35.00,
        copy=True,
        help="The remaining percentage for individual taxpayers.",
    )

    # --- Persones Jurídiques (IS) ---

    general_percentage = fields.Float(
        string="General Percentage (%)",
        digits="Account",
        default=35.00,
        copy=True,
        help="The general percentage for corporate taxpayers.",
    )
    over_3_years_value = fields.Float(
        string="Over 3 Years Percentage (%)",
        digits="Account",
        default=40.00,
        copy=True,
        help="The value for corporate taxpayers with more than 3 years of antiquity.",
    )
    total_partner_records = fields.Integer(
        compute="_compute_totals",
        string="Partners records",
        store=True,
    )
    total_amount = fields.Float(
        compute="_compute_totals",
        string="Total Amount",
        store=True,
    )
    declarant_nature = fields.Selection(
        selection=[
            (
                "1",
                "Entidad beneficiaria de los incentivos "
                "regulados en el Título III de la Ley 49/2002",
            ),
            (
                "2",
                "Fundación legalmente reconocida",
            ),
            (
                "3",
                "Titular o administrador de un patrimonio protegido "
                "regulado en la Ley 41/2003",
            ),
            (
                "4",
                "Partidos Políticos, Federaciones, Coaliciones "
                "o Agrupaciones de Electores",
            ),
        ],
        default="1",
        required=True,
        copy=True,
        help="""
            NATURALEZA DEL DECLARANTE
            1: Entidad beneficiaria de los incentivos regulados en el
            Título III de la Ley 49/2002, de 23 de diciembre, de
            régimen fiscal de las entidades sin fines lucrativos y de
            los incentivos fiscales al mecenazgo.
            2: Fundación legalmente reconocida que rinde cuentas al
            órgano del protectorado correspondiente o asociación
            declarada de utilidad pública a que se refieren el
            artículo 68.3.b) de la Ley del Impuesto sobre la Renta
            de las Personas Físicas.
            3: Titular o administrador de un patrimonio protegido
            regulado en la Ley 41/2003, de 18 de noviembre, de
            protección patrimonial de las personas con
            discapacidad y de modificación del Código Civil, de la
            Ley de Enjuiciamiento Civil y de la Normativa Tributaria
            con esta finalidad.
            4: Partidos Políticos, Federaciones, Coaliciones o
            Agrupaciones de Electores en los términos previstos en
            la Ley Orgánica 8/2007, de 4 de julio, de financiación de
            partidos políticos.
        """,
    )
    partner_record_ids = fields.One2many(
        comodel_name="l10n.es.aeat.mod182.partner_record",
        inverse_name="report_id",
        string="Partner Records",
    )

    def _error_count(self, model):
        records_error_group = self.env["l10n.es.aeat.mod182.%s" % model].read_group(
            domain=[("check_ok", "=", False), ("report_id", "in", self.ids)],
            fields=["report_id"],
            groupby=["report_id"],
        )
        return {
            rec["report_id"][0]: rec["report_id_count"] for rec in records_error_group
        }

    def _compute_error_count(self):
        ret_val = super()._compute_error_count()
        partner_records_error_dict = self._error_count("partner_record")

        for report in self:
            report.error_count += partner_records_error_dict.get(report.id, 0)
        return ret_val

    def button_confirm(self):
        """Different check out in report"""
        for item in self:
            # Browse partner record lines to check if all are correct (all
            # fields filled)
            partner_errors = []
            for partner_record in item.partner_record_ids:
                if not partner_record.check_ok:
                    partner_errors.append(
                        _(
                            "- %(name)s %(id)s",
                            name=partner_record.partner_id.name,
                            id=partner_record.partner_id.id,
                        )
                    )
            error = _(
                "Please review partner records, some of them are in red color:\n\n"
            )
            if partner_errors:
                error += _("Partner record errors:\n")
                error += "\n".join(partner_errors)
                error += "\n\n"
            if partner_errors:
                raise exceptions.ValidationError(error)
        return super(L10nEsAeatMod182Report, self).button_confirm()

    def button_send_mails(self):
        self.partner_record_ids.filtered(
            lambda x: x.state == "pending"
        ).send_email_direct()

    def btn_list_records(self):
        return {
            "domain": "[('report_id','in'," + str(self.ids) + ")]",
            "name": _("Partner records"),
            "view_mode": "tree,form",
            "res_model": "l10n.es.aeat.mod182.partner_record",
            "type": "ir.actions.act_window",
        }

    def _account_move_line_domain(self, taxes):
        """Return domain for searching move lines.

        :param: taxes: Taxes to look for in move lines.
        """
        return [
            ("partner_id.not_in_mod182", "=", False),
            ("move_id.not_in_mod182", "=", False),
            ("date", ">=", self.date_start),
            ("date", "<=", self.date_end),
            "|",
            ("tax_ids", "in", taxes.ids),
            ("tax_line_id", "in", taxes.ids),
            ("parent_state", "=", "posted"),
        ]

    @api.model
    def _get_taxes(self, map_rec):
        """Obtain all the taxes to be considered for 182."""
        self.ensure_one()
        tax_templates = map_rec.mapped("tax_ids")
        if not tax_templates:
            raise exceptions.UserError(_("No Tax Mapping was found"))
        return self.get_taxes_from_templates(tax_templates)

    @api.model
    def _get_partner_182_identification(self, partner):
        country_code, _, vat = partner._parse_aeat_vat_info()
        if country_code == "ES":
            return {
                "partner_vat": vat,
                # Odoo Spanish states codes use car license plates approach
                # (CR, A, M...), instead of ZIP (01, 02...), so we need to
                # convert them, but fallbacking in existing one if not found.
                "partner_state_code": self.SPANISH_STATES.get(
                    partner.state_id.code, partner.state_id.code
                ),
                "partner_country_code": country_code,
            }
        else:
            return {
                "community_vat": vat,
                "partner_state_code": 99,
                "partner_country_code": country_code,
            }

    def _create_partner_records(self, partner_record=None):
        """ """
        sign = 1
        partner_record_obj = self.env["l10n.es.aeat.mod182.partner_record"]
        partner_obj = self.env["res.partner"]

        move_lines = (
            self.env["donation.donation"]
            .search(
                [
                    ("state", "=", "done"),
                ]
            )
            .move_id.line_ids
        )
        domain = [
            ("id", "in", move_lines.ids),
            ("move_id.not_in_mod182", "=", False),
            ("partner_id.not_in_mod182", "=", False),
            ("date", ">=", self.date_start),
            ("date", "<=", self.date_end),
            ("balance", ">", 0.00),
        ]
        if partner_record:
            domain += [("partner_id", "=", partner_record.partner_id.id)]
        groups = self.env["account.move.line"].read_group(
            domain,
            ["partner_id", "balance"],
            ["partner_id"],
        )
        filtered_groups = list(filter(lambda d: abs(d["balance"]) > 0, groups))
        for group in filtered_groups:
            partner = partner_obj.browse(group["partner_id"][0])
            vals = {
                "report_id": self.id,
                "partner_id": partner.id,
                "representative_vat": "",
                "amount": sign * group["balance"],
            }
            vals.update(self._get_partner_182_identification(partner))
            move_groups = self.env["account.move.line"].read_group(
                group["__domain"],
                ["move_id", "balance"],
                ["move_id"],
            )
            vals["move_record_ids"] = [
                (
                    0,
                    0,
                    {
                        "move_id": move_group["move_id"][0],
                        "amount": sign * move_group["balance"],
                    },
                )
                for move_group in move_groups
            ]
            if partner_record:
                vals["move_record_ids"][0:0] = [
                    (2, x) for x in partner_record.move_record_ids.ids
                ]
                partner_record.write(vals)
            else:
                partner_record_obj.create(vals)

    def _create_cash_moves(self):
        partner_obj = self.env["res.partner"]
        move_line_obj = self.env["account.move.line"]
        cash_journals = self.env["account.journal"].search(
            [("type", "=", "cash")],
        )
        if not cash_journals:
            return
        domain = [
            ("account_id.account_type", "=", "asset_receivable"),
            ("journal_id", "in", cash_journals.ids),
            ("date", ">=", self.date_start),
            ("date", "<=", self.date_end),
            ("partner_id.not_in_mod182", "=", False),
        ]
        cash_groups = move_line_obj.read_group(
            domain, ["partner_id", "balance"], ["partner_id"]
        )
        for cash_group in cash_groups:
            partner = partner_obj.browse(cash_group["partner_id"][0])
            partner_record_obj = self.env["l10n.es.aeat.mod182.partner_record"]
            amount = abs(cash_group["balance"])
            if amount > 0:
                move_lines = move_line_obj.search(cash_group["__domain"])
                partner_record = partner_record_obj.search(
                    [
                        ("partner_id", "=", partner.id),
                        ("report_id", "=", self.id),
                    ]
                )
                if partner_record:
                    partner_record.write(
                        {
                            "cash_record_ids": [(6, 0, move_lines.ids)],
                        }
                    )
                else:
                    vals = {
                        "report_id": self.id,
                        "partner_id": partner.id,
                        "representative_vat": "",
                        "amount": 0,
                        "cash_record_ids": [(6, 0, move_lines.ids)],
                    }
                    vals.update(self._get_partner_182_identification(partner))
                    partner_record_obj.create(vals)

    def calculate(self):
        for report in self:
            # Delete previous partner records
            report.partner_record_ids.unlink()
            with self.env.norecompute():
                self._create_partner_records()
                self._create_cash_moves()
            self.env.flush_all()
            report.partner_record_ids.calculate_quarter_totals()
        return True
