// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Enroll Report"] = {
	"filters": [
        {
			"fieldname":"name",
			"label": __("ID"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"workshop_name",
			"label": __("Workshop Name"),
			"fieldtype": "Data",
		},
	]
};
