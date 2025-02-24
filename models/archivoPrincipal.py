# Imports del modelo
from odoo import models, fields, api
from datetime import timedelta


class MiModeloGenerico(models.Model):
    _name="mi.modelo.generico" # es el identificador del modelo, y tiene que llamarse como la clase
    _description = "[Descripcion del modelo]"
    _inherit= ['mail.thread', 'mail.activity.mixin'] # Para habilitar la funcionalidad de seguimiento y actividades dentro de Odoo

    # Ahora tratamos con los campos relevantes de nuestro modelo
    # estos entran por definicion en record tanto aqui como en el kanban[vease más tarde en views]
    name = fields.Char(string="Nombre", required=True, tracking=True)
    descripcion = fields.Text(string="Descripción", tracking=True)
    fecha_creacion = fields.Date(string="Fecha de Creación", default=fields.Date.context_today, tracking=True)
    fecha_caducidad = fields.Date(string="Fecha de Caducidad", compute="_compute_fecha_caducidad", store=True, tracking=True)
    usuario_responsable = fields.Many2one('res.users', string="Responsable", required=True, tracking=True)

    # Campo de estado
    state = fields.Selection([
        ('borrador', 'Borrador'),
        ('proceso', 'En Proceso'),
        ('completado', 'Completado')
    ], string="Estado", default='borrador', tracking=True)

    # Vamos a definir la función de creacion de nuestro modelo
    @api.model
    def create(self, vals):
        record=super(MiModeloGenerico, self).create(vals)
        return record
    
    # Y ahora creamos las funciones para cambiar los valores del Estado
    def action_en_proceso(self):
        self.write({'state': 'proceso'})

    def action_completar(self):
        self.write({'state': 'completado'})

    @api.depends('fecha_crecion')
    def _compute_fecha_caducidad(self):
        for record in self:
            if record.fecha_creacion:
                record.fecha_caducidad = record.fecha_creacion+timedelta(days=30)
            else:
                record.fecha_caducidad = False # así la dejamos vacia si no hay fecha inicial