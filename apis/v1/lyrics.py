# musixmatch_lyrics.py (inside your Django app)

import requests
from decouple import config
from ninja import Router

router = Router(tags=['Lyrics Router'])

# Define the MusixMatch API base URL and API key
MUSIXMATCH_BASE_URL = "https://api.musixmatch.com/ws/1.1"
MUSIXMATCH_API_KEY = config('MUSIXMATCH_API_KEY')

@router.get("/lyrics/{track_id}")
def get_lyrics(request, track_id: int):
    try:
        # Send a request to MusixMatch API to get lyrics by track ID
        response = requests.get(
            f"{MUSIXMATCH_BASE_URL}/track.lyrics.get",
            params={"track_id": track_id, "apikey": MUSIXMATCH_API_KEY},
        )

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()

            # Extract the lyrics from the MusixMatch API response
            lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]

            return {"lyrics": lyrics}
        else:
            return {"error": "Failed to retrieve lyrics"}

    except Exception as e:
        return {"error": str(e)}
    
   
@router.get('lyrics2/{trackName}/{artistName}') 
# Sample code to search for a track and fetch lyrics using MusixMatch API
def get_lyrics_by_track_name_and_artist(request, trackName, artistName):
    try:
        # Step 1: Search for the track
        response = requests.get(
            f"{MUSIXMATCH_BASE_URL}/matcher.track.get?apikey={MUSIXMATCH_API_KEY}&q_artist=eminem&q_track=lose%20yourself%20(soundtrack)"
        )
            # params={
            #     "q_track": trackName,
            #     "q_artist": artistName,
            #     "apikey": config('MUSIXMATCH_API_KEY'),
            # },
        # ) 

        if response.status_code == 200:
            data = response.json()
            print(data)
            
            # Step 2: Extract the track_id of the best matching track (you can choose based on your criteria)
            track_id = data["message"]["body"]["track_list"][0]["track"]["track_id"]
            print(track_id)
            
            # Step 3: Query lyrics by track_id
            response = requests.get(
                f"{MUSIXMATCH_BASE_URL}/track.lyrics.get",
                params={"track_id": track_id, "apikey": MUSIXMATCH_API_KEY},
            )

            if response.status_code == 200:
                lyrics_data = response.json()
                # print(lyrics_data)
                lyrics = lyrics_data["message"]["body"]["lyrics"]["lyrics_body"]
                return {"lyrics": lyrics}
            else:
                return {"error": "Failed to retrieve lyrics"}

        else:
            return {"error": "Failed to find the track"}

    except Exception as e:
        return {"error": str(e)}

