import json

def createUrl(event):
    # TODO implement
    input = json.loads(event)
    
    approvalUrl=input['albUrl'] + "/execution?action=approve&ex=" + input['executionName'] + "&sm=" + input['statemachineName'] + "&taskToken=" + input['taskToken'];
    rejectUrl=input['albUrl'] + "/execution?action=reject&ex=" + input['executionName'] + "&sm=" + input['statemachineName'] + "&taskToken=" + input['taskToken'];
    
    urls = {
            "approve": approvalUrl,
            "reject": rejectUrl
           }
    
    #print(urls)
    
    return json.dumps(urls)
