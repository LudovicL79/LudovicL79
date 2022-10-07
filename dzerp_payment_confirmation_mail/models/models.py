# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

import logging
import base64
import logging


from odoo import _, api, fields, models, tools
from odoo.exceptions import UserError

from odoo import api, models, fields, _, SUPERUSER_ID
from odoo.addons.sale.models.payment import PaymentTransaction as OriginalPaymentTransaction
from odoo.addons.mail.models.mail_template import MailTemplate as OriginalMailTemplate

_logger = logging.getLogger(__name__)

#
class PaymentConfirmationMail(models.Model):
    _inherit = 'account.move'

    def payment_confirmation_mail(self):
        if self.env.su:
            # sending mail in sudo was meant for it being sent from superuser
            self = self.with_user(SUPERUSER_ID)

        template = self.env.ref('dzerp_payment_confirmation_mail.mail_template_payment_confirmation')

        if template:
            self.with_context(force_send=True).message_post_with_template(template.id, composition_mode='comment',
                                                                               email_layout_xmlid="mail.mail_notification_paynow")


class InvoiceReportsRefCustom(models.Model):
    _inherit = 'account.payment'

    @api.model
    def create(self, vals):
        res = super(InvoiceReportsRefCustom, self).create(vals)
        sale_order_id = self.env['sale.order'].search([('name', '=', self.ref)],
                                                      limit=1)
        if len(self.reconciled_invoice_ids) == 1:
            invoice = res.reconciled_invoice_ids
            if res.amount == invoice.amount_total:
                invoice.payment_confirmation_mail()
        return res

    def write(self, vals):
        res = super(InvoiceReportsRefCustom, self).write(vals)
        sale_order_id = self.env['sale.order'].search([('name', '=', self.ref)],
                                                      limit=1)
        if len(self.reconciled_invoice_ids) == 1:
            invoice = self.reconciled_invoice_ids
            if self.amount == invoice.amount_total and sale_order_id.website_id:
                invoice.payment_confirmation_mail()
        return res
