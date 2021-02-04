# -*- coding: utf-8 -*-
# Copyright (c) 2020, Siddhant and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
import ast


class EnrollChildren(Document):
    pass


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
    return doc
