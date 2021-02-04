# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import getdate, add_years, nowdate, date_diff


class GuardianRegistration(Document):

	def autoname(self):
		naming_series = Document.get("guardian_naming_series")
		if naming_series:
			self.naming_series = naming_series


	def validate(self):
		self.name = " ".join(filter(None, [self.first_name, self.middle_name, self.last_name]))

	def on_submit(self):
		guardian_form = frappe.get_doc("Guardians", filters={"guardian_registration": self.name})
		if guardian_form:
			guardian_form.insert()
