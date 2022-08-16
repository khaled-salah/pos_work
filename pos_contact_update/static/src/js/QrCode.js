odoo.define('pos_contact_update.pos', function (require) {
"use strict";

const { Gui } = require('point_of_sale.Gui');
var models = require('point_of_sale.models');
var rpc = require('web.rpc');
var session = require('web.session');
var core = require('web.core');
var utils = require('web.utils');

var _t = core._t;
var round_di = utils.round_decimals;


var _super_order = models.Order.prototype;
models.Order = models.Order.extend({
    export_for_printing: function() {
      var result = _super_order.export_for_printing.apply(this,arguments);
          const codeWriter = new window.ZXing.BrowserQRCodeSvgWriter()
          console.log('result.name',result.name)
          let qr_values = this.compute_sa_qr_code(result.name);
          let qr_code_svg = new XMLSerializer().serializeToString(codeWriter.write(qr_values, 150, 150));
          result.qr_code = "data:image/svg+xml;base64,"+ window.btoa(qr_code_svg);

      return result;
    },
    compute_sa_qr_code(name) {
        const seller_name_enc = this._compute_qr_code_field(1, name);
        const str_to_encode = seller_name_enc;

        let binary = '';
        for (let i = 0; i < str_to_encode.length; i++) {
            binary += String.fromCharCode(str_to_encode[i]);
        }
        return btoa(binary);
    },

    _compute_qr_code_field(tag, field) {
        const textEncoder = new TextEncoder();
        const name_byte_array = Array.from(textEncoder.encode(field));
        const name_tag_encoding = [tag];
        const name_length_encoding = [name_byte_array.length];
        return name_tag_encoding.concat(name_length_encoding, name_byte_array);
    },

});

});
