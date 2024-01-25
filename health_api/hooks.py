from . import __version__ as app_version

app_name = "health_api"
app_title = "Health Api"
app_publisher = "IT Systematic"
app_description = "Helth Api"
app_email = "sales@itsystematic.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/health_api/css/health_api.css"
# app_include_js = "/assets/health_api/js/health_api.js"

# include js, css files in header of web template
# web_include_css = "/assets/health_api/css/health_api.css"
# web_include_js = "/assets/health_api/js/health_api.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "health_api/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Patient Appointment" : "public/js/patient_appointment.js" ,
    "Patient Encounter" : "public/js/patient_encounter.js" ,
    "Patient" : "public/js/patient.js" ,
	"Nursing Task":"public/js/nursing_task.js",
    "Healthcare Settings":"public/js/healthcare_settings.js"
    
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "health_api.utils.jinja_methods",
#	"filters": "health_api.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "health_api.install.before_install"
# after_install = "health_api.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "health_api.uninstall.before_uninstall"
# after_uninstall = "health_api.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "health_api.utils.before_app_install"
# after_app_install = "health_api.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "health_api.utils.before_app_uninstall"
# after_app_uninstall = "health_api.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "health_api.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"Patient Appointment": {
		"validate": "health_api.override.patient_appointment_validate",
	},
	
}

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"health_api.tasks.all"
#	],
#	"daily": [
#		"health_api.tasks.daily"
#	],
#	"hourly": [
#		"health_api.tasks.hourly"
#	],
#	"weekly": [
#		"health_api.tasks.weekly"
#	],
#	"monthly": [
#		"health_api.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "health_api.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "health_api.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "health_api.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["health_api.utils.before_request"]
# after_request = ["health_api.utils.after_request"]

# Job Events
# ----------
# before_job = ["health_api.utils.before_job"]
# after_job = ["health_api.utils.after_job"]

# User Data Protection
# --------------------


user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"health_api.auth.validate"
# ]

fixtures = [
    {
        "dt": ("Property Setter"),
        "filters": [
            ["doc_type", "in", (
                "Patient-main-field_order",
				"Patient Appointment-from_sister_clinic-hidden",
				"Patient Encounter-main-field_order",
				"Patient Appointment-main-field_order",
				"Appointment Type-main-translated_doctype",
				"Patient Encounter-naming_series-options",
				"Patient Encounter-naming_series-default",
				"Patient Appointment-naming_series-options",
				"Patient Appointment-naming_series-default",
				"Patient Appointment-section_break_3-hidden",
				"Patient Appointment-procedure_template-hidden",
				"Patient Appointment-get_procedure_from_encounter-hidden",
				"Patient Appointment-therapy_type-hidden",
				"Patient Appointment-therapy_plan-hidden",
				"Patient Appointment-duration-hidden",
				"Patient Appointment-status-in_standard_filter",
				"Patient Appointment-status-default",
				"Healthcare Practitioner-naming_series-options",
				"Medical Report-supervising__doctor-fetch_from",
				"Medical Report-doctor_email-fetch_from",
				"Medical Report-doctor_mobile-fetch_from",
				"Medical Report-to-default",
				"Medical Report-from-default",
				"Medical Report-date-default",
				"Healthcare Practitioner-middle_name-hidden",
				"Healthcare Practitioner-main-field_order",
				"Employee-salutation-hidden",
				"Employee-main-field_order",
				"Customer-main-field_order",
				"Clinical Procedure-notes-width",
				"Clinical Procedure-main-field_order",
				"Clinical Procedure-practitioner_name-hidden",
				"Healthcare Service Unit-occupancy_status-in_standard_filter",
				"Inpatient Record-status-in_standard_filter",
				"Inpatient Record-main-field_order",
				"Patient Companions Details-mobile-in_list_view",
				"Patient Companions Details-id_number-in_list_view",
				"Patient Companions Details-rrelative_relation-in_list_view",
				"Patient Companions Details-name1-in_list_view",

			)]]
    },
    # {
    #     "dt": ("Custom Field"),
    #     "filters": [["dt", "in", ("Patient Appointment","Vital Signs" ,"Patient Encounter" ,"Patient")]]
    # },
    {
        "dt": ("Custom Field"),
        "filters": [
            ["name" , "in" , (
                "Item-custom_the_active_ingredient",
                "Item-custom_column_break_sh8al",
                "Item-custom_medicine_name_in_arabic",
                "Item-custom_medicines",
                "Issue-custom_location",
                "Healthcare Practitioner-custom_religion",
                "Healthcare Practitioner-custom_nationality",
                "Employee-custom_nationality",
                "Employee-custom_religion",
                "Customer-custom_religion",
                "Customer-custom_nationality",
                "Patient-custom_nationality",
                "Patient-custom_religion",
                "Clinical Procedure-custom_confirm_notification2",
                "Clinical Procedure-custom_confirm_notification1",
                "Clinical Procedure-custom_confirm_notification",
                "Clinical Procedure-custom_anesthesiologist",
                "Clinical Procedure-custom_column_break_xcrug",
                "Clinical Procedure-custom_healthcare_practitioner_secondary",
                "Clinical Procedure-custom_column_break_5qccc",
                "Clinical Procedure-custom_section_break_zyxo9",
                "Inpatient Record-custom_patient_companions_details",
                "Inpatient Record-custom_patients_companions",
                "Patient Encounter-custom_radiology",
                "Patient Encounter-custom_customer",
                "Patient Appointment-inpatient_visit_charge",
                "Patient Appointment-from_sister_clinic",
                "Patient Appointment-surgrey_rate",
                "Patient Appointment-surgrey",
                "Patient Encounter-radiology",
                "Patient Encounter-surgery",
			)]
            ]
    },

    
    {
        "dt": ("Workspace"),
        "filters": [["name", "in", ("Clinic Ext" ,"Healthcare")]]
    },
	{
		"dt" : ("DocType") ,
		"filters" : [["name", "in", ("Healthcare Settings")]]
	},
    {
        "dt": ("Print Format") ,
        "filters" : [
            ["name" , "in" , ("Patient Appointment" , "Lab test print format 2" , "Custom Lab Test Print")]
		]
	}

]