
import uuid
import json

def check_uuid(uuid_str):
    try:
        val = uuid.UUID(uuid_str, version=4)
    except ValueError:
        # If it's a value error, then the string 
        # is not a valid hex code for a UUID.
        return False
    
    return True