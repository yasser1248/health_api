import frappe
from frappe import _

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def get_user_roles(doctype,txt, searchfield, start, page_len, filters):
	return  frappe.db.sql("""
	SELECT a.name FROM `tabUser` as a 
	INNER JOIN `tabHas Role` as b 
	on a.name = b.parent 
	where b.role = %(role)s
	AND a.{key} LIKE %(txt)s;
    """.format(**{
            'key': searchfield,
        }), {'role': filters.get('role'),'txt': "%{}%".format(txt)})