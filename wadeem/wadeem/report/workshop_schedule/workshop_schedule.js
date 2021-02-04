// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Workshop Schedule"] = {
	"filters": [
        {
			"fieldname":"program_id",
			"label": __("Program Name"),
			"fieldtype": "Link",
			"options": "Programs",
		},
		{
			"fieldname":"child_id",
			"label": __("Child Name"),
			"fieldtype": "Link",
			"options": "Children",
		},
		{
			"fieldname":"workshop_id",
			"label": __("Workshop"),
			"fieldtype": "Link",
			"options": "Workshop",
		},
		{
		    "fieldname":"status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": "\nEnrolled \nNot Enrolled \nCompleted"
		}
	]
};
