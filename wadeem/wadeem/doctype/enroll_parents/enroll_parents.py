# -*- coding: utf-8 -*-
# Copyright (c) 2021, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import ast

class EnrollParents(Document):
	pass


@frappe.whitelist(allow_guest=False)
def create_form():
	args = frappe.form_dict
	doc = frappe.new_doc('Enroll Parents')
	if args:
		doc.user_id = args.get('user')
		doc.program_id = args.get('program')
		if args.get('selected_workspaces'):
			workshops = ast.literal_eval(args.get('selected_workspaces'))
			for workshop in workshops:
				doc.append("workshop_id", {
					"workshop_id": workshop
				})
	doc.insert(ignore_permissions=True)
	doc.save(ignore_permissions=True)
	print("in create form",args)
	return doc
