import requests
import json

fortify_ssc_api_url = "<Fortify URL>/api/v1/projectVersions"
token = "FortifyToken <token>"              #Use Unified token
headers = {
    "Authorization": token,
    "Content-Type": "application/json",
    "Accept": "application/json"
}


response = requests.get(fortify_ssc_api_url, headers=headers)

if response.status_code == 200:
    projects = response.json()['data']
    for project in projects:
        project_id = project['id']
        
        delete_url = f"{fortify_ssc_api_url}/{project_id}"
        delete_response = requests.delete(delete_url, headers=headers)

        if delete_response.status_code == 200:
            print(f"Project deleted! : {project_id}")
        else:
            print(f"Error occured while deleting..: {project_id}")
else:
    print("Error occured while listing projects")
