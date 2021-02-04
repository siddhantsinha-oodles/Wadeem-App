from __future__ import unicode_literals
import frappe
from frappe import _

sitemap = 1


def get_context(context):

	context.no_cache = True
	context.show_sidebar = True
	ls = frappe.get_all('Programs', fields=['program_name','program_topics','program_includes','prog_desc','image','selling_price',
											'type','duration'], filters={'show_in_website': 1})
	context.all_duration = frappe.get_all('Programs', fields=['duration'], filters={'show_in_website': 1})
	context.all_programs = ls



