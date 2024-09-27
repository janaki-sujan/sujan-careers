from flask import Flask, jsonify, render_template, jsonify 

app = Flask(__name__)
JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 10000
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi,India',
    'salary': 25000
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 15000
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 20000
}, {
    'id': 5,
    'title': 'Software Engineer',
    'location': 'San Francisco, USA',
    'salary': 50000
}, {
    'id': 6,
    'title': 'Machine Learning Engineer',
    'location': 'San Francisco, USA',
    'salary': 80000
}, {
    'id': 7,
    'title': 'Data Engineer',
    'location': 'San Francisco, USA',
    'salary': 400000
}, {
    'id': 8,
    'title': 'Product Manager',
    'location': 'San Francisco, USA',
    'salary': 60000
}, {
    'id': 9,
    'title': 'Business Analyst',
    'location': 'San Francisco, USA',
    'salary': 33000
}]


@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)


@app.route('/')
def hello():
    return render_template('home.html', jobs=JOBS)


print(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
