# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import date
from dateutil.relativedelta import relativedelta
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
            "label": _("Age Group"),
            "fieldtype": "Data",
            "fieldname": "age_group",
            "width": 200
        },
        {
            "label": _("Total Children Enrolled"),
            "fieldtype": "Int",
            "fieldname": "total_children",
            "width": 200
        }
    ]

    return columns


def get_conditions(filters):
    conditions = {}

    if filters.get("age_group"):
        conditions["age_group"] = filters.age_group

    return conditions

def get_data(filters):
    data = []
    print(filters)
    conditions = get_conditions(filters)

    query = """SELECT 
                `tabChildren`.name AS child,
                `tabChildren`.birth_date as birth_date,
               `tabEnroll Children`.child_id AS child_id,
                `tabEnroll Children`.application_status AS application_status
    			FROM `tabEnroll Children`
    			LEFT JOIN `tabChildren` ON `tabChildren`.name = `tabEnroll Children`.child_id
    			WHERE `tabEnroll Children`.application_status = 'Enrolled'
    			ORDER BY `tabChildren`.name"""

    result = frappe.db.sql(query,as_dict=1)

    print(result)
    age_results = {
        "0-5": 0,
        "5-10": 0,
        "10-15": 0,
        "15-20": 0
    }
    for item in result:
        birth_date = item.get("birth_date")
        age = relativedelta(date.today(), birth_date).years
        if 0 <= age < 5:
            age_results["0-5"] += 1
        elif 5 <= age < 10:
            age_results["5-10"] += 1
        elif 10 <= age < 15:
            age_results["10-15"] += 1
        elif 15 <= age < 20:
            age_results["15-20"] += 1

    for key, value in age_results.items():
        data.append({
            "age_group": key,
            "total_children": value,
        })

    return data
