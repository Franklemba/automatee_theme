# Copyright (c) 2025, Logic Links and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import re
import random
import string
import hashlib
from frappe.utils import now_datetime
import hashlib
from frappe.utils import now_datetime


class MM365Contacts(Document):
        def autoname(self):
                # Generate referral links when creating new record
                self.ensure_referral_links()

        def before_insert(self):
                # Ensure both referral links are generated for new records
                self.ensure_referral_links()

        def before_save(self):
                # Ensure referral links exist before saving (for any creation method)
                self.ensure_referral_links()

        def validate(self):
                # Ensure referral links exist during validation
                self.ensure_referral_links()

        def ensure_referral_links(self):
                """Ensure both referral links are generated if they don't exist"""
                if not self.homeowners_referral_link:
                        self.generate_homeowners_referral_link()
                if not self.homebuyers_referral_link:
                        self.generate_homebuyers_referral_link()

        def generate_unique_identifier(self, link_type):
                """Generate a unique identifier for referral links"""
                # Get first name and last name, with fallbacks
                first_name = self.first_name or "contact"
                last_name = self.last_name or ""

                # Clean the first name and last name (remove special characters, convert to lowercase)
                clean_first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name.lower())
                clean_last_name = re.sub(r'[^a-zA-Z0-9]', '', last_name.lower())

                # Create a base string from registration data
                base_string = f"{link_type}_{clean_first_name}_{clean_last_name}_{now_datetime().strftime('%Y%m%d%H%M%S')}"
                
                # Generate a hash
                hash_object = hashlib.md5(base_string.encode())
                hash_hex = hash_object.hexdigest()[:8]
                
                # Create a readable identifier
                readable_id = f"{link_type[:3]}_{hash_hex}"
                
                return readable_id.upper()

        def generate_homeowners_referral_link(self):
                """Generate a unique homeowners referral link"""
                # Generate unique identifier
                unique_id = self.generate_unique_identifier("homeowners")
                
                # Create the homeowners referral link
                self.homeowners_referral_link = f"https://moneymoves365.com/register/{unique_id}"

        def generate_homebuyers_referral_link(self):
                """Generate a unique homebuyers referral link"""
                # Generate unique identifier
                unique_id = self.generate_unique_identifier("homebuyers")
                
                # Create the homebuyers referral link
                self.homebuyers_referral_link = f"https://moneymoves365.com/register/{unique_id}" 