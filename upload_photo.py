import boto3

import os


access_key = 'AKIASYJI4PBHNJY72AVK'
secret_access_key = '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'

client = boto3.client('s3',
                      aws_access_key_id=access_key,
                      aws_secret_access_key=secret_access_key)
for file in os.listdir():
    if '.png' in file:
        upload_file_bucket = 'employbucket'
        upload_file_key = 'photo/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)
        os.remove(file)
