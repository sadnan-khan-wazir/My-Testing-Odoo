# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
from odoo.exceptions import Warning


class Finishurantee(models.Model):
    _name = 'guarantee.closing'
    _rec_name = 'number'

    number = fields.Char('Sequence')
    letter_guarantee_id = fields.Many2one(comodel_name='guarantee.letter', string="Gurantee Letter", domain=[('is_close', '=', False)])

    state = fields.Selection(string="State", selection=[('draft', 'Draft'),
                                                        ('confirm', 'Confirm'),
                                                        ], required=False, default="draft")
    
    partner_id = fields.Many2one(related='letter_guarantee_id.partner_id', string='Customer', comodel_name='res.partner')    
    journal_id = fields.Many2one(related='letter_guarantee_id.journal_id', string='journal')
    letter_type = fields.Selection(string="Letter Type", related='letter_guarantee_id.letter_type')
    bank_expense_account_id = fields.Many2one('account.account', string="Account Expenses Debit")
    transaction_date = fields.Date(string="Transaction Date", related='letter_guarantee_id.transaction_date')
    start_date = fields.Date(string="Start Date", related='letter_guarantee_id.start_date')
    end_date = fields.Date(string="End Date", related='letter_guarantee_id.end_date')
    letter_number = fields.Char('Letter Number', related='letter_guarantee_id.letter_number')
    expenses_amount = fields.Float('Expenses Amount', )
    extend_start_date = fields.Date(string='Extend Start Date', compute='compute_amount')
    extend_end_date = fields.Date('Last Extend End Date', compute='compute_date')

    move_id = fields.Many2one('account.move', 'Account Journal')
    config_id = fields.Many2one(related='letter_guarantee_id.config_id', string='Letter Name')
    note = fields.Text('Note')

    letter_amount = fields.Float('Letter Amount', related='letter_guarantee_id.letter_amount')
    raise_amount = fields.Float('Raise Amount', compute='compute_amount')
    down_amount = fields.Float('Down Amount', compute='compute_amount')
    net_letter_amount = fields.Float('Net Letter Amount', compute='compute_amount')
    cov_letter_amount = fields.Float('Net Cover Amount', compute='compute_amount')
    is_close=fields.Boolean('Is Closed',)


    # @api.depends('letter_guarantee_id')
    # def compute_closed(self):
    #     for rec in self:
    #         letter = self.env['guarantee.letter'].search([('id', '=', rec.letter_guarantee_id.id)])
    #         dw = self.env['guarantee.reduction'].search([('id', '=', rec.letter_guarantee_id.id)])
    #         if rec.state=='confirm':
    #             for dd in dw:

    #                 dd.is_close=True

    #             letter.is_close=True
    #             rec.is_close =letter.is_close
    #         else:
    #             letter.is_close = False
    #             rec.is_close = letter.is_close



    @api.onchange('letter_guarantee_id')
    def compute_date(self):
        for rec in self:
            dat = self.env['guarantee.extension'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)], limit=1,
                                                     order='create_date desc')
            rec.extend_end_date =dat.extend_end_date

    @api.onchange('letter_guarantee_id')
    def compute_amount(self):
        for rec in self:
            raise_guarantee = self.env['guarantee.increase'].search([('letter_guarantee_id','=',rec.letter_guarantee_id.id)])
            r=0.0
            cov=0.0
            for ras in raise_guarantee:
                r= r + ras.raise_amount
                cov= cov + ras.cover_amount
                rec.raise_amount = r
            down_amount =self.env['guarantee.reduction'].search([('letter_guarantee_id','=',rec.letter_guarantee_id.id)])
            x=0.0
            dow_cov=0.0
            for down in down_amount:
                x = x + down.down_amount
                dow_cov = dow_cov + down.cover_amount
                rec.down_amount =x
            rec.net_letter_amount =rec.letter_amount +r-x
            rec.cov_letter_amount = rec.letter_guarantee_id.cover_amount+ cov - dow_cov


    @api.constrains('letter_guarantee_id')
    def _letter_guarantee_id(self):
        if self.letter_guarantee_id:
            downs = self.env['guarantee.closing'].search(
                [('id','!=',self.id),('letter_guarantee_id', '=', self.letter_guarantee_id.id)])
            if downs:
                raise Warning(_('This Gurantee Letter Closed Before'))


    def cancel_button(self):
        for rec in self:
            if rec.move_id:
                rec.move_id.button_cancel()
                rec.move_id.unlink()
                rec.state = 'draft'
                rec.is_close = False
                letter = self.env['guarantee.letter'].search([('id', '=', self.letter_guarantee_id.id)])
                dw = self.env['guarantee.reduction'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                rs = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                ex = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                for dd in dw:
                    dd.is_close = False
                for rais in rs:
                    rais.is_close = False
                for ext in ex:
                    ext.is_close = False
                for li in letter:
                    li.is_close = False

            else:
                rec.is_close = False
                letter = self.env['guarantee.letter'].search([('id', '=', self.letter_guarantee_id.id)])
                dw = self.env['guarantee.reduction'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                rs = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                ex = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
                for dd in dw:
                    dd.is_close = False
                for rais in rs:
                    rais.is_close = False
                for ext in ex:
                    ext.is_close = False
                for li in letter:
                    li.is_close = False
                rec.state = 'draft'

    @api.constrains('letter_guarantee_id')
    def _letter_guarantee_id(self):
        if self.letter_guarantee_id:
            letter = self.env['guarantee.letter'].search([('id', '=', self.letter_guarantee_id.id)])
            for li in letter:
                li.is_close =True


    def confirm_button(self):
        for rec in self:
            config = self.env['guarantee.letter.setting'].search([('id', '=', rec.config_id.id)])
            move = self.env['account.move'].create({
                'journal_id': rec.journal_id.id,
                'date': rec.start_date,
            })
            self.env['account.move.line'].with_context(check_move_validity=False).create(
                {
                    'move_id': move.id,
                    'account_id': rec.journal_id.default_debit_account_id.id,
                    'name': 'Close Gurantee Letter',
                    'debit': rec.cov_letter_amount,
                })
            self.env['account.move.line'].with_context(check_move_validity=False).create(
                {
                    'move_id': move.id,
                    'account_id': config.account_id.id,
                    'name': 'Close Gurantee Letter',
                    'credit': rec.cov_letter_amount,
                })
            move.post()
            rec.move_id=move.id
            rec.state = "confirm"
            letter = self.env['guarantee.letter'].search([('id', '=', rec.letter_guarantee_id.id)])
            dw = self.env['guarantee.reduction'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
            rs = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
            ex = self.env['guarantee.increase'].search([('letter_guarantee_id', '=', rec.letter_guarantee_id.id)])
            for dd in dw:
                dd.is_close = True
            for rais in rs:
                rais.is_close = True
            for ext in ex:
                ext.is_close = True
            letter.is_close = True
            rec.is_close = letter.is_close


    @api.model
    def create(self, vals):
        seq = self.env['ir.sequence'].next_by_code('guarantee.closing') or '/'
        vals['number'] = seq
        return super(Finishurantee, self).create(vals)

