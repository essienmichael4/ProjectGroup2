from flask import Flask, render_template, request
import requests
import pyowm
app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
#def index():
#    temp = ""
 #   if request.method == 'POST':
  #      if request.form.get('temperature')=='temperature':
   #         temp = "10"

    #return render_template('index.html', temperature = temp )
def get_data():
    return requests.get('https://192.168.43.231:5000/api/humidity').content
    




#@app.route('/', methods=['GET', 'POST'])
#def index():
#    temp = ""
#    if request.method == 'POST':
#        if request.form.get('temperature')=='temperature':
#            temp = "10"

#   return 'Hello world'
#    return render_template('index.html', temperature = temp )

@app.route('/temperature/', methods=['POST'])
def temperature():
    print("10")
    return render_template('index.html')


if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
