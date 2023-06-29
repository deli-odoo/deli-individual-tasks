from odoo import fields, api, models

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    cost = fields.Float(string="Cost", compute="_compute_cost")
    ext_cost = fields.Float(string="Ext. Cost", compute="_compute_ext_cost")

    @api.depends('name')
    def _compute_cost(self):
        for line in self:
            if line.product_template_id: 
                line.cost = line.product_template_id.standard_price
            else:
                line.cost = False
    
    @api.depends('name', 'product_uom_qty')
    def _compute_ext_cost(self):
        for line in self:
            if line.cost:
                line.ext_cost = line.cost * line.product_uom_qty
            else:
                line.ext_cost = False