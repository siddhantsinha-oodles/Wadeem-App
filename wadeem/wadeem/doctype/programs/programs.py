# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe import _


class Programs(WebsiteGenerator):
	website = frappe._dict(
		page_title_field="program_name",
		condition_field="show_in_website",
		no_cache=1
	)

	def validate(self):
		super(Programs, self).validate()
		self.validate_price()

	def make_route(self):
		if not self.route:
			return '/' + self.scrub(self.program_name)

	def get_context(self, context):
		context.show_search = True
		children = frappe.frappe.get_all("Children", fields=["full_name"])
		context.children = children
		context.title = self.title
		context.parents = [{'name': 'Programs', 'title': _('Programs'), 'route': 'programs'}]
		return context

	def get_title(self):
		return _("Program {0}").format(self.program_name)

	def validate_price(self):
		box_price = 0
		developers_price = 0
		workshop_price = 0

		if self.box_id:
			box_price = self.get_box_price()
		if self.developers:
			developers_price = self.get_developers_rate()
		if self.workshop_id:
			workshop_price = self.get_workshop_price()

		self.price = box_price + developers_price + workshop_price

	def get_box_price(self):
		query = f"SELECT price_list_rate FROM `tabItem Price` WHERE item_code='{self.box_id}'"
		item_bundle = frappe.db.sql(query, as_dict=1)
		return item_bundle[0].get("price_list_rate")

	def get_developers_rate(self):
		rate = 0
		# for single_dev in self.developers:
		# 	rate += single_dev.pay
		return rate

	def get_workshop_price(self):
		workshop_price = 0
		for workshop in self.workshop_id:
			single_workshop_price = frappe.db.get_value("Workshop",workshop.workshop_id,["total_cost"])
			workshop_price += single_workshop_price
		print(workshop_price)
		return workshop_price