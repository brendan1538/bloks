#!/usr/bin/python3

import boto3
from botocore.exceptions import ClientError
import os

def upload_to_s3(bucket, s3, repoDir, buildOutputFolder):
    # declare objectName and fileName
    buildDir = os.path.join(repoDir, buildOutputFolder[0].replace('/', ''))
    files = [os.path.join(dirpath, name)
             for dirpath, subdirs, files in os.walk(buildDir, topdown=True)
             for name in files
            ]

    print(f'Pushing contents of {buildOutputFolder[0]} to {bucket} s3 bucket')
    for file in files:
      fileName = file.split(repoDir)[1].lstrip('/')
      try:
        res = s3.upload_file(file, bucket, fileName)
      except ClientError as err:
        print(err)
    print(f'Successfully pushed to {bucket}')

def main_process(processArgs, repoDir, buildOutputFolder):
    bucketName = processArgs['bucket']
    AWS_ACCESS_KEY_ID = processArgs['access_key']
    AWS_SECRET_ACCESS_KEY = processArgs['secret_key']

    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    upload_to_s3(bucketName, s3, repoDir, buildOutputFolder)

if __name__ == '__s3__':
    main_process()
