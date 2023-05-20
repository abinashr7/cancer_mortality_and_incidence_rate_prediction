from flask import Flask,render_template,request, send_file
import pickle
app = Flask(__name__)
model = pickle.load(open(r"naivemodel.pkl",'rb'))
@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/predict")
def prediction():
    print("prediction")
    return render_template("userInput.html")

@app.route("/submittedValue",methods = ["GET", "POST"])
def predictingBasedOnUserInput():
    
    if request.method == 'POST':
        index1_str=request.form.get('index')
        recentTrend_str=request.form.get('recentRate')
        fips_str=request.form.get('fips')    
        lowerConfidence1_str=request.form.get('lowerConfidence')
        ageAdjusted_str=request.form.get('aai')
        upperConfidence1_str=request.form.get('upperConfidence')
        lowerConfidence2_str=request.form.get('lowerConfidenceInterval')
        upperConfidence2_str=request.form.get('upperConfidenceInterval')
        annualCount_str=request.form.get('annualCount')
        country=request.form.get('country')
        state=request.form.get('state')
        province=request.form.get('province')   
        total = [[1151.0,
                  float(ageAdjusted_str),
                  float(lowerConfidence1_str),
                  float(upperConfidence1_str),
                  float(annualCount_str),
                  float(recentTrend_str),
                  float(lowerConfidence2_str),
                  float(upperConfidence2_str),
                  float(index1_str),
                  float(fips_str)]]
        t = model.predict(total)
        rate = {1:'falling',2:'stable',3:'*',4:'rising',5:'_',6:'__'}
       
        resVal=str(rate[int(t[0])])
        

        return render_template("userInput.html",showMessage=resVal,num=float(upperConfidence1_str))
    
    
 
if __name__ == '__main__':
    app.run()