import boto3

def get_instances():
    ec2 = boto3.client('ec2')
    dynamodb = boto3.client('dynamodb')
    return "foo"