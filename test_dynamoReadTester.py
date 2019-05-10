import boto3
import json
import os
import pytest

client = boto3.resource('dynamodb',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ[
'AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
table = client.Table('TravisTest')



def dynamoGet(diningCommon, metric):
    #PreCondition: DiningCommon and metric are both strings
    #PostCondition: returns the wanted metric as a string
    #DiningCommon = "dlg","carrillo","ortega"
    #metric = "capacity","line"
    dynamoResponse = table.get_item(Key = {'diningCommon' : diningCommon})
    metric = dynamoResponse['Item'][metric]
    metric = str(metric)
    return metric

def test_dynamoRead():
    assert dynamoGet("dlg","line") == "45"

def test_dynamoUpdate():
    table.update_item(
    Key={'diningCommon': 'dlg'},
    UpdateExpression="set line =:line",
    ExpressionAttributeValues={
        ':line': 42
    },
    ReturnValues="UPDATED_NEW"
    )

    assert dynamoGet("dlg", "line") == "42"