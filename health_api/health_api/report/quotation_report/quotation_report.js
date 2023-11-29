// Copyright (c) 2023, IT Systematic and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Quotation Report"] = {
	"filters": [
		{
			fieldname:"from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.datetime.add_months(frappe.datetime.get_today(), -1)
		},
		{
			fieldname:"to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: frappe.datetime.get_today()
		},
		{
			"fieldname":"quotation_to",
			"label": __("Quotation To"),
			"fieldtype": "Link",
			"options": "DocType",
			"get_query": function() {
				return {
					filters: {"name": ["in", ["Customer", "Lead" , "Prospect"]]}
				}
			}
		},
		{
			fieldname : "party_name" ,
			label: __("Party") ,
			fieldtype : "Dynamic Link" ,
			options : "quotation_to",
		},
		{
			fieldname : "item_code" ,
			label: __("Item") ,
			fieldtype : "Link" ,
			options : "Item",
		}
	]
};
