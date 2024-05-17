import logging
import loading
import simulation

from aiogram import Bot, Dispatcher, executor, types
from team import Team

# log level
logging.basicConfig(level=logging.INFO)

# bot initialization
TOKEN = "A12345678" # That's obviously a wrong token
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# start
@dp.message_handler(commands=["start"], commands_prefix='/')
async def start(message: types.Message):
	with open("start_message.txt", 'r') as file:
		await message.answer(file.read())

# help
@dp.message_handler(commands=["help"], commands_prefix='/')
async def start(message: types.Message):
	with open("help_message.txt", 'r') as file:
		await message.answer(file.read())

@dp.message_handler()
async def simulate(message: types.Message):
	text = message.text
	if text.count(" : ") != 1:
		await message.answer("Wrong Format.")
		return

	a_name, b_name = text.split(" : ")
	for team_name in a_name, b_name:
		if not teams['team_name'].eq(team_name).any():
			await message.answer(f'I don\'t know the team "{team_name}."')
			return

	a, b = Team(teams[teams['team_name'] == a_name].iloc[0]), Team(teams[teams['team_name'] == b_name].iloc[0])
	score = simulation.simulate(a, b)

	await message.answer(a_name + " " + " : ".join(map(str, score)) + " " + b_name)

# main
teams = loading.upload_teams("male_teams.csv")
executor.start_polling(dp, skip_updates=True)
