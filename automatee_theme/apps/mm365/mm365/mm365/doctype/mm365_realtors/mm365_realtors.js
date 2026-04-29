// Copyright (c) 2025, Logic Links and contributors
// For license information, please see license.txt

frappe.ui.form.on("MM365 Realtors", {
        refresh(frm) {
                // Make both referral link fields read-only
                frm.set_df_property('realtor_referral_link', 'read_only', 1);
                frm.set_df_property('homeowner_homebuyer_link', 'read_only', 1);

                // Add copy buttons for referral links if they exist
                if (frm.doc.realtor_referral_link) {
                        frm.add_custom_button(__('Copy Realtor Referral Link'), function() {
                                frappe.utils.copy_to_clipboard(frm.doc.realtor_referral_link);
                                frappe.show_alert(__('Realtor referral link copied to clipboard!'), 3);
                        }, __('Actions'));
                }

                if (frm.doc.homeowner_homebuyer_link) {
                        frm.add_custom_button(__('Copy Homeowner/Homebuyer Referral Link'), function() {
                                frappe.utils.copy_to_clipboard(frm.doc.homeowner_homebuyer_link);
                                frappe.show_alert(__('Homeowner/Homebuyer referral link copied to clipboard!'), 3);
                        }, __('Actions'));
                }
        },

        first_name: function(frm) {
                // Generate both referral links when first name is entered (for new records)
                if (!frm.doc.realtor_referral_link && frm.doc.first_name) {
                        generateUniqueRealtorReferralLink(frm.doc.first_name).then(function(link) {
                                frm.set_value('realtor_referral_link', link);
                        });
                }

                if (!frm.doc.homeowner_homebuyer_link && frm.doc.first_name) {
                        generateUniqueHomeownerReferralLink(frm.doc.first_name).then(function(link) {
                                frm.set_value('homeowner_homebuyer_link', link);
                        });
                }
        }
});

function generateUniqueRealtorReferralLink(firstName) {
        return new Promise((resolve) => {
                // Clean the first name (remove special characters, convert to lowercase)
                const cleanName = firstName.toLowerCase().replace(/[^a-z0-9]/g, '');

                // Generate a random 6-character string
                const randomSuffix = Math.random().toString(36).substring(2, 8);

                // Create the realtor referral link with new format
                const uniqueLink = `https://moneymoves365.com/register/REA_${randomSuffix.toUpperCase()}`;
                resolve(uniqueLink);
        });
}

function generateUniqueHomeownerReferralLink(firstName) {
        return new Promise((resolve) => {
                // Clean the first name (remove special characters, convert to lowercase)
                const cleanName = firstName.toLowerCase().replace(/[^a-z0-9]/g, '');

                // Generate a random 6-character string
                const randomSuffix = Math.random().toString(36).substring(2, 8);

                // Create the homeowner/homebuyer referral link with new format
                const uniqueLink = `https://moneymoves365.com/register/HOM_${randomSuffix.toUpperCase()}`;
                resolve(uniqueLink);
        });
} 