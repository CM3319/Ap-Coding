from helperfunctions import get_season_totals_by_position, plot_position_stat_bar, get_player_stats, export_player_season_png, plot_player_stat_by_week


stat = get_player_stats(2024, "Aaron","Rodgers")
# print(stat)


# plot_player_stat_by_week(2024, "Aaron", "Rodgers", stat_col = 'passing_yards', save_path="Aaron_Rodgers_passing_yards_2011")

stats = export_player_season_png(2024, "Aaron", "Rodgers", png_path="aaron_Rdogers_passing_yards_2024")