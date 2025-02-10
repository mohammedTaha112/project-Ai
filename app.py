from flask import Flask,render_template,request
import pickle
import numpy as np

with open("house_price_model.pkl", "rb") as file:
    model = pickle.load(file)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)[0]

        return render_template("index.html", prediction_text=f"السعر المتوقع: {prediction:.2f} دولار")
    
    except Exception as e:
        return render_template("index.html", prediction_text=f"حدث خطأ: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/contact",methods = ['POST'])
# def contact():
#     txt = request.form['text']
#     number = request.form['number',]

#     return render_template("contact.html",mytext = txt,mynumber =number )
# app.run()