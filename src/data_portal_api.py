
import requests
import pandas as pd


def get_portal_data(endpoint, offset=None):
    
    df = pd.DataFrame()

    if offset:
        for offset in range(0, 60000, 1000):
            portal_url = endpoint + f"?$limit=1000&$offset={offset}"
            response = requests.get(portal_url)
            offset_df = pd.DataFrame(response.json())
            df = pd.concat([df,offset_df])

    else: 
        response = requests.get(endpoint)
        df = pd.DataFrame(response.json())
        
    return df