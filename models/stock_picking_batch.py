from odoo import models, fields

class StockPickingBatch(models.Model):
    _inherit='stock.picking.batch'


    # main fields
    driver_assistant = fields.Many2one('res.partner', string="Ayudante")
    n_platforms = fields.Integer("Numero de Tarimas")

    # Page fields
    truck_type = fields.Selection([
        ('complete','Caja Completa'),
        ('consolidated','Consolidado')
    ], "Tipo")
    driver = fields.Char("Chofer")
    plate = fields.Char("Placa")
    capacity = fields.Char("Capacidad")
    invoice_ref = fields.Char("Referencia Factura")
