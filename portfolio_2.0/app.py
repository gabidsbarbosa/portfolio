from flask import Flask, render_template
app = Flask('__name__')

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
@app.route('/sobre')
def about():
    return render_template('about.html')

@app.route('/projects')
@app.route('/projetos')
def projects():
    return render_template('projects.html')

@app.route('/contact')
@app.route('/contato')
def contact():
    return render_template('contact.html')

@app.route('/project_1')
@app.route('/projeto_1')
def projeto_1():
    return render_template('project_1.html')

@app.route('/project_2')
@app.route('/projeto_2')
def projeto_2():
    return render_template('project_2.html')

@app.route('/project_3')
@app.route('/projeto_3')
def projeto_3():
    return render_template('project_3.html')




