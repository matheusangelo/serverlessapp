import json
import boto3
from elasticsearch import Elasticsearch

s3 = boto3.client('s3')
S3_BUCKET_NAME = 'bucket'
key = 'data.json'
es_host = 'localhost'
es_port = 9200
session = boto3.Session()
credentials = session.get_credentials()

es = Elasticsearch('localhost:9200')

def create(event, context):

    json_data = json.dumps(event['body'])

    es.index(index='people', doc_type='person', id=1, body=event['body'])

    s3.put_object(Bucket=S3_BUCKET_NAME, Key='data.json', Body=json_data) 

    return {
        "statusCode": 200,
        "body": json_data
    }
  
def get(event, context):
    response = s3.get_object(Bucket=S3_BUCKET_NAME, Key=key)

    json_data = response['Body'].read().decode('utf-8')
    data = json.loads(json_data)


    search_result = es.search(index='people', body={'query': {'match': {'city': 'New York'}}})

    response = {
        "statusCode": 200,
        "body": json.dumps(search_result['hits']['hits'])
    }
    
    return response