import discord
import requests as r
import os

from dotenv import load_dotenv

bot = discord.Client()
load_dotenv()
DISCORD_TOKEN = os.environ.get('DISCORD_TOKEN')

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")

		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	isChar = True
	isShip = True
	isPlanet = True
	isBook = True
	isSpecies = True
	try:
		if message.content.startswith("!"):
			data = r.get(f'http://127.0.0.1:5000/api/character/{message.content[1::]}')
			if data.status_code == 200:
				data = data.json()
		
			name = data[0]['name']
			alias = data[0]['alias']
			affiliation = data[0]['affiliation']
			species = data[0]['species_name']
			await message.channel.send(f'{name} aka {alias}. They are a member of the {species} and works for the {affiliation}')
	except:
		isChar = False

	if isChar == False:
		try:
			if message.content.startswith("!"):
				data = r.get(f'http://127.0.0.1:5000/api/ship/{message.content[1::]}')
				if data.status_code == 200:
					data = data.json()
				
				shipname = data[0]['shipname']
				shiptype = data[0]['shiptype']
				armament = data[0]['armament']
				status = data[0]['status']
				print("test")
				await message.channel.send(f'{shipname} is a {shiptype}. {shipname} has an armament of {armament}, and is is currently {status}')
		except:
			isShip = False
	if isShip == False:
		try:
			if message.content.startswith("!"):
				data = r.get(f'http://127.0.0.1:5000/api/planet/{message.content[1::]}')
				if data.status_code == 200:
					data = data.json()
				
				name = data[0]['name']
				nickname = data[0]['nickname']
				planetdata = data[0]['planetdata']

				await message.channel.send(f'Planet Name: {name}. Nickname: {nickname}. Known Planet Data: {planetdata}')
		except:
			isPlanet = False
	if isPlanet == False:
		try:
			if message.content.startswith("!"):
				data = r.get(f'http://127.0.0.1:5000/api/book/{message.content[1::]}')
				if data.status_code == 200:
					data = data.json()
				
				bookname = data[0]['bookname']
				authorsummary = data[0]['authorsummary']
				next = data[0]['next']
				previous = data[0]['previous']

				await message.channel.send(f'Bookname: {bookname}. authorsummary: {authorsummary}. {previous}. {next}. ')
		except:
			isBook = False
	if isBook == False:
		try:
			if message.content.startswith("!"):
				data = r.get(f'http://127.0.0.1:5000/api/Species/{message.content[1::]}')
				if data.status_code == 200:
					data = data.json()
				print('test')
				species_name = data[0]['species_name']
				appearence = data[0]['appearence']
				nickname = data[0]['nickname']
				clients = data[0]['client']
				patron = data[0]['patron']

				await message.channel.send(f'The {species_name}. Their nickname, if any, is {nickname}. Their appearence is {appearence}. Their patron are the {patron}, and their client(s), if any, are the {clients} ')
		except:
			isSpecies = False

	if isSpecies == True and isBook == True and isChar == True and isPlanet == True and isShip == True:
		print(f'Sorry, but the command you typed ({message}) is either misspelled, or not valid. Please try again')

bot.run(DISCORD_TOKEN)