from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"

    if 'counter' in session:
        session['counter'] += 1
        session['pagevisits'] += 1
        return render_template('index.html', x=session['counter'], page)

    if __name__ == "__main__":
        app.run(debug=True)
#Virtual environment failed to be created
# Create the virtual environment
# 	a. in terminal
# 	b. pip3 install pipenv —> press enter
# 	c. pip3 list —> press enter to see the version of pipenv installed
# 	d. open VSC folder (counter) —> press command-shift-c
# 	e. python3 -m pipenv shell —> press enter to activate virtual environment
# ERROR:: --system is intended to be used for pre-existing Pipfile installation, not installation of specific packages. Aborting.
# boydlever@Boyds-MacBook-Air Counter % 
# 	 f. python3 server.py —> Launch the server after server.py is set up