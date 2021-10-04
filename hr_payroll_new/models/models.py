# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil import relativedelta
import babel
from datetime import date, datetime, time
from dateutil.relativedelta import relativedelta
from pytz import timezone
from odoo import api, fields, models, tools, _
from odoo.exceptions import UserError, ValidationError

from odoo.tools.safe_eval import datetime


class hr_payroll_new(models.Model):
    _inherit = 'hr.payslip'

    chk = fields.Char(string="Number of days", store=True)

    @api.model
    def get_worked_day_lines(self, contracts, date_from, date_to):
        """
                @param contract: Browse record of contracts
                @return: returns a list of dict containing the input that should be applied for the given contract between date_from and date_to
                """
        res = []
        # fill only if the contract as a working schedule linked
        for contract in contracts.filtered(lambda contract: contract.resource_calendar_id):
            day_from = datetime.combine(fields.Date.from_string(date_from), time.min)
            day_to = datetime.combine(fields.Date.from_string(date_to), time.max)

            # compute leave days
            leaves = {}
            calendar = contract.resource_calendar_id
            tz = timezone(calendar.tz)
            # day_leave_intervals = contract.employee_id.list_leaves(day_from, day_to, calendar=contract.resource_calendar_id)
            day_leave_intervals = contract.employee_id.list_leaves(day_from, day_to,
                                                                   calendar=contract.resource_calendar_id)
            for day, hours, leave in day_leave_intervals:
                holiday = leave.holiday_id
                current_leave_struct = leaves.setdefault(holiday.holiday_status_id, {
                    'name': holiday.holiday_status_id.name or _('Global Leaves'),
                    'sequence': 5,
                    'code': holiday.holiday_status_id.name or 'GLOBAL',
                    'number_of_days': 0.0,
                    'number_of_hours': 0.0,
                    'contract_id': contract.id,
                })
                current_leave_struct['number_of_hours'] += hours
                work_hours = calendar.get_work_hours_count(
                    tz.localize(datetime.combine(day, time.min)),
                    tz.localize(datetime.combine(day, time.max)),
                    compute_leaves=False,
                )
                if work_hours:
                    current_leave_struct['number_of_days'] += hours / work_hours

            # compute worked days
            c = contract.first_contract_date
            d = self.date_from
            f = c.month
            e = d.month
            if f == e:

                first_contract_date = datetime.combine(fields.Date.from_string(contract.first_contract_date), time.max)

                # work_data = contract.employee_id._get_work_days_data(day_from, day_to, calendar=contract.resource_calendar_id)
                work_data = contract.employee_id._get_work_days_data(day_from, first_contract_date,
                                                                     calendar=contract.resource_calendar_id)
                attendances = {
                    'name': _("Normal Working Days paid at 100%"),
                    'sequence': 1,
                    'code': 'WORK100',
                    'number_of_days': work_data['days'],
                    'number_of_hours': work_data['hours'],
                    'contract_id': contract.id,
                }
            else:
                work_data = contract.employee_id._get_work_days_data(day_from, day_to,
                                                                     calendar=contract.resource_calendar_id)

                attendances = {
                    'name': _("Normal Working Days paid at 100%"),
                    'sequence': 1,
                    'code': 'WORK100',
                    'number_of_days': work_data['days'],
                    'number_of_hours': work_data['hours'],
                    'contract_id': contract.id,
                }

            res.append(attendances)
            res.extend(leaves.values())

        return super(hr_payroll_new, self).get_worked_day_lines()





@api.onchange('date_to')
def _onchange_chk(self):
    # datetime.datetime.strptime('2012-01-01', '%Y-%m-%d')
    date_1 = self.contract_id.first_contract_date
    if date_1:
        d = date_1.month

        date_2 = self.date_to
        c = date_2.month
        if d == c:
            timedelta = date_1 - date_2
            a = timedelta
            c = abs(a)
            self.chk = c
            print(c)
        else:
            timedelta = self.date_from - date_2
            a = timedelta
            c = abs(a)
            self.chk = c
            print(c)

    # timedelta = date_1 - date_2
    # a = timedelta
    # c = abs(a)
    # self.chk = c
    # print(c)
