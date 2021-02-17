# Copyright (c) 2013, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	filters = frappe._dict(filters or {})
	print(filters)
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters=None):
	columns = [
		{
			"label": _("Child Name"),
			"fieldtype": "Link",
			"fieldname": "child_id",
			"options": "Children",
			"width": 100
		},
		{
			"label": _("Program Name"),
			"fieldtype": "Link",
			"fieldname": "program_id",
			"options": "Programs",
			"width": 100
		},
	]

	return columns

def get_conditions(filters):
	conditions = {}

	if filters.program_name:
		conditions["program_id"] = filters.program_id
		return conditions

	if filters.child_id:
		conditions["child_id"] = filters.child_id

	return conditions

def get_data(filters):

	data = []

	conditions = get_conditions(filters)
	enroll_data = frappe.db.get_all("Enroll Children", fields=["name", "program_id","child_id","application_status"])
	print(enroll_data)
	for data in enroll_data:
		row = {"ID": data.name, "Child Name":data.child_id ,"Program Name": data.program_id}
		data.append(row)
	return data
