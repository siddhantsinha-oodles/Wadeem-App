from __future__ import unicode_literals
from frappe.model.naming import get_default_naming_series
import frappe
from frappe.utils import parse_addr

def get_context(context):
	# do your magic here
	pass

@frappe.whitelist(allow_guest=True)
def create_lead():
	args = frappe.form_dict
	print(args)
	creator_name = None
	email = None
	notes = None
	phone = None
	event_type = None
	if args:
		creator_name = args.get('person')
		notes = args.get('message')
		phone = args.get('phone')
		email = args.get("email")
		event_type = args.get("event_type")
	try:
		lead = frappe.get_doc({
			'doctype': "Lead",
			'lead_name': creator_name,
			'email_id': email,
			'status': "Lead",
			'notes': notes,
			'phone': phone,
			"naming_series": get_default_naming_series("Lead")
		})
		lead.insert(ignore_permissions=True)
	except Exception as e:
		print("in Exception:")
		print(e)
	return True

