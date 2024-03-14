

import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""
if __name__ =="__main__":
    print(extract_session_id("projects/ariel-pepb/agent/sessions/59320a28-3336-77b4-d1f6-e027c54bf52b/contexts/ongoing-order"))