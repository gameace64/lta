import basic_util

def main():
  print "Running REST calls to Riot Games API."
  championDict = basic_util.getChampions()
  summonerName = raw_input('Summoner Name: ').lower()
  summonerId = str(basic_util.getSummonerId(summonerName))
  teams = basic_util.getTeams(summonerId)
  for number, team in enumerate(teams):
    print '\t' + str(number) + ") " + team['name']
  desiredTeam = input('Select a team: ')
  selectedTeam = teams[desiredTeam]
  for member in selectedTeam['roster']['memberList']:
    print member
  matchIds = basic_util.getMatchIds(summonerId)
  matches = {}
  #Add this whenever we actually want lots of data
  #for matchId in matchIds:
  #  matches[matchId] = getMatch(matchId)
  matches[matchIds[0]] = basic_util.getMatch(matchIds[0])
  print matches[matchIds[0]]

if __name__ == "__main__":
  main()