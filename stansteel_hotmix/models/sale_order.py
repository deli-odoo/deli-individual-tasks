from odoo import fields, api, models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    cost_total = fields.Float(string="Total Cost", compute="_compute_total_cost")

    @api.depends('order_line')
    def _compute_total_cost(self):
        total = 0.0
        for line in self.order_line:
            if line.ext_cost:
                total += line.ext_cost
        self.cost_total = total