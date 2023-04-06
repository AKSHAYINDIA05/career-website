from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  "id": 1,
  "title": "Data Scientist",
  "location": "Hyderabad",
  "salary": "₹ 50,00,000"
}, {
  "id": 2,
  "title": "Machine Learning Engineer",
  "location": "Bengaluru",
  "salary": "₹ 30,00.000"
}, {
  "id": 3,
  "title": "Data Analyst",
  "location": "Delhi",
  "salary": "₹ 20,00,000"
}, {
  "id": 4,
  "title": "Front-End Developer",
  "location": "Delhi",
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="#codEasy")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
