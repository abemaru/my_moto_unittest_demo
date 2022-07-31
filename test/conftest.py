import os
import pytest

import boto3
from moto import mock_dynamodb

def set_env():
    """公式推奨のenv設定
    万が一にも本番環境へ変更が当たらないようにする
    """
    os.environ['AWS_ACCESS_KEY_ID'] = 'test'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'test'
    os.environ['AWS_DEFAULT_REGION'] = 'ap-northeast-1'
    os.environ['AWS_SECURITY_TOKEN'] = 'test'
    os.environ['AWS_SESSION_TOKEN'] = 'test'


@pytest.fixture
def create_db_by_context_manager():
    set_env()

    with mock_dynamodb():
        dynamodb = boto3.client('dynamodb')
        table = dynamodb.create_table(
            TableName='test_table',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        yield table


@pytest.fixture
def create_db_by_decorator():
    set_env()

    dynamodb = boto3.client('dynamodb')
    table = dynamodb.create_table(
        TableName='test_table',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table