# import main Flask class and request object
from flask import Flask,render_template, request,session,redirect,secrets
# create the Flask app
app = Flask(__name__)

app.secret_key = 'A secret string'

# Form Page
@app.route('/', methods = ["GET"])
def index():
    return render_template('index.html')

# # Have the "/result" route display the information on a new HTML Page

@app.route("/result", methods=["POST"])
def form_result():
    
        session["name"] = request.form["name"]
        session["location"]=request.form["location"]
        session["language"]=request.form["language"]
        session["comments"]=request.form["comments"]
        
        return redirect("result.html")

if __name__=="__main__":
    
    app.run(debug=True)
    

