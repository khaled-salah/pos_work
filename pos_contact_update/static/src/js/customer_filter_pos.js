
odoo.define('pos_contact_update.customer_filter_pos', function(require){
    'use strict';

    var models = require('point_of_sale.models');
    var _super_product = models.PosModel.prototype;
    models.load_models({
        model: 'student.grade',
        fields: ['name'],
        domain: [],
        loaded: function(self,grades){
        self.grades = grades;},
    });

    models.load_models({
        model: 'student.school',
        fields: ['name'],
        domain: [],
        loaded: function(self,schools){
        self.schools = schools;},
    });
    models.load_models({
        model: 'student.class',
        fields: ['name'],
        domain: [],
        loaded: function(self,classes){
        self.classes = classes;},
    });

    models.PosModel = models.PosModel.extend({
        initialize: function(session, attributes){
            var self = this;
            models.load_fields('res.partner', ['has_pos_show_logo_partner','student_id','grade','grade_name','classes','classes_name','school','school_name']);
            models.load_fields('res.users', ['has_pos_show_logo']);
            _super_product.initialize.apply(this, arguments);
        }
    });
});