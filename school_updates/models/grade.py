from odoo import models, fields, api, exceptions, _
from odoo.exceptions import UserError, ValidationError

class StudentGrade(models.Model):
    _name = 'student.grade'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char('Name',required=True)


class StudentSchool(models.Model):
    _name = 'student.school'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char('Name',required=True)



class StudentClasses(models.Model):
    _name = 'student.class'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char('Name',required=True)