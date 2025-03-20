import subprocess
import time
import webbrowser
import os

def main():
    # Start the website server in the background
    server_process = subprocess.Popen(['python3', 'serve.py'])
    
    # Wait a moment for the server to start
    time.sleep(2)
    
    # Start ngrok
    print("\nStarting ngrok tunnel...")
    ngrok_process = subprocess.Popen(['ngrok', 'http', '8000'])
    
    # Wait for ngrok to start
    time.sleep(3)
    
    print("\n=== Website is now accessible worldwide! ===")
    print("\nThe public URL will appear in the ngrok window.")
    print("Share that URL with anyone to let them view the website.")
    print("\nTo stop the servers, press Ctrl+C in both windows.")
    print("==========================================\n")
    
    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nShutting down servers...")
        server_process.terminate()
        ngrok_process.terminate()
        print("Done!")

if __name__ == "__main__":
    main() 