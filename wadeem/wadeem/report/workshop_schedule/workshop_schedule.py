# Copyright (c) 2013, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns(filters)
    data = get_data(filters)
    # chart = get_chart_data(data)

    return columns, data


def get_columns(filters):
    columns = [
        {
            "label": _("Children"),
            "fieldtype": "Link",
            "fieldname": "child_id",
            "options": "Children",
            "width": 100
        },
        {
            "label": _("Program"),
            "fieldtype": "Link",
            "fieldname": "program_id",
            "options": "Programs",
            "width": 100
        },
        {
            "label": _("Workshop ID"),
            "fieldtype": "Link",
            "fieldname": "workshop_id",
            "options": "Workshop",
            "width": 100
        },
        {
            "label": _("Status"),
            "fieldtype": "Select",
            "fieldname": "application_status",
            "options": "Enrolled \nNot Enrolled \nCompleted",
            "width": 100
        }
    ]
    return columns


def get_data(filters):
    data = []

    session_info_query = f"""
    			SELECT `tabWorkshop_session`.start_time, `tabWorkshop_session`.end_time, `tabWorkshop_session`.name, `tabWorkshop_session`.zoom_link, `tabWorkshop_session`.session_date
    			FROM `tabWorkshop_session`
    			RIGHT JOIN
    			ORDER BY
    					name"""

    map_results = frappe.db.sql(f"""
    			SELECT child_id, program_id, name, application_status
    			FROM `tabEnroll Children`
    			WHERE owner LIKE '{frappe.session.user}'
    			ORDER BY
    					name""", as_dict=1)


    print(map_results)

    for test in map_results:
        data.append({
        'program_id': test.program_id,
        'name': test.name,
        'child_id': test.child_id,
        'application_status': test.application_status
        })

    return data
