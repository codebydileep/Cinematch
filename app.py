from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    full_name = "Dileep Guttur"  # Replace with your actual name
    
    # System username fallback
    system_username = os.environ.get('USER') or os.environ.get('USERNAME') or 'Unknown User'
    
    # Server time in IST (Indian Standard Time)
    ist_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Running the `ps aux` command to get system info (replacing `top` for testing)
    top_output = subprocess.getoutput('ps aux')

    # HTML response with the required data
    response = f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> {full_name}</p>
    <p><strong>Username:</strong> {system_username}</p>
    <p><strong>Server Time (IST):</strong> {ist_time}</p>
    <pre><strong>Process Output:</strong><br>{top_output}</pre>
    """
    
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
