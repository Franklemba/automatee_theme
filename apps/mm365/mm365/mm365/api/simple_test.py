# Copyright (c) 2025, Logic Links and contributors
# For license information, please see license.txt

import frappe
from frappe import _

@frappe.whitelist()
def test_mm365_sync():
    """Simple test function for MM365 sync"""
    try:
        # Test 1: Check if doctype exists
        if frappe.db.exists("DocType", "MM365 Contacts"):
            result = "✅ MM365 Contacts doctype exists!\n"
        else:
            result = "❌ MM365 Contacts doctype does NOT exist!\n"
            return result
        
        # Test 2: Check if we can access the doctype
        try:
            doc = frappe.get_doc("MM365 Contacts")
            result += "✅ Can access MM365 Contacts doctype!\n"
        except Exception as e:
            result += f"❌ Cannot access MM365 Contacts: {str(e)}\n"
            return result
        
        # Test 3: Try to create a test contact
        try:
            test_contact = frappe.new_doc("MM365 Contacts")
            test_contact.first_name = "Test"
            test_contact.last_name = "Contact"
            test_contact.referred_by_realtor = "MM365R-25-09-04"
            
            # This should trigger the sync function
            test_contact.insert()
            result += "✅ Test contact created successfully!\n"
            result += "✅ Sync function should have been triggered!\n"
            
        except Exception as e:
            result += f"❌ Error creating contact: {str(e)}\n"
        
        return result
        
    except Exception as e:
        return f"❌ General error: {str(e)}"
