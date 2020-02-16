import requests
import array
import json

########################
def getList(patch):
    URL = 'http://ddragon.leagueoflegends.com/cdn/' + patch + '/data/en_US/champion.json'
    response = requests.get(URL)
    parsed = response.json()
    parsed = parsed["data"]
    champList = []

    for x in parsed:
        champList.append(parsed[x]["id"])

    return champList


######################
def allChampInfo(list, patch):
    URL = 'http://ddragon.leagueoflegends.com/cdn/' + patch + '/data/en_US/champion/'
    champInfo = []

    for x in range(0, 2):
        champInfo.append(requests.get(URL + str(list[x]) + ".json").json()["data"])
        print('On champion ' + str(x+1) + ' of 148')

    with open('champInfo.txt', 'w') as f:
        for item in champInfo:
            f.write("%s\n" % item)
    f.close()

    return champInfo

########################
def classCount(list, champInfo):
    print(champInfo)


    for x in range(0, len(champInfo)):
        print(champInfo[x][str(list[x])]['id'])
        print(champInfo[x][str(list[x])]['stats'])
        # print(champInfo[x][str(list[x])]['tags'])

