# Copyright (c) 2013, Siddhant and contributors
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
            "label": _("Gender"),
            "fieldtype": "Data",
            "fieldname": "gender",
            "width": 200
        },
        {
            "label": _("Nos. of Children"),
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
                count(case when gender='Male' then 1 end) as Male,
                count(case when gender='Female' then 1 end) as Female,
                count(case when gender='Other' then 1 end) as Other
    			FROM `tabChildren`
    			GROUP BY gender"""

    result = frappe.db.sql(query,as_dict=1)
    print(result)
    for key, value in result[0].items():
        data.append({
            "gender": key,
            "total_children": value
        })

    return data