from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
#	return 'Hello world'
	return render_template('index.html')

#@app.route('/about')
#def about():
#        return render_template('about.html')

#@app.route('/signup')
#def signup():
#        return render_template('signup.html')

#@app.route('/services')
#def services():
#        return render_template('services.html')

#@app.route('/login')
#def login():
#        return render_template('login.html')

#@app.route('/contacts')
#def contacts():
#        return render_template('contacts.html')

#@app.route('/whereami')
#def whereami():
#	return 'Ghana!'


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
