import json

def generic_json(data, message=None):
    return {"status": data.status,
        "status_code": data.status_code,
        "mimetype": data.mimetype,
        "data": data.json,
        "message": message}