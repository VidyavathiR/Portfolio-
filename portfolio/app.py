from flask import Flask, render_template, request
from database import add_msg_to_db

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def myapp():
    if request.method == 'POST':
        data = request.form
        add_msg_to_db(data)
        return render_template("index.html", data=data)
    else:
       
        return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)