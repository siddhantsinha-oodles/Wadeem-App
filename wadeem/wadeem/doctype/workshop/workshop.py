# -*- coding: utf-8 -*-
# Copyright (c) 2021, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import time

from datetime import datetime, timedelta

from dateutil import parser


def get_time_from_datetime_str(date_str):
	datetime_obj = convert_str_to_datetime(date_str)
	return datetime_obj.time()


def convert_str_to_datetime(date_str):
	return parser.parse(date_str)

class Workshop(Document):
	def validate(self):
		self.validate_session_time()
		self.validate_cost()

	def validate_session_time(self):
		sessions = self.session_id
		for session in sessions:
			if session.start_time >= session.end_time:
				raise Exception

	def validate_cost(self):

		teacher_rate = self.get_teacher_rate()
		workshop_hours = self.get_hours()
		assistant_teacher_rate = 0
		if self.assistant_teacher:
			assistant_teacher_rate = self.get_assistant_teacher_rate()
		self.total_cost = (teacher_rate + assistant_teacher_rate) * workshop_hours

	def get_teacher_rate(self):

		query = f"SELECT salary_structure FROM `tabSalary Structure Assignment` WHERE employee='{self.teacher_id}'"
		# print(query)
		salary_structure_assignment = frappe.db.sql(query,as_dict=1)
		# print(salary_structure_assignment)
		salary_structure = salary_structure_assignment[0].get('salary_structure')
		# print(salary_structure)
		query = f"SELECT hour_rate FROM `tabSalary Structure` WHERE name='{salary_structure}'"
		hour_rate = frappe.db.sql(query,as_dict=1)
		# print(hour_rate)
		return hour_rate[0].get("hour_rate")

	def get_assistant_teacher_rate(self):

		query = f"SELECT salary_structure FROM `tabSalary Structure Assignment` WHERE employee='{self.assistant_teacher}'"
		salary_structure_assignment = frappe.db.sql(query,as_dict=1)
		salary_structure = salary_structure_assignment[0].get('salary_structure')
		query = f"SELECT hour_rate FROM `tabSalary Structure` WHERE name='{salary_structure}'"
		hour_rate = frappe.db.sql(query,as_dict=1)
		return hour_rate[0].get("hour_rate")

	def get_hours(self):
		sessions = self.session_id
		time_id = 0
		for session in sessions:
			start_time = session.start_time
			end_time = session.end_time
			time_difference = convert_str_to_datetime(end_time) - convert_str_to_datetime(start_time)
			hours = divmod(time_difference.total_seconds(), 3600)
			time_id += hours[0]
		return time_id