from odoo import fields, api, models

class ConfSettings(models.TransientModel):
    _inherit = "res.config.settings"

    disable_price_and_cart = fields.Boolean(string="Disable Price and Cart", store=True)
    print(disable_price_and_cart)