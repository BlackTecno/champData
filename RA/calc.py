import requests
import csv
from RA import championList
def baseStats(patchList):
    w = csv.writer(open("statData.csv", "w"))
    for x in range(0, len(patchList)):
        patch = str(patchList[x])
        champList = championList.getList(patch)
        # 20 total stats
        allStats = {
                'hp':                   0,
                'hpperlevel':           0,
                'mp':                   0,
                'mpperlevel':           0,
                'movespeed':            0,
                'armor':                0,
                'armorperlevel':        0,
                'spellblock':           0,
                'spellblockperlevel':   0,
                'attackrange':          0,
                'hpregen':              0,
                'hpregenperlevel':      0,
                'mpregen':              0,
                'mpregenperlevel':      0,
                'crit':                 0,
                'critperlevel':         0,
                'attackdamage':         0,
                'attackdamageperlevel': 0,
                'attackspeedperlevel':  0,
                'attackspeed':          0
            }

        for x in range(0, len(champList)):
            champ = str(champList[x])
            URL = 'http://ddragon.leagueoflegends.com/cdn/' + patch + '/data/en_US/champion/' + champ + '.json'
            stats = requests.get(URL).json()['data'][champ]['stats']
            allStats['hp'] += stats['hp']
            allStats['hpperlevel'] += stats['hpperlevel']
            allStats['mp'] += stats['mp']
            allStats['mpperlevel'] += stats['mpperlevel']
            allStats['movespeed'] += stats['movespeed']
            allStats['armor'] += stats['armor']
            allStats['armorperlevel'] += stats['armorperlevel']
            allStats['spellblock'] += stats['spellblock']
            allStats['spellblockperlevel'] += stats['spellblockperlevel']
            allStats['attackrange'] += stats['attackrange']
            allStats['hpregen'] += stats['hpregen']
            allStats['hpregenperlevel'] += stats['hpregenperlevel']
            allStats['mpregen'] += stats['mpregen']
            allStats['mpregenperlevel'] += stats['mpregenperlevel']
            allStats['crit'] += stats['crit']
            allStats['critperlevel'] += stats['critperlevel']
            allStats['attackdamage'] += stats['attackdamage']
            allStats['attackdamageperlevel'] += stats['attackdamageperlevel']
            allStats['attackspeedperlevel'] += stats['attackspeedperlevel']
            allStats['attackspeed'] += stats['attackspeed']
            print('Patch ' + patch + ', adding stats for ' + champ + ', champion ' + str(x+1) + ' of ' + str(len(champList)))

        totalChamps = len(champList)

        allStats['hp'] /= totalChamps
        allStats['hpperlevel'] /= totalChamps
        allStats['mp'] /= totalChamps
        allStats['mpperlevel'] /= totalChamps
        allStats['movespeed'] /= totalChamps
        allStats['armor'] /= totalChamps
        allStats['armorperlevel'] /= totalChamps
        allStats['spellblock'] /= totalChamps
        allStats['spellblockperlevel'] /= totalChamps
        allStats['attackrange'] /= totalChamps
        allStats['hpregen'] /= totalChamps
        allStats['hpregenperlevel'] /= totalChamps
        allStats['mpregen'] /= totalChamps
        allStats['mpregenperlevel'] /= totalChamps
        allStats['crit'] /= totalChamps
        allStats['critperlevel'] /= totalChamps
        allStats['attackdamage'] /= totalChamps
        allStats['attackdamageperlevel'] /= totalChamps
        allStats['attackspeedperlevel'] /= totalChamps
        allStats['attackspeed'] /= totalChamps

        print(patch + ' ' + str(allStats))

        for key, val in allStats.items():
            w.writerow([patch, key, val])





