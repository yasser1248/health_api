frappe.ui.form.on('Healthcare Settings', {
	setup: function(frm) {

		// filter print formats on doc
		frm.set_query("patient_appointment_print_format",function(doc) {
			return {
				filters: {
					'doc_type':'Patient Appointment',
				}
			};
		});
    },
});