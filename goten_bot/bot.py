#Runs all code here; and uses discord import to go to Discord 
#Responses import for responses

import discord
import responses #Not resolved? But responses work

async def send_message(message, user_message, is_private): # async and await incase multi messages
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e: #catch-all feature to inform us of error
        print(e)


def run_discord_bot():
    TOKEN = 'INSERT-TOKEN-HERE' #Token so bot knows what server to go to 
    intents = discord.Intents.default() #boilerplate
    intents.message_content = True # required to read message from user
    client = discord.Client(intents=intents)

    @client.event 
    async def on_ready():
        print(f'{client.user} is now running!')

        # client.run(TOKEN)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return         #prevents an infinite loop
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':      #If user gives message indicating they want a private response
            user_message = user_message [1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)