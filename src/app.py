from flask import Flask, request, jsonify
from scheduler import schedule_jobs

app = Flask(__name__)

@app.route('/schedule', methods=['POST'])
def get_schedule():
    data = request.get_json()
    jobs = data.get("jobs", [])
    try:
        jobs = [(job['start'], job['end'], job['profit']) for job in jobs]
    except:
        return jsonify({"error": "Invalid job format"}), 400

    max_profit = schedule_jobs(jobs)
    return jsonify({"max_profit": max_profit}), 200

if __name__ == '__main__':
    app.run(debug=True)
