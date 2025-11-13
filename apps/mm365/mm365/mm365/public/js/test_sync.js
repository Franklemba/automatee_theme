// Test function for MM365 sync
function testMM365Sync() {
    frappe.call({
        method: "mm365.mm365.api.test_sync.test_sync_function",
        callback: function(r) {
            if (r.message) {
                console.log("Test result:", r.message);
                frappe.msgprint("Test completed! Check console for details.");
            }
        }
    });
}

// Make function available globally
window.testMM365Sync = testMM365Sync;

console.log("MM365 Test function loaded! Call testMM365Sync() to test.");
