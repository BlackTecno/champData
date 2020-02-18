import json
import http.client
import requests
import multiprocessing as par
from RA import championList
from RA import calc
from RA import helpers

key = 'RGAPI-3d17a56d-f9d4-471d-a14d-a5c26b64369f'

print('Starting Up')

patchList = helpers.patchList()
# helpers.grabHistory(patchList)

if __name__ == '__main__':
    p = par.Pool(8)
    p.map(calc.avgStats, patchList)

# list = championList.getList()
# champInfo = championList.allChampInfo(list)
# championList.classCount(list, champInfo)