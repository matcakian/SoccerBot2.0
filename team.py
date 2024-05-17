import pandas

''' A class representing a soccer team '''
class Team:
	def __init__(self, name: str, attributes: tuple = (0, 0, 0)):
		if not isinstance(name, str):
			raise TypeError
		if not ('__iter__' in dir(attributes)) or not all(isinstance(x, int) for x in attributes):
			raise TypeError
		if not (len(attributes) == 3) or not all(0 <= x < 100 for x in attributes):
			raise ValueError

		self.__name = name
		self.__attributes = tuple(attributes)

	def __init__(self, info: pandas.core.series.Series, 
		col_names: list = ['team_name', 'attack', 'midfield', 'defence']):
		if not isinstance(info, pandas.core.series.Series) or not isinstance(col_names, list):
			raise TypeError

		if len(col_names) != 4 or not all(isinstance(col, str) for col in col_names):
			raise ValueError

		self.__name = info[col_names[0]]
		self.__attributes = info[col_names[1:4]]

	def get_attributes(self):
		return self.__attributes

	def __str__(self):
		return self.__name + ": " + ", ".join(map(str, self.__attributes))