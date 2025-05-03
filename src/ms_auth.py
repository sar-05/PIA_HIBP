from msal import PublicClientApplication
import webbrowser

def ms_graph_token(app_id, authority_url, az_scopes):
    #Creating client object
    client_obj = PublicClientApplication(
        app_id,
        authority=authority_url
    )
    #Geting access token through device flow authentication
    flow = client_obj.initiate_device_flow(scopes=az_scopes)
    print(flow['user_code'])
    webbrowser.open(flow['verification_uri'])
    access_token_dict = client_obj.acquire_token_by_device_flow(flow)
    return access_token_dict["access_token"]
