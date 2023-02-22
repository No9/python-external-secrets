import os
from dotenv import load_dotenv

load_dotenv()

import ibm_boto3
from ibm_botocore.client import Config, ClientError

import ibm_boto3

COS_CREDENTIAL = os.getenv('COS_CREDENTIAL')
COS_ENDPOINT = os.environ.get('COS_ENDPOINT')
COS_SERVICE_INSTANCE_ID = os.environ.get('COS_SERVICE_INSTANCE_ID')
COS_AUTH_ENDPOINT = os.environ.get('COS_AUTH_ENDPOINT')

cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_CREDENTIAL,
    ibm_service_instance_id=COS_SERVICE_INSTANCE_ID,
    ibm_auth_endpoint=COS_AUTH_ENDPOINT,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)


def get_buckets():
    print("Retrieving list of buckets")
    try:
        buckets = cos.buckets.all()
        for bucket in buckets:
            print("Bucket Name: {0}".format(bucket.name))
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve list buckets: {0}".format(e))

get_buckets()

import time
while True: time.sleep(0.2)