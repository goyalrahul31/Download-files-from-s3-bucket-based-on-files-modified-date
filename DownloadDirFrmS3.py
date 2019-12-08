from boto3.session import Session
from datetime import date, timedelta
import boto3
import re


def Download_pdf_specifc_date_subfolder(bucket_name,download_path)
    ACCESS_KEY = 'XYZ'
    SECRET_KEY = 'ABC'
    Bucket_name=bucket_name

    # code to create a session 
    session = Session(aws_access_key_id=ACCESS_KEY,
              aws_secret_access_key=SECRET_KEY)
    s3 = session.resource('s3')
    bucket = s3.Bucket(Bucket_name)

    # code to get the yesterdays date
    yesterday = date.today() - timedelta(days=1)
    x=yesterday.strftime('20%y-%m-%d')
    print(x)

    #code to add the files to a list which needs to be downloaded
    files_to_downloaded = []
    #code to take all the files from s3 under a specific bucket
    for fileObject in bucket.objects.all():
        file_name = str(fileObject.key)
        last_modified=str(fileObject.last_modified)
        last_modified=last_modified.split()
        if last_modified[0]==x:
    # Enter the specific bucketname in the regex in place of Airports to filter only the particluar subfolder
            if re.findall(r"Airports/[a-zA-Z]+", file_name):
                files_to_downloaded.append(file_name)

     # code to Download into a specific Folder 
    for fileObject in bucket.objects.all():
        file_name = str(fileObject.key)
        if file_name in files_to_downloaded:
            print(file_name)
            d_path=download_path + file_name
            print(d_path)
            bucket.download_file(file_name,d_path)

Download_pdf_specifc_date_subfolder(bucket_name,download_path)
