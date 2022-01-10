
#from xgboost import XGBRFClassifier
import pickle
import numpy
from flask import Flask,render_template,request

app=Flask(__name__)

model=pickle.load(open("customer_churn_prediction.pkl","rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET","POST"])

def predict():
    if request.method=="POST":
        
        tenure= int(request.form["tenure"])
        MonthlyCharges=int(request.form["MonthlyCharges"])
        TotalCharges=int(request.form["TotalCharges"])
        gender=request.form["gender"]
        if(gender=="Male"):
            Male=1
            Female=0
        else:
            Male=0
            Female=1
        SeniorCitizen=request.form["SeniorCitizen"]
        if (SeniorCitizen=="Yes"):
            scyes=1
            scno=0
        else:
            scyes=0
            scno=1
        Partner=request.form["Partner"]
        if (Partner=="Yes"):
            part_yes=1
            part_no=0
        else:
            part_yes=0
            part_no=1
        Dependents=request.form["Dependents"]
        if (Dependents=="Yes"):
            dep_yes=1
            dep_no=0
        else:
            dep_yes=0
            dep_no=1
               
        PhoneService=request.form["PhoneService"]
        if (PhoneService=="Yes"):
            phone_yes=1
            phone_no=0
        else:
            phone_yes=0
            phone_no=1
           
        MultipleLines=request.form["MultipleLines"]
        if (MultipleLines=="Yes"):
            m_yes=1
            m_no=0
            m_No_phone_service=0
        elif (MultipleLines=="No"):
            m_yes=0
            m_no=1
            m_No_phone_service=0
        else:
            No_phone_service=1
            m_yes=0
            m_no=0
           
        InternetService=request.form["InternetService"]
        if (InternetService=="DSL"):
            int_yes=1
            int_no=0
            int_Fiber_optic=0
        elif (InternetService=="No"):
            int_yes=0
           int_no=1
           int_Fiber_optic=0
        else:
           int_yes=0
           int_no=0
           int_Fiber_optic=1
    
       
        OnlineSecurity=request.form["OnlineSecurity"]
        if (OnlineSecurity=="Yes"):
           online_yes=1
           online_no=0
           online_No_internet_service=0
        elif (OnlineSecurity=="No"):
           online_yes=0
           online_no=1
           online_No_internet_service=0
        else:
           online_yes=0
           online_no=0
           online_No_internet_service=1
           
       
        OnlineBackup=request.form["OnlineBackup"]
        if (OnlineBackup=="Yes"):
           backup_yes=1
           backup_no=0
           backup_No_internet_service=0
        elif (OnlineBackup=="No"):
           backup_yes=0
           backup_no=1
           backup_No_internet_service=0
        else:
           backup_yes=0
           backup_no=0
           backup_No_internet_service=1
           
        DeviceProtection=request.form["DeviceProtection"]
        if (DeviceProtection=="Yes"):
           devprot_yes=1
           devprot_no=0
           devprot_No_internet_service=0
        elif (OnlineBackup=="No"):
           devprot_yes=0
           devprot_no=1
           devprot_No_internet_service=0
        else:
           devprot_yes=0
           devprot_no=0
           devprot_No_internet_service=1
             
           
        TechSupport=request.form["TechSupport"]
        if (TechSupport=="Yes"):
           techsupp_yes=1
           techsupp_no=0
           techsupp_No_internet_service=0
        elif (TechSupport=="No"):
           techsupp_yes=0
           techsupp_no=1
           techsupp_No_internet_service=0
        else:
           techsupp_yes=0
           techsupp_no=0
           techsupp_No_internet_service=1
       
       
        StreamingTV=request.form["StreamingTV"]
        if (StreamingTV=="Yes"):
           str_yes=1
           str_no=0
           str_No_internet_service=0
        elif (StreamingTV=="No"):
           str_yes=0
           str_no=1
           str_No_internet_service=0
        else:
           str_yes=0
           str_no=0
           str_No_internet_service=1
       
       
        StreamingMovies=request.form["StreamingMovies"]
        if (StreamingMovies=="Yes"):
           strm_yes=1
           strm_no=0
           strm_No_internet_service=0
        elif (StreamingMovies=="No"):
           strm_yes=0
           strm_no=1
           strm_No_internet_service=0
        else:
           strm_yes=0
           strm_no=0
           strm_No_internet_service=1
       
           
        Contract=request.form["Contract"]
        if (Contract=="One year"):
           con_one=1
           con_two=0
           con_mtm=0
        elif (Contract=="Two year"):
           con_one=0
           con_two=1
           con_mtm=0
        else:
           con_one=0
           con_two=0
           con_mtm=1    
       
       
        PaperlessBilling=request.form["PaperlessBilling"]
        if (PaperlessBilling=="Yes"):
            pbil_yes=1
            pbil_no=0
        else:
            pbil_yes=0
            pbil_no=1
            
            
        PaymentMethod=request.form["PaymentMethod"]
        if (PaymentMethod=="Credit card (automatic)"):
           paycc=1
           payec=0
           paymc=0
           paybt=0
        elif (PaymentMethod=="Electronic check"):
           paycc=0
           payec=1
           paymc=0
           paybt=0
        elif (PaymentMethod=="Mailed check"):
           paycc=0
           payec=0
           paymc=1
           paybt=0   
        else:
           paycc=0
           payec=0
           paymc=0
           paybt=1
       
       
        outcome=model.predict([[tenure,MonthlyCharges,TotalCharges,Male,scyes,part_yes,dep_yes,phone_yes,m_yes,m_No_phone_service,int_no,int_Fiber_optic,online_yes,online_No_internet_service,backup_yes,backup_No_internet_service,devprot_yes,devprot_No_internet_service,techsupp_No_internet_service,techsupp_yes,str_No_internet_service,str_yes,strm_yes,strm_No_internet_service,con_one,con_two,pbil_yes,paycc,payec,paymc]])
        prob=model.predict_proba([[tenure,MonthlyCharges,TotalCharges,Male,scyes,part_yes,dep_yes,phone_yes,m_yes,m_No_phone_service,int_no,int_Fiber_optic,online_yes,online_No_internet_service,backup_yes,backup_No_internet_service,devprot_yes,devprot_No_internet_service,techsupp_No_internet_service,techsupp_yes,str_No_internet_service,str_yes,strm_yes,strm_No_internet_service,con_one,con_two,pbil_yes,paycc,payec,paymc]])
        
        prob0=round(prob[:,0][0],2)*100
        prob1=round(prob[:,1][0],2)*100
        
        if outcome==1:
            result1="Customer will Churn"
            result2="Probabilty is {}".format(prob1)
        else:
            result1="Customer will not churn"
            result2="Probability is {}".format(prob0)
            
        return  render_template("home.html", prediction_text1=result1, prediction_text2=result2)
    return render_template("home.html")

if __name__== "__main__":
    app.run(debug=(True))
    