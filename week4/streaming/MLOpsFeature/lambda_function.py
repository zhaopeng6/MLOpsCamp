import json
import boto3
import pandas as pd
from codeguru_profiler_agent import with_lambda_profiler

@with_lambda_profiler(profiling_group_name="aws-lambda-codeguru")
def lambda_handler(event, context):
    churn = pd.read_csv("./churn.txt")
    pd.set_option("display.max_columns", 500)
    churn = churn.drop("Phone", axis=1)
    churn["Area Code"] = churn["Area Code"].astype(object)
    churn = churn.drop(["Day Charge", "Eve Charge", "Night Charge", "Intl Charge"], axis=1)
    model_data = pd.get_dummies(churn)
    model_data = pd.concat(
        [model_data["Churn?_True."], model_data.drop(["Churn?_False.", "Churn?_True."], axis=1)], axis=1
    )
    model_data = model_data.astype(float)
    model_data.head()
    model_data.to_csv("/tmp/results.csv", header=False, index=False)
    s3 = boto3.client('s3')
    s3_file = "feature/results.csv"

    try:
        s3.upload_file("/tmp/results.csv", "sagemaker-us-west-2-846634201516", s3_file)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': "sagemaker-us-west-2-846634201516",
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except:
        print("error")
        return None
