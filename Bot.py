import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import sys
import subprocess
import os
import json
import traceback
import random



start_time = time.time()


bot = commands.Bot(command_prefix='-')
print (discord.__version__)


	
	

@bot.event
async def on_ready():
    print ("Bot Toxic On")
    print ("quem ta falando é o " + bot.user.name)
    print ("Meu numero do ZipZop: " + bot.user.id)
    await bot.change_presence(game=discord.Game(name='Fui criado pelo El_Brahmaᶠᶸᶜᵏᵧₒᵤ| t!ajuda'.format(len(bot.servers)), type=2))
    await asyncio.sleep(20)
    await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members())))+ ' soldados Toxic!', type=3))
    await asyncio.sleep(20)
    await bot.change_presence(game=discord.Game(name='FREE FIRE'))


    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial Toxic')
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def perfil(ctx, user: discord.Member):
    embed = discord.Embed(title="perfil de {}".format(user.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
    embed.add_field(name="Nome", value=user.name, inline=True)
    embed.add_field(name="ID do usuário", value=user.id, inline=True)
    embed.add_field(name="Status do usuário", value=user.status, inline=True)
    embed.add_field(name="Melhor cargo", value=user.top_role)
    embed.add_field(name="entrou no servidor", value=user.joined_at)
    embed.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial Toxic')
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
@bot.command(pass_context=True)
async def serverinfo(ctx):
	server = ctx.message.server
	roles = [x.name for x in
	server.role_hierarchy]
	role_length = len(roles)
	
	if role_length > 50:
		roles = roles[:50]
		roles.append('>>>> [50/%s] Roles'%len(roles))
		roles = ', '.join(roles)
		channelz = len(server.channels);
		time = str(server.created_at); time = time.split(' '); time= time[0];
		join = discord.Embed(description= '%s '%(str(server)),title = 'Nome', colour = 0xFFFF);
		join.set_thumbnail(url = server.icon_url);
		join.add_field(name = '👑 Dono',
		value = str(server.owner) + '\n' + server.owner.id);
		join.add_field(name = '💻ID', value = str(server.id))
		join.add_field(name = '👥Total de membros', value = str(server.member_count));
		join.add_field(name = '📝Total de canais Texto/voz', value = str(channelz));
		join.add_field(name="🎭 Total de roles", value=len(ctx.message.server.roles), inline=True)
		join.add_field(name='🌎 Região', value=server.region)
		join.add_field(name ='📆Criado em', value='Data: %s'%time);
		
		join.add_field(name='👮Role Top1', value=server.role_hierarchy[0])
		join.set_footer(text ='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ | Bot Oficial TOXIC');
		await bot.say(embed=join);

@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, userName: discord.User):
	await bot.kick(userName)
	embed = discord.Embed(title='usuário kickado', description='{} usuário kickado com sucesso'.format(ctx.message.author.mention), color=0xff0bb)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=embed)
	print ("user has kicked")		
	
			
@bot.command(pass_context=True)
async def ajuda(ctx):
    embed = discord.Embed(title="Toxic Bot", description="Meu comandos são", color=0x00ff00)
    embed.set_footer(text="Bot Oficial TOXIC")
    embed.set_author(name="Fui criado pelo By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ ")
    embed.add_field(name="ban", value="bane o usuário", inline=True)
    embed.add_field(name="kick", value="expulsa o usuário", inline=True)
    embed.add_field(name="serverinfo", value="Veja informações do servidor do discord Atual!", inline=True)
    embed.add_field(name="perfil", value="mostra seu perfil!", inline=True)
    embed.add_field(name="ping", value="Veja minha velocidade de resposta!", inline=True)
    embed.add_field(name="avatar", value="Veja o avatar de determinado usuário!", inline=True)
    embed.add_field(name="deathnote", value="escreva o nome de determinado usuário em seu death note!", inline=True)
    embed.add_field(name="kiss", value="O amor esta no ar.. beije determinado usuário!", inline=True)
    embed.add_field(name="hug", value="abrace seu/sua melhor amigo(a)!", inline=True)
    embed.add_field(name="flipcoin", value="cara ou coroa?", inline=True)
    await bot.say(embed=embed)	
    
@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)    								
  
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user, userName: discord.User, arg):
	await bot.ban(userName)
	embed = discord.Embed(title='comando ban foi executado', description='usuário banido com sucesso {}'.format(ctx.message.author.mention), color=0xff0Ab)
	embed.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=embed)
	print("user has banned")

@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)  

@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)
	await asyncio.sleep(5)
	hugemb = discord.Embed(title='Death Note 💔',  description='**{}** morreu apos um ataque cardiaco depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_footer(text='By: El_Brahmaᶠᶸᶜᵏᵧₒᵤ| Bot Oficial TOXIC')
	await bot.say(embed=hugemb)
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))																								
																																				
bot.login('process.env.BOT_TOKEN')
