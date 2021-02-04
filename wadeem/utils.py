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
    item.save()
    return item.name

##testing

def create_customer(doc, method):
    user = frappe.session.user
    customer_name = frappe
    existing_customer_name = frappe.db.get_value("Customer",
			filters={"name": customer_name}, fieldname="name")

    if existing_customer_name:
        filters = [
				["Dynamic Link", "link_doctype", "=", "Customer"],
				["Dynamic Link", "link_name", "=", existing_customer_name],
				["Dynamic Link", "parenttype", "=", "Contact"]
			]

        existing_contacts = frappe.get_list("Contact", filters)

        if existing_contacts:
            pass
        else:
            new_contact = frappe.new_doc("Contact")
            new_contact.first_name = customer_name
            new_contact.append('links', {
				"link_doctype": "Customer",
				"link_name": existing_customer_name
			})
            new_contact.insert()

        return existing_customer_name
    else:
        new_customer = frappe.new_doc("Customer")
        new_customer.customer_name = customer_name
        new_customer.customer_group = mws_customer_settings.customer_group
        new_customer.territory = mws_customer_settings.territory
        new_customer.customer_type = mws_customer_settings.customer_type
        new_customer.save()

        new_contact = frappe.new_doc("Contact")
        new_contact.first_name = customer_name
        new_contact.append('links', {
			"link_doctype": "Customer",
			"link_name": new_customer.name
		})

        new_contact.insert()

        return new_customer.name


def create_sales_order(doc, method):
    print("Doc Name", doc.name)
    user = frappe.get_doc('User', frappe.session.user)

    print(frappe.get_roles())
    item_code = doc.workshop_id[0].workshop_id
    item = frappe.get_doc('Item', f"Workshop-{item_code}")
    print(item.name)
    so = frappe.new_doc("Sales Order")
    so.customer_name = user.get_fullname()
    so.set_warehouse = ""
    so.transaction_date = date.today()
    so.company = frappe.defaults.get_defaults().company
    so.customer = frappe.session.user
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
    so.save(ignore_permissions=True)
    so.submit()
    print("SO created")
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