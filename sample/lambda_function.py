import boto3

def lambda_handler(event, context):
    dynamodb = boto3.client('dynamodb')
    return "do something"

def get_table_name_from_res(res):
    return res['Table']['TableName']
