# Copyright 2019 Tecnativa - Pedro M. Baeza
# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import http

from odoo.addons.mail.controllers.mail import MailController


class Mod182Controller(http.Controller):
    @http.route(
        "/mod182/accept", type="http", auth="public", methods=["GET"], website=True
    )
    def mod182_accept(self, res_id, token):
        (comparison, record, _) = MailController._check_token_and_record_or_redirect(
            "l10n.es.aeat.mod182.partner_record",
            int(res_id),
            token,
        )
        if comparison and record:
            try:
                record.sudo().action_confirm()
            except Exception:
                return http.request.render("l10n_es_aeat_mod182.communication_failed")
        return http.request.render("l10n_es_aeat_mod182.communication_success")

    @http.route(
        "/mod182/reject", type="http", auth="public", methods=["GET"], website=True
    )
    def mod182_reject(self, res_id, token):
        (comparison, record, _) = MailController._check_token_and_record_or_redirect(
            "l10n.es.aeat.mod182.partner_record",
            int(res_id),
            token,
        )
        if comparison and record:
            try:
                record.sudo().action_exception()
            except Exception:
                return http.request.render("l10n_es_aeat_mod182.communication_failed")
        return http.request.render("l10n_es_aeat_mod182.communication_success")
