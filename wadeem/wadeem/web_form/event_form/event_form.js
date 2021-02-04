frappe.ready(function() {
	frappe.web_form.after_save = () => {
    console.log(" In form save")
    data = frappe.web_form.get_values()
    let name = data.creator_name;
    let event = data.event_type;
    let phone = data.phone;
    let message_notes = data.message;
    let email_id = data.email;
    frappe.call({
				method: "wadeem.wadeem.web_form.event_form.event_form.create_lead",
				args: {
					person: name,
					phone: phone,
					event_type: event,
					message: message_notes,
					email:email_id
				},
				callback: function (res) {
				    console.log("In JS callback")
                    return True
				}
			});
    }
})
