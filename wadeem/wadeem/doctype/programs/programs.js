// Copyright (c) 2020, Siddhant and contributors
// For license information, please see license.txt

frappe.ui.form.on('Programs', {
    show_register_dialog() {
		if(frappe.session.user === 'Administrator') {
			frappe.msgprint(__('You need to be a user other than Administrator with System Manager and Item Manager roles to register on Marketplace.'));
			return;
		}

		if (!is_subset(['System Manager', 'Item Manager'], frappe.user_roles)) {
			frappe.msgprint(__('You need to be a user with System Manager and Item Manager roles to register on Marketplace.'));
			return;
		}

		this.register_dialog = EnrollDialog(
			__('Enroll in the Program'),
			{
				label: __('Enroll'),
				on_submit: this.children_enrollment.bind(this)
			}
		);

		this.register_dialog.show();
	}
});
