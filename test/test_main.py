import boto3
import logging
from moto import mock_dynamodb

from utils import create_table

from sample.lambda_function import get_table_name_from_res

logger = logging.getLogger(__name__)


def test_context_managerでtest_tableが作られているか確認する(create_db_by_context_manager):
    dynamodb_client = boto3.client('dynamodb')
    res = dynamodb_client.describe_table(TableName='test_table')
    assert get_table_name_from_res(res) == 'test_table'


@mock_dynamodb
def test_decoratorでtest_tableが作られているか確認する():
    create_table()
    dynamodb_client = boto3.client('dynamodb')
    res = dynamodb_client.describe_table(TableName='test_table')
    assert get_table_name_from_res(res)  == 'test_table'
