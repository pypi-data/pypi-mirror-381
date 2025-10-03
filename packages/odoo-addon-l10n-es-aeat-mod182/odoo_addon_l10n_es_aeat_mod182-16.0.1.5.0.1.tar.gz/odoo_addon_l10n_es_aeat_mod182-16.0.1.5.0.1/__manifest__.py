# Copyright 2004-2011 Pexego Sistemas Informáticos. (http://pexego.es)
# Copyright 2012 NaN·Tic  (http://www.nan-tic.com)
# Copyright 2013 Acysos (http://www.acysos.com)
# Copyright 2013 Joaquín Pedrosa Gutierrez (http://gutierrezweb.es)
# Copyright 2016 Tecnativa - Antonio Espinosa
# Copyright 2016 Tecnativa - Angel Moya <odoo@tecnativa.com>
# Copyright 2018 PESOL - Angel Moya <info@pesol.es>
# Copyright 2014-2022 Tecnativa - Pedro M. Baeza
# Copyright 2023-2024 QubiQ - Adrià González <adria.gonzalez@qubiq.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "AEAT modelo 182",
    "version": "16.0.1.5.0",
    "author": "Tecnativa,PESOL,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-spain",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": [
        "account_tax_balance",
        "base_vat",
        "l10n_es",
        "l10n_es_aeat",
        "portal",
    ],
    "data": [
        "data/aeat_export_mod182_partner_data.xml",
        "data/aeat_export_mod182_data.xml",
        "data/regional_community_deduction_data.xml",
        "data/tax_code_map_mod182_data.xml",
        "security/ir.model.access.csv",
        "security/mod_182_security.xml",
        "views/account_move_view.xml",
        "views/mod182_import_lines_view.xml",
        "views/mod182_templates.xml",
        "views/mod182_view.xml",
        "views/regional_community_deduction_view.xml",
        "views/report_182_partner.xml",
        "views/res_partner_view.xml",
        "wizard/mod182_import_wizard_menu.xml",
        "wizard/mod182_import_wizard_views.xml",
        "data/mail_template_data.xml",
    ],
    "installable": True,
    "images": ["images/l10n_es_aeat_mod182.png"],
}
