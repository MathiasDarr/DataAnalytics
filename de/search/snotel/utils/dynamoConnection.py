import boto3

def getDynamoResource(local=True):
    if local==True:
        return boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    else:
        return boto3.resource('dynamodb', region_name='us-east-2')

def getDynamoDBClient(local=True):
    '''
    If local is set to true then this will return a connection to the local database running in a docker container.
    :param local:
    :return:
    '''
    if local:
        return boto3.client('dynamodb', endpoint_url='http://localhost:8000')
    else:
        return boto3.client('dynamodb', region_name='us-west-2')