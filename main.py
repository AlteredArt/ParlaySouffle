import pandas as pd
import requests
pd.set_option('display.max_columns', None)
import time
import numpy as np

test_url = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=PerGame&Scope=S&Season=2024-25&SeasonType=Pre%20Season&StatCategory=PTS'

r = requests.get(url=test_url).json()
table_headers = r['resultSet']['headers']
# pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)

<<<<<<< HEAD

# print(r)
print(table_headers)
# temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)
=======
print(r)
temp_df1 = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)

is this the same as juypter
>>>>>>> de8a169b928bf0bb8e2dd883d19b877184a0ea87
