# Copyright (c) 2013, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from datetime import date


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
            "width": 200
        },
        {
            "label": _("Workshop Name"),
            "fieldtype": "Data",
            "fieldname": "workshop_name",
            "width": 200
        },
        {
            "label": _("Total Cost"),
            "fieldtype": "Float",
            "fieldname": "total_cost",
            "width": 200
        },
        {
            "label": _("Total Sold"),
            "fieldtype": "Float",
            "fieldname": "total_sold",
            "width": 200
        },
        {
            "label": _("Net Profit/Loss"),
            "fieldtype": "Float",
            "fieldname": "net",
            "width": 200
        }
    ]

    return columns


def get_conditions(filters):
    conditions = {}

    if filters.get("start_date"):
        conditions["start_date"] = filters.start_date
    if filters.get("to_date"):
        conditions["to_date"] = filters.to_date

    return conditions


def get_data(filters):
    data = []
    print(filters)
    conditions = get_conditions(filters)

    query_1 = f"""SELECT
                SUM(`tabEnroll Children`.selling_price) AS total_sold,
                `tabEnroll Children`.application_status,
                `tabEnroll Workshops`.workshop_id AS workshop_id,
                `tabEnroll Workshops`.parent,
                `tabEnroll Children`.name,
                `tabWorkshop`.name,
                `tabWorkshop`.workshop_name AS workshop_name,
                `tabWorkshop`.total_cost as total_cost
            FROM `tabEnroll Children`
            LEFT JOIN `tabEnroll Workshops` ON
            `tabEnroll Children`.name = `tabEnroll Workshops`.parent
            LEFT JOIN `tabWorkshop` ON
            `tabEnroll Workshops`.workshop_id = `tabWorkshop`.name
            WHERE `tabEnroll Children`.application_status = 'Enrolled'
            AND `tabEnroll Children`.enrollment_date BETWEEN '{filters.get("start_date",'1970-01-01')}' AND '{filters.get("end_date",date.today().strftime('%Y-%m-%d'))}'
            AND `tabWorkshop`.total_cost IS NOT NULL
            AND `tabEnroll Children`.selling_price IS NOT NULL
            GROUP BY `tabWorkshop`.name
            ORDER BY `tabWorkshop`.name;"""

    result = frappe.db.sql(query_1, as_dict=1)
    print(result)

    for item in result:
        data.append({
            "workshop_id": item.workshop_id,
            "workshop_name": item.workshop_name,
            "total_sold": item.total_sold,
            "total_cost": item.total_cost,
            "net": item.total_sold - item.total_cost
        })

    return data
