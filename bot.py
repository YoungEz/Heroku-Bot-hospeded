import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
from random import choice
import request


start_time = time.time()


bot = commands.Bot(command_prefix='d!')
print (discord.__version__)



	
	

@bot.event
async def on_ready():
    print ("Bot Diretor On")
    print ("quem ta falando é o " + bot.user.name)
    print ("Meu numero do ZipZop: " + bot.user.id)
    while True:
    	await bot.change_presence(game=discord.Game(name='Fui criado pelo El_Brahmaᶠᶸᶜᵏᵧₒᵤ#3483| d!ajuda'.format(len(bot.servers)), type=2))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name='para ' + str(len(set(bot.get_all_members())))+ ' usuários!👥', type=1))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name='Sendo Desenvolvido 📱💻'))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name='Bot Oficial do servidor mais Top do discord'))
    	await asyncio.sleep(20)
    	await bot.change_presence(game=discord.Game(name='Quer ser staff? Entre em contato com o დ σ ρєqυєทσ yυυτσ დ#7643', type=2))
    	await asyncio.sleep(20)


    
@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.User, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``s!ban <@usuário> <motivo>``')
	else:
		await bot.ban(user)
		embed = discord.Embed(title='usuário banido!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário banido', value=user.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		await bot.send_message(member, embed=embed)
		
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``s!kick <@usuário> <motivo>``')
	else:
		await bot.kick(user)
		embed = discord.Embed(title='usuário expulso!', description='{} usuário foi expulso com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário expulso', value=user.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		await bot.send_message(user, embed=embed)
	
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await bot.say('Você precisa falar algo para votar')
	else:
			vote = await bot.say(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
			
			
			
	
			
	
	
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
	embed = discord.Embed(title="perfil de {}".format(user.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
	embed.add_field(name="Nome", value=user.name, inline=True)
	embed.add_field(name="ID do usuário", value=user.id, inline=True)
	embed.add_field(name="Status do usuário", value=user.status, inline=True)
	embed.add_field(name="Melhor cargo", value=user.top_role)
	embed.add_field(name="entrou no servidor", value=user.joined_at)
	embed.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def invite(ctx):
	await bot.say('{} https://discordapp.com/oauth2/authorize?client_id=539468157291855903&permissions=8&scope=bot'.format(ctx.message.author.mention))
	
@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' serverinfo".format(ctx.message.server.name), description="s!ajuda para ver meus comandos!.", color=0x00fA00)
	embed.add_field(name="📄Nome do servidor", value=ctx.message.server.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.server.owner) + '\n' + ctx.message.server.owner.id);
	embed.add_field(name="💻ID do servidor", value=ctx.message.server.id, inline=True)
	embed.add_field(name="🎓Total de roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="👥Quantidade de Membros", value=len(ctx.message.server.members))
	embed.add_field(name='🌎 Região', value=ctx.message.server.region)
	embed.add_field(name='👮Role Top1', value=ctx.message.server.role_hierarchy[0])
	embed.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	

	
@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494353694097438/feliz-aniversario-6224237-140820161718.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def kepiada(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589504/Piada_mulher_de_tpm_cafe.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589505/images_6.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589506/images_4.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537711026177/o_rapaz_apaixonado_diz_a_sua_amada.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604810/images_5.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604812/ladrao-em-casa-3684XBr1G1DBAQ.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567424/Passa_Passa_Passa.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567425/na_delegacia_seu_delegado_meu_marido_saiu_de_casa.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='Piadas', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def meme(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349760/images_9.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349761/cara-mano-tatuei-o-nome-da-minha-namora-e-ela-20426746.png', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032640/images_7.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032641/images_10.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088002383883/images_11.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088455630855/3d6dcd431d328b82ac2bc8edf5f754ee--kawaii.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='SO MEME DE QUALIDADE MONSTRA', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)

	

	
@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await bot.change_nickname(user, nickname)
    emb = discord.Embed(title='Apelido alterado')
    emb.add_field(name='usuário', value =user.name)
    emb.add_field(name='Autor', value =ctx.message.author.name)
    await bot.say(embed=emb)
    
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	await bot.send_message(member, content)
	await bot.say(embed=embed)  
	
@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Role Adicionada com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)
  
    
@bot.command(pass_context=True)
async def falar(ctx, *, arg):
	await bot.say(arg)

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def removerole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Role removida com sucesso', color=0xff0000)
    await bot.say(embed=embed)
	
@bot.command(pass_context=True)
async def slap(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352112713760/giphy.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Tapa!',  description=':scream:| **{}** Deu Um tapa em **{}**! Que Tapa!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def brigar(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516094273290240/300px-DarkCureFight.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802763/source.gif'
	

	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='BRIGA!',  description=':scream:| **{}** Brigou com **{}**!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def dance(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539516095900418104/fanfiction-naruto-ao-seu-lado-2635515231020140950.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550868/ed8964dd9fb2f90e5eb4b19c577bec74.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539516093593550869/Akatsuki28.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Dançando!',  description=':man_dancing:| **{}** Esta dançando com **{}**! Passinho dos Maloka 😎'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def matar(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802762/b19b70f5c546ec7c67c2f0b4e61c21f743a5acaf_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733902097645568/tumblr_m6rerquar01qd4f2uo1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Assasino!',  description='👮☎| **{}** Matou **{}**! ASSASINO!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	

	
	
@bot.command(pass_context=True)
async def atack(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539494351030452238/tumblr_mzh5vtuEIC1rm4wgqo4_r2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494352926277633/01_Rikka.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494350053310475/G4dfvA5.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733423418376194/large.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Atack!',  description='💥| **{}** Atacou **{}**! Como ousas me atacar!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	

@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Chorar...',  description='😭| **{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)

@bot.command(pass_context=True)
async def voadora(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733422621589504/giphy_6.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Voadora',  description='**{}** Deu uma voadora em **{}** EITA!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def deathnote(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/534806488531599380/14ae937e622c452bc45e509ed43c8e38a410fc0b_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533615190273425409/67dc6ce11c0ebe1c723983f18d7f68a8b0d11887_hq.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Death Note 💀',  description='**{}** escreveu o nome de **{}** em seu Death Note'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	await bot.say(embed=hugemb)
	await asyncio.sleep(5)
	hugemb = discord.Embed(title='Death Note 💔',  description='**{}** morreu apos um ataque cardiaco depois de ter seu nome escrito no Death Note de **{}**'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_footer(text ='Comando pedido por: {} | Shiryu Bot Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494351555002379/tumblr_mdi1l8AaDi1rcm8d4o1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)  
	
@bot.command()
async def flipcoin():
	list = 'tapa na **CARA**', 'Rei perdeu a **COROA**'
	await bot.say(random.choice(list))																								
@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voicemute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=True)
    emb = discord.Embed(title='Usuário mutado voz', description='{} foi mutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
    await bot.say(embed=emb)  

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(member: discord.Member):
	await bot.server_voice_state(member,mute=False)
	emb = discord.Embed(title='Usuário desmutado voz', description='{} foi desmutado com sucesso.'.format(member.mention), color=0x00ffbb)
	emb.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
	await bot.say(embed=emb)

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=100):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
            try:
                await bot.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description="**{}** mensagens apagadas com sucesso! {} :smile:".format(limit, ctx.message.author.mention), color=0x00ff00)
    embed.set_footer(text ='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
    await bot.say (embed=embed)
    
@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'd!modajuda ',value ='Comandos de moderação Ex: ban,kick e clear etc...',inline = False)
    embed.add_field(name = 'd!diversaoajuda ',value ='Comandos de diversão e que todos podem usar! Ex: kiss,hug e deathnote.',inline = False)
    embed.set_footer(text='Comando realizado por {} | De YoungStudios Para School Night'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    
@bot.command(pass_context = True)
async def modajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'd!!kick ',value ='como usar ``d!kick @usuário`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = 'd!ban ',value ='Como usar ``d!ban @usuário`` bane o usuário marcado',inline = False)
    embed.add_field(name = 'd!addrole ',value ='Como usar ``d!addrole @role @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 'd!removerole',value ='Como usar ``d!removerole @role @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 'd!clear',value ='Como usar ``d!clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 'd!avisar',value ='Como usar ``s!avisar @usuário`` avisa um usuário no PV ',inline = False)


    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    
@bot.command(pass_context=True)
async def roleta(ctx, *, pergunta: str = None):
    if not pergunta:
        return await bot.say("Você precisa perguntar alguma coisa.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro'])
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await bot.say(embed=embed)
    
    
   
   
@bot.command(pass_context=True)
async def diversaoajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'd!dance ',value ='Como usar ``d!dance`` dance com algum usuário',inline = False)
    embed.add_field(name = 'd!kiss ',value ='Como usar ``d!kiss @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = 'd!hug ',value ='Como usar ``d!abraçar @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = 'd!flipcoin ',value ='Como usar ``d!flipcoin`` Cara ou coroa?',inline = False)
    embed.add_field(name = 'd!deathnote ',value ='Como usar ``d!deathnote @usuário`` Escreva o nome de determinado usuário em seu Death Note ',inline = False)
    embed.add_field(name = 'd!avatar ',value ='Como usar ``s!avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="d!meme", value="como usar ``d!meme`` que tal ver alguns memes?!", inline=False)
    embed.add_field(name="d!ping", value="como usar ``d!ping`` Veja meu tempo de resposta!", inline=False)
    embed.add_field(name="d!userinfo", value="como usar ``d!userinfo @usuário`` Veja o perfil de um determinado usuário!", inline=True)
    embed.add_field(name="d!voadora", value="como usar ``d!voadora @usuário`` de uma voadora em alguem!", inline=True)
    embed.add_field(name="d!brigar", value="como usar ``d!brigar @usuário`` Use esse comando se alguem estiver merecendo apanhar!", inline=True)  	
    embed.add_field(name="d!matar", value="como usar ``d!matar @usuário`` Use esse comando se alguem estiver merecendo!", inline=True)
    embed.add_field(name="d!slap", value="como usar ``d!slap @usuário`` Use esse comando se alguem estiver merecendo levar uns tapa cabuloso", inline=True)
    embed.add_field(name="d!falar", value="como usar ``d!userinfo @usuário`` Faça eu falae alguma coisa!", inline=True)
    embed.add_field(name="d!suicidio", value="como usar ``d!suicidio`` suicidio💔", inline=True)
    embed.add_field(name="d!kepiada", value="como usar ``d!kepiada`` Que tal uma piada?!", inline=True)
    embed.add_field(name="d!atack", value="como usar ``d!atack @usuário`` use este comando para atacar alguem!", inline=True)
    embed.add_field(name="d!chorar", value="como usar ``d!chorar`` Chorar faz bem para os olhos...", inline=True)
     	     	     	     	     	     	     	     	
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    
bot.run(str(os.environ.get('BOT_TOKEN')))
