import disnake
from disnake.ext import commands, tasks
import asyncio
import io
from PIL import Image, ImageDraw, ImageFont, ImageOps



class On_Ready(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Мы подключены и готовы')
        search_message.start(self.bot)
        status.start(self.bot)
        banner.start(self.bot)
        



@tasks.loop(seconds = 30) #код для обновления баннера
async def banner(bot):
    guild = bot.get_guild(1079792436727009280)
    members = guild.members
    voice_all_mambers = 0
    voice_channels = [member for member in members if member.voice and member.voice.channel]

    with Image.open('banner.png') as image:
        # Создание объекта ImageDraw для рисования на изображении
        draw = ImageDraw.Draw(image)

    font = ImageFont.truetype('ofont.ru_Montserrat.ttf', size = 120)
    draw.text((900, 530), f' {len(members)}', fill='white', font=font)
    
    
    bot.guild = bot.get_guild(id)
    for vc in guild.voice_channels:
        voice_all_mambers+=len(vc.members)
    print(voice_all_mambers)

    font = ImageFont.truetype('ofont.ru_Montserrat.ttf', size = 130)
    draw.text((1000, 350), f'{voice_all_mambers}', fill = 'white', font=font)

    image_bytes = io.BytesIO()
    image.save(image_bytes, format='PNG')
    image_bytes.seek(0)

    await guild.edit(banner=image_bytes.read())

@tasks.loop(seconds = 15) #код для статуса
async def status(bot):
    await bot.change_presence(status = disnake.Status.online, activity = disnake.Activity(name = f'Я лучше Бибы', type = disnake.ActivityType.competing)) #Кастомный статус
    await asyncio.sleep(15)
    members = 0
    for guild in bot.guilds:
        for member in guild.members:
            members += 1
    await bot.change_presence(status = disnake.Status.idle, activity = disnake.Activity(name = f'за {members} участниками', type = disnake.ActivityType.watching)) #Общее количество участников, за которыми следит бот (Находятся на серверах)
    await asyncio.sleep(15)        


@tasks.loop(minutes=1)
async def search_message(bot):
    channel = disnake.utils.get(bot.get_all_channels(), id=1079792437339357216)
    message = await channel.send('<@&1067855700014940200> Устал сидеть в одиночестве? Заходи к нам на сервер, проходи верификацию, и гуляй по комнатам в поиске общения!)')
    await asyncio.sleep(3600)
    await message.delete()


def setup(bot):
    bot.add_cog(On_Ready(bot))