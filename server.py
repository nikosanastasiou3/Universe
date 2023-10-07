from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route('/<string:page_name>')
def page_name(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Not Saved to database.'
    else:
        return 'Something went wrong, please go back'


def write_to_database(data):
    with open('./database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

#check this again not working as expected on newline
def write_to_csv(data):
    with open('./database2.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
