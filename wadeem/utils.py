from __future__ import unicode_literals
import frappe
from frappe.utils import today
from datetime import date


def create_item(doc, method):
    print("create item called")
    item_name = f"Workshop-{doc.name}"
    print(item_name)
    if frappe.db.exists({
        'doctype': 'Item',
        'item_code': item_name,
    }):
        print("Item exists called")
        return frappe.db.get_value('Item', {'item_code': item_name})
    item = frappe.new_doc('Item')
    item.item_code = item_name
    item.item_name = item_name
    item.item_group = 'Services'
    item.is_stock_item = 0
    print("Creating new item")
    try:
        item.save()
    except Exception as e:
        print(e)
    return item.name


def create_sales_order(doc, method):

    user = frappe.get_doc('User', frappe.session.user)
    customer = frappe.get_doc('Customer', {'owner': user.name})
    print(customer.customer_name)
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
    so.delivery_date = today()
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
    return

def set_default_role(doc, method):
    if frappe.flags.setting_role or frappe.flags.in_migrate:
        return

    roles = frappe.get_roles()

    if frappe.get_value('Guardians', dict(email=doc.email)) and 'Guardians' not in roles:
        doc.add_roles('Guardians')

def create_link(doc,method):
    print("Children hook called")
    owner = doc.owner
    print(owner)
    guardian_user = frappe.get_value("Guardians",{"email":owner})
    print("ID",guardian_user)
    frappe.db.set_value("Children", doc.name, "guardian_link", guardian_user)
    doc.guardian_link = guardian_user
    print(doc.guardian_link)

def create_guardian(doc, method):

    if doc.get('user_type') != 'Website User':
        return
    first_name = doc.get('first_name')
    email = doc.get('email')
    if frappe.db.exists("Guardians", {'first_name': first_name, 'email': email}):
        print("Guardian not created")
        return
    else:
        print("Creating New Guardian")
        guardian = frappe.new_doc("Guardians")
        guardian.update({
            "first_name": first_name,
            "email": email,
            "guardian_user": email
        })
        guardian.flags.ignore_mandatory = True
        guardian.insert(ignore_permissions=True)
        print("Guardian hook completed")
        return