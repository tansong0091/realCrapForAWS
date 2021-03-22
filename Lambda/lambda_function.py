import json
import boto3
import requests

client = boto3.client('codedeploy')

def lambda_handler(event, context):
    # TODO implement
    print(type(event))
    print('DeploymentId:', event['DeploymentId'])
    print('LifecycleEventHookExecutionId:', event['LifecycleEventHookExecutionId'])
    
    print('test starts')
    TestWebLink = 'http://tstest-XXXXX.cn-north-1.elb.amazonaws.com.cn:90/test.html'
    response = requests.get(TestWebLink)
    print(type(response.status_code))
    
    if response.status_code == 200:
        rStatus = 'Succeeded'
    else:
        rStatus = 'Failed'
    
    print('test fini')    
    print('test is', rStatus)
    
    
    response = client.put_lifecycle_event_hook_execution_status(
        deploymentId = event['DeploymentId'],
        lifecycleEventHookExecutionId = event['LifecycleEventHookExecutionId'],
        #status='Succeeded'|'Failed'
        status = rStatus
    )

