import re
from html import unescape
from odoo import api, fields, models, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    numero_economico = fields.Char('Número Economico')

    @api.depends('numero_economico', 'model_id.name', 'license_plate')
    def _compute_vehicle_name(self):
        for record in self:
            record.name = (record.numero_economico or '') + '/' + (record.model_id.name or '') + '/' + (record.license_plate or _('No Plate'))

    _sql_constraints = [
        ('unique_numero_economico', 'unique(numero_economico)', 'Ya existe otro vehiculo con el mismo número economico, escoger uno nuevo o revisar información')
    ]