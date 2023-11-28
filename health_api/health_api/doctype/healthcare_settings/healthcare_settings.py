# Copyright (c) 2023, IT Systematic and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from healthcare.healthcare.doctype.healthcare_settings.healthcare_settings import HealthcareSettings

class HealthcareSettings(HealthcareSettings):

	def before_save(self):
		self.set_auto_naming_to_practitioner()

	def set_auto_naming_to_practitioner(self):
		naming_rule , autoname = 'By "Naming Series" field' ,'naming_series:'
		if self.practitioner_name_by == "Practitioner Name" :
			naming_rule , autoname = 'By fieldname' , 'field:first_name'

		frappe.db.set_value("DocType" , "Healthcare Practitioner" , {
				"naming_rule" : naming_rule ,
				"autoname":autoname
			})
		frappe.db.commit()
