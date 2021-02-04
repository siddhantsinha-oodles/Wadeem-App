# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class WorkshopPrograms(Document):


	def get_records(self,workshop_id):

		workshops = frappe.get_doc("Workshop",workshop_id)
		print(workshops)
		return workshops
