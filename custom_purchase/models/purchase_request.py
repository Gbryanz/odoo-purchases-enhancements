from odoo import models, fields, api

class PurchaseRequest(models.Model):
    _name = 'purchase.request'
    _description = 'Purchase Request'

    name = fields.Char('Request Reference', required=True, copy=False, readonly=True, default='New')
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True)
    department_id = fields.Many2one('hr.department', string='Department')
    date_request = fields.Date('Request Date', default=fields.Date.today())
    state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('rfq_created', 'RFQ Created'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft')
    description = fields.Text('Description')
    line_ids = fields.One2many('purchase.request.line', 'request_id', 'Products')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('purchase.request') or 'New'
        return super(PurchaseRequest, self).create(vals)

class PurchaseRequestLine(models.Model):
    _name = 'purchase.request.line'
    _description = 'Purchase Request Line'

    request_id = fields.Many2one('purchase.request', string='Purchase Request')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Text('Description')
    quantity = fields.Float('Quantity', default=1.0)
    uom_id = fields.Many2one('uom.uom', string='Unit of Measure')

