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

from flask import abort
from flask import Flask, render_template, request
from user import *
import sqlite3
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    """
    Renders the main homepage and send it to the server
    :return: rendered html template
    """
    students = students_list()
    return render_template('index.html', students=students)


@app.route('/user_detail', methods=['GET', 'POST'])
def user_detail():
    """
    Displays the user's details
    :return: rendered html template
    """
    if request.method == 'GET':
        id = request.args.get('id', type=int)
        user = User(id)
        user_data = user.retrieve_data()
        courses = user.retrieve_courses()
        context = {
            'student': {
                'name': user_data[0],
                'PIN': user_data[1],
                'id': user_data[2],
            },
            'courses': courses,
        }
        return render_template("user_detail.html", context=context)

    if request.method == 'POST':
        pin = request.form['pin']
        crn = request.form['crn']
        id = request.args.get('id')
        # Process form data to database here
        user = User(id)
        if user.pin != pin:
            return "Incorrect PIN. Please try again."

        try:
            user.add_course_through_crn(crn)

        except TypeError:
            abort(404)

        except sqlite3.IntegrityError:
            return "Class already added"


        context = {
            'student_id': id
        }
        return  render_template("confirmation_page.html", context=context)




if __name__ == '__main__':
    app.run(debug=True)

