# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import ast
from datetime import date

class EnrollChildren(Document):
    pass



def create_invoice(doc):
    item = []
    for val in doc.items:
        item.append({
                'doctype': 'Sales Invoice Item',
                'item_code': val.item_code,
                'qty': 1,
                "rate": val.base_price_list_rate,
                'income_account': frappe.db.get_value('Company', doc.company, 'default_income_account'),
                'cost_center': frappe.db.get_value('Company', doc.company, 'cost_center'),
                'expense_account': frappe.db.get_value('Company', doc.company, 'default_expense_account')
            })
    invoice = frappe.new_doc("Sales Invoice")
    invoice.customer = doc.customer
    invoice.company = doc.company
    invoice.due_date = date.today()
    invoice.currency = doc.currency
    invoice.taxes_and_charges = ""
    invoice.debit_to = ""
    invoice.taxes = []
    invoice.append("items", item[0])
    invoice.flags.ignore_mandatory = True
    try:
        invoice.save(ignore_permissions=True)
        invoice.submit()
        print("Invoice created")
    except Exception as e:
        print("Invoice not created",e)

    return invoice

def create_sales_order(doc):
    print("In Sales Order")
    user = frappe.get_doc('User', frappe.session.user)
    customer = frappe.get_doc('Customer', {'owner': user.name})
    item_code = doc.workshop_id[0].workshop_id
    item = frappe.get_doc('Item', f"Workshop-{item_code}")
    so = frappe.new_doc("Sales Order")
    so.customer_name = customer.customer_name
    so.set_warehouse = ""
    so.transaction_date = date.today()
    so.company = frappe.defaults.get_defaults().company
    so.customer = customer.customer_name
    so.currency = frappe.defaults.get_defaults().currency
    so.selling_price_list = frappe.defaults.get_defaults().default_price_list
    so.delivery_date = date.today()
    so.append("items", {
        "item_code": item.name,
        "warehouse": "",
        "qty": 1,
        "uom": None,
        "rate": doc.selling_price,
        "price_list_rate": doc.selling_price
    })
    so.payment_schedule = []
    so.flags.ignore_mandatory = True
    try:
        so.save(ignore_permissions=True)
        so.submit()
        print("SO created")
    except Exception as e:
        print("Sales order not created",e)

    return so

@frappe.whitelist(allow_guest=True)
def create_form():
    args = frappe.form_dict
    doc = frappe.new_doc('Enroll Children')
    if args:
        doc.child_id = args.get('children')
        doc.program_id = args.get('program')
        doc.selling_price = args.get('selling_price')
        if args.get('selected_workspaces'):
            workshops = ast.literal_eval(args.get('selected_workspaces'))
            for workshop in workshops:
                doc.append("workshop_id", {
                    "workshop_id": workshop
                })
    doc.insert(ignore_permissions=True)
    doc.save(ignore_permissions=True)
    doc.submit()
    so = create_sales_order(doc)
    frappe.db.set_value("Enroll Children", doc.name, "sales_order_id", so.name)
    invoice = create_invoice(so)
    frappe.db.set_value("Enroll Children", doc.name, "sales_invoice_id", invoice.name)
    return doc
