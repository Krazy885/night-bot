import disnake
from disnake.ext import commands
import asyncio
import datetime


class Modal1(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot

        #детали окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Длительность",
                placeholder="К примеру: 10min/1h/3d",
                custom_id="длительность",
                max_length=10,
                ),
            disnake.ui.TextInput(
                label="Число призовых мест",
                placeholder="1; 2; 15; 46",
                custom_id="числомест",
                ),
            disnake.ui.TextInput(
                label="Приз",
                placeholder="1 место - Нитро на месяц\n2 место - Нитро на год\n3 место - шаурма (в сырном лаваше)",
                custom_id="приз",
                #style=TextInputStyle.paragraph,
                ),
            disnake.ui.TextInput(
                label="Описание розыгрыша",
                placeholder="Команда сервера разыгрывает призы в честь нового года!",
                custom_id="описание",
                #style=TextInputStyle.paragraph,
                ),
            ]
    

        super().__init__(
            title="Новый розыгрыш",
            custom_id="Новый розыгрыш",
            components=components,
            )    

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        channel = inter.channel
        amount = 0
        #cool_time = disnake.utils.format_dt(, style='R')
        embed = disnake.Embed(title="Розыгрыш", description = f"{inter.text_values['описание']}\n**Заканчивается**: \n**Участников: {amount}**\nПризовых мест: {inter.text_values['числомест']}\n**Призы: **\n{inter.text_values['приз']}", colour = 0x4F78E8)
        await channel.send(embed=embed)
        await channel.send(view = Button_for_compet(self.bot))
        await inter.response.send_message('Розыгрыш успешно запущен!', ephemeral = True)


class Button_for_compet(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.blurple, emoji='🎉')
    async def competitive(self, button: disnake.ui.Button, inter: disnake.Interaction):
    	amount += 1
    	await inter.response.edit_message(embed)




class compet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.slash_command(name='gcreate', description='Создать розыгрыш!') #здесь модальное окно отправляется все супер
    async def gcreate(self, inter: disnake.ApplicationCommandInteraction):
    	await inter.response.send_modal(Modal1(self.bot))


#розыгрыш работает так: пишется команда, выдается модальное окно с настройками, потом отправляется embed в канале и кнопка чтобы присоединиться. Когда кто то нажимает он прибавляет amount +1 и изменяет embed чтобы там число участников менялось и отправляет сообщение что вы успешно присоединились к розыгрышу
#потом там есть настройка времени, нужно чтобы оно после истечения это времени в embed появлялось еще одно окно(победитель и там рандомно выбирался победитель), соответственнно embed после выбора победителя тоже изменяется и добавляет эту строку, а кнопка пропадать
#добавить команду /greroll выбирать нового победителя(пусть просто отправляется новый embed  сновым победителем моментально)

def setup(bot):
    bot.add_cog(compet(bot))