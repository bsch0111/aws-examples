import json
import boto3

from botocore.exceptions import ClientError

def put_song(yyyymmdd, title, singer, country):
    dynamodb = boto3.resource("dynamodb", region_name ='us-east-1')
    
    try :
        response = dynamodb.Table('song').put_item(
            Item={
                "yyyymmdd" : yyyymmdd,
                "title" : title,
                "info" : {
                    "singer" : singer,
                    "country": country
                }
            }
        )
    except ClientError as e :
        print(e.response["Error"]["Message"])
    else:
        return response

def get_song(yyyymmdd, title):
    dynamodb = boto3.resource("dynamodb", region_name="us-ease-1")
    
    try:
        response = dynamodb.Table("song").get_item(
            Key={"yyyymmdd": yyyymmdd, "title" : title})
    except ClientError as e:
        print("clientError")
        print(e.response["Error"]["Message"])
    else:
        print("invoke success")
        return response
        
def update_song(yyyymmdd, title, singer, country):
    """docstring for update_song"yyyymmdd, title, singer, country"""
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    
    try:
        response = dynamodb.Table("song").update_item(
            Key={"yyyymmdd": yyyymmdd, "title" : title},
                UpdateExpression = "SET info= :values",
                ExpressionAttributeValues = {
                    ":values": {"singer": singer, "country": country}
                }
            )
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        return response
    
    
def lambda_handler(event, context):
    # TODO implement
    # song_put_reponse = put_song(20120715, "gangnam stryle", "psy", "korea")
    #update_response = update_song(20120715, "gangnam stryle", "psy", "south korea")
    #body = json.loads(event.get(['body']))
    
    put_song_response = put_song(1111111,"32312312312312","qqqq","qeqe")
    return put_song_response
