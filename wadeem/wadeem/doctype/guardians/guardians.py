# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import pycountry

class Guardians(Document):
	def on_submit(self):
		self.create_guardian()

	def create_guardian(self):

		print("In guardian hook")
		if self.get('user_type') != 'Website User':
			return
		first_name = self.get('first_name')
		email = self.get('email')
		if frappe.db.exists("Guardians", {'first_name': first_name, 'email': email}):
			print("Guardian not created")
			return
		else:
			print("Creating New Guardian")
			guardian = frappe.new_doc("Guardians")
			guardian.update({
				"first_name": first_name,
				"email": email,
				"guardian_user": email
			})
			guardian.flags.ignore_mandatory = True
			guardian.insert(ignore_permissions=True)
			print("Guardian hook completed")
			return