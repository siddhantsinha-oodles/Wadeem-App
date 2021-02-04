# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
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
            "label": _("ID"),
            "fieldtype": "Data",
            "fieldname": "name",
            "width": 100
        },
        {
            "label": _("Workshop Name"),
            "fieldtype": "Data",
            "fieldname": "workshop_name",
            "width": 200
        },
        {
            "label": _("Total Enrollments"),
            "fieldtype": "Int",
            "fieldname": "total_enrollments",
            "width": 200
        }
    ]

    return columns


def get_conditions(filters):
    conditions = {}
    return conditions
    print("Filters here:", filters)

    if filters.child_id:
        conditions["name"] = filters.name
        return conditions

    if filters.program_id:
        conditions["workshop_name"] = filters.workshop_name

    return conditions


def get_data(filters):
    data = []
    print(filters)
    conditions = get_conditions(filters)

    query = """SELECT 
                `tabEnroll Workshops`.workshop_id AS workshop_id,
                `tabWorkshop`.name AS name,
               `tabWorkshop`.workshop_name AS workshop_name,
                COUNT(`tabEnroll Workshops`.workshop_id) AS total_enrollments
    			FROM `tabEnroll Workshops`
    			LEFT JOIN `tabWorkshop` ON `tabWorkshop`.name = `tabEnroll Workshops`.workshop_id
    			GROUP BY `tabWorkshop`.name
    			ORDER BY `tabWorkshop`.name"""

    map_results = frappe.db.sql(query, filters,as_dict=1)

    print(map_results)

    for test in map_results:
        data.append({
            'workshop_id': test.workshop_id,
            'name': test.name,
            "workshop_name": test.workshop_name,
            'total_enrollments': test.total_enrollments,
        })

    return data
