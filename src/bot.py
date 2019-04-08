import discord
import asyncio

TOKEN = 'NTMwODU3MzU2MjEzNDg1NTgw.D2eqWA.WzsciPbeQFgexvqfafWFx9csWA8'

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as', self.user.name)
        print('User ID:', self.user.id)
        print('------')

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}, please make sure to respond to the DM with your unique code to gain access to the server!'.format(member, guild)
            await guild.system_channel.send(to_send)

        codes = open('codes.txt').read().splitlines()

        role = discord.utils.get(guild.roles, name="Hacker")

        await member.send('Welcome! Please reply with the unique code given to you to gain access to the server.')

        try:
            guess = await self.wait_for('message')
        except asyncio.TimeoutError:
            return await member.send('Sorry, you took too long.')

        if guess.content in codes:
            await member.add_roles(role)
            await member.send('CORRECT! \nWelcome to the BeachHacks 2019 Official Server! \nPlease make sure to read the rules!')
            print(member, 'has joined the battle.')
            outfile = open('codes.txt','w')
            for line in codes:
                if line != guess.content:
                    outfile.write(line+'\n')
            outfile.close()
        else:
            await member.send('Sorry wrong.')

client = MyClient()
client.run(TOKEN)

