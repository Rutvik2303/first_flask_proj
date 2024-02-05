from flask import Flask  , request 

app = Flask(__name__)
tocken="123456"
prd_lst=['prd1','prd2']

@app.route("/",methods=['GET', 'POST'])
def hello_world():
    crad= request.json
    crad_keys=crad.keys()
    if ("email" and "password" in crad_keys):
        if (crad["email"]=="John" and crad["password"]==30):
            return tocken
        else:
            return "wrong credentials",401
    else:
        return "wrong credentials",401


    print(crad["email"])
    return "index.html"

@app.route("/product/" ,methods=['GET', 'POST','PUT','PATCH','DELETE']  )
def ok():
    auth=request.headers['Authorization']
    print(type(request.method))
    if (auth==tocken):
        if (request.method =="GET"):
            return prd_lst
        elif(request.method =="POST"):
            prd=request.json
            print(prd['prod'])
            prd_lst.append(prd['prod'])
            return prd_lst
        else:
            return "wrong Methord",405
    else:
        return "wrong credentials",400


app.run(debug=True)