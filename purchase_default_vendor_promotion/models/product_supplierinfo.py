# Copyright 2024 Camptocamp (<https://www.camptocamp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class ProductSupplierinfo(models.Model):
    _inherit = "product.supplierinfo"

    def _is_promotion_active(self, date=None):
        self.ensure_one()
        if not date:
            date = fields.Date.today()
        if not self.date_start:
            return self.date_end >= date
        if not self.date_end:
            return date >= self.date_start
        return date >= self.date_start and date <= self.date_end
