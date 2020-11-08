import discord
import discord.ext.commands
import discord.utils

# Creates a connection to discord.
client = discord.Client()

among_us_hosts = []

# Handle bot init
@client.event
async def on_ready():
    await client.wait_until_ready()
    print('We have logged in as {0.user}'.format(client))

# Handle bot text commands
@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content == 'aul':
        among_us_hosts.append(message.author)
        await message.channel.send('You are now a leader in your among us session!')
    if message.content == 'naul':
        among_us_hosts.remove(message.author)
        await message.channel.send('You are no longer a leader in your among us session!')
    if message.content.startswith('Diz olá ao Kebab'):
        await message.channel.send('Olá Kebab!')

    if message.content.startswith('$muteall') and message.author.voice and message.author.voice.channel:
        channel = message.author.voice.channel
        for member in channel.members:
            await member.edit(mute=True)

    if message.content.startswith('$unmuteall') and message.author.voice and message.author.voice.channel:
        channel = message.author.voice.channel
        for member in channel.members:
            await member.edit(mute=False)

# Among us mute utility
@client.event
async def on_voice_state_update(member, before, after):
    if among_us_hosts.__contains__(member):
        if not before.self_mute and after.self_mute:
            for memberino in member.voice.channel.members:
                if memberino != member:
                    await memberino.edit(mute=True)
        else:
            if before.self_mute and not after.self_mute:
                for memberino in member.voice.channel.members:
                    if memberino != member:
                        await memberino.edit(mute=False)

# ADD REACTION ROLE
@client.event
async def on_raw_reaction_add(payload):
    guild_id = 312101041380524032
    message_id = 661371005993746512
    await add_reaction_roles(payload, guild_id, message_id)


async def add_reaction_roles(payload, guild_id, message_id):
    await client.wait_until_ready()

    if payload.message_id == message_id:
        guild = client.get_guild(guild_id)

        # Role ---- S.W.A.T.
        test_role_id = 690929095894237254
        test_role_emoji = '🦅'
        await check_emoji_addition(payload, guild, test_role_id, test_role_emoji)

        # Role ---- Industrial Revolutionairs
        industrial_role_id = 723298667603427420
        industrial_role_emoji = '⚙️'
        await check_emoji_addition(payload, guild, industrial_role_id, industrial_role_emoji)

        # Role ---- Tyrian
        tyrian_role_id = 728766403414589461
        tyrian_role_emoji = '🛡️'
        await check_emoji_addition(payload, guild, tyrian_role_id, tyrian_role_emoji)

        # Role ---- Summoner
        summoner_role_id = 661363780227170304
        summoner_role_emoji = '🧂'
        await check_emoji_addition(payload, guild, summoner_role_id, summoner_role_emoji)

        # Role ---- Hunter
        hunter_role_id = 661365423622848518
        hunter_role_emoji = '🐉'
        await check_emoji_addition(payload, guild, hunter_role_id, hunter_role_emoji)

        # Role ---- Freeloaders
        freeloader_role_id = 747138837230125087
        freeloader_role_emoji = '🤑'
        await check_emoji_addition(payload, guild, freeloader_role_id, freeloader_role_emoji)

        # Role ---- Tieflings
        tiefling_role_id = 748883424000999475
        tiefling_role_emoji = '🧝'
        await check_emoji_addition(payload, guild, tiefling_role_id, tiefling_role_emoji)


async def check_emoji_addition(payload, guild, role_id, emoji_unicode):
    if payload.emoji.name == emoji_unicode:
        role = discord.utils.get(guild.roles, id=role_id)
        member = payload.member
        print('Member "', member, '" has reacted to the welcome message with the emote "', emoji_unicode,
              '", and as such has been given the role of "', role, '".')
        await member.add_roles(role)


# REMOVE REACTION ROLE
@client.event
async def on_raw_reaction_remove(payload):
    message_id = 661371005993746512
    await remove_reaction_roles(payload, message_id)


async def remove_reaction_roles(payload, message_id):
    print('Reaction removal to message with ID ', payload.message_id, ' and emoji ', payload.emoji.name, ' detected!')
    await client.wait_until_ready()

    if payload.message_id == message_id:
        guild = await client.fetch_guild(payload.guild_id)
        member = await guild.fetch_member(payload.user_id)
        # Payload.user id returns the user's ID as an int.
        print("User ID: " + str(payload.user_id))
        # member = guild.get_member(payload.user_id)

        # Role ---- S.W.A.T.
        swat_role_id = 690929095894237254
        swat_role_emoji = '🦅'
        await check_emoji_removal(payload, guild, swat_role_id, member, swat_role_emoji)

        # Role ---- Industrial Revolutionairs
        industrial_role_id = 723298667603427420
        industrial_role_emoji = '⚙️'
        await check_emoji_removal(payload, guild, industrial_role_id, member, industrial_role_emoji)

        # Role ---- Tyrian
        tyrian_role_id = 728766403414589461
        tyrian_role_emoji = '🛡️'
        await check_emoji_removal(payload, guild, tyrian_role_id, member, tyrian_role_emoji)

        # Role ---- Summoner
        summoner_role_id = 661363780227170304
        summoner_role_emoji = '🧂'
        await check_emoji_removal(payload, guild, summoner_role_id, member, summoner_role_emoji)

        # Role ---- Hunter
        hunter_role_id = 661365423622848518
        hunter_role_emoji = '🐉'
        await check_emoji_removal(payload, guild, hunter_role_id, member, hunter_role_emoji)

        # Role ---- Freeloaders
        freeloader_role_id = 747138837230125087
        freeloader_role_emoji = '🤑'
        await check_emoji_removal(payload, guild, freeloader_role_id, member, freeloader_role_emoji)

        # Role ---- Tieflings
        tiefling_role_id = 748883424000999475
        tiefling_role_emoji = '🧝'
        await check_emoji_removal(payload, guild, tiefling_role_id, member, tiefling_role_emoji)


async def check_emoji_removal(payload, guild, role_id, member, emoji_unicode):
    if payload.emoji.name == emoji_unicode:
        role = discord.utils.get(guild.roles, id=role_id)
        print('Member "', member, '" has removed the reaction from the welcome message with the emote "', emoji_unicode,
              '", and as such has been removed from the role of "', role, '".')
        await member.remove_roles(role)


f = open("serverID.txt", "r")
client.run(f.read())
