import disnake
from disnake.ext import commands , tasks
from utils.database import UserDataBase


class On_Member_Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = UserDataBase()


    @commands.Cog.listener() 
    async def on_member_join(self, member):
        db1 = await self.db.get_user(member)
        banrole = member.guild.get_role(1079792436727009281)
        if not db1:
            await self.db.create_table()
            await self.db.add_user(member)
            role = member.guild.get_role(1095437615660019752)
            await member.add_roles(role)
            channel = disnake.utils.get(self.bot.get_all_channels(), id=1103321901515935924)
            embed = disnake.Embed(
            title=f':atst: Добро пожаловать странник :atst:', 
            description = f':jediorder: {member.mention}, переходи на темную сторону. У нас есть печеньки) :jediorder:\nОбязательно прочитай:\n:Elements_StarWars_XWing6: <#1082631738938896434> :Elements_StarWars_XWing6:\n:arrow_red: <#1068105952378753065>\n:arrow_red: <#1092375046217019432>\n:arrow_red: <#1068106442197962782> \n:arrow_red: <#1094329688983359579>\n:arrow_red: <#1092375300291186768>\n:xwinglock: Пройди собеседование с одним из представителей сервера!', color=0xff2b2b)
            embed.set_image(url="https://media.discordapp.net/attachments/1092378347759218738/1102164333359796314/3.png?width=384&height=84")
            await channel.send(embed = embed)
        elif db1[2] == 3:
            await member.add_roles(banrole)
            embed = disnake.Embed(title = 'Выдан бан', description =f' Система выдала вам бан.\nЕсли попытаетесь перезайти, то могу сразу предупредить - не выйдет!\n\nПричина: Вы пытались перезайти, чтобы снять бан')
            await user.send(embed=embed)
        



def setup(bot):
    bot.add_cog(On_Member_Join(bot))