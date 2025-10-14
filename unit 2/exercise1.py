import pandas as pd
import nfl_data_py as nfl


schedules = nfl.import_schedules([2024]) 

# print(schedules.collums.tolist())
 
records = get_team_records(2024)

print(records)

# print(records[('team, wins, loses'])
print(records['wins'].mean(2020))

