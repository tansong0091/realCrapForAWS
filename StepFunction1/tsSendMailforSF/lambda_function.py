import json, boto3
from createUrlFunc import createUrl

def lambda_handler(event, context):
    
    print(event)
    step = 'SendApprovalRequest' 
    if step == 'SendApprovalRequest':
        # Prepare for creating Url
        input = {
           "albUrl": event['APIGatewayEndpoint'],
           "taskToken": event['ExecutionContext']['Task']['Token'],
           "executionName": event['ExecutionContext']['Execution']['Name'],
           "statemachineName": event['ExecutionContext']['StateMachine']['Name']
        }
        
        #Call createrul function by sending data in json format
        urls = json.loads(createUrl(json.dumps(input)))
        print(urls)
   
        # Compose email
        email_subject = 'Step Functions example approval request'

        email_body = """Hello {name},
        Click below (these could be better in HTML emails):

        Approve:
        {approve}

        Reject:
        {reject}
        """.format(
            name= 'ts',
            approve=urls['approve'],
            reject=urls['reject']
        )
        
    print('Sending email:', email_body)
    response = boto3.client('sns').publish(
        TopicArn='arn:aws-cn:sns:cn-north-1:XXXX:tsSFTopic',
        Subject=email_subject,
        Message=email_body
    )
    print(response)
    return { "status": 200}
