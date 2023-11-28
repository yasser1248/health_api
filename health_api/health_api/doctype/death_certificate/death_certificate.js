// Copyright (c) 2023, IT Systematic and contributors
// For license information, please see license.txt

frappe.ui.form.on('Death Certificate', {
	refresh: function(frm) {
		frappe.call({
			method:"erpnext.setup.doctype.company.company.get_default_company_address",
			args:{name:frappe.defaults.get_default('company')},
			callback: function(r){
				if (r.message){
					// frm.set_value("company_address",r.message)
					frappe.db.get_doc("Address", r.message)
						.then(doc => {
							frm.set_value("city",doc.city)
							frm.refresh_field("city")
						})
				}}
			})
		
			// if name is empty
			if (frm.doc.name1 == null){
				console.log("True")
				frm.set_value("name1","")
				frm.refresh_field("name1")
				frm.set_value("gender","")
				frm.refresh_field("gender")
				frm.set_value("id_number","")
				frm.refresh_field("id_number")
				frm.set_value("marital_status","")
				frm.refresh_field("marital_status")
				frm.set_value("nationality","")
				frm.refresh_field("nationality")
				frm.set_value("birth_date","")
				frm.refresh_field("birth_date")
				frm.set_value("religion","")
				frm.refresh_field("religion")
				// frm.set_value("gender","")
				// frm.set_value("gender","")
				// frm.set_value("gender","")
			}
	}
});
