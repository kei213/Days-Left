from flask import Flask, render_template
import datetime
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.static_folder = 'static'

today = datetime.date.today()
future = datetime.date(2036,4,21)
diff = future - today
days_left =(diff.days)

days_dict = {'days': days_left}
days_dict_json = json.dumps(days_dict)

@app.route("/")
def index():    
    return render_template("base.html", days_left=days_left)

@app.route('/api')  
def api():
    return days_dict_json

if __name__== "__main__":
	app.run(debug=True)

