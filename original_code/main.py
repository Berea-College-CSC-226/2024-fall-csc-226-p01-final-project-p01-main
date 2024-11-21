####################################################
# Name: Besher Kitaz
# username: kitazb
#
# CSC: 226
#
####################################################
#
#
# Inspired by: https://docs.google.com/document/d/1ww0ajH0ahH8wBKCp3uY6fe_THjE8BJZ_3iYgnOO8ovg/edit?tab=t.0#heading=h.qg98s23ap4mh
#
#
####################################################


from flask import Flask, render_template, request
from user import *
app = Flask(__name__, template_folder='templates')
students = students_list()

@app.route('/')
def index():
    """
    Renders the main homepage and send it to the server
    :return:
    """
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def home():
    """Renders a form and sends it to the server"""

    # Still not complete
    if request.method == 'POST':
        name = request.form['name']
        pin = request.form['pin']
        # Process form data to database here

        print(name, pin) # For testing; to be removed

        return f"Form submitted! Name: {name}, PIN: {pin}"

    return render_template('student_form.html')



if __name__ == '__main__':
    app.run(debug=True)

