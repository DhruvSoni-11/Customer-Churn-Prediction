from fastapi import FastAPI
from fastapi.responses import JSONResponse
from  pydantic import BaseModel, Field
from typing import Annotated, Literal
import pickle
import pandas as pd

with open("churn_model.pkl", "rb") as f:
    saved_data = pickle.load(f)

model = saved_data["model"]
columns = saved_data["columns"]

    
class UserInput(BaseModel):
    tenure : Annotated[int,Field(...,description='tenure of subscription(in Months)')]
    monthly: Annotated[float, Field(..., description='Monthly charges')]
    total: Annotated[float, Field(..., description='Total charges')]
    contract: Annotated[Literal['Month-to-month','One year','Two year'], Field(...,description='type of contract of user')] 
    internet: Annotated[Literal['DSL','Fiber optic','No'], Field(...,description='type of Internet')]
    

app = FastAPI()

@app.post('/predict')
def predict_churn(data: UserInput):

    # Input dictionary
    input_data = {
        "tenure": data.tenure,
        "MonthlyCharges": data.monthly,
        "TotalCharges": data.total,

        "Contract_One year": 0,
        "Contract_Two year": 0,

        "InternetService_Fiber optic": 0,
        "InternetService_No": 0
    }

    # Contract Encoding
    if data.contract == "One year":
        input_data["Contract_One year"] = 1

    elif data.contract == "Two year":
        input_data["Contract_Two year"] = 1

    # Internet Encoding
    if data.internet == "Fiber optic":
        input_data["InternetService_Fiber optic"] = 1

    elif data.internet == "No":
        input_data["InternetService_No"] = 1

    # DataFrame
    input_df = pd.DataFrame([input_data])

    # Match columns
    input_df = input_df.reindex(columns=columns, fill_value=0)

    # Prediction
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    # Output
    if pred == 1:
        result = f"High Risk of Churn ({prob*100:.2f}%)"
    else:
        result = f"Low Risk of Churn ({(1-prob)*100:.2f}%)"

    return JSONResponse(status_code=200,content={'result':result})