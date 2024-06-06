# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    supplier_id = fields.Many2one(
        compute="_compute_supplier_id", readonly=False, store=True
    )

    @api.depends("route_id", "route_id.is_force_default_vendor")
    def _compute_supplier_id(self):
        for rec in self:
            if rec.route_id and rec.route_id.is_force_default_vendor:
                suppliers = rec.product_id._prepare_sellers(False).filtered(
                    lambda x: x.is_promotion and x._is_promotion_active()
                )
                suppliers = suppliers.sorted(key=lambda x: x.price)
                if suppliers:
                    rec.supplier_id = suppliers[0].id
