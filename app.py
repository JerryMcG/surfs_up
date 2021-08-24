from flask import Flask

#create new flask instance
app= Flask(__name__)

#creating routes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/contact')
def contact():
    return 'Call me on my cellphone'