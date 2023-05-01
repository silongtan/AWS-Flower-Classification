import boto3
import json

def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)

    return response

def load_labels(file_name, bucket):
    """
    Function to load labels of the image
    """
    s3 = boto3.resource('s3')
    json_data = ""
    # lables = ""
    try:
        obj = s3.Object('output-res', f"{file_name}.json")
        data = obj.get()['Body'].read().decode('utf-8')
        json_data = json.loads(data)
        # labels = str(json_data['Labels'])
    except Exception as e:
        pass

    return json_data

def download_file(file_name, bucket):
    """
    Function to download a given file from an S3 bucket
    """
    s3 = boto3.resource('s3')
    output = f"downloads/{file_name}"
    s3.Bucket(bucket).download_file(file_name, output)

    return output

def list_files(bucket):
    """
    Function to list files in a given S3 bucket
    """
    s3 = boto3.client('s3')
    contents = []
    try:
        for item in s3.list_objects(Bucket=bucket)['Contents']:
            print(item)
            contents.append(item)

        #for item in s3.list_objects(Bucket="output-res")['Contents']:
        #    print(item)
        #    contents.append(item)
    except Exception as e:
        pass

    return contents