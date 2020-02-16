import json
import http.client
import requests
from RA import championList
from RA import calc
from RA import helpers


key = 'RGAPI-3d17a56d-f9d4-471d-a14d-a5c26b64369f'

print('Starting Up')

patchList = helpers.patchList()
# helpers.grabHistory(patchList)
calc.baseStats(patchList)

# list = championList.getList()
# champInfo = championList.allChampInfo(list)
# championList.classCount(list, champInfo)