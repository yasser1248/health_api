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


// add custom button for birth and death certificate
frappe.ui.form.on('Patient', {
    refresh:function(frm){
        add_certificate_buttons(frm)
    }
})

function add_certificate_buttons(frm) {
    frm.add_custom_button(__("Birth Certificate"),function(){
        frappe.route_options = {
            // "birth_day": frm.doc.dob,
            "name1": frm.doc.name,
            // "gender":frm.doc.sex,
            // "religion":frm.doc.custom_religion,
            // "nationality":frm.doc.custom_nationality,
            // city:frappe.db.get_doc("Address",frm.doc.name).city,
            // "blood_type":frm.doc.blood_group,
            // "uid":frm.doc.uid,
            // "father_name":getFatherName(frm.doc.patient_relation),
            // "mother_name":getMotherName(frm.doc.patient_relation),

          };
        frappe.set_route('Form', 'Birth Certificate', 'new-birth-certificate');

    }, __('Create'));

    frm.add_custom_button(__("Death Certificate"),function(){
        frappe.new_doc("Death Certificate",{
            "name1":frm.doc.patient_name,
            // "birth_date":moment("2020-10-10").format("DD-MM-YYYY"),
            // "father_name":getFatherName(frm.doc.patient_relation),
            // "death_date":frappe.datetime.nowdate(),
            // "city":frappe.db.get_doc("Address",frm.doc.name).city,
            // "gender":frm.doc.sex,
            // "religion":frm.doc.custom_religion,
            // "id_number":frm.doc.uid,
            // // "death_time":frappe.datetime.now_time(),
            // "nationality":frm.doc.custom_nationality,
            // "martial_status":frm.doc.martial_status,
            
        })
    }, __('Create'));
    frm.add_custom_button(__("Medical Report"),function(){
        frappe.new_doc("Medical Report",{
            "name_of_patient":frm.doc.patient_name,
            "hospital":frappe.defaults.get_default('company'),
            "nationality":frm.doc.custom_nationality,
            "patient_age":calculate_age(Date.parse(frm.doc.dob))
        })
    }, __('Create'));

    frm.add_custom_button(__("Transfer Letter"),function(){
        frappe.new_doc("Patient Transfer Letter",{
            "patient":frm.doc.name,
            // "uid":frm.doc.uid,
        })
    }, __('Create'));
}

// Function to get Father's name from patient_relation child table
function getFatherName(patientRelationTable) {
    for (var i = 0; i < patientRelationTable.length; i++) {
        if (patientRelationTable[i].relation == 'Father') {
            return patientRelationTable[i].patient;
        }
    }
    return null;  // Return null if no Father record is found
}

// Function to get Mother's name from patient_relation child table
function getMotherName(patientRelationTable) {
    for (var i = 0; i < patientRelationTable.length; i++) {
        if (patientRelationTable[i].relation == 'Mother') {
            return patientRelationTable[i].patient;
        }
    }
    return null;  // Return null if no Father record is found
}

// Function to calculate age from birth date
function calculate_age(birthMS) {
    var age = new Date()
    var today = new Date()
    age.setTime(birthMS);
	var years =  today.getFullYear() - age.getFullYear();
    var months = today.getMonth() - age.getMonth();
    var days = today.getDate() - age.getDate();
	return years + " Year(s) " + months + " Month(s) " + days + " Day(s)";

    
}