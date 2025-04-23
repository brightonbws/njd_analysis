import polars as pl


teams_df = pl.read_csv('teams.csv')
# print(teams_df.columns)
skaters_df = pl.read_csv('skaters.csv')
# print(skaters_df.columns)

filtered_teams = teams_df.select(['team', 'season', 'name', 'position',
                                  'situation', 'xGoalsPercentage'])

njd_team = filtered_teams.filter(pl.col("team") == 'NJD')
print(njd_team)

filtered_skaters = skaters_df.select(['playerId', 'season', 'name', 'team',
                                      'position', 'situation', 'onIce_xGoalsPercentage'])

njd_players = filtered_skaters.filter(pl.col("team") == 'NJD')
print(njd_players.filter(pl.col("name") == 'Jack Hughes'))
