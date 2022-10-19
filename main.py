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
    aerospaceData = [
        ('MIT.jpg', 'Massachusetts Institute of Technology',
         'Private Institution', 1, 55510, [
             'Introduction to Computer Science Programming in Python',
             'Introduction to Computational Thinking and Data Science',
             'Unified Engineering: Signals and Systems',
             'Unified Engineering: Fluid Dynamics',
             'Unified Engineering: Thermodynamics and Propulsion',
             'Principles of Automatic Control', 'Dynamics',
             'Statistics and Probability', 'Introduction to Probability',
             'Differential Equations'
         ]),
        ('Illinois.jpg', 'University of Illinois Urbana-Champaign',
         'Public University', 2, 18998, [
             'Aerospace Computer-Aided Design', 'Aerospace Flight Mechanics',
             'Incompressible Flow', 'Compressible Flow',
             'Mechs of Aerospace Structures', 'Applied Aerospace Structures',
             'Aerospace Dynamical Systems', 'Aerospace Control Systems',
             'Thermodynamics', 'Engineering Materials',
             'Introduction to Statics', 'Introductory Dynamics'
         ]),
        ('Michigan.jpg', 'University of Michigan - Ann Arbor',
         'Public Institution', 3, 28338, [
             'Intro to Aerospace Engineering',
             'Intro to Solid Mechanics and Aerospace Structures',
             'Intro to Gas Dynamics', 'Aircraft and Spacecraft Structures',
             'Aerodynamics', 'Aircraft and Spacecraft Propulsion',
             'Aircraft Dynamics or AEROSP 343 Spacecraft Dynamics',
             'Introduction to Aerospace Computing',
             'Control of Aerospace Vehicles'
         ])
    ]

    civilData = [
        ('Berkeley.jpg', 'University of California - Berkeley',
         'Public Institution', 4, 43980, ['Structural reliability', 'Mechanics of solids', 'Concrete technology', 'Construction, scheduling, resource allocation', 'Advanced soil mechanics', 'Linear programming', 'Reliability theory', 'Applied dynamic programming']),
        ('MIT.jpg', 'Massachusetts Institute of Technology',
         'Private Institution', 5, 57986, ['Engineering computation and data science', 'Intro to computer programming and numerical methods for engineering applications', 'Startup sustainable technologies', 'Experiential sustainability', 'Tools for sustainable design', 'Engineering for a sustainable world', 'Climate change', 'Probability and casual interference', 'Senior civil and environmental design', 'Fundamentals of ecology', 'Mechanics of materials']),
        ('Oregon.jpg', 'Oregon State University',
         'Public Institution', 6, 29421, ['Design engineering and problem solving', 'Computational and algorithmic thinking', 'Chemistry', 'General physics w/ calc', 'Differential calc', 'Integral calc', 'Vector calc', 'English composition', 'Structural theory', 'Hydrology', 'Reinforced concrete', 'Geotechnical engineering', 'Intro to highway engineering'])
    ]
    return render_template('education.html', aerospaceData=aerospaceData, civilData=civilData)


# app.run(host='0.0.0.0', port=81, debug=True)
