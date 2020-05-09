#!/usr/bin/python3

import boto3
from botocore.exceptions import ClientError
import os
import sys

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
        print(f'Successfully pushed to {bucket}')
      except:
        print(f'Failed to push to {bucket}')

def main_process(processArgs, repoDir, buildOutputFolder):
    bucketName = processArgs['bucket']
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_KEY')
    
    if AWS_ACCESS_KEY_ID == None or AWS_SECRET_ACCESS_KEY == None:
      print('AWS_ACCESS_KEY and AWS_SECRET_KEY environment variables need to be set.')
      sys.exit()
    else:
      s3 = boto3.client(
          's3',
          aws_access_key_id=AWS_ACCESS_KEY_ID,
          aws_secret_access_key=AWS_SECRET_ACCESS_KEY
      )

      upload_to_s3(bucketName, s3, repoDir, buildOutputFolder)

if __name__ == '__main__':
    main_process()
