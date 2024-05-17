import pandas

''' Creates and returns a dataframe containing the information about soccer teams from a .csv file '''
def upload_teams(filename: str, col_names: list = 
	['team_name', 'attack', 'midfield', 'defence']) -> pandas.core.frame.DataFrame:
	if not isinstance(filename, str):
		raise TypeError
	if not isinstance(col_names, list) or not all(isinstance(col, str) for col in col_names):
		raise TypeError
	if (len(col_names) != 4):
		raise ValueError

	return pandas.read_csv(filename)[col_names]

