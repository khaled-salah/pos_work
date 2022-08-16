from odoo import models, fields, api, exceptions, _
from odoo.exceptions import UserError, ValidationError
from odoo.tools import float_is_zero, float_compare
import datetime


class SchoolResPartner(models.Model):
    _inherit = 'res.partner'

    student_id = fields.Char(string='Student ID')
    grade = fields.Many2one('student.grade', string='Grade')
    grade_name = fields.Char(related='grade.name', string='Grade')
    classes = fields.Many2one('student.class', string='Class')
    classes_name = fields.Char(related='classes.name', string='Grade')

    school = fields.Many2one('student.school', string='School')
    school_name = fields.Char(related='school.name', string='Grade')
    has_pos_show_logo_partner = fields.Boolean('Show Logo POS Receipt')

    @api.onchange('student_id')
    def cal_student_digit(self):
        for rec in self:
            if rec.student_id:
                print(rec.student_id.isdigit())
                if rec.student_id.isdigit() == False:
                    raise ValidationError('Student ID must be integer values only')
