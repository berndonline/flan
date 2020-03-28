import boto3
import sys
import os

filename = sys.argv[1]

s3_client = boto3.client('s3',
                        region_name = os.getenv('region'),
                        endpoint_url = os.getenv('s3url')
                        )
try:
    response = s3_client.upload_file("/" + filename, os.getenv('bucket'),
                                     filename)
except Exception as e:
    print('Error uploading to s3')
    print(e)
