import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# load the saved model
kmeans = joblib.load("model/model.pkl")

# instantiate the FastApi app
app = FastAPI(
    title="K-Means Clustering API",
    description="An API for clustering customer data based on annual income"
                " and spending score using k-Means Clustering"
)

#Define the input data schema
class CustomerData(BaseModel):
    annual_income: float
    spending_score: float



@app.post("/predict",
          summary="predict customer cluster",
          description="predict whether the customer belongs to cluster 0,1,2,3,4",
          tags = ["predictions"]
)
def predict_cluster(data: CustomerData):
    # prepare the input for prediction
    input_data = np.array([[data.annual_income, data.spending_score]])
    cluster = kmeans.predict(input_data)[0]

    # map cluster numbers to letters
    cluster_mapping = {
        0: "Prudent spenders",
        1: "Generous spenders",
        2: "Extravagant spenders",
        3: "Wise spenders",
        4: "Loose spenders"
    }

    cluster_label = cluster_mapping,.get(cluster, "Unknown Cluster")
    return {"cluster": cluster_label}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)












