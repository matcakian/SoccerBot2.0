import numpy as np
from team import Team

''' Represents the model used to simulate a sigle chance during a soccer match '''
def __f(x: int, y: int, mu: float = 0, sigma: float = 1) -> bool:
	return np.random.normal(mu, sigma) < (x - y)

''' Simulates the result of a soccer match between two teams '''
def simulate(a: Team, b: Team, avg_chances: int = 10, mu_1: float = 0.0, 
	sigma_1: float = 8.0, mu_2: float = 12.5, sigma_2: float = 12.5) -> tuple:
	if not isinstance(a, Team) or not isinstance(b, Team):
		raise TypeError
	if not isinstance(avg_chances, int) or not all(isinstance(x, float) or 
		isinstance(x, int) for x in (mu_1, sigma_1, mu_2, sigma_2)):
		raise TypeError
	if not (avg_chances >= 0):
		raise ValueError

	a_attack, a_midfield, a_defence = a.get_attributes()
	b_attack, b_midfield, b_defence = b.get_attributes()
	a_goals, b_goals = 0, 0

	chances = np.random.poisson(avg_chances)

	for i in range(chances):
		if __f(a_midfield, b_midfield, mu_1, sigma_1):
			a_goals += int(__f(a_attack, b_defence, mu_2, sigma_2))
		else:
			b_goals += int(__f(b_attack, a_defence, mu_2, sigma_2))

	return (a_goals, b_goals)