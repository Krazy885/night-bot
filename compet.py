import disnake
from disnake.ext import commands, tasks
import asyncio
import datetime
import random



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
        time = inter.text_values['длительность']
        if time[-1] == 'd':
            time_untill = time[0:len(time) - 2]
            time_t = datetime.datetime.now() + datetime.timedelta(days=int(time_untill))
        elif time[-1] == 'h':
            time_untill = time[0:len(time) - 2]
            time_t = datetime.datetime.now() + datetime.timedelta(hours=int(time_untill))
        elif time[-1] == 'n':
            time_untill = time[0:len(time) - 4]
            time_t = datetime.datetime.now() + datetime.timedelta(minutes=int(time_untill))
        cool_time = disnake.utils.format_dt(time_t, style='R')
        embed = disnake.Embed(title="Розыгрыш", description = f"{inter.text_values['описание']}\n**Заканчивается**: {cool_time}\n**Участников: 0**\nПризовых мест: {inter.text_values['числомест']}\n**Призы: **\n{inter.text_values['приз']}", colour = 0x4F78E8)
        message = await channel.send(embed=embed, view = Button_for_compet(self.bot, inter.text_values['описание'], inter.text_values['числомест'], inter.text_values['приз'], cool_time))
        await inter.response.send_message('Розыгрыш успешно запущен!', ephemeral = True)
        await wait_finish.start(inter.text_values['длительность'], datetime.datetime.now(), message)


class Button_for_compet(disnake.ui.View):
    def __init__(self, bot, desc, priz_mest, priz, cool_time, amount = 0):
        global memebr_list
        self.bot = bot
        self.desc = desc
        self.priz_mest = priz_mest
        self.priz = priz
        self.cool_time = cool_time
        self.amount = amount 
        memebr_list = list()
        super().__init__(timeout=None)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.blurple, emoji='🎉')
    async def competitive(self, button: disnake.ui.Button, inter: disnake.Interaction):
        if inter.author not in memebr_list:
            self.amount += 1
            memebr_list.append(inter.author)
            embed = disnake.Embed(title="Розыгрыш", description = f"{self.desc}\n**Заканчивается**: {self.cool_time}\n**Участников: {self.amount}**\nПризовых мест: {self.priz_mest}\n**Призы: **\n{self.priz}", colour = 0x4F78E8)
            message = inter.message
            await message.edit(embed=embed)
            await inter.response.send_message('Теперь вы участвуете в розыгрыше!', ephemeral = True)
        else:
            await inter.response.send_message('Вы уже участвуете в розыгрыше!', ephemeral = True)


@disnake.ext.tasks.loop(seconds = 5)
async def wait_finish(time, now, message):
    if time[-1] == 'd':
        time_untill = time[0:len(time) - 2]
        if datetime.datetime.now() - now >= datetime.timedelta(days=int(time_untill)):
            r = random.randint(0, len(memebr_list) - 1)
            winner = memebr_list[r]
            view = disnake.ui.View()
            embed= disnake.Embed(
                title='Ура победа',
                description=f'{winner.mention} победил'
            )
            await message.edit(embed=embed, view=view)
            wait_finish.stop()
    elif time[-1] == 'h':
        time_untill = time[0:len(time) - 2]
        if datetime.datetime.now() - now >= datetime.timedelta(hours=int(time_untill)):
            r = random.randint(0, len(memebr_list) - 1)
            winner = memebr_list[r]
            view = disnake.ui.View()
            embed= disnake.Embed(
                title='Ура победа',
                description=f'{winner.mention} победил'
            )
            await message.edit(embed=embed, view=view)
            wait_finish.stop()
    elif time[-1] == 'n':
        time_untill = time[0:len(time) - 4]
        if datetime.datetime.now() - now >= datetime.timedelta(minutes=int(time_untill)):
            r = random.randint(0, len(memebr_list) - 1)
            winner = memebr_list[r]
            view = disnake.ui.View()
            embed= disnake.Embed(
                title='Ура победа',
                description=f'{winner.mention} победил'
            )
            await message.edit(embed=embed, view=view)
            wait_finish.stop()




class compet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.slash_command(name='gcreate', description='Создать розыгрыш!') #здесь модальное окно отправляется все супер
    async def gcreate(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_modal(Modal1(self.bot))


    @commands.slash_command(name='greroll', description='Выбрать другого победителя!') #здесь модальное окно отправляется все супер
    async def greroll(self, inter: disnake.ApplicationCommandInteraction):
        r = random.randint(0, len(memebr_list) - 1)
        winner = memebr_list[r]
        embed= disnake.Embed(
                title='Ура победа',
                description=f'{winner.mention} победил'
            )
        await inter.response.send_message(embed=embed)



#розыгрыш работает так: пишется команда, выдается модальное окно с настройками, потом отправляется embed в канале и кнопка чтобы присоединиться. Когда кто то нажимает он прибавляет amount +1 и изменяет embed чтобы там число участников менялось и отправляет сообщение что вы успешно присоединились к розыгрышу
#потом там есть настройка времени, нужно чтобы оно после истечения это времени в embed появлялось еще одно окно(победитель и там рандомно выбирался победитель), соответственнно embed после выбора победителя тоже изменяется и добавляет эту строку, а кнопка пропадать
#добавить команду /greroll выбирать нового победителя(пусть просто отправляется новый embed  сновым победителем моментально)

def setup(bot):
    bot.add_cog(compet(bot))