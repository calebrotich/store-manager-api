import json

def convert_response_to_json(response):
    """Converts the response to a json type"""
    
    json_response = json.loads(response.data.decode('utf-8'))
    return json_response