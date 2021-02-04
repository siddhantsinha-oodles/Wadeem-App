// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Program Report"] = {
	"filters": [
        {
			fieldname:"program_name",
			label: __("Program Name"),
			fieldtype: "Link",
			options: "Programs",
		},
		{
			fieldname:"child_id",
			label: __("Child Name"),
			fieldtype: "Link",
			options: "Children",
		}
	]
};
