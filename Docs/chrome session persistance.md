## **Persisting Chrome Instance Without Losing Session Login**

### **Overview**
To avoid repeatedly logging in and closing Chrome after each message session, you can persist the Chrome instance by manually launching it and allowing the Python script to connect to that session.

### **Step 1: Configuration**
- Locate the `config.ini` file in the project root directory.
- Find the following key:
  
  ```ini
  [Chrome]
  single_instance = True
  ```
  
- If `single_instance` is set to `True`, you must manually start Chrome.
- By default, it is set to `False` because many users prefer not to persist their Chrome session.

### **Step 2: Launching Chrome Manually**
To manually invoke the Chrome instance, run the following command in the Command Prompt (`cmd`):

```sh
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium\ChromeProfile"
```

- This command starts Chrome with a remote debugging port and a user data directory, keeping your session active.
- Ensure that the specified `user-data-dir` exists and is accessible.

### **Step 3: Running the Script**
- When you start the program and press `Open WhatsApp`, the script will automatically refresh the page to load WhatsApp Web within the persistent Chrome session.
- This ensures you don’t have to log in repeatedly.

### **Final Notes**
- This approach improves efficiency by keeping Chrome open, reducing unnecessary reloads.
- If you face issues, ensure that no other Chrome instance is running without the debugging port enabled.
- If needed, update the `config.ini` settings to match your requirements.

