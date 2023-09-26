


frappe.ui.form.on('Patient Appointment', {
	refresh: function (frm) {
		if (frm.doc.__islocal == undefined) {
			frm.toggle_reqd('mode_of_payment', 1);
		}
		if (frm.doc.invoiced == 0 && frm.doc.status != "") {
			frm.add_custom_button('Pay', () => {
				if (!frm.doc.mode_of_payment) {
					frappe.msgprint({
						title: __('Not Allowed'),
						message: __('Please select Mode Of Payment'),
						indicator: 'red'
					});
				} else {
					frm.call({
						method: "health_api.override.create_sales_invoice",
						args: {
							doc_name: frm.doc.name
						},
						callback: function (r) {
							setTimeout(() => {
								frm.remove_custom_button('Pay');
								frm.reload_doc();
							}, 10);
						},
					})
				}
			});
		}

	},
	patient: function (frm) {
		frm.toggle_display('mode_of_payment', 1);
		frm.toggle_display('paid_amount', 1);
		// frm.toggle_reqd('mode_of_payment', 1);

	},

})
