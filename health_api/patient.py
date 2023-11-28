import frappe
from frappe import _
import json

@frappe.whitelist()
def make_birth_certificate(patient):
    patient = json.loads(patient)
    frappe.errprint(patient)
    # Assuming you have a Birth Certificate DocType with the necessary fields
    birth_certificate = frappe.new_doc('Birth Certificate')
    frappe.errprint(patient.get('patient_name'))
    birth_certificate.name1 = patient.get('patient_name')
    if patient.get('custom_religion'):
        birth_certificate.custom_religion = patient.get('custom_religion')
    if patient.get('dob')  :
        birth_certificate.birth_day = patient.get('dob')  

    # Set other required fields

    try:
        birth_certificate.insert()
        return birth_certificate.name
    except frappe.exceptions.ValidationError as e:
        frappe.msgprint(f"Validation Error: {e}")
        return None