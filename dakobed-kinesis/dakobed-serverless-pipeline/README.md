# Dakobed Serverless Pipeline

sam package --template-file ./template.yaml --output-template-file ./kinesis-lambda.yml --s3-bucket dakobed-serverless-pipeline

### Deploy with the SAM cli,  

sam deploy --template-file /data/mddarr/DakobedBard/dakobed-streams/dakobed-kinesis/dakobed-serverless-pipeline/kinesis-lambda.yml --stack-name DakobedServerlessStack

### Deploy with CloudFormation 

aws cloudformation deploy --template-file ./kinesis-lambda.yml  --stack-name DakobedServerlessStack --capabilities CAPABILITY_IAM


### Add Record to Stream

aws kinesis put-record --stream-name DakobedStream --partition-key 1 --data "Hello, this is a test."


