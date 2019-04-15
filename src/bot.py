import discord
import asyncio

TOKEN = 'NTMwODU3MzU2MjEzNDg1NTgw.D2eqWA.WzsciPbeQFgexvqfafWFx9csWA8'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user.name)
        print('User ID: ',self.user.id)
        print('-----------------)

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}, please make sure to read the PM to learn about how our server works or read #read-this!'.format(member, guild)
            await guild.system_channel.send(to_send)

        role = discord.utils.get(guild.roles, name="Hackers")
        await member.send('Welcome to the BeachHacks 2019 Server!\n\nPlease read the #rules channel for our server rules.\n\n#announcements will be the text-chat where our organizers will post BeachHacks related announcements about food, parking, etc.')
        await member.add_roles(role)
        print(member, 'has joined the battle.')


client = MyClient()
client.run(TOKEN)

