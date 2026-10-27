from datetime import date, timedelta
from odoo import api, fields, models

class TimePeriod(models.Model):
    _name = 'time.period'
    _description = 'Time Period'
    _order = 'period_start, grain'

    # period_id = the built-in `id` (PK)
    name = fields.Char(compute='_compute_name', store=True)
    grain = fields.Selection(
        [('day', 'Day'), ('week', 'Week'), ('month', 'Month'),
         ('quarter', 'Quarter'), ('year', 'Year')], required=True)
    period_index = fields.Integer()
    period_start = fields.Date(required=True)
    period_end = fields.Date(required=True)
    year = fields.Integer(required=True)
    month = fields.Integer()
    day = fields.Integer()
    day_of_week = fields.Integer()
    week_of_year = fields.Integer()

    _sql_constraints = [
        ('grain_start_uniq', 'unique(grain, period_start)', 'Period already exists.'),
    ]

    @api.depends('grain', 'period_start')
    def _compute_name(self):
        for r in self:
            r.name = f"{r.grain} {r.period_start}"

    @api.model
    def generate_days(self, start, end):
        existing = set(self.search([('grain', '=', 'day')]).mapped('period_start'))
        vals, d, idx = [], start, 0
        while d <= end:
            if d not in existing:
                vals.append({
                    'grain': 'day', 'period_index': idx,
                    'period_start': d, 'period_end': d,
                    'year': d.year, 'month': d.month, 'day': d.day,
                    'day_of_week': d.weekday(),
                    'week_of_year': d.isocalendar()[1],
                })
            d += timedelta(days=1)
            idx += 1
        return self.create(vals)

    @api.model
    def action_generate_current_year(self):
        year = date.today().year
        self.generate_days(date(year, 1, 1), date(year, 12, 31))
        return True