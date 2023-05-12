import disnake
from disnake.ext import commands
import asyncio




class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistents_views_added = False



    @commands.command(name='tickets')
    async def tickets(self, inter: disnake.ApplicationCommandInteraction):
        embed1 = disnake.Embed(title ='Панель обращений', description = 'Нажмите на кнопку ниже, чтобы решить вашу проблему!\n\nКак только ваше обращение будет создано, пожалуйста максимально подробно опишите проблему и желательно прикрепляйте скриншоты.\n\nЕсли вы выиграли в розыгрыше, нажмите "Розыгрыши"\nЕсли вы хотите написать жалобу на участника или модератора, нажмите "Жалоба"\nЕсли вашей проблемы нет в списке или у вас другой вопрос то, нажмите "Помощь"\n\nПомните, что модераторы могут быть заняты другими проблемами. Пожалуйста сохраняйте терпение и ждите пока вам помогут!', color=0x4e77eb)
        await inter.send(embed = embed1, view = Button_for_tickets(self.bot))


    @commands.command()
    async def join(self, inter):
        connected = inter.author.voice
        if not connected:
            await inter.response.send_message("Тебе нужно находится в голосовом канале!", ephemeral = True)
            return
        global vc
        vc = await connected.connect()
       # (channel.id)
        #await channel.connect()




    @commands.slash_command(name='claim', description='Взять обращение в работу')
    async def claim(self, inter: disnake.ApplicationCommandInteraction):
        author = inter.author
        channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        channel = inter.channel
        role = inter.guild.get_role(1079792436865400880)
        author = inter.user
        await channel.set_permissions(role, read_messages=False, send_messages=False, view_channel=False)
        await channel.set_permissions(author, read_messages=True, send_messages=True, view_channel=True)
        embed1 = disnake.Embed(title = f'Обращение взято в работу', description = f'Модератор: {author.mention} работает над обращением!', color=0x4e77eb)
        await channel1.send(embed=embed1)


    @commands.slash_command(name='close', description='Закрыть обращение')
    async def close(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message('Вы уверены, что хотите закрыть обращение?', view = Button_for_close(self.bot), ephemeral = True)


    @commands.Cog.listener()
    async def on_connect(self):
        if self.persistents_views_added:
            return
        

        self.bot.add_view(Button_for_tickets(self.bot), message_id=1106309230887182416)


class Button_for_close(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)


    @disnake.ui.button(label='Да', style=disnake.ButtonStyle.success, emoji='✅')
    async def Da(self, button: disnake.ui.Button, inter: disnake.Interaction):
        author = inter.author
        channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        await inter.response.send_message('Обращение было закрыто!\nЧерез 5 секунд канал сам удалится!', ephemeral=True)
        await asyncio.sleep(5)
        await inter.channel.delete()
        embed1 = disnake.Embed(title = f'Обращение закрыто', description = f'Модератор: {author.mention} закрыл обращение', color=0x4e77eb)
        await channel1.send(embed=embed1)




    @disnake.ui.button(label='Нет', style=disnake.ButtonStyle.danger, emoji='❌')
    async def Net(self, button: disnake.ui.Button, inter: disnake.Interaction):
        await inter.response.send_message('Вы отказались от закрытия, в любое время используйте команду еще раз!', ephemeral=True)




class Button_for_tickets(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)


    @disnake.ui.button(label='Розыгрыш', style=disnake.ButtonStyle.blurple, emoji='🎉', custom_id ='розыгрыш')
    async def rozigrish(self, button: disnake.ui.Button, inter: disnake.Interaction):
        category = disnake.utils.get(self.bot.get_all_channels(), id=1079792439105159319)
        role1 = inter.guild.get_role(1079792436865400880)
        overwrites = {
        inter.guild.default_role: disnake.PermissionOverwrite(read_messages=False),
        #inter.guild.role(role): disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
        inter.guild.me: disnake.PermissionOverwrite(read_messages=True),               #<-- настройка прав доступа к текстовому каналу
        inter.user: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True)
        }
        channel = await inter.guild.create_text_channel(f'{inter.user.name} - обращение', overwrites=overwrites, category=category)   #создаём текст.канал(тикет)
        await channel.set_permissions(role1, read_messages=True, send_messages=True, view_channel=True)
        embed = disnake.Embed(title='Обращение создано', description='Вы создали тикет чтобы получить свой приз из розыгрыша!\n\nПожалуйста предоставьте скриншоты доказательства того что вы выиграли в розыгрыше.\nЕсли призов было несколько, пожалуйста укажите какой именно приз вы хотите получить.\n\n\nНе забудьте открыть личные сообщения чтобы модератор мог прислать вам ваш приз.', color=0x4e77eb)
        embed.set_footer(text='Получение приза может занять до недели')
        await channel.send(embed=embed)
        await inter.response.send_message(f"Ваще обращение успешно создано, перейдите в канал: {channel.mention} и опишите свой вопрос!", ephemeral=True)


    @disnake.ui.button(label='Жалоба', style=disnake.ButtonStyle.danger, emoji ='👮‍♂️', custom_id ='жалоба')
    async def zaloba(self, button: disnake.ui.Button, inter: disnake.Interaction):
        category = disnake.utils.get(self.bot.get_all_channels(), id=1079792439105159319)
        role1 = inter.guild.get_role(1079792436865400880)
        overwrites = {
        inter.guild.default_role: disnake.PermissionOverwrite(view_channel=False),
        #inter.guild.role1: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
        inter.guild.me: disnake.PermissionOverwrite(read_messages=True),               #<-- настройка прав доступа к текстовому каналу
        inter.user: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True)
        }
        channel = await inter.guild.create_text_channel(f'{inter.user.name} - обращение', overwrites=overwrites, category=category)   #создаём текст.канал(тикет)
        await channel.set_permissions(role1, read_messages=True, send_messages=True, view_channel=True)
        embed = disnake.Embed(title='Обращение создано', description='Вы создали тикет чтобы пожаловаться на участника/модератора\n\nПожалуйста укажите имя нарушителя, нарушение, и предоставьте доказательства нарушения (скриншоты или ссылки на сообщения)\n\nЕсли вы хотите написать жалобу на модератора то заполните эту форму:\nИмя модератора:\nРоль/позиция модератора:\nЧто делал модератор:\nТакже прикрепите доказательства нарушений\n\nПосле этого администратор рассмотрит вашу жалобу и постарается решить проблему!', color=0x4e77eb)
        embed.set_footer(text='Ложные жалобы приведут к наказанию!!')
        await channel.send(embed=embed)
        await inter.response.send_message(f"Ваще обращение успешно создано, перейдите в канал: {channel.mention} и опишите свой вопрос!", ephemeral=True)


    @disnake.ui.button(label='Помощь', style=disnake.ButtonStyle.success, emoji='🤔', custom_id='помощь')
    async def pomosh(self, button: disnake.ui.Button, inter: disnake.Interaction):
        category = disnake.utils.get(self.bot.get_all_channels(), id=1079792439105159319)
        role1 = inter.guild.get_role(1079792436865400880)
        overwrites = {
        inter.guild.default_role: disnake.PermissionOverwrite(read_messages=False),
     #   inter.guild.role: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
        inter.guild.me: disnake.PermissionOverwrite(read_messages=True),               #<-- настройка прав доступа к текстовому каналу
        inter.user: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True)
        }
        channel = await inter.guild.create_text_channel(f'{inter.user.name} - обращение', overwrites=overwrites, category=category)   #создаём текст.канал(тикет)
        await channel.set_permissions(role1, read_messages=True, send_messages=True, view_channel=True)
        embed = disnake.Embed(title='Обращение создано', description='Вы создали тикет чтобы получить помощь\nПожалуйста опишите проблему чтобы мы могли вам помочь!', color=0x4e77eb)
        embed.set_footer(text='Команда поддержки Night')
        await channel.send(embed=embed)
        await inter.response.send_message(f"Ваще обращение успешно создано, перейдите в канал: {channel.mention} и опишите свой вопрос!", ephemeral=True)



def setup(bot):
    bot.add_cog(ticket(bot))