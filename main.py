import discord
from discord.ext import commands
from random import randint

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

ROLE_ID = 1335605844955500647

count = {}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

async def brigada(message):

    mentioned_roles = message.role_mentions
    role_ids = [role.id for role in mentioned_roles]

    if ROLE_ID in role_ids:
        await message.add_reaction('💀')

        count[message.author.id] = count.get(message.author.id, 0) + 1

        messages = [
            f'{message.author.mention} ia-ti un job, ai dat ping de {count[message.author.id]} ori 💀',
            f'{message.author.mention} esti labubu',
            f'vote kick {message.author.mention} 1/5',
            f'unemployment final boss ^',
            f'mergi la somn {message.author.mention}',
            f'bruh {message.author.mention}',
            f'taci {message.author.mention} ca iara pierdem',
            f'treci la curs {message.author.mention}',
            f'fa ceva util {message.author.mention}',
            f'kys {message.author.mention}',
            f'iar ia AB vacanta',
            f'stai ca vrea AB shaorma',
            f'{message.author.mention} e gay',
            f'stai ca-i AB la baie',
            f'https://tenor.com/view/job-job-application-jobless-gif-2757097081210871087',
            f'https://tenor.com/view/give-me-money-no-money-no-money-meme-money-please-beggar-emoji-gif-7109609360249280076'
        ]

        await message.channel.send(
            messages[randint(0, len(messages) - 1)]
        )

async def ranking(message):

    if not bot.user.id in [member.id for member in message.mentions]:
        return
    
    if not count:
        await message.channel.send('n-a dat nimeni ping inca')
        return

    sorted_counts = sorted(count.items(), key=lambda item: item[1], reverse=True)
    ranking_message = 'Ping count:\n'
    for user_id, ping_count in sorted_counts:
        user = bot.get_user(user_id)
        ranking_message += f'{user.name}: {ping_count} pings\n'

    await message.channel.send(ranking_message)

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:  
        return

    await brigada(message)
    await ranking(message)

    await bot.process_commands(message)


with open('token', 'r') as f:
    token = f.read().strip()

# test

bot.run(token)
