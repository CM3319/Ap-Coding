from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_advanced_team_records, get_player_stats_by_name, plot_player_stat
import matplotlib.pyplot as plt

'4. which division had the strongest defense based on yards allowed per game in 2024'

#teamstats = get_advanced_team_records(2024)
#print(teamstats)

# this is a factual question because it asks  
# cannot be answered due to the limit of code

teamstats =  get_season_Results_By_team(2024, 'PHI')
# print(teamstats)

'5. which wr had the most targets vs receptions in 2024'
wrstats = get_player_stats_by_name(2024, 'J.Chase', 'WR')
#print(wrstats)

# this is a focused question, because its direct
# and asking one thing
# i used the helper function above because 
# it gives all of the wr stats and i entered 
# the top 5 wide receivers because they would 
# they're top 5 in all stats-+

# jamarr had the most targets and receptions in 2024


'3. does time of possesion strongly correlate with wins in 2024'
# this question cannot be answered because of how the code doesnt 
# give feedback on time of possession
adv= get_advanced_team_records(2024)
print(adv)

# this question is a clarity question because 
# its easy to understand becuase its asking, time of possession 
# we know what that isa and how does it connect 
# with wins, i used the helper function above 
# because it gives out all the stats in each game