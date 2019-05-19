//test_leastCrowdedIntent.py

import boto3
import json
import os
import pytest
import decimal
from boto3.dynamodb.conditions import Key, Attr

from dynamoFunctions import *

client = boto3.resource('dynamodb',aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ[
'AWS_SECRET_ACCESS_KEY'], region_name='us-east-1')
table = client.Table('leastCrowdedTest')

def test_readCapacities():
    print("\ntest_readCapacities():\n")
    print("dlg == 1")
    assert dynamoGet("dlg", "capacity") == "1"
    print("carrillo == 2")
    assert dynamoGet("carrillo", "capacity") == "2"
    print("ortega == 3")
    assert dynamoGet("ortega", "capacity") == "3"

def test_leastCrowded():
    print("\ntest_leastCrowded():\n")
    dlg = ("dlg", dynamoGet("dlg", "diningCapacity"))
    carrillo = ("carrillo", dynamoGet("carrillo", "diningCapacity"))
    ortega = ("ortega", dynamoGet("ortega", "diningCapacity"))

    if (dlg[1] == 0) and (carrillo[1] == 0) and (ortega[1] == 0):
        speech = buildSpeech("The dining commons are closed")
    else:
        if (dlg[1] <= carrillo[1]) and (dlg[1] <= ortega[1]):
            leastCrowded = (dlg[0], dlg[1])
        elif (carrillo[1] <= dlg[1]) and (carrillo[1] <= ortega[1]):
            leastCrowded = (carrillo[0], carrillo[1])
        else:
            leastCrowded = (ortega[0], ortega[1])
        speech = buildSpeech("The least crowded dining common is " +
                                leastCrowded[0] + " with capacity " + leastCrowded[1])
    print("testing least crowded:\n")
    assert leastCrowded[0] == "dlg"
    print("testing capacity:\n")
    assert leastCrowded[1] == "1"

    
