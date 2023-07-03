from odoo import fields, api, models

class ProductGroup(models.Model):
    _name = 'product.group'
    _rec_name = 'product_group'

    _sql_constraints = [
        ('check_product_group', 'CHECK(isinstance(product_group, int))',
         'The product group must be a positive integer with two or more digits')
    ]

    product_group = fields.Integer(string="Product Group", required=True)