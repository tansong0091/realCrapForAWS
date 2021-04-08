import json, boto3


def lambda_handler(event, context):
    
    print(event['queryStringParameters'])
    if event['queryStringParameters']['action'] == 'approve':
        userAction = 'approve'
        message = {"Status": "Approved! Task approved"}
        print('approve')
    elif event['queryStringParameters']['action'] == 'reject':
        userAction = 'reject'
        message = {"Status": "Rejected! Task rejected"}
        print('reject')
    else:
        return{}
    
    client = boto3.client('stepfunctions')    
    response = client.send_task_success(
        taskToken=event['queryStringParameters']['taskToken'],
        output = json.dumps(message)
    )    

    return {
        'statusCode': 200,
        'body': json.dumps(userAction)
    }

