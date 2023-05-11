import disnake
from disnake.ext import commands
import datetime


class audit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        inviter = invite.inviter
        maxage = invite.max_age
        maxuses = invite.max_uses
        if maxuses == 0:
            maxuses = 'без ограничений'
        else:
            pass
        if maxage < 3600:
            embed1 = disnake.Embed(title = f'Создано приглашение', description = f'Пользователь: {inviter.mention} cоздал приглашение: {invite}\nПриглашение действует {maxage} секунд и могут зайти {maxuses} людей', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif maxage == 3600:
            embed1 = disnake.Embed(title = f'Создано приглашение', description = f'Пользователь: {inviter.mention} cоздал приглашение: {invite}\nПриглашение действует час и могут зайти {maxuses} людей', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif maxage == 86400:
            embed1 = disnake.Embed(title = f'Создано приглашение', description = f'Пользователь: {inviter.mention} cоздал приглашение: {invite}\nПриглашение действует день и могут зайти {maxuses} людей', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif maxage > 3600 and maxage < 86400:
            maxagenew = maxage / 60
            embed1 = disnake.Embed(title = f'Создано приглашение', description = f'Пользователь: {inviter.mention} cоздал приглашение: {invite}\nПриглашение действует {maxagenew} часов и могут зайти {maxuses} людей', color=0x4e77eb)
            await channel.send(embed=embed1)
        else:
            maxagenew = (maxage / 60) / 60
            embed1 = disnake.Embed(title = f'Создано приглашение', description = f'Пользователь: {inviter.mention} cоздал приглашение: {invite}\nПриглашение действует {maxagenew} дней и могут зайти {maxuses} людей', color=0x4e77eb)
            await channel.send(embed=embed1)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        join = member.joined_at
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        embed1 = disnake.Embed(title = f'Участник вышел', description = f'Пользователь: {member.mention} вышел с сервера\n Находился на сервере с {join}', color=0x4e77eb)
        await channel.send(embed=embed1)



    #@commands.Cog.listener()
   # async def on_guild_emojis_update(self, guild, before, after):
     #   channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
      #  emojs_before = before.id
    #    emojs_after = after.id
      #  emoj1 = []
      #  for emoj_ in after.id:
     #       if emoj_ not in before.id:
     #           emoj1.append(emoj_)
     #           embed2 = disnake.Embed(title = f'Добавлена роль', description = f'Добавлено эмоджи: {after[0]}', color=0x4e77eb)
     #           await channel.send(embed=embed2)
     #   emoj2 = []
     #   for emoj_ in before.id:
      #      if emoj_ not in after.id:
      #          emoj2.append(emoj_)
      #  embed1 = disnake.Embed(title = f'Добавлены эмоджи', description = f'Удалено эмоджи: {after}', color=0x4e77eb)
      # await channel.send(embed=embed1)

    
    @commands.Cog.listener()
    async def on_message_delete(self, message):
        author1 = message.author
        channel1 = message.channel
        content1 = message.content
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        embed1 = disnake.Embed(title = f'Удалено сообщение', description = f'Автор: {author1.mention}\nКанал: {channel1.mention}\n**Контент сообщения**: {content1}\n\n**Если контент пустой, значит это был embed!!!!**', color=0x4e77eb)
        await channel.send(embed=embed1)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        nick_after = after.nick
        nick_before = before.nick
        roles_before = before.roles
        roles_after = after.roles
        role1 = []
        for role_ in after.roles:
            if role_ not in before.roles:
                role1.append(role_)
                embed2 = disnake.Embed(title = f'Добавлена роль', description = f'Пользователь: {before.mention}\nДобавлена роль: {role1[0].mention}', color=0x4e77eb)
                await channel.send(embed=embed2)
        role2 = []
        for role_ in before.roles:
            if role_ not in after.roles:
                role2.append(role_)
                embed3 = disnake.Embed(title = f'Удалена роль', description = f'Пользователь: {before.mention}\nУдалена роль: {role2[0].mention}', color=0x4e77eb)
                await channel.send(embed=embed3)
        if nick_after != nick_before and nick_before != None and nick_after != None:
            embed1 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {nick_after}\nПрошлый ник: {nick_before}', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif nick_after != nick_before and nick_before == None:
            embed4 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {nick_after}\nПрошлый ник: {before}', color=0x4e77eb)
            await channel.send(embed=embed4)
        elif nick_after != nick_before and nick_after == None:
            embed5 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {after}\nПрошлый ник: {nick_before}', color=0x4e77eb)
            await channel.send(embed=embed5)


    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        nick_after = after.name
        nick_before = before.name
        if nick_after != nick_before and nick_before != None and nick_after != None:
            embed1 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {nick_after}\nПрошлый ник: {nick_before}', color=0x4e77eb)
            await channel.send(embed=embed1)
        elif nick_after != nick_before and nick_before == None:
            embed4 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {nick_after}\nПрошлый ник: {before}', color=0x4e77eb)
            await channel.send(embed=embed4)
        elif nick_after != nick_before and nick_after == None:
            embed5 = disnake.Embed(title = f'Никнейм изменен', description = f'Пользователь: {after.mention}\nНовый ник: {after}\nПрошлый ник: {nick_before}', color=0x4e77eb)
            await channel.send(embed=embed5)


    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        role1 = role.id
        embed6 = disnake.Embed(title = f'Создана роль', description = f'Создана роль: <@&{role1}>', color=0x4e77eb)
        await channel.send(embed=embed6)



    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        role2 = role.name
        embed7 = disnake.Embed(title = f'Роль удалена', description = f'Удалена роль: {role2}', color=0x4e77eb)
        await channel.send(embed=embed7)

    @commands.Cog.listener()
    async def on_guild_role_update(self, before, after):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        role = before.id
        perms_before = before.permissions
        perms_after = after.permissions
        perm1 = []
        for perm_ in after.permissions:
            if perm_ not in before.permissions:
                perm1.append(perm_)
        perm2 = []
        for perm_ in before.permissions:
            if perm_ not in after.permissions:
                perm2.append(perm_)
        for i in range(len(perm2)):
            if True in perm1[0] and False in perm2[0]:
                embed2 = disnake.Embed(title = f'Роль изменена', description = f'Роль: <@&{role}>\nДобавлены права: {perm1[i][0]}', color=0x4e77eb)
                await channel.send(embed=embed2)
            if False in perm1[0] and True in perm2[0]:
                embed3 = disnake.Embed(title = f'Роль изменена', description = f'Роль: <@&{role}>\nУдалены права: {perm2[i][0]}', color=0x4e77eb)
                await channel.send(embed=embed3)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        embed6 = disnake.Embed(title = f'Создан канал', description = f'Создан канал: {channel.mention}', color=0x4e77eb)
        await channel1.send(embed=embed6)
                
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        channel1 = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        embed6 = disnake.Embed(title = f'Удален канал', description = f'Удален канал: {channel}', color=0x4e77eb)
        await channel1.send(embed=embed6)

    @commands.Cog.listener()
    async def on_guild_channel_update(self, before, after):
        channel = disnake.utils.get(self.bot.get_all_channels(), id=1079792437775577090)
        channel11 = before.mention
        perms_before = before.overwrites
        perms_after = after.overwrites
        print(perms_before, perms_after)
        perm1 = []
        for perm_ in after.overwrites:
            if perm_ not in before.overwrites:
                perm1.append(perm_)
                print(perm1)
        perm2 = []
        for perm_ in before.overwrites:
            if perm_ not in after.overwrites:
                perm2.append(perm_)
                print(perm2)
        print(perms_before, perms_after)
        for i in range(len(perm2)):
            if True in perm1[0] and False in perm2[0]:
                embed2 = disnake.Embed(title = f'Права канала изменены', description = f'Канал: {channel11}\nДобавлены права: {perm1[i][0]}', color=0x4e77eb)
                await channel.send(embed=embed2)
            if False in perm1[0] and True in perm2[0]:
                embed3 = disnake.Embed(title = f'Права канала изменены', description = f'Канал: {channel11}\nУдалены права: {perm2[i][0]}', color=0x4e77eb)
                await channel.send(embed=embed3)




def setup(bot):
    bot.add_cog(audit(bot))