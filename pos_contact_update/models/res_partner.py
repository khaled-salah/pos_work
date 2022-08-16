# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    has_pos_show_logo_partner = fields.Boolean()


    # def get_students(self, student_id=2):
    #     list_students = []
    #     print('list_students', list_students)
    #     partners = self.search([('student_id', '=', student_id)])
    #     print('partners', partners)
    #     for partner in partners:
    #         print(partner.name)
    #         list_students.append(partner.id)
    #     return list_students
