from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/skills')
def skills():
    aerospaceSkills = [
        'Strong analytical and problem-solving skills',
        'Creative and ability to see alternative ways of things',
        'Communication skills', 'Speed and accuracy',
        'Strong mathematics and Mechanics', 'Technical Expertise',
        'Concern about safety', 'Interested in aviation and science',
        'Sense of Responsibility', 'Work under pressure to meet the deadlines'
    ]
    aerospaceInterests = [
        'You’re fascinated by the history and methodology behind flying machines, from the earliest conceptual sketches to the advancement of modern jets.',
        'You have a keen interest in the mechanics of flight travel.',
        'You’re intrigued by computer simulations and in seeing how aircraft machinery performs under extreme conditions.'
    ]

    civilSkills = [
        'Math', 'Physics', 'Map reading', 'Reviewing blueprints',
        'Design techniques', 'Cad software', 'Strong and clear communication',
        'Detail-oriented', 'Strong presenter'
    ]
    civilInterests = [
        'Designing and building things',
        'Mechanics, hydraulics, geotechnics, material science, and statistical analysis',
        'Developing your design skills, including CAD'
    ]
    return render_template('skills.html',
                           aerospaceSkills=aerospaceSkills,
                           aerospaceInterests=aerospaceInterests,
                           civilSkills=civilSkills,
                           civilInterests=civilInterests)


@app.route('/salary')
def salary():
    return render_template('salary.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/education')
def education():
    return render_template('education.html')


app.run(host='0.0.0.0', port=81, debug=True)
