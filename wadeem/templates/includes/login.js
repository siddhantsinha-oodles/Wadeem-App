$(".form-signup").on("submit", function(event) {
		event.preventDefault();
		var args = {};
		args.cmd = "frappe.core.doctype.user.user.sign_up";
		args.usertype = $("#usertype").val();
//		console.log(ars.usertype)
		args.email = ($("#signup_email").val() || "").trim();
		args.redirect_to = get_url_arg("redirect-to") || '';
		args.firstname = ($("#firstname").val() || "").trim();
		args.mobile_no = ($("#mobile_no").val() || "").trim()

		if(!args.email || !valid_email(args.email) || !args.full_name) {
			login.set_indicator("{{ _("Valid email and name required") }}", 'red');
			return false;
		}
		login.call(args);
		return false;
	});