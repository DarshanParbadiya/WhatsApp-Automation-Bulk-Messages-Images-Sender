import subprocess
import time
import os


class ChromeLauncher:
    def __init__(self, chrome_path, debugging_port="9222", user_data_dir=r"C:\selenium\ChromeProfile"):
        """
        Initialize the ChromeLauncher with the path to chrome.exe, the remote debugging port,
        and the user data directory for a persistent session.
        """
        self.chrome_path = chrome_path
        self.debugging_port = debugging_port
        self.user_data_dir = user_data_dir
        self.process = None

    def launch(self):
        """
        Launch Chrome with remote debugging enabled.
        """
        # Ensure the user data directory exists
        os.makedirs(self.user_data_dir, exist_ok=True)

        # Build the command to launch Chrome
        command = [
            self.chrome_path,
            f"--remote-debugging-port={self.debugging_port}",
            f"--user-data-dir={self.user_data_dir}"
        ]

        try:
            # Launch Chrome using subprocess.Popen
            self.process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print("Chrome launched with remote debugging enabled on port", self.debugging_port)
        except Exception as e:
            print("Failed to launch Chrome:", e)
            return False

        # Optionally wait a bit to ensure Chrome starts up
        time.sleep(2)
        return True

    def is_running(self):
        """
        Check if the Chrome process is still running.
        """
        return self.process and self.process.poll() is None

    def wait(self):
        """
        Keep the launcher running until user input, so that Chrome stays open.
        """
        input("Press Enter to exit. Chrome will remain open if not manually closed.")

    @staticmethod
    def launch_chrome():
    # Update the chrome_path to the full path of your Chrome executable
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Create an instance of ChromeLauncher
        launcher = ChromeLauncher(chrome_path)

        # Launch Chrome
        if launcher.launch():
            # Keep the script running until user hits Enter
            launcher.wait()
        else:
            print("Unable to launch Chrome.")
