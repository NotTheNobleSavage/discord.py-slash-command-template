#Make sure is discord py 2.0 or higher
import discord

#file with token
import secret

#Define client (optional setup for intents)
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#Creates the command tree this is an container that holds all the commands
tree = discord.app_commands.CommandTree(client)

#Get out guild id
guild_id = discord.Object(id = 563586646423896080)


#Basic on ready client event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #This syncs the command tree with discord
    #This will only sync one guilds commands
    #If you want to sync all guilds you can use the following code:
    #await tree.sync()
    #Be aware that sync time can be long when syncing to many guilds compared to when syncing one guild
    await tree.sync(guild = guild_id)

#We use the command tree 
@tree.command(
    #This is where you specify what guild the command is for, again this can be removed if you want to sync all guilds
    guild = guild_id, 
    #Simple name must have no space or capital letters
    name = "ping", 
    #This is the description of the command go nuts
    description = "Simple Ping and Pong", 
)
async def slash(interaction: discord.Interaction):
    #The slash command is classed as an interaction this is what you will use to interact back with the user
    #interactions are an entire new ballpark and will require more learning to fully understand
    #You can only reply back to an interaction ONCE and a reply must be givin within 15sec or the user gets "The aaplication did not respond"

    #Sends an simple message back no fuss
    await interaction.response.send_message("Pong")

if __name__ == '__main__':
    client.run(secret.token)
