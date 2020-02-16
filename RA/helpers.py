import requests

def patchList():
    URL = 'https://ddragon.leagueoflegends.com/api/versions.json'
    response = eval(str(requests.get(URL).json()))
    removeList = []
    for x in range(0, len(response)):
        if 'lolpatch' in str(response[x]):
            removeList.append(response[x])

    for x in range(0, len(removeList)):
            response.remove(removeList[x])

    return response

def grabHistory(patchList):
    print(patchList[0])

    for x in range(0, len(patchList)):
        try:
            print(requests.get('http://ddragon.leagueoflegends.com/cdn/' + patchList[x] + '/data/en_US/champion/Aatrox.json').json())
        except:
            print('Didn\'t exist in patch ' + patchList[x])

    return()