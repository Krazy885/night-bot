import disnake
from disnake.ext import commands
import asyncio
import datetime



class voice(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command(name='voicehub') #здесь все супер, уже отправляется и кнопки есть
    async def voicehub(self, inter: disnake.ApplicationCommandInteraction):
        embed1 = disnake.Embed(title ='Управление приватной комнатой', description = '**Жми следующие кнопки, чтобы настроить свою комнату**\nИспользовать их можно только когда у тебя есть приватный канал\n\n<:VoiceHideRoom:1106136331714834435> - Скрыть комнату для всех\n<:VoiceChangeName:1106136322411872297> - Изменить название комнаты\n<:VoiceChangeOwner:1106136333862326303> - Передать владение комнатой\n<:VoiceKickUser:1106136326576816198> - Выгнать из комнаты\n<:VoiceGiveRoomAccess:1106136338949996554> - Выдать доступ в комнату\n\n<:VoiceRemoveRoomAccess:1106136317647142972> - Забрать доступ в комнату\n<:VoiceGiveSpeech:1106136311817056317> - Выдать право говорить\n<:VoiceRemoveSpeech:1106136314253950977> - Забрать право говорить\n<:VoiceChangeUserLimit:1106136336924164197> - Изменить лимит пользователей\n<:VoiceOpenForAll:1106136328623620106> - Открыть комнату для всех\n<:VoiceCloseForAll:1106136319291314186> - Закрыть комнату для всех', color=0x4e77eb)
        await inter.send(embed = embed1, view = Button_for_voice(self.bot))


    @commands.Cog.listener()   
    async def on_voice_state_update(self, member, before, after):
        channel_hub = disnake.utils.get(self.bot.get_all_channels(), id=1105134032959844537)
        category = disnake.utils.get(self.bot.get_all_channels(), id=1079792439105159319)
        overwrites = {
        self.guild.default_role: disnake.PermissionOverwrite(view_channel=True, connect = True, speak = True, use_voice_activation = True),
        #inter.guild.role(role): disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True),
        self.guild.me: disnake.PermissionOverwrite(read_messages=True),               #<-- настройка прав доступа к каналу
        self.user: disnake.PermissionOverwrite(read_messages=True, send_messages=True, view_channel=True)
        } # <- тут я получил войс 
        if before.channel == channel_hub:
            print(123)
            channel = await inter.guild.create_voice_channel(f'{inter.user.name} - рума', overwrites=overwrites, category=category)#присоединился -> принт123
            await asyncio.sleep(2)
            await member.move_to(channel)





class Modal1(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot

        #детали окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="название",
                placeholder="",
                custom_id="название",
                max_length=100,
                ),
            ]
    

        super().__init__(
            title="Новое название",
            custom_id="Новое название",
            components=components,
            )    

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
#здесь должно изменяться название канала
        await print(1)

class Modal2(disnake.ui.Modal):
    def __init__(self, bot):
        self.bot = bot

        #детали окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="лимит(макс.)",
                placeholder="Любое число до 99, либо 0 чтобы убрать лимит",
                custom_id="лимит",
                max_length=100,
                ),
            ]
    

        super().__init__(
            title="Новый лимит",
            custom_id="Новый лимит",
            components=components,
            )    

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
#здесь должен изменяться лимит участников голосового канала
        await print(1)



class Button_for_voice(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceHideRoom:1106136331714834435>')
    async def Hide(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь евриван убираем право видеть руму
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceChangeName:1106136322411872297>')
    async def Name(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь высылаем модальное окно с заменой названия
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceChangeOwner:1106136333862326303>')
    async def Owner(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы поменять владельца комнаты
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceKickUser:1106136326576816198>')
    async def Kick(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы выгнать кого-то из комнаты
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceGiveRoomAccess:1106136338949996554>')
    async def Give(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы выдать ему право подключаться
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceRemoveRoomAccess:1106136317647142972>')
    async def Remove(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы забрать у кого то право подключаться
        await print(1)

    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceGiveSpeech:1106136311817056317>')
    async def MicOn(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы выдать право говорить
        await print(1)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceRemoveSpeech:1106136314253950977>')
    async def MicOff(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выпадаюбщее меню с выбором пользователя, чтобы забрать право говорить
        await print(1)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceChangeUserLimit:1106136336924164197>')
    async def Limit(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь модальное окно которое меняет лимит
        await print(1)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceOpenForAll:1106136328623620106>')
    async def Unlock(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь выдать всем возможность подключаться
        await print(1)


    @disnake.ui.button(label='', style=disnake.ButtonStyle.grey, emoji='<:VoiceCloseForAll:1106136319291314186>')
    async def Lock(self, button: disnake.ui.Button, inter: disnake.Interaction):
        #здесь забрать у всех возможность подключаться
        await print(1)







def setup(bot):
    bot.add_cog(voice(bot))










    #вопросы:
    #загляни в ког тикеты там ивент чтобы после перезапуска все работало, не работает
    #загляни в ког compet там все расписано
    #загляни в он мембер джойн там что то с бд жаловалось чекни все ли ок?
    #а так вроде бы это все