# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    grade_name = fields.Char(related='grade.name', string='Grade')
    classes_name = fields.Char(related='classes.name', string='Grade')
    school_name = fields.Char(related='school.name', string='Grade')
    has_pos_show_logo_partner = fields.Boolean('Show Logo POS Receipt')
    has_edit_partner_pos = fields.Boolean('Edit POS Partner',store=True)



    # def get_students(self, student_id=2):
    #     list_students = []
    #     print('list_students', list_students)
    #     partners = self.search([('student_id', '=', student_id)])
    #     print('partners', partners)
    #     for partner in partners:
    #         print(partner.name)
    #         list_students.append(partner.id)
    #     return list_students
