#!/usr/bin/env bash

## Complete the following steps to get Docker image pushed to aws ecr locally
region="us-west-1"
ecr_repo="798223350085.dkr.ecr.us-west-1.amazonaws.com"
image_name="iris_pred"
image_tag="latest"
echo Logging in to Amazon ECR...
aws --version
aws ecr get-login-password --region $region | docker login --username AWS --password-stdin $ecr_repo
docker build --tag=$image_name .
docker tag $image_name:$image_tag $ecr_repo/$image_name:$image_tag
docker push $ecr_repo/$image_name:$image_tag
