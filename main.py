 
from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("index.html", title="docs page")

@app.route("/about")
def about():
    return render_template("index.html", title="about page")
 
@app.route("/predict")
def predict():
    if request.method == 'POST': 
		  
    #my_prediction = predict_single(request.files['image'])
	   return render_template('results.html',prediction = "hi",comment = "Ahffan")
    return()
   

if __name__ == "__main__":
    app.run(debug=True)
