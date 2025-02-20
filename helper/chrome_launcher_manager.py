import subprocess
import time
import os
import requests  # You may need to install this package (pip install requests)


class ChromeLauncher:
    def __init__(self, chrome_path, debugging_port="9222", user_data_dir=None):
        """
        Initialize ChromeLauncher.
        :param chrome_path: Full path to chrome executable.
        :param debugging_port: Remote debugging port.
        :param user_data_dir: Path to your existing Chrome user data directory.
        """
        self.chrome_path = chrome_path
        self.debugging_port = debugging_port

        if user_data_dir is None:
            raise ValueError("Please provide the path to your Chrome user data directory.")
        self.user_data_dir = user_data_dir
        self.process = None

    def is_debug_port_active(self):
        """
        Check if Chrome is already running with the specified remote debugging port.
        """
        url = f"http://localhost:{self.debugging_port}/json"
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                print("Detected an active Chrome instance with remote debugging enabled.")
                return True
        except requests.RequestException:
            pass
        return False

    def launch(self):
        """
        Launch Chrome with remote debugging using the specified profile,
        but only if it's not already running.
        """
        if self.is_debug_port_active():
            print("Using the existing Chrome instance.")
            return True

        # Ensure the user data directory exists
        if not os.path.exists(self.user_data_dir):
            print("The specified user data directory does not exist.")
            return False

        command = [
            self.chrome_path,
            f"--remote-debugging-port={self.debugging_port}",
            f"--user-data-dir={self.user_data_dir}"
        ]

        try:
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Launched a new Chrome instance with remote debugging enabled on port", self.debugging_port)
        except Exception as e:
            print("Failed to launch Chrome:", e)
            return False

        # Wait a moment to allow Chrome to start
        time.sleep(2)
        return True

    def wait(self):
        """
        Keep the script running until user input.
        """
        input("Press Enter to exit. Chrome will remain open if not manually closed.")


if __name__ == "__main__":
    # Set the path to your Chrome executable
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    # Set your existing user data directory (adjust to your system and desired profile folder)
    user_data_dir = r"C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data"

    launcher = ChromeLauncher(chrome_path, user_data_dir=user_data_dir)

    if launcher.launch():
        launcher.wait()
    else:
        print("Unable to launch or connect to Chrome.")
