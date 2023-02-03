import discord
import responses

async def send_message(message, user_message, is_private, author, permission):
    try:
        response = responses.handle_response(user_message, author, permission)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "" #here comes the bot's token from the Discord Developer page
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is ready! SASAGEYO!')
        
        await client.change_presence(activity = discord.Activity(type=discord.ActivityType.listening, name="Indecisive Foes.."))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '>':
            user_message = user_message[1:]
            if "#" not in user_message:
                await send_message(message, user_message, is_private=True, author=username, permission="YES")
            else:
                messages_split = user_message.split()
                username2 = messages_split[1]
                user_message2 = ' '.join([messages_split[0], *messages_split[2:]])
                await send_message(message, user_message2, is_private=True, author=username2, permission="NO")
        else:
            if "#" not in user_message:
                await send_message(message, user_message, is_private=False, author=username, permission="YES")
            else:
                messages_split = user_message.split()
                username2 = messages_split[1]
                user_message2 = ' '.join([messages_split[0], *messages_split[2:]])
                await send_message(message, user_message2, is_private=False, author=username2, permission="NO")

    client.run(TOKEN)
