from odoo import fields, api, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_group = fields.Many2one(comodel_name='product.group', string='Product Group', readonly=False, required=True)
    barcode = fields.Char(string='Barcode', compute='_compute_barcode')

    @api.depends('product_group')
    def _compute_barcode(self):
        if self.product_group:
            first_two_digits_of_product_group = str(self.product_group.product_group)[:2]
            self.barcode = first_two_digits_of_product_group + '.' + self.env['ir.sequence'].next_by_code('barcode.number')

