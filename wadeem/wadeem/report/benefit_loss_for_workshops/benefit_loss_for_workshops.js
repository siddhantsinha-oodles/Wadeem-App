// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Benefit Loss for Workshops"] = {
	"filters": [
         {
			"fieldname":"workshop_id",
			"label": __("Workshop ID"),
			"fieldtype": "Data",
		},
		{
		    "fieldname":"workshop_name",
			"label": __("Workshop Name"),
			"fieldtype": "Data",
		},
		{
		    "fieldname":"start_date",
			"label": __("Start Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -12)
		},
		{
		    "fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"default": frappe.datetime.get_today()
		}
	]
};
