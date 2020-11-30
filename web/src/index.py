from flask import Flask , render_template , request
from moduls import gmail

app =  Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/carta')
def carta():
    return render_template('carta.html')

@app.route('/cursos')
def cursos():
    return render_template('cursos.html')

@app.route('/proyects')
def proyects():
    return render_template('proyects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/add_Contact', methods=['POST'])
def add_Contact():
    if request.method == 'POST':
        Nombre = request.form['Nombre']
        Email = request.form['Email']
        Mensaje = request.form['Mensaje']
        
        gmail.sendMailWithGmail(Nombre,Email,Mensaje)

    return render_template('Contact.html')

if __name__ == '__main__':
    app.run(port = 3000,debug = True)

