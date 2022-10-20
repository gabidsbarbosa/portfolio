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




