import spotipy
import webbrowser
import datetime
import requests
import base64
from datetime import datetime
import time
import configparser
import os
import requests
import sys 
from pytesseract import pytesseract
import pandas as pd
import re
import subprocess
import win32gui
from win32con import SW_SHOW, SW_RESTORE
import win32com.client
import win32con
import pyautogui
from thefuzz import fuzz
import random

spotify_auth_path = r"C:\Users\sbuca\Documents\pierre\music_files"
sys.path.insert(0, spotify_auth_path)

from spotify_auth import re_authenticate, setup_spotify #Works well at least for re_auth

config = configparser.ConfigParser()

def get_config_file():
    current_file_path = os.getcwd()
    config_file_path = current_file_path + "\\music_files\\spotify_config.ini"
    
    return config_file_path


def check_expiration():
    
    config_file_path = get_config_file()
    config.read(config_file_path)
    
    token_expiration = config["TOKENS"]["expires_at"]
    
    if float(token_expiration) < float(time.mktime(datetime.now().timetuple())):
        re_authenticate(config_file_path)
        
        
def create_spotify_connection():
    #Must fix, must be ran twice to reauthenticate
    config_file_path = get_config_file()
    
    if os.path.exists(config_file_path):
        config.read(config_file_path)
        
        #Update tokens if outdated
        check_expiration()
        
        #Connect to spotify
        spotifyObject = spotipy.Spotify(auth=config["TOKENS"]["access_token"])
        
        return spotifyObject
        
    
    else:
        setup_spotify()
        create_spotify_connection()
        

        
### WINDOW MANAGEMENT ###        
def get_open_apps():
    apps = {}
    
    def winEnumHandler( hwnd, ctx,):
        if win32gui.IsWindowVisible( hwnd ):
            #int(hex(hwnd)) converts hex back to int
            apps[win32gui.GetWindowText( hwnd )] = hex(hwnd)

    win32gui.EnumWindows( winEnumHandler, None )
    
    return apps


def get_memory_location(app_name):
    apps = get_open_apps()
    app_name = app_name.lower()

    for app in apps:
        if app_name in app.lower():
            return apps[app]
        
        
def manage_window_placement(application_name, use_hex=False):
    """Given application name function brings 
        it to front of screen and maximizes.
        Works if application was minimized or in the back"""
    #Must check to see premium name
    
    #Get spotify window ID
    if use_hex is False:
        window_id = win32gui.FindWindow(None, application_name) #Change name to apply to any program
        
    else:
        config.read(config_file_path)
        hex_id = config["APPLICATION"]["memory_address"]

        window_id = int(hex_id, 16)

    if window_id:
        if win32gui.GetWindowPlacement(window_id)[1] == 2:
            win32gui.ShowWindow(window_id, SW_RESTORE)
            
        else:
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')

            win32gui.SetForegroundWindow(window_id)
            
        #win32gui.SetActiveWindow(window_id) #will set monitor 1 or 2 as the main
        
        win32gui.ShowWindow(window_id, win32con.SW_MAXIMIZE)
        
        return 1
        
    else:
        return -1
        
        
def open_spotify():
    """Opens spotify based on user preference (web or app)"""
    
    config_file_path = get_config_file()
    #Checks what type of spotify to open, webbrowser or application
    config.read(config_file_path)
    spotify_preference = config["SETUP"]["preference"]
    
    spotify_version = "Spotify Free" #Used for later
    
    #Handles application and webbrowser seperatley
    if spotify_preference == "application":

        subprocess.Popen(config["APPLICATION"]["path"], shell=True) #Open Spotify App, does nothing if alreayd open


        #Check if spotify is premium or free and bring it to front of screen and enlarge
        if manage_window_placement("Spotify Free") == -1:
            manage_window_placement("Spotify Premium")
            spotify_version = "Spotify Premium"

        while get_memory_location(spotify_version) is None:
            continue
        
        #Get memory address of application for future use (Check if app is still open and what not)
        print(get_memory_location(spotify_version))
        config["APPLICATION"]["memory_address"] = str(get_memory_location("Spotify Premium"))
        
        #Write new memory address to config file
        with open(config_file_path, 'w') as configfile:
            config.write(configfile)
            
            
def restart_device(client):
    devices = client.devices()['devices']
    
    #Check if we have an active device
    for device in devices:
        if device['is_active'] is True:
            return 1
        
    return devices[0]['id']


#Must add error handling (trying to play song when already playing)
def navbar_controller(action, client):
    if action in ["next", "skip"]:
        client.next_track()
        
    if action in ["back", "previous"]:
        client.previous_track()
        
    if action in ["pause", "stop"]:
        client.pause_playback()
        
    if action in ["resume"]:
        client.start_playback()
        
    if action == "shuffle":
        client.shuffle(True)

    if action == "replay":
        client.previous_track()
        client.next_track()



def get_command_type(command):
    pattern = re.compile(r"(.+) by (.+)")
    match = pattern.search(command)
    
    song_name = match.group(1)
    artist_name = match.group(2)
    
    return song_name, artist_name



def find_best_song(command, track_artist, client):
    tracks = client.search(q=command, type="track")
    
    track_popularity = dict()
    
    for track in tracks['tracks']['items']:
        
        #To get specific song like no flocking by kodak
        artist = track['artists'][0]['name'].lower()
        track_name = track['name'].lower()
        track_id = track['id']
        
        if track_artist == "":
            artist = ""
        
        track_fuzz = fuzz.ratio(command, track_name)
        
        #Temp solution will need to convert to similar structure like playlist one
        #may need to do for album as well
#         if track_fuzz < 50:
#             continue
        
        if track_fuzz < 70 or fuzz.ratio(track_artist, artist):
            if fuzz.partial_ratio(track_artist, artist) < 70:
                continue
            
        track_popularity[(track['popularity'] + track_fuzz)] = track_id
        
        
    return track_popularity[max(track_popularity)]



#Could add functioinality when you say next playlist and it will move to second choice
def playlist_ranker(likes_dict, fuzz_dict):
    likes_rank = sorted(likes_dict.values())[::-1]
    fuzz_rank = sorted(fuzz_dict.values())[::-1]
    
    id_ranks = dict()
    
    for id_ in likes_dict:
        likes = likes_dict[id_]
        l_rank = likes_rank.index(likes) + 1
        
        
        fuzz = fuzz_dict[id_]
        f_rank = fuzz_rank.index(fuzz) + 1
        
        id_ranks[id_] = l_rank + f_rank
        
    return min(id_ranks, key=id_ranks.get)


#may be able to merge with best song function but not sure after adding the ranking stuff
#This may need to be the standard for album and song searching
#the playlist search is the perfect example
def find_best_playlist(command, client, spotify_enabled=False, spotify_iter=0):
    playlists = client.search(q=command, type="playlist")
    
    playlist_likes = dict()
    playlist_fuzz = dict()

    #Loop through all playlist
    for playlist in playlists['playlists']['items']:
        
        playlist_name = playlist['name'].lower()
        playlist_id = playlist['id']
        playlist_creator = playlist['owner']['id'].lower()

        #Filter for non spotify playlists (They generally suck - too many features included)
        if playlist_creator == "spotify" and spotify_enabled is False:
            continue
            
        name_fuzz = fuzz.ratio(playlist_name, command)
        name_pfuzz = fuzz.partial_ratio(playlist_name, command)
        #maybe change to and so both have to be horrible matches
        #but the following code should provide only the best
        if name_fuzz <= 70 or name_pfuzz <= 70:
            continue
            
        #Given any playlist and creator, returns how many people follow it
        playlist_followers = client.user_playlist(user=playlist_creator, playlist_id=playlist_id)["followers"]["total"]
        
        playlist_likes[playlist_id] = playlist_followers
        playlist_fuzz[playlist_id] = name_fuzz
        #may add pfuzz as another rank to get more accurate
        
        
    if playlist_likes == {}:
        spotify_iter += 1
        if spotify_iter < 2:
            return find_best_playlist(command, client, True, spotify_iter)
        else:
            return "Not Found"
    
    
    else:
        best_id = playlist_ranker(playlist_likes, playlist_fuzz)
        return best_id
    


#Can probably merge this function with best songs since they have similar properties
def find_best_album(command, album_artist, client):
    #Need to fix this to make it better
    
    albums = client.search(q=command, type="album")
    
    album_score = dict()
    
    for album in albums['albums']['items']:
        
        album_name = album['name'].lower()
        album_id = album['id']
        artist = album['artists'][0]['name'].lower()
        
        if album_artist == "":
            artist = ""
            

        album_fuzz = fuzz.ratio(command, album_name)
        artist_fuzz = fuzz.ratio(album_artist, artist)
        artist_pfuzz = fuzz.partial_ratio(album_artist, artist)
        
        #Temp solution
        if fuzz.ratio(command, album_name) < 50:
            continue
        
        if fuzz.ratio(command, album_name) < 70 or fuzz.ratio(album_artist, artist) < 70:
            if fuzz.partial_ratio(album_artist, artist) < 70:
                continue

                
        #If we dont have a artist we go based off popularity (her loss album will return wrong album without popularity)
        if album_artist == "":
            popularity = client.album(album_id)['popularity']
            album_score[(album_fuzz+popularity)] = album_id
        
        #Dont need popularity because the artist name should elimainate all but one
        else:   
            popularity = client.album(album_id)['popularity']
            album_score[(artist_fuzz+popularity)] = album_id
                
    return album_score[max(album_score)]  


def find_user_playlist(client, target_playlist):
    #May need to convert numbers in playlists to the word version (4 -> four)
    
    playlists = dict()
    
    results = client.current_user_playlists()['items']
    for playlist in results:
        ratio = fuzz.ratio(target_playlist.lower(), playlist['name'].lower())
        
        if ratio >= 70:
            playlists[ratio] = playlist['id']
            
    if playlists == {}:
        return None
        
        
    return playlists[max(playlists)]


def get_liked_songs(client):
    song_ids = []
    
    #Wrap in while loop
    #while length spotify_client.current_user_saved_tracks == 50
    #Then keep doing it but increase offest paramter by 50 each time
    
    for song in client.current_user_saved_tracks(limit=50)['items']:
        song_id = song['track']['id']
        song_id = "spotify:track:" + song_id
        
        song_ids.append(song_id)
        
        
    random.shuffle(song_ids)
        
    return song_ids


def search_music(command, client):
    if "playlist" in command:
        #Captures only playlists
        command = command.replace(" playlist", "")
        
        id_ = find_user_playlist(client, command)
        
        if id_ is not None:
            return ("spotify:playlist:" + id_)
            
        return ("spotify:playlist:" + find_best_playlist(command, client))
    
    if "album" in command:
        #Captures albums
        command = command.replace(" album", "")
        
        if "by" in command:
            album, artist = get_command_type(command)
            
            return ("spotify:album:" + find_best_album(command, artist, client))
            
        else:
            return ("spotify:album:" + find_best_album(command, "", client))
            
        
        return
        
    if "by" in command:
        #Caputres"No Flockin by Kodak"
        track, artist = get_command_type(command)
        
        return ("spotify:track:" + find_best_song(track, artist, client))
        
    else:
        #captures No Flockin
        return ("spotify:track:" + find_best_song(command, "", client))
        


def play_controller(command, client):
    command = command.replace("play ", "")
    
    if "liked songs" in command or "favorite songs" in command or "favorites" in command:
        #For some reason when you add queueu or do multiple uris it doesnt show on queue on app
        #it shows on phone though
        #spotify_client.start_playback(uris=[liked_songs[0]])
#         for song in liked_songs:
#             client.add_to_queue(song)
        
        liked_songs = get_liked_songs(client)
        client.start_playback(uris=liked_songs)
        
        return
    
    else:
        uri = search_music(command, client)
        
        if "not found" in uri.lower():
            return "Not Found"
        
        if "track" in uri:
            client.start_playback(uris=[uri])
            
        else:
            client.start_playback(context_uri=uri)
            
            
def queue_controller(command, client):
    #must search for the id then add song to queue
    #EX "Add no flockin by kodak black to queue"
    
    command = re.sub(r'(add|to queue|to the queue|[^a-zA-Z\s])', '', command, flags=re.IGNORECASE) #removes add to queue words
    command = command.strip()
    
    uri = search_music(command, client)
    client.add_to_queue(uri=uri)


#Types of commands
# Navbar like commands (pause, resume, skip etc)
# Play songs/albums/playlist commands (play No Flocking by Kodak Black)
#Play liked songs
#Add song to queue
def spotify_controller(command):
    client = create_spotify_connection()
    client = create_spotify_connection()
    
    command = command.lower()
    
    if "play " in command: #Space at end of play so it doesnt play commands with playlist in them unles told to play that playlist
        #Send to play controller then search function
        play_controller(command, client)
        return
    
    if "queue" in command:
        #send to queue handler
        queue_controller(command, client)
        return
    
    for action in ["resume", "shuffle", "pause", "next", "back"]:
        if action in command:
            #send to navbar handler
            try:
                navbar_controller(action, client)
                return
                
            except spotipy.SpotifyException as e:
                return
    
    return
        
        
    #If no active devices we must manually restart device
    #To manually restart we can pass in device id to start playback or whatever and restart
#     open_spotify() #Temporary solution to bring spotify to front of screen
#     pyautogui.press('space')

if __name__ == "main":
    spotify_controller(command)