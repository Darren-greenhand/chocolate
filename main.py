#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask
from flask import request,render_template
from keras.models import load_model


# In[2]:


app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        NP = request.form.get("NP_TA")
        TL = request.form.get("TL_TA")
        WC = request.form.get("WC_TA")
        print(NP,TL,WC)
        model = load_model("bankruptPrediction")
        pred = model.predict([[float(NP),float(TL),float(WC)]])
        print(pred)
        pred = pred[0][0]
        s = "The predicted Bankrupty score is : "+str(pred)
        result = s
        return(render_template("main.html",result = s))
    else:
        return(render_template("main.html",result = "Please try again"))


# In[ ]:


if __name__ == "__main__":
    app.run()



# In[ ]:




