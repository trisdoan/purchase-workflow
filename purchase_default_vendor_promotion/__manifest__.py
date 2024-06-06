# Copyright 2024 Camptocamp (<https://www.camptocamp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Purchase Default Vendor with Promotion",
    "version": "16.0.1.0.0",
    "development_status": "Beta",
    "category": "Purchase Management",
    "summary": "Set default vendor with promotion in Replenishment",
    "author": "Camptocamp, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/purchase-workflow",
    "license": "AGPL-3",
    "depends": ["purchase_vendor_promotion"],
    "data": [
        "views/stock_route.xml",
    ],
    "installable": True,
    "auto_install": False,
}
