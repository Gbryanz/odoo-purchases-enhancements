from odoo import models, fields

class PurchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    vendor_ids = fields.Many2many('res.partner', string='Vendors', domain="[('supplier_rank', '>', 0)]")
    bid_ids = fields.One2many('purchase.bid', 'rfq_id', string='Bids')
    winning_bid_id = fields.Many2one('purchase.bid', string='Winning Bid')
    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request')


class PurchaseBid(models.Model):
    _name = 'purchase.bid'
    _description = 'Purchase Bid'

    rfq_id = fields.Many2one('purchase.order', string='RFQ')
    vendor_id = fields.Many2one('res.partner', string='Vendor', required=True)
    bid_amount = fields.Float('Bid Amount', required=True)
    bid_date = fields.Date('Bid Date', default=fields.Date.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('won', 'Won'),
        ('lost', 'Lost')
    ], string='Status', default='draft')
    note = fields.Text('Notes')
