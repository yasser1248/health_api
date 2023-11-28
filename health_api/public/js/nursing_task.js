frappe.ui.form.on('Nursing Task', {
    refresh: function(frm){
        
		// Filter on user to return only users with role "nursing user"
		frm.set_query("user", function() {
			return {
				query:"health_api.nursing_task.get_user_roles",
				filters: {
                    role: 'Nursing User',
                }
			}
		});

		// Filter on task doctype link to return only doctypes inside clinic
		frm.set_query("task_doctype", function() {
			return{
				"filters":{
					"module": "Healthcare"
				}
			}
		})
    }
    
});