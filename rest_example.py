"""
purpose of this module is to read data from sample rest apis and store it into json files.
"""
import json
import requests

#Module level variables 
SERVER = "http://dummy.restapiexample.com"

def _fetch(uri):
    """
    #Private
    Opens a connection with rest server and sends response back in json formant.
    Params:
    uri = Part of url or resource name from which data needs to be extracted.
    """
    resp = None
    url = "{}/api/v1/{}".format(SERVER,uri)
    headers = {"content-type" : "application/json"}
    try:
        resp = requests.get(url, headers=headers)
        if resp.status_code != 200:
            print("Error while calling api {} : {}".format(url, resp.contents))
        resp = resp.json()
        assert "data" in resp
        
    except Exception as e:
        print(e)
        raise
    return resp

def collect_emp_data(resource):
    """
    Collects employee data and dump it into json file.
    """
    emp_data = _fetch(resource)['data']
    for emp in emp_data:
        filename = r"json_store\%s.json"%(emp['id'])
        with open(filename, 'w') as fp:
            json.dump(emp, fp)

collect_emp_data("employees")
    
