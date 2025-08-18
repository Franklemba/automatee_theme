# Copyright (c) 2025, Logic Links and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
import random
import string
import hashlib
from frappe.utils import now_datetime


class MM365Realtors(Document):
        def autoname(self):
                # Generate referral links when creating new record
                if not self.realtor_referral_link:
                        self.generate_realtor_referral_link()
                if not self.homeowner_homebuyer_link:
                        self.generate_homeowner_homebuyer_link()

        def generate_unique_identifier(self, link_type):
                """Generate a unique identifier for referral links"""
                # Get first name, with fallback
                first_name = self.first_name or "realtor"

                # Clean the first name (remove special characters, convert to lowercase)
                clean_first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name.lower())

                # Create a base string from registration data
                base_string = f"{link_type}_{clean_first_name}_{now_datetime().strftime('%Y%m%d%H%M%S')}"
                
                # Generate a hash
                hash_object = hashlib.md5(base_string.encode())
                hash_hex = hash_object.hexdigest()[:8]
                
                # Create a readable identifier
                readable_id = f"{link_type[:3]}_{hash_hex}"
                
                return readable_id.upper()

        def generate_realtor_referral_link(self):
                """Generate a unique realtor referral link"""
                if not self.first_name:
                        return

                # Generate unique identifier
                unique_id = self.generate_unique_identifier("realtor")
                
                # Create the realtor referral link
                self.realtor_referral_link = f"https://moneymoves365.com/register/{unique_id}"

        def generate_homeowner_homebuyer_link(self):
                """Generate a unique homeowner/homebuyer referral link"""
                if not self.first_name:
                        return

                # Generate unique identifier
                unique_id = self.generate_unique_identifier("homeowner")
                
                # Create the homeowner/homebuyer referral link
                self.homeowner_homebuyer_link = f"https://moneymoves365.com/register/{unique_id}"

        def before_insert(self):
                # Ensure both referral links are generated for new records
                if not self.realtor_referral_link:
                        self.generate_realtor_referral_link()
                if not self.homeowner_homebuyer_link:
                        self.generate_homeowner_homebuyer_link() 