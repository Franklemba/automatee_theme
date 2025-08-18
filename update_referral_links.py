#!/usr/bin/env python3
"""
Script to update existing referral links to the new format
"""

import frappe
import re
import hashlib
from frappe.utils import now_datetime

def generate_unique_identifier(link_type, first_name, last_name=""):
    """Generate a unique identifier for referral links"""
    # Clean the first name and last name (remove special characters, convert to lowercase)
    clean_first_name = re.sub(r'[^a-zA-Z0-9]', '', (first_name or "contact").lower())
    clean_last_name = re.sub(r'[^a-zA-Z0-9]', '', (last_name or "").lower())

    # Create a base string from registration data
    base_string = f"{link_type}_{clean_first_name}_{clean_last_name}_{now_datetime().strftime('%Y%m%d%H%M%S')}"
    
    # Generate a hash
    hash_object = hashlib.md5(base_string.encode())
    hash_hex = hash_object.hexdigest()[:8]
    
    # Create a readable identifier
    readable_id = f"{link_type[:3]}_{hash_hex}"
    
    return readable_id.upper()

def update_mm365_contacts():
    """Update all MM365 Contacts referral links"""
    print("Updating MM365 Contacts referral links...")
    
    contacts = frappe.get_all("MM365 Contacts", fields=["name", "first_name", "last_name", "homeowners_referral_link", "homebuyers_referral_link"])
    
    for contact in contacts:
        doc = frappe.get_doc("MM365 Contacts", contact.name)
        updated = False
        
        # Update homeowners referral link
        if doc.homeowners_referral_link and "moneymoves365.com/h/" in doc.homeowners_referral_link:
            unique_id = generate_unique_identifier("homeowners", doc.first_name, doc.last_name)
                            doc.homeowners_referral_link = f"https://moneymoves365.com/register/{unique_id}"
            updated = True
            print(f"Updated homeowners link for {contact.name}: {doc.homeowners_referral_link}")
        
        # Update homebuyers referral link
        if doc.homebuyers_referral_link and "moneymoves365.com/b/" in doc.homebuyers_referral_link:
            unique_id = generate_unique_identifier("homebuyers", doc.first_name, doc.last_name)
                            doc.homebuyers_referral_link = f"https://moneymoves365.com/register/{unique_id}"
            updated = True
            print(f"Updated homebuyers link for {contact.name}: {doc.homebuyers_referral_link}")
        
        if updated:
            doc.save()
    
    print(f"Updated {len(contacts)} MM365 Contacts records")

def update_mm365_realtors():
    """Update all MM365 Realtors referral links"""
    print("Updating MM365 Realtors referral links...")
    
    realtors = frappe.get_all("MM365 Realtors", fields=["name", "first_name", "realtor_referral_link", "homeowner_homebuyer_link"])
    
    for realtor in realtors:
        doc = frappe.get_doc("MM365 Realtors", realtor.name)
        updated = False
        
        # Update realtor referral link
        if doc.realtor_referral_link and "moneymoves365.com/r/" in doc.realtor_referral_link:
            unique_id = generate_unique_identifier("realtor", doc.first_name)
                            doc.realtor_referral_link = f"https://moneymoves365.com/register/{unique_id}"
            updated = True
            print(f"Updated realtor link for {realtor.name}: {doc.realtor_referral_link}")
        
        # Update homeowner/homebuyer referral link
        if doc.homeowner_homebuyer_link and "moneymoves365.com/h/" in doc.homeowner_homebuyer_link:
            unique_id = generate_unique_identifier("homeowner", doc.first_name)
                            doc.homeowner_homebuyer_link = f"https://moneymoves365.com/register/{unique_id}"
            updated = True
            print(f"Updated homeowner/homebuyer link for {realtor.name}: {doc.homeowner_homebuyer_link}")
        
        if updated:
            doc.save()
    
    print(f"Updated {len(realtors)} MM365 Realtors records")

def main():
    """Main function to update all referral links"""
    print("Starting referral link update...")
    
    try:
        update_mm365_contacts()
        update_mm365_realtors()
        print("Referral link update completed successfully!")
        
    except Exception as e:
        print(f"Error updating referral links: {str(e)}")
        frappe.log_error(f"Referral Link Update Error: {str(e)}")

if __name__ == "__main__":
    main() 