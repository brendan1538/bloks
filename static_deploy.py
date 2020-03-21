#!/usr/bin/python3

import boto3

s3 = boto3.resource('s3')
def list_bucket_objects(bucketName):
    bucket = s3.Bucket(bucketName)
    for bucket_obj in bucket.objects.all():
        print(bucket_obj)

if __name__ == '__main__':
    list_bucket_objects(bucket)
