from flask import Flask, render_template
import datetime

today = datetime.date.today()
future = datetime.date(2036,4,21)
diff = future - today
days_left =(diff.days)

app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def index():	
	return render_template("base.html", days_left=days_left)



if __name__== "__main__":
	app.run(debug = True)

