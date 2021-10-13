import boto3
import botocore.exceptions
import os
import logging
import json

s3 = boto3.client('s3')
client_lambda = boto3.client('lambda', region_name='eu-west-1')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    file_validation = []
    validation_map = [
        'File_Format_Valid',
        'File_Encoding_Valid',
        'Column_Name_Valid',
        'Column_Number_Valid',
        'Delimiter_Valid'
    ]

    triggered_key = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']

    logger.info("New file has been downloaded into S3 for processing : {}".format(triggered_key))

    path, name = os.path.split(triggered_key)
    local_file = f"/tmp/{name}"

    download_file_s3(bucket_name, triggered_key, local_file)

    file_validation = file_format_validation(local_file, file_validation)
    file_validation = file_encoding_validation(local_file, file_validation)

    if triggered_key.startswith("folder1/"):
        file_validation = folder1_file_col_name(local_file, file_validation)
        file_validation = folder1_file_delimiter_colnumber(local_file, file_validation)
    elif triggered_key.startswith("folder2/"):
        file_validation = folder2_file_col_name(local_file, file_validation)
        file_validation = folder2_file_delimiter_colnumber(local_file, file_validation)

    file_validation.sort()
    validation_map.sort()

    invoking_event = {
        'triggered_key': triggered_key,
        'bucket_name': bucket_name
    }

    if file_validation == validation_map and triggered_key.startswith("folder1/"):
        logger.info(f"File {triggered_key} is valid")
        response = client_lambda.invoke(
            FunctionName='a250348-folder1-text-json-conversion',
            InvocationType='Event',
            Payload=json.dumps(invoking_event)
        )
        logger.info("Response from Invocation - {}".format(response))
    elif file_validation == validation_map and triggered_key.startswith("folder2/"):
        logger.info(f"File {triggered_key} is valid")
        response = client_lambda.invoke(
            FunctionName='a250348-folder2-text-json-conversion',
            InvocationType='Event',
            Payload=json.dumps(invoking_event)
        )
        logger.info("Response from Invocation - {}".format(response))
    else:
        logger.error(f"File {triggered_key} is invalid")

    cleanup(local_file)


def download_file_s3(bucket_name, key, file_location):
    try:
        s3.download_file(bucket_name, key, file_location)
        logger.info("File downloaded to : {}".format(file_location))
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            logger.error("The object does not exist in bucket : {}".format(bucket_name))
        raise e


def file_format_validation(file_key, file_validation):
    if os.path.splitext(file_key)[-1].lower() == '.txt':
        file_validation.append('File_Format_Valid')
    else:
        logger.error("File Format is not a valid Text file")

    return file_validation


def file_encoding_validation(file_key, file_validation):
    try:
        with open(file_key, 'r', encoding='utf-8') as file:
            pass
        file_validation.append('File_Encoding_Valid')
    except UnicodeDecodeError:
        logger.error("Invalid UTF-8 encoding used")

    return file_validation


def folder1_file_col_name(file_key, file_validation):
    folder1_file_expected_cols = [
        'Name',
        'ID',
        'Country',
        'DetailNumber',
        'Description',
        'EffDate',
        'ExpDate'
    ]

    with open(file_key, 'r', encoding='utf-8-sig') as header_value:
        folder1_file_actual_cols = header_value.readline().rstrip('\n').split('|')
        if folder1_file_actual_cols == folder1_file_expected_cols:
            file_validation.append('Column_Name_Valid')
        else:
            logger.error("Column Names are not valid : {}".format(folder1_file_actual_cols))

    return file_validation


def folder2_file_col_name(file_key, file_validation):
    folder2_file_expected_cols = [
        'Id',
        'Name',
        'EffDate',
        'ExpDate',
        'DetailNum',
        'ExportCountry',
        'ImportCountry',
        'LicenseNeed'
    ]

    with open(file_key, 'r', encoding='utf-8-sig') as header_value:
        folder2_file_actual_cols = header_value.readline().rstrip('\n').split('|')
        if folder2_file_actual_cols == folder2_file_expected_cols:
            file_validation.append('Column_Name_Valid')
        else:
            logger.error("Column Names are not valid : {}".format(folder2_file_actual_cols))

    return file_validation


def folder1_file_delimiter_colnumber(file_key, file_validation):
    with open(file_key, 'r') as description_data:
        for line in description_data:
            line = line.strip()
            description_row = line.split('|')
            if len(description_row) == 7:
                valid_check = True
            else:
                logger.error("Delimiter is not Pipe operator/Column Number is Invalid : {}".format(line))
                valid_check = False
                break
        if valid_check:
            file_validation.append('Delimiter_Valid')
            file_validation.append('Column_Number_Valid')

    return file_validation


def folder2_file_delimiter_colnumber(file_key, file_validation):
    with open(file_key, 'r') as license_data:
        for line in license_data:
            line = line.strip()
            license_row = line.split('|')
            if len(license_row) == 8:
                valid_check = True
            else:
                logger.error("Delimiter is not Pipe operator/Column Number Invalid : {}".format(line))
                valid_check = False
                break
        if valid_check:
            file_validation.append('Delimiter_Valid')
            file_validation.append('Column_Number_Valid')

    return file_validation


def cleanup(file_key):
    if os.path.exists(file_key):
        os.remove(file_key)
        logger.info("Cleanup of tmp directory is complete")
    else:
        logger.info("Can not delete the file as it does not exist")
