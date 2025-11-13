# Copyright (c) 2025, Logic Links and contributors
# For license information, please see license.txt

import frappe
from frappe import _

@frappe.whitelist()
def test_sync_function():
    """Test function to check if sync is working"""
    try:
        # Test if MM365 Contacts doctype exists
        if frappe.db.exists("DocType", "MM365 Contacts"):
            frappe.msgprint("✅ MM365 Contacts doctype exists!")
        else:
            frappe.msgprint("❌ MM365 Contacts doctype does NOT exist!")
            return "DocType not found"
        
        # Test if we can create a contact
        test_contact = frappe.new_doc("MM365 Contacts")
        test_contact.first_name = "Test"
        test_contact.last_name = "Contact"
        test_contact.referred_by_realtor = "MM365R-25-09-04"  # Test realtor
        test_contact.insert()
        
        frappe.msgprint("✅ Test contact created successfully!")
        return "Success"
        
    except Exception as e:
        frappe.msgprint(f"❌ Error: {str(e)}")
        return f"Error: {str(e)}"
