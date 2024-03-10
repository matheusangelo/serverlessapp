SET AWS_ACCESS_KEY_ID=S3RVER
SET AWS_SECRET_ACCESS_KEY=S3RVER
SET AWS_DEFAULT_REGION=us-east-1
SET AWS_IGNORE_CONFIGURED_ENDPOINT_URLS=true
@REM aws dynamodb create-table --table-name ddb --attribute-definitions AttributeName=Id,AttributeType=N --key-schema AttributeName=Id,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5 --endpoint-url http://localhost:5008

serverless offline start