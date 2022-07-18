import discogs_client
import random

def generateRandomVinyl():
    """
    Gets a random vinyl from users collection
    returns: Dictionary containing the title of the record and artist
    """
    # establishes a connection to a user account
    d = discogs_client.Client("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                                user_token='ieWdLYtBuxnjaGZhFaOhyNUiyrnCaRMwdSQCCnCW')
    me = d.identity()
    randomVinyl = (random.randrange(len(me.collection_folders[0].releases))-1)
    vinylData = {}

    # gets all of the basic info for a random item in the collection
    basicInfo = me.collection_folders[0].releases[randomVinyl].data["basic_information"]
    vinylData['artist'] = basicInfo['artists'][0]['name']
    vinylData['title'] = basicInfo["title"]
    return vinylData

def getGenreSpecificVinyl(genre):
    """
    Gets a random vinyl from users collection that matches the genre they inputted
    returns: Dictionary containing the title of the record and artist or dictionary with error message
    """
    # establishes a connection to a user account
    d = discogs_client.Client("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                                user_token='ieWdLYtBuxnjaGZhFaOhyNUiyrnCaRMwdSQCCnCW')
    me = d.identity()
    # makes a list of integers that span the length of a users collection
    numList = []
    for num in range(len(me.collection_folders[0].releases)):
        numList.append(num)
    
    for i in range(len(me.collection_folders[0].releases)):
        vinylIndex = random.randrange(len(numList)-1)
        vinylInfo = me.collection_folders[0].releases[numList[vinylIndex]].data["basic_information"]

        # gets all of the basic info for a random item in the collection if the genre matches
        if genre in vinylInfo["genres"]:
            vinylData = []
            vinylData.append(vinylInfo['artists'][0]['name'])
            vinylData.append(vinylInfo["title"])
            return vinylData
        # if the genre doesn't match, remove the entry and try again.
        else:
            numList.remove(numList[vinylIndex])
        print("Iteration "  + str(i))

    # if none are found return a filler list
    return ["Couldn't find a match."]



