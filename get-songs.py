import pymongo
from pymongo import MongoClient

import urllib, json

#for inserting lyrics
client = MongoClient('mongodb://localhost:27017/')
db = client['lyrical-nlp']
lyrics_collection = db['songs-lyrics']


#for getting lyrics from musixMatch
apikey_musixmatch = '44b2e9853ebcd623a3e3854be77f42fa'
apiurl_musixmatch = 'http://api.musixmatch.com/ws/1.1/'


#Query components
artist_search = 'artist.search?'
artist_param = 'q_artist='
page_param = '&page_size=5'
auth_param = "&apikey=" + apikey_musixmatch + "&format=plain"

#     lyricData = { "artist": artistName, "album": a.name, "track": track.name, "lyrics": lyrics }
#     lyrics_id = lyrics_collection.insert_one(lyricData).inserted_id
#     print(lyrics_id)


def findArtistID(artist_name):
    q_artist = artist_name.strip()
    q_artist = q_artist.replace("%20", " ")
    query_string = apiurl_musixmatch + artist_search + q_artist + page_param + auth_param
    print(query_string)
    response = urllib.urlopen(query_string)
    data = json.loads(response.read())
    body = data["message"]["body"]["artist_list"]
    num_artists = len(body)
    if num_artists==0:
                return(("No results for: " + artist_name))
    for result in body:
        print(result)
        if result['artist_id'] > 0:
            return result['artist_id']


def test(artist_list):
    for artist in artist_list:
        artistID = findArtistID(artist)
        print((artist + ' : ' + artistID))

def main():
    artist_file = open("artists.txt", "r")
    artist_list = artist_file.readlines()
    #Test with first 5 artists
    test(artist_list[:5])


if __name__ == '__main__':
    main()
