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
	try:
		if message.content.startswith("!"):
			print("I'm Here!")
			print(message.content[1::])
			data = r.get(f'http://127.0.0.1:5000/api/character/{message.content[1::]}')
			print(data.status_code)
			if data.status_code == 200:
				data = data.json()
			
			name = data[0]['name']
			alias = data[0]['alias']
			affiliation = data[0]['affiliation']
			species = data[0]['species_name']
			print("test")
			await message.channel.send(f'{name} aka {alias}. They are a member of the {species} and works for the {affiliation}')
	except:
		print(f"Unfortunately, {message.content} doesn't exist")

bot.run(DISCORD_TOKEN)