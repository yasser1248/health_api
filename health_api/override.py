import frappe
from erpnext.healthcare.doctype.healthcare_settings.healthcare_settings import (
	get_income_account,
	get_receivable_account,
)
from erpnext.healthcare.utils import get_service_item_and_practitioner_charge
from erpnext import get_company_currency
from frappe.utils import getdate
from frappe import _
import json

@frappe.whitelist()
def create_sales_invoice(doc_name):
	appointment_doc = frappe.get_doc("Patient Appointment" , doc_name)
	sales_invoice = frappe.new_doc("Sales Invoice")
	sales_invoice.patient = appointment_doc.patient
	sales_invoice.customer = frappe.get_value("Patient", appointment_doc.patient, "customer")
	sales_invoice.currency = frappe.get_value(
		"Customer", sales_invoice.customer, "default_currency"
	) or get_company_currency(appointment_doc.company)

	sales_invoice.appointment = appointment_doc.name
	sales_invoice.due_date = getdate()
	sales_invoice.company = appointment_doc.company
	sales_invoice.debit_to = get_receivable_account(appointment_doc.company)
	if appointment_doc.from_sister_clinic == 0 :
		item = sales_invoice.append("items", {})
		item = get_appointment_item(appointment_doc, item)
	if appointment_doc.appointment_type == "Surgery" :
		surgrey_item = surgrey_item_details(appointment_doc, {})
		sales_invoice.append("items", surgrey_item )


	# Add payments if payment details are supplied else proceed to create invoice as Unpaid
	if appointment_doc.mode_of_payment and appointment_doc.paid_amount:
		sales_invoice.is_pos = 1
		payment = sales_invoice.append("payments", {})
		payment.mode_of_payment = appointment_doc.mode_of_payment
		payment.amount = appointment_doc.paid_amount

	sales_invoice.set_missing_values(for_validate=True)
	sales_invoice.flags.ignore_mandatory = True
	sales_invoice.save(ignore_permissions=True)
	sales_invoice.submit()
	frappe.msgprint(_("Sales Invoice {0} created").format(sales_invoice.name), alert=True)
	frappe.db.set_value(
		"Patient Appointment",
		appointment_doc.name,
		{"invoiced": 1, "ref_sales_invoice": sales_invoice.name},
	)
@frappe.whitelist()
def get_appointment_item(appointment_doc, item):
	details = get_service_item_and_practitioner_charge(appointment_doc)
	# charge = appointment_doc.paid_amount or details.get("practitioner_charge")
	charge = details.get("practitioner_charge")
	item.item_code = details.get("service_item")
	item.description = _("Consulting Charges: {0}").format(appointment_doc.practitioner)
	item.income_account = get_income_account(appointment_doc.practitioner, appointment_doc.company)
	item.cost_center = frappe.get_cached_value("Company", appointment_doc.company, "cost_center")
	item.rate = charge
	item.amount = charge
	item.qty = 1
	item.reference_dt = "Patient Appointment"
	item.reference_dn = appointment_doc.name

	return item


@frappe.whitelist()
def surgrey_item_details(appointment_doc, item):
	details = frappe.get_doc("Item" , appointment_doc.surgrey )
	item['item_code'] = details.get("item_code")
	item['description'] = details.get("description")
	item['income_account'] = frappe.get_cached_value("Company", appointment_doc.company, "default_income_account")
	item['cost_center'] = frappe.get_cached_value("Company", appointment_doc.company, "cost_center")
	item['rate'] = details.get("rate")
	item['amount'] = details.get("rate")
	item['qty'] = 1
	
	return item



@frappe.whitelist()
def patient_appointment_validate(doc, event):
	if doc.invoiced == 0 :
		total = 0
		if doc.from_sister_clinic == 0 :
			details = get_service_item_and_practitioner_charge(doc)
			total += details.get("practitioner_charge")
		if doc.appointment_type == "Surgery" and doc.surgrey :
			total += doc.surgrey_rate

		doc.paid_amount = total

@frappe.whitelist()
def patient_before_save(self,event):
	self.sex = self.animal_sex



@frappe.whitelist()
def get_mobile(document):
	data = json.loads(document)
	if data.get("customer") :
		if frappe.db.exists("Contact" , {"first_name" : data.get("customer")}) :
			mobile = frappe.get_doc("Contact" , {"first_name" : data.get("customer")}) 
			return mobile.mobile_no
