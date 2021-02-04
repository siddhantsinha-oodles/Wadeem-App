# Copyright (c) 2013, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	if not filters:
		filters = {}

	# columns = get_columns(filters)
	# data = get_data(filters)
	# # chart = get_chart_data(data)
	# return columns, data

# def get_columns(filters):
# 	columns = [
#         {
#             "label": _("Workshop ID"),
#             "fieldtype": "Data",
#             "fieldname": "workshop_id",
#             "width": 200
#         },
#         {
#             "label": _("Workshop Name"),
#             "fieldtype": "Data",
#             "fieldname": "workshop_name",
#             "width": 200
#         }
#     ]
#
#     return columns
