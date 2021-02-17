# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "wadeem"
app_title = "Wadeem"
app_publisher = "Siddhant"
app_description = "LMS Module"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "siddhant.sinha@oodlestechnologies.com"
app_license = "MIT"

# on_session_creation = [
# 	"wadeem.utils.create_guardian"
# ]

doc_events = {
	'User': {
		"after_insert": "wadeem.utils.create_guardian"
	},
	'Workshop': {
		"after_insert": "wadeem.utils.create_item"
	},
	"Guardians": {
		"after_insert": "wadeem.utils.create_guardian"
	},
	"Children": {
		"after_insert": "wadeem.utils.create_link"
	}
}

website_route_rules = [
	{"from_route": "/programs/<program_name>", "to_route": "Programs"}
]
default_roles = [
	{'role': 'Customer', 'doctype':'Customer', 'email_field': 'email_id'}
]


# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/wadeem/css/wadeem.css"
# app_include_js = "/assets/wadeem/js/wadeem.js"

# include js, css files in header of web template
# web_include_css = "/assets/wadeem/css/wadeem.css"
# web_include_js = "/assets/wadeem/js/wadeem.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "wadeem.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
website_generators = ["Programs"]

# Installation
# ------------

# before_install = "wadeem.install.before_install"
# after_install = "wadeem.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "wadeem.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events



# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"wadeem.tasks.all"
# 	],
# 	"daily": [
# 		"wadeem.tasks.daily"
# 	],
# 	"hourly": [
# 		"wadeem.tasks.hourly"
# 	],
# 	"weekly": [
# 		"wadeem.tasks.weekly"
# 	]
# 	"monthly": [
# 		"wadeem.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "wadeem.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "wadeem.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "wadeem.task.get_dashboard_data"
# }

