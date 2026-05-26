from fastapi import FastAPI
import pickle 

with open('linear_sale.pkl', 'rb') as f :
    model = pickle.load(f)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "model ML du doan sales"}


@app.post("/predict")
def predict (price: float, ads_cost: float):
    input_data = [[price, ads_cost]]
    prediction = model.predict(input_data)
    return {"predicted_sales_volume": prediction[0][0]}


