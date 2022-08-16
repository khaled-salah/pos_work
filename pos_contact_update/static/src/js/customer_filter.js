odoo.define('pos_contact_update.customer_filter', function (require) {
    'use strict';

    var PosDB = require('point_of_sale.DB');
    var models = require('point_of_sale.models');


    PosDB.include({
        _partner_search_string: function(partner){
            var str =  partner.name || '';
            if(partner.student_id){
                str += '|' + partner.student_id;
            }
            if(partner.address){
                str += '|' + partner.address;
            }
            if(partner.phone){
                str += '|' + partner.phone.split(' ').join('');
            }
            if(partner.mobile){
                str += '|' + partner.mobile.split(' ').join('');
            }
            if(partner.email){
                str += '|' + partner.email;
            }
            if(partner.vat){
                str += '|' + partner.vat;
            }

            str = '' + partner.id + ':' + str.replace(':','') + '\n';
        return str;
    },
});
});

