from odoo import models, fields

class StockPickingBatch(models.Model):
    _inherit='stock.picking.batch'


    # main fields
    driver_assistant = fields.Many2one('res.partner', string="Ayudante")

    # Page fields

    truck_type = fields.Selection([
        ('complete','Caja Complete'),
        ('consolidated','Cosolidado')
    ], "Tipo")
    driver = fields.Char("Chofer")
    plate = fields.Char("Placa")
    capacity = fields.Char("Capacidad")
    invoice_ref = fields.Char("Referencia Factura")
    n_platforms = fields.Integer("Numero de Tarimas")
