import http.server
import socketserver
import socket
import webbrowser
import os

def get_local_ip():
    try:
        # Get local IP address
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def main():
    PORT = 8000
    local_ip = get_local_ip()
    
    # Create handler
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Create server
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("\n=== Website is now running! ===")
        print(f"\nLocal access:")
        print(f"http://localhost:{PORT}")
        print(f"\nNetwork access (for other devices):")
        print(f"http://{local_ip}:{PORT}")
        print("\nTo stop the server, press Ctrl+C")
        print("===========================\n")
        
        # Open in default browser
        webbrowser.open(f"http://localhost:{PORT}")
        
        # Start serving
        httpd.serve_forever()

if __name__ == "__main__":
    main() 