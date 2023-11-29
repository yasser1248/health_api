# Copyright (c) 2023, IT Systematic and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	data = get_data(filters)
	columns = get_columns(filters)
	return columns, data


def get_data(filters:dict={}):
    conditions = ""
    
    if filters.get("party_name") :
        conditions += "AND q.party_name = %(party_name)s"
    
    if filters.get("from_date") and filters.get("to_date") :
        conditions += "AND (q.transaction_date >= %(from_date)s AND q.transaction_date <= %(to_date)s )"
        
    if filters.get("item_code") :
        conditions += "AND qi.item_code = %(item_code)s "
    
    quotations = frappe.db.sql("""
								SELECT 
        							q.name , q.transaction_date , q.status , q.quotation_to , q.party_name ,
									qi.item_code , qi.qty , qi.rate , qi.amount 
								FROM `tabQuotation` q
								LEFT JOIN `tabQuotation Item` qi
									ON q.name = qi.parent
								WHERE q.docstatus = 1
									{conditions}


                            """.format(conditions=conditions),{
								"party_name" : filters.get("party_name") ,
								"from_date" : filters.get("from_date"),
								"to_date" : filters.get("to_date"),
								"item_code" : filters.get("item_code"),
							} , as_dict=1)
    return quotations

def get_columns(filters:dict={}):
    columns = [
        {
			"label":_("Quotation ID"),
			"fieldname":"name",
			"fieldtype":"Link",
			"options":"Quotation",
			"width":"180",
		},
        {
			"label":_("Date"),
			"fieldname":"transaction_date",
			"fieldtype":"Date",
			"width":"100",
		},
        {
			"label":_("Status"),
			"fieldname":"status",
			"fieldtype":"Select",
			"width":"100",
		},
        {
			"label":_("Quotation To"),
			"fieldname":"quotation_to",
			"fieldtype":"Link",
			"options":"DocType",
			"width":"120",
		},
        {
			"label":_("Party Name"),
			"fieldname":"party_name",
			"fieldtype":"Dynamic Link",
			"options":"quotation_to",
			"width":"200",
		},
        {
			"label":_("Item Code"),
			"fieldname":"item_code",
			"fieldtype":"Link",
			"options":"Item",
			"width":"250",
		},
        {
			"label":_("Qty"),
			"fieldname":"qty",
			"fieldtype":"Float",
			"width":"100",
		},
        {
			"label":_("Rate"),
			"fieldname":"rate",
			"fieldtype":"Float",
			"width":"100",
		},
        {
			"label":_("Amount"),
			"fieldname":"amount",
			"fieldtype":"Float",
			"width":"100",
		},
	] 
    return columns


