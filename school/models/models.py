# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from datetime import date, timedelta
import datetime


class school(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    state = fields.Selection([
        ('draft', 'Not Confirmed'),
        ('new', 'New'),
        ('confirmed', 'Confirmed'),
        ('update', 'Update'),
        ('del', 'Del'),
    ], string='Status')
    name = fields.Char('School Name')
    reg_num = fields.Integer('Reg Number')
    address = fields.Char('Address')
    total_students = fields.Char('Total students')
    campus_id = fields.Many2one('subcampus.subcampus', required='1')
    school_type = fields.Selection([('public', 'Public'),
                                    ('private', 'Private')], string="Types of School", required="1")

    date_id = fields.Date('Open date')
    date_chk = fields.Date('Date')
    chk_box = fields.Boolean('Check box')
    # chk = fields.Char('check',compute='difference_chk',)
    rank_auto = fields.Integer( string="Auto Rank")
    # chk = fields.Integer(string="duree stage", store=True)
    chk = fields.Char(string="duree sgtage", store=True)

    @api.onchange('date_chk')
    def _onchange_chk(self):
        v = 6

        date_1 = self.date_id
        date_2 = self.date_chk
        timedelta = date_1 - date_2
        a = timedelta
        c =abs(a)
        self.chk = c
        print(c)
        # cek_day = re.sub('[^0-9]', '', str(cek_hasil))
        # self.chk = (int(cek_day))  # / 100000
    def test(self):
        self.state= 'new'



    # def _auto_rank_populate(self):
    #     for rec in self:
    #         if rec.school_type == "private":
    #             rec.rank_auto = 100
    #         elif rec.school_type == "public":
    #             rec.rank_auto = 50
    #         else:
    #             rec.rank_auto = 00
    @api.onchange('school_type')
    def _onchange_methods(self):
        for rec in self:
            if rec.school_type == "private":
                rec.rank_auto = 100
            elif rec.school_type == "public":
                rec.rank_auto = 50
            else:
                rec.rank_auto = 00
