// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Benefit Loss for Workshops"] = {
	"filters": [
         {
			"fieldname":"workshop_id",
			"label": __("Workshop"),
			"fieldtype": "Data",
		},
		{
		    "fieldname":"workshop_name",
			"label": __("Workshop"),
			"fieldtype": "Data",
		}
	]
};
