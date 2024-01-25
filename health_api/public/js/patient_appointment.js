frappe.ui.form.on("Patient Appointment", {
  refresh: function (frm) {
    if (frm.doc.__islocal == undefined) {
      frm.toggle_reqd("mode_of_payment", 1);
    }
    if (frm.doc.invoiced == 0 && frm.doc.status != "") {
      frm.add_custom_button("Pay", () => {
        if (!frm.doc.mode_of_payment) {
          frappe.msgprint({
            title: __("Not Allowed"),
            message: __("Please select Mode Of Payment"),
            indicator: "red",
          });
        } else {
          frm.call({
            method: "health_api.override.create_sales_invoice",
            args: {
              doc_name: frm.doc.name,
            },
            callback: function (r) {
              setTimeout(() => {
                frm.remove_custom_button("Pay");
                frm.reload_doc();
              }, 10);
              // print the patient appointment on pay
              frappe.db.get_doc("Healthcare Settings").then((doc) => {
                if (doc.enable_patient_appointment_autoprint) {
                  load_print_page(
                    doc.patient_appointment_print_format,
                    frm.doc.name
                  );
                }
              });
            },
          });
        }
      });
    }
  },
  patient: function (frm) {
    frm.toggle_display("mode_of_payment", 1);
    frm.toggle_display("paid_amount", 1);
    // frm.toggle_reqd('mode_of_payment', 1);
  },
});

async function load_print_page(doc_print_format, doc_name) {
  const print_format = doc_print_format;
  var letter_head;
  await frappe.db.get_doc("Letter Head",null, { 'is_default': 1 })
  .then((doc) => {
    letter_head = doc.name || 0;
  });
  console.log(letter_head)

  const url =
    frappe.urllib.get_base_url() +
    "/printview?doctype=Patient%20Appointment&name=" +
    doc_name +
    "&trigger_print=1" +
    "&format=" +
    print_format +
    "&no_letterhead=" +
    letter_head +
    "&_lang=ar";
  const printWindow = window.open(url, "Print");
  printWindow.onload =function () {
    printWindow.print();
  };

  // printWindow.print();
  // printWindow.focus();
  // console.log("Prined")
  // printWindow.close();
  // printWindow.addEventListener(
  //   'load',
  //   function () {
  // 	console.log("loaded")
  // 	printWindow.print();
  // 	// printWindow.close();
  // 	// NOTE : uncomoent this to auto closing printing window
  //   },
  //   true
  // );

}

// function load_print_page(doc_print_format, doc_name) {
//     const print_format = doc_print_format;
//     const letter_head = 0;
//     const url =
//         frappe.urllib.get_base_url() +
//         '/printview?doctype=Patient%20Appointment&name=' +
//         doc_name +
//         '&trigger_print=1' +
//         '&format=' +
//         print_format +
//         '&no_letterhead=' +
//         letter_head +
// 		'&_lang=en';

//     // Create an invisible iframe
//     const iframe = document.createElement('iframe');
//     iframe.style.display = 'none';
//     document.body.appendChild(iframe);

//     // Set the iframe source to the print view URL
//     iframe.src = url;

//     // Wait for the iframe to load and then trigger the print operation
//     iframe.onload = function () {
// 		console.log("loaded")
// 		// var printButton = window.frames[1].document.querySelector("button");
// 		// console.log(printButton)
// 		console.log(iframe.contentWindow)
//         iframe.contentWindow.focus();
//         iframe.contentWindow.print();
//         document.body.removeChild(iframe); // Remove the iframe after printing
//     };
// }
