# -*- coding: utf-8 -*-

from odoo import fields, models


class AccountBalanceReport(models.TransientModel):
    _inherit = "account.common.account.report"
    _name = 'account.balance.cl.report'
    _description = 'Trial Balance CL Report'

    journal_ids = fields.Many2many('account.journal', 'account_balance_cl_report_journal_rel', 'account_id', 'journal_id', string='Journals', required=True, default=[])

    def _print_report(self, data):
        data = self.pre_print_report(data)
        records = self.env[data['model']].browse(data.get('ids', []))
        return self.env.ref('l10n_cl_balance.action_report_cl_trial_balance').report_action(
            records, data=data)
