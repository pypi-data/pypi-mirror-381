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

import datetime
from calendar import monthrange

from odoo import models, fields, api, exceptions, _

KEY_TAX_MAPPING = {
    "A": "l10n_es_aeat_mod182.aeat_mod182_map_a",
    "B": "l10n_es_aeat_mod182.aeat_mod182_map_b",
}


class L10nEsAeatMod182PartnerRecord(models.Model):
    _name = "l10n.es.aeat.mod182.partner_record"
    _inherit = ["mail.thread", "mail.activity.mixin", "portal.mixin"]
    _description = "Partner Record"
    _rec_name = "partner_vat"
    _order = "check_ok asc,id"

    user_id = fields.Many2one(
        comodel_name="res.users",
        string="Salesperson",
        tracking=True,
        default=lambda self: self.env.user,
        copy=False,
    )
    state = fields.Selection(
        selection=[
            ("pending", "Pending"),
            ("sent", "Sent"),
            ("confirmed", "Confirmed"),
            ("exception", "Exception"),
        ],
        default="pending",
    )
    community_vat = fields.Char(
        string="Community VAT number",
        size=17,
        help="VAT number for professionals established in other state "
        "member without national VAT",
    )
    partner_country_code = fields.Char(
        string="Country Code",
        size=2,
    )
    amount = fields.Float(
        string="Operations amount",
        digits="Account",
        tracking=True,
    )
    origin_year = fields.Integer(
        help="Origin cash operation year",
    )
    move_record_ids = fields.One2many(
        comodel_name="l10n.es.aeat.mod182.move.record",
        inverse_name="partner_record_id",
        string="Move records",
    )
    cash_record_ids = fields.Many2many(
        comodel_name="account.move.line",
        string="Cash payments",
        readonly=True,
    )
    check_ok = fields.Boolean(
        compute="_compute_check_ok",
        string="Record is OK",
        store=True,
        help="Checked if this record is OK",
    )
    error_text = fields.Char(
        compute="_compute_check_ok",
        store=True,
    )

    # --- Partner fields --- #

    @api.model
    def _default_record_id(self):
        return self.env.context.get("report_id", False)

    report_id = fields.Many2one(
        comodel_name="l10n.es.aeat.mod182.report",
        string="AEAT 182 Report",
        ondelete="cascade",
        default=_default_record_id,
    )
    representative_vat = fields.Char(
        string="L.R. VAT number",
        size=9,
        help="N.I.F. DEL DECLARANTE",
    )
    partner_vat = fields.Char(
        string="VAT number",
        size=9,
        help="N.I.F. DEL DECLARADO",
    )
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="Partner",
        required=True,
        help="",
    )
    partner_state_code = fields.Char(
        string="State Code",
        size=2,
        help="CÓDIGO PROVINCIA",
    )
    operation_key = fields.Selection(
        selection=[
            (
                "A",
                "A. Donativos no incluidos en las actividades o programas "
                "prioritarios de mecenazgo (...)",
            ),
            (
                "B",
                "B. Donativos incluidos en las actividades o programas "
                "prioritarios de mecenazgo (...)",
            ),
            ("C", "C. Aportación al patrimonio de discapacitados."),
            (
                "D",
                "D. Disposición del patrimonio de discapacitados.",
            ),
            (
                "E",
                "E. Gasto de dinero y consumo de bienes fungibles "
                "aportados al patrimonio protegido (...)",
            ),
            ("F", "F. Cuotas de afiliación y aportaciones (...)"),
            ("G", "G. Resto de donaciones y aportaciones percibidas."),
        ],
        help="""
            CLAVE

            Las entidades acogidas al régimen de deducciones
            recogidas en el Título III de la Ley 49/2002, de 23 de
            diciembre lo consignarán según el siguiente detalle:

            A. Donativos no incluidos en las actividades o programas
            prioritarios de mecenazgo establecidos por la Ley de
            Presupuestos Generales del Estado.

            B. Donativos incluidos en las actividades o programas
            prioritarios de mecenazgo establecidos por la Ley de
            Presupuestos Generales del Estado.

            Tratándose de aportaciones o disposiciones relativas a
            patrimonios protegidos, deberá consignarse alguna de las
            siguientes claves:

            C. Aportación al patrimonio de discapacitados.

            D. Disposición del patrimonio de discapacitados.

            E. Gasto de dinero y consumo de bienes fungibles
            aportados al patrimonio protegido en el año natural al que
            se refiere la declaración informativa o en los cuatro
            anteriores para atender las necesidades vitales del
            beneficiario y que no deban considerarse como
            disposición de bienes o derechos a efectos de lo
            dispuesto en el artículo 54.5 de la Ley 35/2006, de 28 de
            noviembre, del Impuesto sobre la Renta de las Personas
            Físicas.

            Los Partidos Políticos, Federaciones, Coaliciones o
            Agrupaciones de Electores consignarán las siguientes
            claves:

            F: cuotas de afiliación y aportaciones previstas en el
            artículo 2.Dos.a) de la Ley Orgánica 8/2007, de 4 de julio,
            sobre financiación de los partidos políticos.

            G: resto de donaciones y aportaciones percibidas.
        """,
    )
    deduction_percentage = fields.Char(
        compute="_compute_deduction_percentage",
        size=10,
        store=True,
        readonly=False,
        help="""
            % DE DEDUCCIÓN

            Cuando se haya hecho constar en el campo
            "NATURALEZA DEL DECLARANTE" (posición 160) del
            tipo de registro 1, el dígito numérico indicativo de la
            naturaleza del declarante 1, 2 o 4, se hará constar el
            porcentaje de deducción aplicable a los donativos
            efectuados. En particular, si se hubiera consignado un 1 en
            dicho campo, el porcentaje que deberá declararse en
            relación con los contribuyentes del Impuesto sobre la Renta
            de las Personas Físicas será el que corresponda a la parte
            de la base de deducción que exceda de 150 euros. Si la
            base de la deducción no excede de esta cantidad, el
            porcentaje que deberá declararse en relación con estos
            contribuyentes será el establecido en el artículo 19 de la
            Ley 49/2002. De la misma forma se consignará en el caso
            de que se haya hecho constar en el campo “NATURALEZA
            DEL DECLARANTE” (posición 160) del tipo de registro 1 el
            dígito 4, y en el campo “CLAVE” (posición 78) del tipo de
            registro 2 la letra G.

            Para el resto de claves (dígito 3 en la posición 160
            “NATURALEZA DEL DECLARANTE” del tipo de registro 1)
            se rellenará a blancos.

            Este campo se subdivide en otros dos:

            79-81 ENTERO Numérico Parte entera:
                  Se consignará la parte entera el
                  porcentaje (si no tiene, consignar CEROS).

            82-83 DECIMAL Numérico Parte decimal:
                  Se consignará la parte decimal del
                  porcentaje (si no tiene, consignar CEROS).
        """,
    )

    @api.depends(
        "report_id.declarant_nature",
        "report_id.under_limit_percentage",
        "report_id.under_limit_value",
        "report_id.rest_percentage_value",
        "report_id.rest_3_years_old_value",
        "operation_key", "amount",
    )
    def _compute_deduction_percentage(self):
        """
        """
        for rec in self:
            if rec.deduction_percentage:
                continue
            # Declarant nature is "1"
            elif rec.report_id.declarant_nature in ["1"]:
                # Check against under limit percentage and set deduction percentage accordingly
                if rec.amount > rec.report_id.under_limit_percentage:
                    rec.deduction_percentage = rec.report_id.under_limit_value
                elif rec.donation_recurrence:
                    rec.deduction_percentage = rec.report_id.rest_3_years_old_value
                else:
                    rec.deduction_percentage = rec.report_id.rest_percentage_value
            # Declarant nature is "4" and operation key is "G"
            elif rec.report_id.declarant_nature in ["4"] and rec.operation_key in ["G"]:
                # Check against under limit percentage and set deduction percentage accordingly
                if rec.amount > rec.report_id.under_limit_percentage:
                    rec.deduction_percentage = rec.report_id.under_limit_value
                elif rec.donation_recurrence:
                    rec.deduction_percentage = rec.report_id.rest_3_years_old_value
                else:
                    rec.deduction_percentage = rec.report_id.rest_percentage_value
            else:
                # Default case, set deduction percentage to False
                rec.deduction_percentage = False

    donation_amount = fields.Float(
        compute="_compute_donation_amount",
        size=13,
        store=True,
        readonly=False,
        help="""
            IMPORTE O VALORACIÓN DEL DONATIVO, APORTACIÓN O DISPOSICIÓN

            Campo numérico de 13 posiciones.
            Se consignará sin signo y sin coma decimal, el importe
            anual del donativo, aportación o disposición, en el caso de
            que éste haya sido dinerario, correspondiente a un mismo
            porcentaje de deducción.

            En los donativos, aportaciones o disposiciones en especie,
            se hará constar la valoración de lo donado, aportado o
            dispuesto, determinado de acuerdo con las reglas del
            artículo 18 de la Ley 49/2002.

            En caso de que se haya marcado la CLAVE E en la
            posición 78, deberá consignarse el importe del dinero
            gastado o el valor de los bienes fungibles consumidos.

            Cuando un mismo donante haya satisfecho donativos a los
            que se apliquen distintos porcentajes de deducción,
            consigne registros de declarados independientes.

            Este campo se subdivide en dos:

            84-94 ENTERO Numérico:
                  Parte entera del importe del donativo, aportación o
                  disposición, si no tiene contenido se consignará a ceros.

            95-96 DECIMAL Numérico
                  Parte decimal del importe del donativo, aportación o
                  disposición, si no tiene contenido se consignará a ceros.
        """,
    )

    @api.depends("amount")
    def _compute_donation_amount(self):
        """
        TODO: Split lines?
        """
        for rec in self:
            if not rec.donation_amount:
                rec.donation_amount = rec.amount

    donation_or_contribution_in_kind = fields.Selection(
        string="Donation or Contribution in Kind",
        selection=[
            ("X", "X: Donativo, aportación o disposición ha sido en especie"),
            ("", "Empty"),
        ],
        help="""
            DONATIVO, APORTACIÓN O DISPOSICIÓN EN ESPECIE

            En el caso de que el donativo, aportación o disposición
            haya sido en especie, se consignará una "X". En cualquier
            otro caso este campo se rellenará a blancos.
        """,
    )
    regional_community_deduction_id = fields.Many2one(
        comodel_name="regional.community.deduction",
        help="""
            DEDUCCIÓN COM. AUTÓNOMA

            Cuando se haya hecho constar en el campo
            "NATURALEZA DEL DECLARANTE" (posición 160) del
            tipo de registro 1, el dato numérico indicativo de la
            naturaleza del declarante 1 ó 2, en el caso de que el
            donativo pueda dar derecho a la aplicación en el Impuesto
            sobre la Renta de las Personas Físicas de alguna de las
            deducciones aprobadas por las Comunidades Autónomas,
            indique la clave de la Comunidad Autónoma que
            corresponda, conforme a la siguiente relación:

            ANDALUCÍA......................... 01
            ARAGÓN ........................... 02
            PRINCIPADO DE ASTURIAS ........... 03
            ILLES BALEARS .................... 04
            CANARIAS.......................... 05
            CANTABRIA......................... 06
            CASTILLA-LA MANCHA ............... 07
            CASTILLA Y LEÓN .................. 08
            CATALUÑA ......................... 09
            EXTREMADURA....................... 10
            GALICIA .......................... 11
            MADRID ........................... 12
            REGIÓN DE MURCIA ................. 13
            LA RIOJA ......................... 16
            COMUNIDAD VALENCIANA ............. 17
        """,
    )

    @api.constrains("regional_community_deduction_id")
    def _require_regional_community_deduction_id(self):
        for rec in self:
            if (
                rec.report_id.declarant_nature in ["1", "2"]
                and not rec.regional_community_deduction_id
            ):
                raise exceptions.ValidationError(
                    _(
                        "'DEDUCCIÓN COM. AUTÓNOMA' is required because "
                        "'NATURALEZA DEL DECLARANTE' is set as %s.",
                        rec.report_id.declarant_nature,
                    )
                )

    regional_deduction_percentage = fields.Char(
        size=5,
        compute="_compute_regional_deduction_percentage",
        store=True,
        readonly=False,
        help="""
            % DE DEDUCCIÓN COM. AUTÓNOMA

            Cuando el campo anterior "Deducción Com. Autónoma"
            tenga contenido, se consignará el porcentaje de deducción
            en la cuota íntegra del I.R.P.F. aprobado por la Comunidad
            Autónoma que corresponda.

            Este campo se subdivide en otros dos:

            100-102 ENTERO Numérico Parte entera:
                    Se consignara la parte entera del
                    porcentage (si no tiene, consignar CEROS).

            103-104 DECIMAL Numérico Parte decimal:
                    Se consignara la parte decimal del
                    porcentage (si no tiene, consignar CEROS).
        """,
    )

    @api.depends("regional_community_deduction_id")
    def _compute_regional_deduction_percentage(self):
        for rec in self:
            rec.regional_deduction_percentage = (
                rec.regional_community_deduction_id.deduction
            )

    @api.constrains("regional_deduction_percentage")
    def _require_regional_deduction_percentage(self):
        for rec in self:
            if (
                rec.regional_community_deduction_id
                and not rec.regional_deduction_percentage
            ):
                raise exceptions.ValidationError(
                    _(
                        "'% DE DEDUCCIÓN COM. AUTÓNOMA' is required because "
                        "'DEDUCCIÓN COM. AUTÓNOMA' is set as %s.",
                        rec.regional_community_deduction_id,
                    )
                )

    declared_nature = fields.Selection(
        selection=[
            ("F", "F: Persona física"),
            ("J", "J: Persona jurídica"),
            ("E", "E: Entidad en régimen de atribución de rentas"),
            ("", "Empty"),
        ],
        help="""
            NATURALEZA DEL DECLARADO

            Para las claves A o B se hará constar la naturaleza del
            declarado de acuerdo con las siguientes claves:
            ----------------------
            'Clave', 'Descripción'
            ----------------------
            'F', 'Persona física'
            'J', 'Persona jurídica'
            'E', 'Entidad en régimen de atribución de rentas'

            Para el resto de claves se rellenará a blancos.
        """,
    )

    @api.constrains("declared_nature")
    def _require_declared_nature(self):
        for rec in self:
            if rec.operation_key in ["A", "B"] and not rec.declared_nature:
                raise exceptions.ValidationError(
                    _(
                        "'NATURALEZA DEL DECLARADO' is required because "
                        "'CLAVE' is set as %s.",
                        rec.operation_key,
                    )
                )

    revocation = fields.Selection(
        selection=[
            ("X", "X: Persona física"),
            ("", "Empty"),
        ],
        help="""
            REVOCACIÓN

            Para las claves A o B cuando la entidad declarante goce
            del régimen de incentivos fiscales al mecenazgo previsto
            en el Título III de la Ley 49/2002 y se hubiera producido
            durante el ejercicio, en los términos del art. 17 de dicha
            Ley, la revocación de una donación con derecho a
            deducción recibida en ejercicios anteriores, deberá
            rellenarse este campo con una X, además del resto de
            datos de la donación revocada.

            Para el resto de claves se rellenará a blancos.
        """,
    )
    year_of_revoked_donation = fields.Char(
        string="Year of Revoked Donation",
        size=4,
        help="""
            EJERCICIO EN QUE SE EFECTUÓ LA DONACIÓN REVOCADA

            Para las claves A o B cuando se haya rellenado con X el
            campo "Revocación", se hará constar el ejercicio en el que
            se efectuó la donación revocada. En caso contrario, este
            campo se consignará a ceros.
        """,
    )

    @api.constrains("year_of_revoked_donation")
    def _require_year_of_revoked_donation(self):
        for rec in self:
            if (
                rec.operation_key in ["A", "B"]
                and rec.revocation in ["X"]
                and not rec.year_of_revoked_donation
            ):
                raise exceptions.ValidationError(
                    _(
                        "'EJERCICIO EN QUE SE EFECTUÓ LA DONACIÓN REVOCADA' is "
                        "required because "
                        "'CLAVE' is set as %s and "
                        "'REVOCACIÓN' is set as %s.",
                        rec.operation_key,
                        rec.revocation,
                    )
                )

    kind_of_good = fields.Selection(
        string="Kind of Good",
        selection=[
            ("I", "I: Inmueble"),
            ("V", "V: Valores mobiliarios"),
            ("O", "O: Otros"),
            ("", "Empty"),
        ],
        help="""
            TIPO DE BIEN

            Para las claves C o D, en caso de que se haya marcado la
            casilla "donativo, aportación o disposición en especie", se
            hará constar el tipo de bien cuya aportación o disposición
            se declara, de acuerdo con las siguientes claves:

            ----------------------
            'Clave', 'Descripción'
            ----------------------
            'I', 'Inmueble'
            'V', 'Valores mobiliarios'
            'O', 'Otros'

           En caso contrario se rellenará a blancos.
        """,
    )

    item_identification = fields.Char(
        size=20,
        help="""
            IDENTIFICACIÓN DEL BIEN

            Cuando el campo anterior "TIPO DE BIEN" tenga contenido
            se hará constar la identificación del bien cuya aportación o
            disposición se declara: NRC en caso de inmuebles e ISIN
            en caso de valores mobiliarios. Tratándose de otros bienes
            se rellenará a blancos.
        """,
    )

    @api.constrains("item_identification", "kind_of_good")
    def _require_item_identification(self):
        for rec in self:
            if rec.kind_of_good and not rec.item_identification:
                raise exceptions.ValidationError(
                    _(
                        "'IDENTIFICACIÓN DEL BIEN' is required because "
                        "'TIPO DE BIEN' is set as '%s'.",
                        rec.kind_of_good,
                    )
                )

    donation_recurrence = fields.Selection(
        selection=[
            (
                "1",
                "1: Si en los dos períodos impositivos inmediatos "
                "anteriores se hubieran realizado por el declarado, "
                "donativos donaciones o aportaciones (...)",
            ),
            (
                "2",
                "2: Si en los dos períodos impositivos inmediatos "
                "anteriores no se hubieran realizado por el declarado, "
                "donativos donaciones o aportaciones (...)",
            ),
            ("", "Empty"),
        ],
        compute="_compute_donation_recurrence",
        store=True,
        readonly=False,
        help="""
            RECURRENCIA DONATIVOS

            Deberá cumplimentarse cuando se haya hecho constar en
            el campo «NATURALEZA DEL DECLARANTE» (posición
            160) del tipo de registro 1, el dígito numérico indicativo de
            la naturaleza del declarante 1 y en el campo «CLAVE»
            (posición 78) del tipo de registro 2 la letra A o B. Asimismo,
            deberá cumplimentarse este campo cuando se haya
            hecho constar en el campo «NATURALEZA DEL
            DECLARANTE» (posición 160) del tipo de registro 1, el
            dígito numérico indicativo de la naturaleza del declarante 4
            y en el campo «CLAVE» (posición 78) del tipo de registro
            2 la letra G.

            En dichos supuestos, se cumplimentará este campo según
            el siguiente detalle:

            1: Si en los dos períodos impositivos inmediatos
            anteriores se hubieran realizado por el declarado,
            donativos, donaciones o aportaciones con derecho a
            deducción en favor de dicha entidad por importe igual o
            superior, en cada uno de ellos, al del ejercicio anterior.

            2: Si en los dos períodos impositivos inmediatos
            anteriores no se hubieran realizado por el declarado,
            donativos, donaciones o aportaciones con derecho a
            deducción en favor de dicha entidad por importe igual o
            superior, en cada uno de ellos, al del ejercicio anterior.
        """,
    )

    @api.depends("partner_id")
    def _compute_donation_recurrence(self):
        """
        Introduce automated computation of donation recurrence if the partner
        has declared donations in the last two consecutive years.
        """
        for rec in self:
            if rec.donation_recurrence:
                continue

            previous_year_1 = rec.report_id.year - 1
            previous_year_2 = rec.report_id.year - 2

            # Search for donations made by the partner in the last two preceding years
            previous_donations = rec.search(
                [
                    ("partner_id", "=", rec.partner_id.id),
                    ("report_id.state", "=", "done"),
                    (
                        "report_id.year",
                        "in",
                        [previous_year_1, previous_year_2],
                    ),
                ]
            )
            imported_donations = rec.env["l10n.es.aeat.mod182.import.lines"].search(
                [
                    ("partner_vat", "=", rec.partner_id.vat),
                    ("year", "in", [str(previous_year_1), str(previous_year_2)]),
                ]
            )

            # Create a dictionary mapping each year's donation amount
            donations_by_year = {}

            if previous_donations:
                donations_by_year.update(
                    {
                        donation.report_id.year: donation.amount
                        for donation in previous_donations
                    }
                )

            if imported_donations:
                donations_by_year.update(
                    {
                        donation.year: donation.donation_amount
                        for donation in imported_donations
                    }
                )

            # Retrieve donation amounts for the two preceding years
            donation_year_1 = donations_by_year.get(previous_year_1)
            donation_year_2 = donations_by_year.get(previous_year_2)

            # Check if donations exist for both preceding years
            if donation_year_1 is not None and donation_year_2 is not None:
                # Compare the donation amounts of the two preceding years
                if donation_year_1 >= donation_year_2:
                    rec.donation_recurrence = (
                        "1"  # Condition 1: Donations are equal or increased
                    )
                else:
                    rec.donation_recurrence = (
                        "2"  # Condition 2: Donations have decreased
                    )
            else:
                rec.donation_recurrence = (
                    "2"  # Condition 2: No donations in one or both years
                )

    @api.constrains("donation_recurrence")
    def _require_donation_recurrence(self):
        for rec in self:
            if (
                rec.report_id.declarant_nature in ["1"]
                and rec.operation_key in ["A", "B"]
                and not rec.donation_recurrence
            ):
                raise exceptions.ValidationError(
                    _(
                        "'RECURRENCIA DONATIVOS' is required because "
                        "'NATURALEZA DEL DECLARANTE' is set as %s and 'CLAVE' is set as %s.",
                        rec.report_id.declarant_nature,
                        rec.operation_key,
                    )
                )
            elif (
                rec.report_id.declarant_nature in ["4"]
                and rec.operation_key in ["G"]
                and not rec.donation_recurrence
            ):
                raise exceptions.ValidationError(
                    _(
                        "'RECURRENCIA DONATIVOS' is required because "
                        "'NATURALEZA DEL DECLARANTE' is set as %s and 'CLAVE' is set as %s.",
                        rec.report_id.declarant_nature,
                        rec.operation_key,
                    )
                )

    protected_patrimony_holder_nif = fields.Char(
        string="Protected Patrimony Holder NIF",
        size=9,
        help="""
            N.I.F. DEL TITULAR DEL PATRIMONIO PROTEGIDO

            Cuando el declarante tenga la condición de administrador,
            se consignará en este campo el N.I.F. del titular del
            patrimonio protegido.
        """,
    )
    protected_patrimony_holder_name = fields.Char(
        size=40,
        help="""
            APELLIDOS Y NOMBRE DEL TITULAR DEL PATRIMONIO PROTEGIDO

            Cuando el declarante tenga la condición de administrador,
            se consignará en este campo el primer apellido, un
            espacio, el segundo apellido, un espacio y el nombre
            completo del titular del patrimonio protegido.
        """,
    )

    # ---------------------- #

    @api.depends(
        "partner_country_code", "partner_state_code", "partner_vat", "community_vat"
    )
    def _compute_check_ok(self):
        for record in self:
            errors = []
            if not record.partner_country_code:
                errors.append(_("Without country code"))
            if not record.partner_state_code:
                errors.append(_("Without state code"))
            if record.partner_state_code and not record.partner_state_code.isdigit():
                errors.append(_("State code can only contain digits"))
            if not (record.partner_vat or record.partner_country_code != "ES"):
                errors.append(_("VAT must be defined for Spanish Contacts"))
            record.check_ok = not bool(errors)
            record.error_text = ", ".join(errors)

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        """Loads some partner data when the selected partner changes."""
        if self.partner_id:
            self.update(self.report_id._get_partner_182_identification(self.partner_id))

    @api.depends("report_id.representative_vat")
    def calculate_representative_vat(self):
        for rec in self:
            if rec.report_id.representative_vat:
                rec.representative_vat = rec.report_id.representative_vat

    @api.depends("move_record_ids.move_id.date", "report_id.year")
    def calculate_quarter_totals(self):
        def calc_amount_by_quarter(records, year, month_start):
            day_start = 1
            month_end = month_start + 2
            day_end = monthrange(year, month_end)[1]
            date_start = datetime.date(year, month_start, day_start)
            date_end = datetime.date(year, month_end, day_end)
            return sum(
                records.filtered(
                    lambda x: date_start <= x.move_id.date <= date_end
                ).mapped("amount")
            )

    def action_exception(self):
        self.write({"state": "exception"})

    def get_confirm_url(self):
        self.ensure_one()
        return self._notify_get_action_link("controller", controller="/mod182/accept")

    def get_reject_url(self):
        self.ensure_one()
        return self._notify_get_action_link("controller", controller="/mod182/reject")

    def action_confirm(self):
        self.write({"state": "confirmed"})

    def action_send(self):
        self.write({"state": "sent"})
        self.ensure_one()
        template = self.env.ref("l10n_es_aeat_mod182.email_template_182")
        compose_form = self.env.ref("mail.email_compose_message_wizard_form")
        ctx = dict(
            default_model=self._name,
            default_res_id=self.id,
            default_use_template=bool(template),
            default_template_id=template and template.id or False,
            default_composition_mode="comment",
            mark_invoice_as_sent=True,
        )
        return {
            "name": _("Compose Email"),
            "type": "ir.actions.act_window",
            "view_mode": "form",
            "res_model": "mail.compose.message",
            "views": [(compose_form.id, "form")],
            "view_id": compose_form.id,
            "target": "new",
            "context": ctx,
        }

    def button_print(self):
        return self.env.ref("l10n_es_aeat_mod182.182_partner").report_action(self)

    def button_recompute(self):
        self.ensure_one()
        if self.operation_key not in ("A", "B"):
            return
        self.report_id._create_partner_records(
            partner_record=self,
        )
        self.calculate_representative_vat()
        self.calculate_quarter_totals()
        self.action_pending()

    def send_email_direct(self):
        template = self.env.ref("l10n_es_aeat_mod182.email_template_182")
        for record in self:
            template.send_mail(record.id)
        self.write({"state": "sent"})

    def action_pending(self):
        self.write({"state": "pending"})

    def message_get_suggested_recipients(self):
        """
        Add the invoicing partner to the suggested recipients sending an email.
        """
        recipients = super().message_get_suggested_recipients()
        partner_obj = self.env["res.partner"]
        for record in self:
            partner = partner_obj.browse(
                record.partner_id.address_get(["invoice"])["invoice"]
            )
            record._message_add_suggested_recipient(
                recipients,
                partner=partner,
            )
        return recipients
