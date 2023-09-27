// frappe.ui.form.on('Patient', {
// 	customer(frm) {
//         frm.call({
//             method: 'health_api.override.get_mobile',
//             args: {
//                 document: frm.doc
//             },
//             freeze: true,
//             callback: (r) => {
//                 frm.set_value("mobile" , r.message)
//             },
//             // error: (r) => {

//             // }
//         })
// 	}
// })