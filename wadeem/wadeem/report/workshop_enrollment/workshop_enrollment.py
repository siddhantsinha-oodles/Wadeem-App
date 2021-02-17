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
            "label": _("Workshop ID"),
            "fieldtype": "Data",
            "fieldname": "workshop_id",
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

# def get_conditions(filters):
#     conditions = {}
#
#     if filters.program_id:
#         conditions["program_id"] = filters.program_id
#         return conditions
#
#     if filters.program_name:
#         conditions["program_name"] = filters.program_name
#
#     return conditions

def get_data(filters):
    data = []
    print(filters)
    # conditions = get_conditions(filters)

    query = """SELECT 
                `tabEnroll Workshops`.workshop_id AS workshop_id,
                `tabWorkshop`.name AS name,
               `tabWorkshop`.workshop_name AS workshop_name,
                COUNT(`tabEnroll Children`.name) AS total_enrollments
    			FROM `tabEnroll Children`
    			LEFT JOIN `tabEnroll Workshops` ON `tabEnroll Children`.name = `tabEnroll Workshops`.parent
    			LEFT JOIN `tabWorkshop` ON `tabEnroll Workshops`.workshop_id = `tabWorkshop`.name
    			WHERE `tabEnroll Workshops`.workshop_id IS NOT NULL
    			 AND `tabEnroll Children`.application_status = 'Enrolled'
    			GROUP BY `tabWorkshop`.name
    			ORDER BY `tabWorkshop`.name"""

    map_results = frappe.db.sql(query, filters,as_dict=1)
    print(map_results)
    query_2 = """SELECT 
                `tabEnroll Workshops`.workshop_id AS workshop_id,
                `tabWorkshop`.name AS name,
               `tabWorkshop`.workshop_name AS workshop_name,
                COUNT(`tabEnroll Parents`.name) AS total_enrollments
    			FROM `tabEnroll Children`
    			LEFT JOIN `tabEnroll Workshops` ON `tabEnroll Parents`.name = `tabEnroll Workshops`.parent
    			LEFT JOIN `tabWorkshop` ON `tabEnroll Workshops`.workshop_id = `tabWorkshop`.name
    			WHERE `tabEnroll Workshops`.workshop_id IS NOT NULL
    			    AND `tabEnroll Children`.application_status = 'Enrolled'
    			GROUP BY `tabWorkshop`.name
    			ORDER BY `tabWorkshop`.name"""
    map_results_2 = frappe.db.sql(query_2, filters,as_dict=1)
    print("2nd",map_results_2)
    for item in map_results_2:
        map_results.append(item)

    print("3rd", map_results)
    for test in map_results:
        data.append({
            'workshpo_id': test.workshop_id,
            "workshop_name": test.workshop_name,
            'total_enrollments': test.total_enrollments,
        })

    return data