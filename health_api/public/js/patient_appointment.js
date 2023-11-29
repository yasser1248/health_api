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
							// print the patient appointment on pay
							frappe.db.get_doc("Healthcare Settings")
								.then(doc => {
									if (doc.enable_patient_appointment_autoprint) {
										console.log("Checked");
										load_print_page(doc.patient_appointment_print_format,frm.doc.name);
									}
								})

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

// function load_print_page(doc_print_format,doc_name) {
// 	const print_format =
// 	doc_print_format;
// 	const letter_head = 0;
// 	const url =
// 	  frappe.urllib.get_base_url() +
// 	  '/printview?doctype=Patient%20Appointment&name=' +
// 	  doc_name +
// 	  '&trigger_print=1' +
// 	  '&format=' +
// 	  print_format +
// 	  '&no_letterhead=' +
// 	  letter_head;
// 	const printWindow = window.open(url, 'Print');
// 	// printWindow.addEventListener(
// 	//   'load',
// 	//   function () {
// 	// 	console.log("loaded")
// 	// 	printWindow.print();
// 	// 	// printWindow.close();
// 	// 	// NOTE : uncomoent this to auto closing printing window
// 	//   },
// 	//   true
// 	// );
// 	printWindow.onload = function () {
// 		printWindow.focus();
// 		printWindow.print();

// 	}
//   }

function load_print_page(doc_print_format, doc_name) {
    const print_format = doc_print_format;
    const letter_head = 0;
    const url =
        frappe.urllib.get_base_url() +
        '/printview?doctype=Patient%20Appointment&name=' +
        doc_name +
        '&trigger_print=1' +
        '&format=' +
        print_format +
        '&no_letterhead=' +
        letter_head;

    // Create an invisible iframe
    const iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    document.body.appendChild(iframe);

    // Set the iframe source to the print view URL
    iframe.src = url;

    // Wait for the iframe to load and then trigger the print operation
    iframe.onload = function () {
        iframe.contentWindow.focus();
        iframe.contentWindow.print();
        document.body.removeChild(iframe); // Remove the iframe after printing
    };
}
