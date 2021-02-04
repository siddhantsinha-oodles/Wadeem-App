// Copyright (c) 2020, Siddhant and contributors
// For license information, please see license.txt

frappe.ui.form.on('Guardian Registration', {
	setup: function(frm) {
		frm.add_fetch("guardians", "guardian_name", "guardian_name");
	},

	enroll: function(frm) {
		frappe.model.open_mapped_doc({
			method: "erpnext.education.api.register_guardian",
			frm: frm
		})
	}

});
