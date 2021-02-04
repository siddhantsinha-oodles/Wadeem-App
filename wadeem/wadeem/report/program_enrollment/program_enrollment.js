// Copyright (c) 2016, Siddhant and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Program Enrollment"] = {
        "filters": [
        {
			"fieldname":"program_id",
			"label": __("Program ID"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"program_name",
			"label": __("Program Name"),
			"fieldtype": "Data",
		},
	]
};
