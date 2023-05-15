import json
import spotipy
import webbrowser
import datetime
import requests
import base64
from datetime import datetime
import time
import configparser
import os

config = configparser.ConfigParser()

### FOR RETRIEVING FIRST TOKEN ###
def setup_config_file(token_package, credentials):
    """Create config file to store authentication data for api"""
    current_file_path = os.getcwd()
    config_file_path = current_file_path + "\\music_files\\spotify_config.ini" #Re add music_file
    
    config["TOKENS"] = {
        "access_token": token_package['access_token'],
        "refresh_token": token_package['refresh_token'],
        "expires_at": token_package['expires_at'],
    }
    
    config["CREDENTIALS"] = {
        "username": credentials["username"],
        "client_id": credentials["client_id"],
        "client_secret": credentials["client_secret"],
        "redirect_uri": credentials["redirect_uri"],
        "scope": credentials["scope"],
    }
    
    #Writes all of config default to file
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)
        
    return 1
    
    

def setup_auth(credentials):
    """For first time use of api when no refresh token is present"""
    # Create OAuth Object
    oauth_object = spotipy.SpotifyOAuth(username=credentials["username"],
                                        client_id=credentials["client_id"],
                                        client_secret=credentials["client_secret"],
                                        redirect_uri=credentials["redirect_uri"],
                                        scope=credentials["scope"])

    # Create token
    token_dict = oauth_object.get_access_token()
    
    return token_dict

    

def setup_spotify():
    """Creates token for spotify API, will redirect to google and must copy link.
        Only have to copy link on inital setup"""
    
    #API Credentials (From spotify developer webpage)
    credentials = {
        "username": 'sbucarion',
        "client_id": "7cf09e11b901468b8fa62e287678f4c9",
        "client_secret": "0ae14b2bad384527acb6df30a963c163",
        "redirect_uri": 'http://google.com/',
        "scope": "user-library-read user-modify-playback-state playlist-read-collaborative playlist-read-private user-read-playback-state",
    }
    
    auth_tokens = setup_auth(credentials)
    print(auth_tokens)
    setup_status = setup_config_file(auth_tokens, credentials)
    
    

### FOR RETRIEVING NEW TOKENS ###
def encode_client_data(client_id, client_secret):
    """Generates base64 encoded string for generating new refresh token"""
    
    message = client_id + ":" + client_secret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    return base64_message



def get_spotify_refresh_token(config_file_path):
    """Returns  refresh token and unix expiration time"""

    #Retrieve necessary parameters
    config.read(config_file_path)
    
    client_id = config["CREDENTIALS"]["client_id"]
    client_secret = config["CREDENTIALS"]["client_secret"]
    refresh_token = config["TOKENS"]["refresh_token"]

    encoded_client = encode_client_data(client_id, client_secret)
    
    data={"grant_type": "refresh_token", "refresh_token": refresh_token}
    headers={"Authorization": "Basic " + encoded_client}
    
    response = requests.post("https://accounts.spotify.com/api/token",data=data, headers=headers)

    response_json = response.json()
    
    #Find when token will expire
    current_time = datetime.now()
    unix_current_time = time.mktime(current_time.timetuple())
    
    expiration_unix = unix_current_time + response_json['expires_in']
    
    return response_json["access_token"], expiration_unix


def update_config_file(access_token, expiration_time, config_file_path):
    config["TOKENS"]["access_token"] = access_token
    config["TOKENS"]["expires_at"] = str(expiration_time)
    
    with open(config_file_path, 'w') as config_file:
        config.write(config_file)


def re_authenticate(config_file_path):
    access_token, expiration = get_spotify_refresh_token(config_file_path)
    update_config_file(access_token, expiration, config_file_path)
    
    
if __name__ == "main":
    setup_spotify()
    re_authenticate()