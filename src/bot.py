import discord
import asyncio

TOKEN = 'NTMwODU3MzU2MjEzNDg1NTgw.D2eqWA.WzsciPbeQFgexvqfafWFx9csWA8'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user.name)
        print('User ID: ',self.user.id)
        print('-----------------')

    async def on_member_join(self, member):
        guild = member.guild
        #if guild.system_channel is not None:
            #to_send = 'Welcome {0.mention} to {1.name}, please make sure to read the PM to learn about how our server works or read #read-this!'.format(member, guild)
            #await guild.system_channel.send(to_send)

        role = discord.utils.get(guild.roles, name="Hackers")
        welcome_msg = ''
        welcome_msg += 'Welcome to the BeachHacks 2019 Discord server!\n'
        welcome_msg += 'To enhance your BeachHacks experience, this server is meant to be a central hub for event information, announcements during the event, a chance to get to know your fellow hackers, as well as a place where you and your team can ask any questions or request a mentor. We recommend you keep notifications on during the event so you don\'t miss anything!\n'
        welcome_msg += 'Please look over the #read-this channel as well as read our #rules for the server rules and guidelines. So we can recognize who you are, please change your name in the server to your real name.'
        await member.send(welcome_msg)
        await member.add_roles(role)
        print(member, 'has joined the battle.')


client = MyClient()
client.run(TOKEN)