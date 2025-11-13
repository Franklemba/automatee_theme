# Copyright (c) 2025, Logic Links and contributors
# For license information, please see license.txt

import frappe

def test_doctype_exists():
    """Test if MM365 Contacts doctype exists"""
    try:
        # Check if doctype exists
        if frappe.db.exists("DocType", "MM365 Contacts"):
            print("✅ MM365 Contacts doctype exists!")
            return True
        else:
            print("❌ MM365 Contacts doctype does NOT exist!")
            return False
    except Exception as e:
        print(f"❌ Error checking doctype: {str(e)}")
        return False

def test_create_contact():
    """Test creating a contact"""
    try:
        # Create a test contact
        test_contact = frappe.new_doc("MM365 Contacts")
        test_contact.first_name = "Test"
        test_contact.last_name = "Contact"
        test_contact.referred_by_realtor = "MM365R-25-09-04"
        
        # This should trigger the sync function
        test_contact.insert()
        print("✅ Test contact created successfully!")
        print("✅ Sync function should have been triggered!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating contact: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing MM365 Contacts...")
    if test_doctype_exists():
        test_create_contact()
