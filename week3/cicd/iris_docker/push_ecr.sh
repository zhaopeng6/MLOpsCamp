#!/usr/bin/env bash

## Complete the following steps to get Docker image pushed to aws ecr locally
#!/usr/bin/env bash

## Complete the following steps to get Docker image pushed to aws ecr locally
region="us-east-1"
ecr_repo="977098985723.dkr.ecr.us-east-1.amazonaws.com"
image_name="iris_predict_yl"
image_tag="latest"
echo "Logging in to Amazon ECR..."
aws --version
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $ecr_repo
#docker build --tag=$image_name .
#docker tag $image_name:$image_tag $ecr_repo/$image_name:$image_tag
#docker push $ecr_repo/$image_name:$image_tag

