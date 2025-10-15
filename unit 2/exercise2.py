from helperfunctions import get_team_records, get_season_Results_By_team

schedules = get_team_records(2025)
print(schedules)


top6_Teams = ['TB, IND, LA, BUF, SF, SEA']


team_1 =get_season_Results_By_team(2025,'TB')
team_2 =get_season_Results_By_team(2025,'IND')
team_3 =get_season_Results_By_team(2025,'LA')
team_4 =get_season_Results_By_team(2025,'BUF')
team_5 =get_season_Results_By_team(2025,'SF')
team_6 =get_season_Results_By_team(2025,'SEA')

#print(team_1)
print(team_2)
#print(team_3)
#print(team_4)
#print(team_5)
#print(team_6)


# the beest overall is IND
# the worst is .

