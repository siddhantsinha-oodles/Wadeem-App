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
            "label": _("Program ID"),
            "fieldtype": "Data",
            "fieldname": "program_id",
            "width": 100
        },
        {
            "label": _("Program Name"),
            "fieldtype": "Data",
            "fieldname": "program_name",
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
                `tabEnroll Children`.program_id AS program_id,
                `tabPrograms`.name AS name,
               `tabPrograms`.program_name AS program_name,
                COUNT(`tabEnroll Children`.program_id) AS total_enrollments
    			FROM `tabEnroll Children`
    			LEFT JOIN `tabPrograms` ON `tabEnroll Children`.program_id = `tabPrograms`.name
    			GROUP BY `tabPrograms`.name
    			ORDER BY `tabPrograms`.name"""

    map_results = frappe.db.sql(query, filters,as_dict=1)
    print(map_results)
    query_2 = """SELECT 
                    `tabEnroll Parents`.program_id AS program_id,
                    `tabPrograms`.name AS name,
                   `tabPrograms`.program_name AS program_name,
                    COUNT(`tabEnroll Parents`.program_id) AS total_enrollments
        			FROM `tabEnroll Parents`
        			LEFT JOIN `tabPrograms` ON `tabEnroll Parents`.program_id = `tabPrograms`.name
        			GROUP BY `tabPrograms`.name
        			ORDER BY `tabPrograms`.name"""
    map_results_2 = frappe.db.sql(query_2, filters,as_dict=1)
    print("2nd",map_results_2)
    for item in map_results_2:
        map_results.append(item)

    print("3rd", map_results)
    for test in map_results:
        data.append({
            'program_id': test.program_id,
            "program_name": test.program_name,
            'total_enrollments': test.total_enrollments,
        })

    return data