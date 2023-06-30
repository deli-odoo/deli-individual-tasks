from odoo import fields, api, models

class ConfSetting(models.TransientModel):
    _inherit = "res.config.settings"

    disable_price_and_cart = fields.Boolean(string="Disable Price and Cart", store=True)

    def set_values(self):
        res = super(ConfSetting, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('product.disable_price_and_cart', self.disable_price_and_cart)
        self.disable_price_and_cart = self.env['ir.config_parameter'].get_param('product.disable_price_and_cart')
        enabled_cart_view = self.env.ref('kinsman_enterprises.disable_cart')
        # enabled_price_view = self.env.ref('kinsman_enterprises.disable_price')
        if enabled_cart_view.active != self.disable_price_and_cart:
            enabled_cart_view.active = self.disable_price_and_cart
            # enabled_price_view.active = self.disable_price_and_cart
        return res
    
    @api.model
    def get_values(self):
        res = super(ConfSetting, self).get_values()
        ICPSudo = self.env['ir.config_parameter'].sudo()
        res.update(
            disable_price_and_cart = ICPSudo.get_param('product.disable_price_and_cart'),
        )
        return res
