import disnake
from disnake import app_commands
from disnake.ext import commands , tasks
import random
import datetime
import asyncio
from config import settings
from utils.database import UserDataBase
from disnake.utils import get


class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bots = [1102679604847722726, 1103347298894880882, 478321260481478677, 575776004233232386, 677976225876017190, 819457016774656060, 1059010370045497394, 789797049746980895, 740585412560420914, 464272403766444044, 315926021457051650, 315926021457051650, 721772274830540833, 1086010183257436301, 1077962672261304410, 1094024332981846097]
        self.db = UserDataBase()

    @commands.slash_command(name='clear', description='Удалить сообщения из чата')
    async def clear(self, inter: disnake.ApplicationCommandInteraction, количество: int):
        if количество != 0 and количество > 0:
            author = inter.author
            embed = disnake.Embed(description = f':white_check_mark: Удалено {количество} сообщений', color=0x4e77eb)
            embed.set_thumbnail(url = author.avatar.url)
            await inter.channel.purge(limit = количество)
            await inter.response.send_message(embed = embed, ephemeral = True)
            channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
            embed1 = disnake.Embed(title = f'Удалены сообщения', description = f'Модератор: {author.mention}\nКанал: {channel1.mention}\nУдалено {количество} из {количество} сообщений', color=0x4e77eb)
            await channel1.send(embed=embed1)
        elif количество == 0:
            await inter.response.send_message(f'Нельзя указывать 0', ephemeral = True)
        else:
            await inter.response.send_message(f'Нельзя указывать отрицательные числа', ephemeral = True)




    @commands.slash_command(name='timeout', description='Отправить в таймаут')
    async def timeout(self, inter: disnake.ApplicationCommandInteraction, время: int, user: disnake.Member, причина: str):
        время1 = datetime.datetime.now() + datetime.timedelta(minutes=время)
        author = inter.author
        if время != 0 and время > 0:
            if author.id != user.id and user.id not in self.bots:
                await user.timeout(reason = причина, until = время1)
                await inter.response.send_message(f'{user.mention} отправлен подумать о своем поведении до {время1} по причине {причина}', ephemeral = True)
                channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
                embed1 = disnake.Embed(title = f'Пользователь в таймауте', description = f'Модератор: {author.mention}\nПользователь: {user.mention}\nДумает о своем поведении по причине {причина} {время} минут', color=0x4e77eb)
                await channel.send(embed=embed1)
            elif author.id == user.id:
                await inter.response.send_message(f'Боюсь, что на себя нельзя применять данную команду',  ephemeral=True)
            else:
                await inter.response.send_message(f'Боюсь, что на ботов нельзя применять данную команду',  ephemeral=True)
        elif время == 0:
            await inter.response.send_message(f'Нельзя указывать 0', ephemeral = True)
        else:
            await inter.response.send_message(f'Нельзя указывать отрицательные числа', ephemeral = True)


    @commands.slash_command(name='untimeout', description='Отправить в таймаут')
    async def untimeout(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member):
        author = inter.author
        if author.id != user.id and user.id not in self.bots:
            await user.timeout(reason = None, until = None)
            await inter.response.send_message(f'таймаут для {user.mention} снят', ephemeral = True)
            channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
            embed1 = disnake.Embed(title = f'Таймаут снят', description = f'Модератор: {author.mention}\nПользователю: {user.mention} сняли таймаут', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif author.id == user.id:
            await inter.response.send_message(f'Боюсь, что на себя нельзя применять данную команду',  ephemeral=True)
        else:
            await inter.response.send_message(f'Боюсь, что на ботов нельзя применять данную команду',  ephemeral=True)
        
    @commands.slash_command(name='slowmode', description='Медленный режим(для отключения 0)')
    async def slowmode(self, inter: disnake.ApplicationCommandInteraction, задержка: int):
        channel = inter.channel
        if задержка > 0:
            await inter.channel.edit(slowmode_delay = задержка)
            await inter.response.send_message(f'Включен медленный режим с задержкой {задержка}', ephemeral = True)
            channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
            embed1 = disnake.Embed(title = f'Установлен медленный режим', description = f'Модератор: {author.mention}\nКанал: {channel1.mention}\nУстановлен медленный режим с задержкой: {задержка}', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif задержка == 0:
            await inter.channel.edit(slowmode_delay = задержка)
            await inter.response.send_message(f'Выключен медленный режим', ephemeral = True)
        else:
            await inter.response.send_message(f'Нельзя указывать отрицательное число', ephemeral = True)


    @commands.slash_command(name='database')
    async def set_global_balance(self, interaction):
        #for member in interaction.guild.members:
            #if not await self.db.get_user(member):
        await self.db.create_table()
        await self.db.add_user(interaction.author)
        await interaction.response.send_message('всем пользователем дан начальный баланс', ephemeral=True)


    @commands.slash_command(name='warn', description='Выдать варн')
    async def warn(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, причина: str):
        author = inter.author
        if user == inter.author:
            await inter.send_message(f'Нельзя выдать варн себе', ephemeral = True)
        elif user.id in self.bots:
            await inter.send_message(f'Нельзя выдать варн боту', ephemeral = True)
        else:
            await self.db.add_warns(user)
            author_data = await self.db.get_user(author)
            if author_data[2] == 3:
                author_data = await self.db.get_user(author)
                roles = ''
                for role in user.roles:
                    roles += f' {str(role.id)}'
                    await self.db.add_roles(user, roles)
                    await inter.user.add_roles(banrole)
                    await inter.response.send_message(f'у {user.mention} 3 из 3 варнов. Выдан бан.', ephemeral = True)
                    embed = disnake.Embed(title = 'Вы получили 3 из 3 варнов', description =f'Модератор {author.mention} выдал вам бан.\nЕсли попытаетесь перезайти, то могу сразу предупредить - не выйдет!\n\nПричина: 3 из 3 варнов', color=0x4e77eb)
                    await user.send(embed=embed)
                    channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
                    embed1 = disnake.Embed(title = f'Выдан бан', description = f'Модератор\n{author.mention}\nПользователь: {user.mention}\n Выдан варн по причине 3 из 3 варнов!', color=0x4e77eb)
                    await channel.send(embed=embed1)     
            else:
                await inter.response.send_message(f'Варн пользователю {user.mention} по причине {причина} успешно выдан', ephemeral = True)
                embed = disnake.Embed(title = 'Выдано предупреждение', description =f'Модератор {author.mention} выдал вам предупреждение.\nНапоминаем что после 3 предупреждений вы получите бан.\nСейчас у вас {author_data[2]} из 3\n\nПричина: {причина}', color=0x4e77eb)
                await user.send_message(embed=embed)
                channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
                embed1 = disnake.Embed(title = f'Выдан варн', description = f'Модератор: {author.mention}\nПользователь: {user.mention}\n Выдан варн по причине {причина}', color=0x4e77eb)
                await channel.send(embed=embed1)

    @commands.slash_command(name='unwarn', description='Снять варн')
    async def unwarn(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, причина: str):
        author = inter.author
        if user == inter.author:
            await inter.send_message(f'Нельзя снять варн себе', ephemeral = True)
        elif user.id in self.bots:
            await inter.send_message(f'Нельзя снять варн боту', ephemeral = True)
        else:
            author_data = await self.db.get_user(author)
            if author_data[2] == 0:
                await inter.send_message(f'Нельзя сделать число варнов отрицательным', ephemeral = True)
            else:
                await self.db.remove_warns(user)
                await inter.response.send_message(f'Варн пользователю {user.mention} по причине {причина} успешно снят', ephemeral = True)
                embed = disnake.Embed(title = 'Снято предупреждение', description =f'Модератор {author.mention} снял вам предупреждение.\nНапоминаем что после 3 предупреждений вы получите бан.\nСейчас у вас {author_data[2]} из 3\n\nПричина: {причина}', color=0x4e77eb)
                await user.send_message(embed=embed)
                channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
                embed1 = disnake.Embed(title = f'Снят варн', description = f'Модератор: {author.mention}\nПользователь: {user.mention}\nСнят варн по причине {причина}', color=0x4e77eb)
                await channel.send(embed=embed1)             

    @commands.slash_command(name='ban', description='Забанить пользователя')
    async def ban(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, причина: str):
        author = inter.author
        banrole = inter.guild.get_role(1079792436727009281)
        if user == inter.author:
            await inter.response.send_message(f'Нельзя забанить себя', ephemeral = True)
        elif user.id in self.bots:
            await inter.send_message(f'Нельзя забанить бота', ephemeral = True)
        else:
            author_data = await self.db.get_user(author)
            count_warns = 3 - author_data[2]
            await self.db.add_warns(user, count_warns)
            roles = ''
            for role in user.roles:
                roles += f' {str(role.id)}'
            await self.db.add_roles(user, roles)
            await user.add_roles(banrole)
            await inter.response.send_message(f'Бан пользователю {user.mention} по причине {причина} успешно выдан', ephemeral = True)
            embed = disnake.Embed(title = 'Выдан бан', description =f'Модератор {author.mention} выдал вам бан.\nЕсли попытаетесь перезайти, то могу сразу предупредить - не выйдет!\n\nПричина: {причина}', color=0x4e77eb)
            await user.send(embed=embed)
            channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
            embed1 = disnake.Embed(title = f'Выдан бан', description = f'Модератор: {author.mention}\nПользователь: {user.mention}\nВыдан бан по причине {причина}', color=0x4e77eb)
            await channel.send(embed=embed1)

    @commands.slash_command(name='unban', description='Разбанить пользователя')
    async def unban(self, inter: disnake.ApplicationCommandInteraction, user: disnake.Member, причина: str):
        author = inter.author
        banrole = inter.guild.get_role(1079792436727009281)
        if user == inter.author:
            await inter.response.send_message(f'Нельзя разбанить себя', ephemeral = True)
        elif user.id in self.bots:
            await inter.send_message(f'Нельзя разбанить бота', ephemeral = True)
        else:
            author_data = await self.db.get_user(author)
            count_warns = 3 - author_data[2]
            await self.db.remove_warns(user, count_warns)
            roles = list(map(int, author_data[3].split()))
            print(roles)
            for role in roles:
                role = inter.guild.get_role(role)
                await user.add_roles(role)
            await self.db.add_roles(user, '')
            await user.remove_roles(banrole)
            await inter.response.send_message(f'Бан снят {user.mention} по причине {причина} успешно снят', ephemeral = True)
            embed = disnake.Embed(title = 'Бан снят', description =f'Модератор: {author.mention} снял вам бан.\n\nПричина: {причина}', color=0x4e77eb)
            await user.send(embed=embed)
            channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
            embed1 = disnake.Embed(title = f'Бан снят', description = f'Модератор: {author.mention}\nПользователь: {user.mention}\nСнят бан по причине {причина}', color=0x4e77eb)
            await channel.send(embed=embed1)      


def setup(bot):
    bot.add_cog(moderation(bot))