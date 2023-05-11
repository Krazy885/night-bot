import disnake
from disnake import app_commands
from disnake.ext import commands , tasks
from disnake.utils import get
from config import settings

class MyModal(disnake.ui.Modal):
    def __init__(self, bot, admin):
        self.bot = bot
        self.admin = admin
        #детали окна и его компонентов
        components = [
            disnake.ui.TextInput(
                label="Оцените качество верификации от 1 до 10",
                placeholder="1-10",
                custom_id="оценка",
                max_length=3,
                ),
            disnake.ui.TextInput(
                label="Вел ли себя саппорт компетентно?",
                placeholder="ДА/НЕТ",
                custom_id="компетентность",
                ),
            disnake.ui.TextInput(
                label="Поделитесь, понравилась ли вам верификация?",
                placeholder="Поделитесь мнением",
                custom_id="отзыв",
                ),
            ]
    

        super().__init__(
            title="Отзывы на верификацию",
            custom_id="Отзывы на верификацию",
            components=components,
            )    

    # Обработка ответа, после отправки модального окна
    async def callback(self, inter: disnake.ModalInteraction):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577089)
        user_ = inter.author
        embed = disnake.Embed(title="Отзыв на работу саппорта", description = f"пользователь: {user_.mention}, \nсаппорт: {self.admin.mention}, \nОцените качество верификации от 1 до 10: {inter.text_values['оценка']}, \nВел ли себя саппорт компетентно?: {inter.text_values['компетентность']}, \nПоделитесь, понравилась ли вам верификация? {inter.text_values['отзыв']}", colour = 0x4F78E8)

        await channel.send(embed=embed)
        await inter.response.send_message('Спасибо за оставленный отзыв! Вы помогаете нам стать лучше.')
       

class Button_for_feedback(disnake.ui.View):
    def __init__(self, bot, admin):
        self.bot = bot
        self.admin = admin
        super().__init__(timeout=None)


    @disnake.ui.button(label='Оставить отзыв!', style=disnake.ButtonStyle.green)
    async def feedback(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        await interaction.response.send_modal(MyModal(self.bot, self.admin))

class slash_commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='verif', description='Провести верификацию')
    async def verif(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, пол: str = commands.Param(choices=["Мужской", "Женский"])):
        admin = inter.author
        await inter.response.send_message(f'Привет дорогой саппорт! Ты успешно верифицировал {user.mention}\nОтчет отправлен',  ephemeral=True)
        male = inter.guild.get_role(1079792436798304325)
        female = inter.guild.get_role(1079792436827672737)
        new = inter.guild.get_role(1079792436727009286)
        await user.remove_roles(new)
        if пол == "Мужской":
            await user.add_roles(male)
        else:
            await user.add_roles(female)
        await user.send(f'Приветствую на сервере Night! Вы успешно прошли верификацию. Все интересующие вас роли, вы можете взять в памятке. По любым вопросам обращайтесь к администрации сервера. Пожалуйста оцените качество вашей верификации и оставьте нам отзыв!', view = Button_for_feedback(self.bot, admin))







      
        




def setup(bot):
    bot.add_cog(slash_commands(bot))



