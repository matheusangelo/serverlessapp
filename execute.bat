aws lambda list-functions --endpoint-url http://localhost:4566

aws lambda invoke --function-name myService-local-hello --endpoint-url http://localhost:4566 response.json

serverless deploy --stage local