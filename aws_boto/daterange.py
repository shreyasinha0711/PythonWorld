import json
import os
import boto3
from datetime import datetime, timedelta, date
import dateutil
from dateutil.relativedelta import *
from decouple import config
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')
files_url_list = []
files_url_dict = {}
is_valid_auth = True
is_bucket_packet_available = True

def lambda_handler(event, context):
    date_from = event["queryStringParameters"]["FromDate"].replace('/','-').strip()
    date_to = event["queryStringParameters"]["ToDate"].replace('/','-').strip()
    format = '%Y-%m-%d'
    period = ''
    
    if((not(date_from) and date_to) or (not(date_to) and date_from)):
        return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "isBase64Encoded": False,
                "body": "One date parameter is missing"
            }
    elif(not(date_from and date_to)):
        period = 'full'
        today_date = str(date.today())
        get_all_objects_from_s3_full(today_date, period)
    else:
        try:
            period = 'daily'
            date_from_format = datetime.strptime(date_from, format).date()
            date_to_format = datetime.strptime(date_to, format).date()
            delta = date_to_format - date_from_format
            if(date_from_format > date_to_format):
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "isBase64Encoded": False,
                    "body": "Invalid date. From date can't be greater than to date"
                }
            elif((date_from_format >= date.today()-timedelta(days=30)) and delta.days<=30):
                period = 'daily'
                get_all_objects_from_s3_daily(date_from_format, delta, period)
            else: 
                return {
                    "statusCode": 400,
                    "headers": {
                        "Content-Type": "application/json"
                    },
                    "isBase64Encoded": False,
                    "body": "Date range should not be greater/older than 30 days"
                }
        except:
            return {
                "statusCode": 400,
                "headers": {
                    "Content-Type": "application/json"
                },
                "isBase64Encoded": False,
                "body": "Invalid date format. It can be either YYYY/MM/DD or YYYY-MM-DD"
            }
    files_url_dict = {
        "Files": files_url_list
        }
    if(not(is_valid_auth )):
        return {
                "statusCode": 401,
                "headers": {
                    "Content-Type": "application/json"
                },
                "isBase64Encoded": False,
                "body": "Invalid Auth Credentials/Parameters"
            }
    elif(not(is_bucket_packet_available)):
        return {
            "statusCode": 404,
            "headers": {
                "Content-Type": "application/json"
            },
            "isBase64Encoded": False,
            "body": "CFS Bucket/Package doesn't exists"
            }
    elif(len(files_url_list) == 0):
        return {
            "statusCode": 400,
            "headers": {
                "Content-Type": "application/json"
            },
            "isBase64Encoded": False,
            "body": "No files available between specified dates"
            }
    else:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
                },
            "isBase64Encoded": False,
            "body": json.dumps(files_url_dict)
        }

def get_all_objects_from_s3_full(today_date, period):
    try:
        month = today_date[0:7]
        objects = s3.list_objects_v2(
            Bucket='s3_bucket_name', Prefix=f'folder1/{period}/{today_date[0:7]}')
        for obj in objects['Contents']:
            path, filename = os.path.split(obj['Key'])
            if(filename):
                get_download_url_for_s3_objects(obj['Key'], month)
    except:
        a_month = dateutil.relativedelta.relativedelta(months=1)
        previous_month = str(date.today() - a_month)
        objects = s3.list_objects_v2(
            Bucket='s3_bucket_name', Prefix=f'folder1/{period}/{previous_month[0:7]}')
        for obj in objects['Contents']:
            path, filename = os.path.split(obj['Key'])
            if(filename):
                get_download_url_for_s3_objects(obj['Key'], previous_month[0:7])


def get_all_objects_from_s3_daily(date_from_format, delta, period):
    for i in range(delta.days + 1):
        day = date_from_format + timedelta(days=i)
        try:
            objects = s3.list_objects_v2(Bucket='s3_bucket_name', Prefix=f'folder1/{period}/{str(day)}')
            for obj in objects['Contents']:
                path, filename = os.path.split(obj['Key'])
                if(filename):
                    get_download_url_for_s3_objects(obj['Key'], day)
        except:
            logger.info("The object does not exist for %s ", day)

def get_download_url_for_s3_objects(object_key, day):
    downloadURL = get_cfs_url(object_key)
    if(downloadURL == 401):
        global is_valid_auth
        is_valid_auth = False
    elif(downloadURL == 404):
        global is_bucket_packet_available
        is_bucket_packet_available = False
    else:
        header = ["Date", "URL"]
        body = [str(day), downloadURL]
        file_dict = dict(zip(header,body))
        files_url_list.append(file_dict)

def get_access_token():
    authentication_url = "www.eee.com"
    try:
        response = authentication_url
        return response.json()['access_token']
    except:
        return 401

def get_cfs_url(object_key):
    print("hiii")