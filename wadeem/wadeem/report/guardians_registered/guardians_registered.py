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
            "label": _("Total Guardians Registered"),
            "fieldtype": "Int",
            "fieldname": "total_guardians",
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
                `tabGuardians`.first_name AS guardian,
                `tabGuardians`.date_of_birth AS birth_date
    			FROM `tabGuardians`
    			WHERE `tabGuardians`.date_of_birth IS NOT NULL
    			ORDER BY `tabGuardians`.first_name"""

    result = frappe.db.sql(query,filters,as_dict=1)

    print(result)
    age_results = {
        "20-25": 0,
        "25-30": 0,
        "30-35": 0,
        "35-40": 0,
        "40-45": 0,
        "45-50": 0,
        "50-55": 0,
        "55-60": 0,
	"60-65":0,
	"65-70":0,
	"70-75":0,
	"75-80":0,
	"80-85":0,
	"85-90":0,
	"90-95":0,
	"95-100":0
    }
    for item in result:
        birth_date = item.get("birth_date")
        age = relativedelta(date.today() ,birth_date).years
        if 20 <= age < 25:
            age_results["20-25"] += 1
        elif 25 <= age < 30:
            age_results["25-30"] += 1
        elif 30 <= age < 35:
            age_results["30-35"] += 1
        elif 35 <= age < 40:
            age_results["35-40"] += 1
        elif 40 <= age < 45:
            age_results["40-45"] += 1
        elif 45 <= age < 50:
            age_results["45-50"] += 1
        elif 50 <= age < 55:
            age_results["50-55"] += 1
        elif 55 <= age < 60:
            age_results["55-60"] += 1
        elif 55 <= age < 60:
            age_results["60-65"] += 1
        elif 60 <= age < 65:
            age_results["65-70"] += 1
        elif 65 <= age < 70:
            age_results["65-70"] += 1
        elif 70 <= age < 75:
            age_results["75-80"] += 1
        elif 80<= age < 85:
            age_results["80-85"] += 1
        elif 85 <= age < 90:
            age_results["85-90"] += 1
        elif 90 <= age < 95:
            age_results["45-50"] += 1
        elif 95 <= age < 100:
            age_results["95-100"] += 1

    for key, value in age_results.items():
        data.append({
            "age_group": key,
            "total_guardians": value,
        })

    return data