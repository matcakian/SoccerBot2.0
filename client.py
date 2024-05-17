from team import Team
from loading import upload_teams
from simulation import simulate

teams = upload_teams("male_teams.csv")

a_name = input("Enter the first team: ")
b_name = input("Enter the second team: ")

if not teams['team_name'].eq(a_name).any() or not teams['team_name'].eq(b_name).any():
	raise ValueError

a, b = Team(teams[teams['team_name'] == a_name].iloc[0]), Team(teams[teams['team_name'] == b_name].iloc[0])

num_games = int(input("Enter the number of games: "))
print("Game", a_name, b_name, sep='\t')
for i in range(num_games):
	a_goals, b_goals = simulate(a, b)
	print(i, a_goals, b_goals, sep='\t')