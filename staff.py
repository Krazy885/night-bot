import disnake
from disnake.ext import commands
from disnake.interactions.modal import ModalInteraction



class Stuff_Modal(disnake.ui.Modal):
    def __init__(self, arg):
        self.arg = arg
        
        if self.arg == 'Moderator':
            components = [
                disnake.ui.TextInput(label='как тебя зовут, сколько лет?', placeholder='Пример: Дима 17 лет', custom_id='name'),
                disnake.ui.TextInput(label='стояли ли вы на подобной должности?', placeholder='Если да, то расскажите почему', max_length=1000, custom_id='exp'),
                disnake.ui.TextInput(label='сколько времени готовы уделять должности?', placeholder='Пример: 3 часа в день', custom_id='time'),
                disnake.ui.TextInput(label='Расскажите о себе подробнее', placeholder='Какие ваши сильные и слабые стороны?', max_length=1000, custom_id='more'),
                disnake.ui.TextInput(label='почему вы выбрали именно эту должность?', placeholder='', custom_id='why'),
            ]
        elif self.arg == 'Support':
            components = [
                disnake.ui.TextInput(label='как тебя зовут, сколько лет?', placeholder='Пример: Дима 17 лет', custom_id='name'),
                disnake.ui.TextInput(label='ваше время работы и часовой пояс?', placeholder='Утро, ночь, МСК', custom_id='time_zone'),
                disnake.ui.TextInput(label='были ли у тебя муты/варны на сервере', placeholder='Пример: Да, был мут, 13.03.2023 по причине 1.3', max_length=1000, custom_id='warns'),
                disnake.ui.TextInput(label='был ли у тебя подобный опыт работы', placeholder='Да, был. Работал саппортом на сервере...', max_length=1000, custom_id='exp'),
                disnake.ui.TextInput(label='почему мы должны взять именно тебя?', placeholder='Расскажи о себе, свои плохие и хорошие качества', max_length=1000, custom_id='why'),
            ]
        elif self.arg == 'EventMode':
            components = [
                disnake.ui.TextInput(label='укажите имя, возраст и часовой пояс', placeholder='Пример: Дима 17 лет, МСК+1', custom_id='name'),
                disnake.ui.TextInput(label='расскажите немного о себе', placeholder='Укажите плохие и хорошие качества',max_length=1000, custom_id='more'),
                disnake.ui.TextInput(label='какие ивенты умеенте проводить?', placeholder='Пример: JackBox, Мафия, Бункер', custom_id='events'),
                disnake.ui.TextInput(label='работали на каком-либо другом сервере?', placeholder='Если да, то на каком? И почему ушли?', max_length=1000, custom_id='exp'),
                disnake.ui.TextInput(label='почему хотите встать на eventmode', placeholder='', custom_id='why'),
            ]
        elif self.arg == 'TribuneMode':
            components = [
                disnake.ui.TextInput(label='укажите имя, возраст и часовой пояс', placeholder='Пример: Дима 17 лет, МСК+1', custom_id='name'),
                disnake.ui.TextInput(label='расскажите немного о себе', placeholder='Укажите плохие и хорошие качества',max_length=1000, custom_id='more'),
                disnake.ui.TextInput(label='какие трибуны умеенте проводить?', placeholder='Пример: быстрые свидания, Шоу подкатов', custom_id='events'),
                disnake.ui.TextInput(label='работали на каком-либо другом сервере?', placeholder='Если да, то на каком? И почему ушли?', max_length=1000, custom_id='exp'),
                disnake.ui.TextInput(label='почему хотите встать на TribuneMode', placeholder='', custom_id='why'),
            ]
        elif self.arg == 'CloseMode':
            components = [
                disnake.ui.TextInput(label='укажите имя, возраст и часовой пояс', placeholder='Пример: Дима 17 лет, МСК+1', custom_id='name'),
                disnake.ui.TextInput(label='расскажите немного о себе', placeholder='Укажите плохие и хорошие качества',max_length=1000, custom_id='more'),
                disnake.ui.TextInput(label='какие клозы умеенте проводить?', placeholder='Пример: Dota 2, CS:GO, Valorant', custom_id='events'),
                disnake.ui.TextInput(label='работали на каком-либо другом сервере?', placeholder='Если да, то на каком? И почему ушли?', max_length=1000, custom_id='exp'),
                disnake.ui.TextInput(label='почему хотите встать на CloseMode', placeholder='', custom_id='why'),
            ]

        title = f'Набор на должность {self.arg}'

        super().__init__(title=title, components=components, custom_id='stuff_modal_req')

    
    async def callback(self, interaction: disnake.ModalInteraction):
        await interaction.response.send_message(f'Спасибо, что оставили заявку на должность {self.arg}. Мы обязательно рассмотрим вашу заявку и в скором времени вам ответим!', ephemeral=True)
        channel = interaction.guild.get_channel(1102980423333707917)
        if self.arg == 'Moderator':
            values = {
                'имя, возраст': interaction.text_values['name'],
                'опыт': interaction.text_values['exp'],
                'сколько времени готовы уделять': interaction.text_values['time'],
                'о себе': interaction.text_values['more'],
                'почему именно тебя': interaction.text_values['why'],
            }
            embed = disnake.Embed(description=f'заявка от {interaction.author.mention}')
            for key, value in values.items():
                embed.add_field(name=key, value=value)
        elif self.arg == 'Support':
            values = {
                'имя, возраст': interaction.text_values['name'],
                'время работы, час.пояс': interaction.text_values['time_zone'],
                'были ли наказания': interaction.text_values['warns'],
                'был ли опыт': interaction.text_values['exp'],
                'почему именно тебя': interaction.text_values['why'],
            }
            embed = disnake.Embed(description=f'заявка от {interaction.author.mention}')
            for key, value in values.items():
                embed.add_field(name=key, value=value)
        elif self.arg == 'EventMode':
            values = {
                'имя, возраст и час.пояс': interaction.text_values['name'],
                'о себе': interaction.text_values['more'],
                'что умеете проводить': interaction.text_values['events'],
                'опыт': interaction.text_values['exp'],
                'почему на эту должность': interaction.text_values['why'],
            }
            embed = disnake.Embed(description=f'заявка от {interaction.author.mention}')
            for key, value in values.items():
                embed.add_field(name=key, value=value)
        elif self.arg == 'TribuneMode':
            values = {
                'имя, возраст и час.пояс': interaction.text_values['name'],
                'о себе': interaction.text_values['more'],
                'что умеете проводить': interaction.text_values['events'],
                'опыт': interaction.text_values['exp'],
                'почему на эту должность': interaction.text_values['why'],
            }
            embed = disnake.Embed(description=f'заявка от {interaction.author.mention}')
            for key, value in values.items():
                embed.add_field(name=key, value=value)
        elif self.arg == 'CloseMode':
            values = {
                'имя, возраст и час.пояс': interaction.text_values['name'],
                'о себе': interaction.text_values['more'],
                'что умеете проводить': interaction.text_values['events'],
                'опыт': interaction.text_values['exp'],
                'почему на эту должность': interaction.text_values['why'],
            }
            embed = disnake.Embed(description=f'заявка от {interaction.author.mention}')
            for key, value in values.items():
                embed.add_field(name=key, value=value)
        await channel.send(embed=embed)



class Button_for_Stuff(disnake.ui.View):
    def __init__(self, arg):
        self.arg = arg
        super().__init__(timeout=None)


    @disnake.ui.button(label='Подать заявку', style=disnake.ButtonStyle.green)
    async def apply(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        await interaction.response.send_modal(Stuff_Modal(self.arg))
        await interaction.delete_original_message()




class Stuff_Select(disnake.ui.Select):
    def __init__(self, bot):
        self.bot = bot
        options = [
            disnake.SelectOption(label='Набор на должность Moderator', description='Стоим на страже порядка сервара!', value='Moderator'),
            disnake.SelectOption(label='Набор на должность Support', description='Проводим верификацию и экскурсию новичков!', value='Support'),
            disnake.SelectOption(label='Набор на должность EventMode', description='Проводим интерактивные мероприятия на сервере', value='EventMode'),
            disnake.SelectOption(label='Набор на должность TribuneMode', description='Проводим глобальные мероприятия на сервере!', value='TribuneMode'),
            disnake.SelectOption(label='Набор на должность CloseMode', description='Организуем 5 на 5 паблики', value='CloseMode'),
        ]
        super().__init__(
            placeholder='Подать заявочку на стафф', options=options, max_values=1, custom_id='stuff_selector'
        )



    async def callback(self, interaction: disnake.MessageInteraction):
        channel_stuff = disnake.utils.get(self.bot.get_all_channels(), id=1102966373614895156)
        message_stuff = await channel_stuff.fetch_message(1103032119955046501)
        view = disnake.ui.View()
        view.add_item(Stuff_Select(self.bot))
        await message_stuff.edit(view=view)
        if not interaction.values:
            await interaction.response.defer()
        else:
            if interaction.values[0] == 'Moderator':
                embed = disnake.Embed(
                    title='Набор на должность Moderator'
                )
                await interaction.response.send_message(embed=embed, view=Button_for_Stuff(interaction.values[0]), ephemeral=True)
            elif interaction.values[0] == 'Support':
                embed = disnake.Embed(
                    title='Набор на должность Support'
                )
                await interaction.response.send_message(embed=embed, view=Button_for_Stuff(interaction.values[0]), ephemeral=True)
            elif interaction.values[0] == 'EventMode':
                embed = disnake.Embed(
                    title='Набор на должность EventMode'
                )
                await interaction.response.send_message(embed=embed, view=Button_for_Stuff(interaction.values[0]), ephemeral=True)
            elif interaction.values[0] == 'TribuneMode':
                embed = disnake.Embed(
                    title='Набор на должность TribuneMode'
                )
                await interaction.response.send_message(embed=embed, view=Button_for_Stuff(interaction.values[0]), ephemeral=True)
            elif interaction.values[0] == 'CloseMode':
                embed = disnake.Embed(
                    title='Набор на должность CloseMode'
                )
                await interaction.response.send_message(embed=embed, view=Button_for_Stuff(interaction.values[0]), ephemeral=True)



class About_Stuff(commands.Cog):
    def __init__(self, bot):
        self.status = False
        self.bot = bot


    @commands.command()
    async def call_message(self, ctx):
        embed = disnake.Embed(
            title = 'Набор в Night STAFF',
            description = '\n```Что будет вас ждать?```',
            color = 0x383837,
        )
        image = disnake.Embed()
        image.set_image(file=disnake.File('cogs/file.png'))
        embed.add_field(name='\u200b', value='\u200b', inline=False)
        embed.add_field(name='\u200b', value='\u200b', inline=True)
        embed.add_field(name='',value='• Большой и дружный коллектив\n• Еженедельная зарплата в виде серверной валюты', inline=True)
        channel = ctx.guild.get_channel(1102966373614895156)
        await channel.send(embed=image)
        message_stuff = await channel.send(embed=embed)
        view = disnake.ui.View()
        view.add_item(Stuff_Select(self.bot))
        await message_stuff.edit(view=view)
        

    
    @commands.Cog.listener()
    async def on_connect(self):
        if self.status:
            return
        
        view = disnake.ui.View(timeout=None)
        view.add_item(Stuff_Select(self.bot))
        self.bot.add_view(view, message_id=1103032119955046501)



def setup(bot):
    bot.add_cog(About_Stuff(bot))



#59 строка - канал, куда отправляется форма подавшего
#150 строка - канал, где будет лежать сообщение с выбором крч стаф вот это ты понял
#151 строка - сообщение с выбором(делать после инструкции)
#204 строка - канал, где будет лежать сообщение с выбором крч стаф вот это ты понял
#220 строка - сообщение с выбором(делать после инструкции)


'''
инструкция: 
(делать только после замены id)
1) удали с 213 по 220 строку
2) вызови в нужном канале функцию, удали своё сообщение(что бы не мешалось)
3) скопируй id нижнего embed(которое с выбором)
4) верни код с 213 по 220 строку (1 пункт), в 151 и 220 строку добавь нужный id(из прошлого пункта)
'''