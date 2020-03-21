#!/usr/bin/python3

import yaml
import static_deploy

process = {}

def run_process():
    with open('process.yaml') as p:
        process = yaml.load(p, Loader=yaml.FullLoader)
        
    bucket = process['jobs']['deploy']['bucket']
    static_deploy.list_bucket_objects(bucket)

if __name__ == '__main__':
    run_process()

