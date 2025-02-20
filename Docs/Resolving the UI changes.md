# WhatsApp Automation - Troubleshooting Guide

## **Issue: Send Button Not Available or Script Failing to Send Messages**

### **Step 1: Inspecting the Element**
If you encounter an error where the script cannot find the send button or any similar issue, follow these steps:

1. Open WhatsApp Web.
2. Press `F12` to open Developer Tools.
3. Use the **Inspect Element** tool to locate the send button.
4. Check how the script is identifying the button.

### **Step 2: Understanding How the Script Locates the Send Button**
- The script locates the **Send** button using the attribute `aria-label="Send"`.
- If WhatsApp Web has multiple elements with `aria-label="Send"`, the script may fail to send messages.
- In this case, **code refactoring is required**, as there is no other workaround.
- However, if the `aria-label` text itself changes, you can easily update it without modifying the script.
![image](https://github.com/user-attachments/assets/c2d13046-42b0-4891-87a0-5bd6831d7824)


### **Step 3: Updating Configuration**
- Locate the `config.ini` file in the project directory.
- Update the relevant values under the appropriate section.
- This will allow the script to adapt to any changes in WhatsApp Web’s UI.

![image](https://github.com/user-attachments/assets/85e675c4-ceca-47f3-a65e-cb5512f64d01)

### **Step 4: Changing Settings from the App Interface**
- Navigate to the **Settings** page from the left-hand navigation bar.
- Modify values directly within the app.
- Some values are based on `aria-label`, while others use `XPath` or `CSS classes`.
- Ensure that you are modifying the correct selector based on how the script interacts with WhatsApp Web.

### **Step 5: Restart the Program**
- After saving any changes in `config.ini` or through the settings page, **restart the program** for changes to take effect.

### **Step 6: Regional Differences in WhatsApp Web UI**
- Some WhatsApp Web UI elements vary by region.
- If the script fails to send messages, your region may use different class names or attributes.
- Try inspecting elements (`F12` → Inspect) and updating the `config.ini` file accordingly.

### **Final Notes**
- The script has been tested with the current values and is working correctly as of now.
- If you experience issues, check for updates or inspect the UI for any WhatsApp Web changes.

For further assistance, feel free to report issues or contribute to improvements!

