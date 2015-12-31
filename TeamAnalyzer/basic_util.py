import json
import urllib2
#API KEY API KEY API KEY API KEY
KEY_END = "api_key=<API KEY>"
BASE_URL = "https://na.api.pvp.net/api/lol/na/"
STATIC_URL = "https://na.api.pvp.net/api/lol/static-data/na/v1.2/"

def getChampions():
  resp = json.loads(urllib2.urlopen(STATIC_URL + 'champion?dataById=true&' + 
      KEY_END).read())
  return resp['data']

def getSummonerId(name):
  resp = json.loads(urllib2.urlopen(BASE_URL + 'v1.4/summoner/by-name/' +
      name + '?' + KEY_END).read())
  return resp[name.lower()]['id']

def getTeams(summonerId):
  resp = json.loads(urllib2.urlopen(BASE_URL + 'v2.4/team/by-summoner/' +
      summonerId + '?' + KEY_END).read())
  return resp[summonerId]

def getMatchIds(summonerId):
  additionalParams = 'rankedQueues=RANKED_TEAM_5x5&seasons=SEASON2015' \
      '&beginTime=0&endTime=9999999999999&'
  resp = json.loads(urllib2.urlopen(BASE_URL + 'v2.2/matchlist/by-summoner/' +
      summonerId + '?' + additionalParams + KEY_END).read())
  matchIdList = []
  matchReferences = resp['matches']
  for matchReference in matchReferences:
    matchIdList.append(matchReference['matchId'])
  return matchIdList

def getMatch(matchId):
  return json.loads(urllib2.urlopen(BASE_URL + 'v2.2/match/' +
      str(matchId) + '?' + KEY_END).read())