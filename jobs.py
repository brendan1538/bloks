#!/usr/bin/python3

import import_modules.py
import static_deploy
import yaml

def run_job(yamlFile):
    bucket = yamlFile['jobs']['deploy']['bucket']
    static_deploy.list_bucket_objects(bucket)

# build job
def build(yamlFile):
    print(yamlFile['use'])

