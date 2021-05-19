from flask import Flask, render_template, request, redirect , url_for, flash
from flask.globals import request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'CaramitiE.23'
app.config['MYSQL_DB'] = 'contacts'

mysql = MySQL(app)

# setting
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, email, phone) VALUES (%s, %s, %s)', (fullname, email, phone))
        mysql.connection.commit()
        flash('Contact Added successfull')
        return redirect(url_for('Index'))

@app.route('/edit')
def edit_contact():
    return 'edit contact'

@app.route('/delete')
def delete_contact():
    return 'delete contact'


if __name__ == '__main__':
    app.run(port = 3000, debug = True)