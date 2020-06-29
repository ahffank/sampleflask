 
from flask import Flask,render_template,request,url_for
from fastai.basic_train import load_learner
from fastai.vision import open_image
from flask_cors import CORS,cross_origin

app = Flask(__name__)


#learn = load_learner(path='./Model', file='trained_model.pkl')
#classes = learn.data.classes

def predict_single(img_file):
   'function to take image and return prediction'
   prediction = learn.predict(open_image(img_file))
   probs_list = prediction[2].numpy()
   return(probs_list)
   return {
       'category': classes[prediction[1].item()],
       'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(classes)}
   }


@app.route("/")
def homepage():
    return render_template("index.html", title="HOME PAGE")

@app.route("/docs")
def docs():
    return render_template("index.html", title="docs page")

@app.route("/about")
def about():
    return render_template("index.html", title="about page")
 
@app.route("/",methods=['POST']) 
def predict():
    if request.method == 'POST':
        return render_template('results.html',prediction = [1],comment = "asd")
  
   

if __name__ == "__main__":
    app.run(debug=True)
