""""
Copyright © Krypton 2022 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
This is a template to create your own discord bot in python.

Version: 5.1
"""

import platform
import random
import csv

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks


class General(commands.Cog, name="general"):

  def __init__(self, bot):
    self.bot = bot

  @commands.hybrid_command(
    name="ajuda", description="Lista todos comandos que o robô carregou.")
  async def help(self, context: Context) -> None:
    prefix = self.bot.config["prefix"]
    embed = discord.Embed(title="Ajuda",
                          description="Lista de comandos disponíveis:",
                          color=0x9C84EF)
    for i in self.bot.cogs:
      cog = self.bot.get_cog(i.lower())
      commands = cog.get_commands()
      data = []
      for command in commands:
        description = command.description.partition('\n')[0]
        data.append(f"{prefix}{command.name} - {description}")
      help_text = "\n".join(data)
      embed.add_field(name=i.capitalize(),
                      value=f'```{help_text}```',
                      inline=False)
    await context.send(embed=embed)

  @commands.hybrid_command(
    name="botinfo",
    description="Veja algumas informações úteis (ou não) sobre o robô.",
  )
  @checks.not_blacklisted()
  async def botinfo(self, context: Context) -> None:
    """
        Veja algumas informações úteis (ou não) sobre o robô.
        
        :param context: The hybrid command context.
        """
    embed = discord.Embed(
      description=
      "Modelo usado para o desenvolvimento do robô: [Krypton's](https://krypton.ninja)",
      color=0x9C84EF)
    embed.set_author(name="Bot Information")
    embed.add_field(name="Owner:", value="Krypton#7331", inline=True)
    embed.add_field(name="Python Version:",
                    value=f"{platform.python_version()}",
                    inline=True)
    embed.add_field(
      name="Prefix:",
      value=
      f"/ (Slash Commands) ou {self.bot.config['prefix']} comandos normais",
      inline=False)
    embed.set_footer(text=f"Requested by {context.author}")
    await context.send(embed=embed)

  @commands.hybrid_command(
    name="serverinfo",
    description="Veja algumas informações úteis (ou não) sobre o servidor.",
  )
  @checks.not_blacklisted()
  async def serverinfo(self, context: Context) -> None:
    """
        Veja algumas informações úteis (ou não) sobre o servidor.
        
        :param context: The hybrid command context.
        """
    roles = [role.name for role in context.guild.roles]
    if len(roles) > 50:
      roles = roles[:50]
      roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
    roles = ", ".join(roles)

    embed = discord.Embed(title="**Server Name:**",
                          description=f"{context.guild}",
                          color=0x9C84EF)
    if context.guild.icon is not None:
      embed.set_thumbnail(url=context.guild.icon.url)
    embed.add_field(name="Server ID", value=context.guild.id)
    embed.add_field(name="Member Count", value=context.guild.member_count)
    embed.add_field(name="Text/Voice Channels",
                    value=f"{len(context.guild.channels)}")
    embed.add_field(name=f"Roles ({len(context.guild.roles)})", value=roles)
    embed.set_footer(text=f"Created at: {context.guild.created_at}")
    await context.send(embed=embed)

  '''    # EXCLUIR
  @commands.hybrid_command(
    name="imagens",
    description="Envia imagem aleatória da obra em questão.",
  )
  @checks.not_blacklisted()
  async def imagens(self, context: Context) -> None:
    #arquivo = self.img_aleat
    arquivo = random.choice(glob.glob("imagens yotsu/*.png"))
    print(arquivo)
    f = discord.File(arquivo, filename=f"imagem_{arquivo[20:26]}.png")
    e = discord.Embed(color=0x3900f5)
    e.set_image(url=f"attachment://imagem_{arquivo[20:26]}.png")

    await context.send(embed=e, file=f)
    '''

  @commands.hybrid_command(
    name="img-pb",
    description="Envia imagem aleatória, por URL, da obra em questão.",
  )
  @checks.not_blacklisted()
  async def img_pb(self, context: Context) -> None:
  
    arquivo = "dados_outros/LINKS_perfe_blu.csv"

    with open(arquivo) as f:
      leitor = csv.reader(f)
      inicio = next(leitor)
      num_linhas = sum(1 for linhas in leitor)

    with open(arquivo) as f:
      leitor = csv.reader(f)
      num_aleat = random.randint(2, num_linhas - 1)
      for i in range(num_aleat):
        next(f)
      for linha in leitor:
        print(linha)
        break
      numero = linha[0]; link0 = linha[1]; link1 = linha[2]

    if link1 == "":
      este = link0
    else:
      este = link1
    
    embed = discord.Embed(title="", description="", color=0x6a7ae6)
    embed.set_image(url=este)
    embed.set_footer(text=f"imagem_{str(numero).zfill(6)}")
    await context.send(embed=embed)

  @commands.hybrid_command(
    name="img-chihiro",
    description="Envia imagem aleatória, por URL, da obra em questão.",
  )
  @checks.not_blacklisted()
  async def imagem(self, context: Context) -> None:
  
    arquivo = "dados_outros/LINKS_CHIHIRO.csv"

    with open(arquivo) as f:
      leitor = csv.reader(f)
      num_linhas = sum(1 for linhas in leitor)

    with open(arquivo) as f:
      leitor = csv.reader(f)
      num_aleat = random.randint(2, num_linhas - 1)
      for i in range(num_aleat):
        next(f)
      for linha in leitor:
        print(linha)
        break
      numero = linha[0]; link0 = linha[1]; link1 = linha[2]

    if link1 == "": este = link0
    else: este = link1
    
    embed = discord.Embed(title="", description="", color=0xfc2723)
    embed.set_image(url=este)
    embed.set_footer(text=f"imagem_{str(numero).zfill(6)}")
    await context.send(embed=embed)
  
  @commands.hybrid_command(
    name="img-nge",
    description="Envia imagem aleatória, por URL, da obra em questão.",
  )
  @checks.not_blacklisted()
  async def img(self, context: Context) -> None:
  
    arquivo = "dados_outros/LINKS_imagens_yotsu_2.csv"

    with open(arquivo) as f:
      leitor = csv.reader(f)
      inicio = next(leitor)
      num_linhas = sum(1 for linhas in leitor)

    with open(arquivo) as f:
      leitor = csv.reader(f)
      num_aleat = random.randint(2, num_linhas - 1)
      for i in range(num_aleat):
        next(f)
      for linha in leitor:
        print(linha)
        break
      numero = linha[0]; link0 = linha[1]; link1 = linha[2]

    if link1 == "":
      este = link0
    else:
      este = link1
    
    embed = discord.Embed(title="", description="", color=0x9200cb)
    embed.set_image(url=este)
    embed.set_footer(text=f"imagem_{str(numero).zfill(6)}")
    await context.send(embed=embed)
  
  @commands.hybrid_command(
    name="citando",
    description="Envia citação aleatória da obra em questão.",
  )
  @checks.not_blacklisted()
  async def citando(self, context: Context) -> None:
    arquivo = "dados_outros/NOVO_TEXTO.txt"
    
    def citar(arquivo):
      """Extrai um trecho de Grande Sertão: Veredas
      a partir de um caractere aleatório
      """
      with open(arquivo, encoding='utf-8', errors='ignore') as texto:
        leitor = texto.read()
        num_caract = len(leitor)    # Número de caracteres no arquivo
        num_aleat = random.randint(1, num_caract)

        cita = str()
        for letra in leitor[num_aleat: num_aleat + 500]:
          cita += letra

        return cita

    
    def contando_sinais(texto):
      """Conta os sinais ortográficos mais relevantes"""
      cont = 0
      sendo_eles = []
      for _ in trecho:
        if _ in sinais:
          cont += 1
          sendo_eles.append(_)
      
      return cont, sendo_eles

    
    def picotando(texto):
      """Reduzindo o trecho extraído para fazer a citação.
      """
      sinais_extract = contando_sinais(trecho)

      # Primeiro sinal ort. que não seja um ponto de interrogação.
      for i in range(len(sinais_extract[1])):
        if (sinais_extract[1][i] != '?') and (sinais_extract[1][-i] != '-'):
          escolha1 = (sinais_extract[1][i])
          break

      inicio_ = (texto.index(escolha1)); print(inicio_)

      # Último sinal ort. que não seja um ponto de interrogação.
      for i in range(1, len(sinais_extract[1])):
        if (sinais_extract[1][-i] != '?') and (sinais_extract[1][-i] != '-'):
          escolha2 = sinais_extract[1][-i]
          break

      # Texto ao contrário.
      otxet = texto[len(texto)::-1]

      final_1 = otxet.index(escolha2)

      finaleira = '"' + texto[inicio_+1:(len(texto) - final_1)] + '"'

      return finaleira
    
    trecho = citar(arquivo)
    sinais = ['.', '?', '-', '!', '...']

    resposta = "_"+picotando(trecho)+"_"

    embed = discord.Embed(title="", description=resposta, color=0xe31a10)
    await context.send(embed=embed)


  @commands.hybrid_command(
    name="ola_roborta",
    description="Envia uma saudação.",
  )
  @checks.not_blacklisted()
  async def oi(self, context: Context) -> None:
    resps = [".Olá", ".Oi", ".Salve", "Ei!"]
    embed = discord.Embed(title="", description=f"{random.choice(resps)}")
    await context.send(embed=embed)

  @commands.hybrid_command(
    name="ping",
    description="Checa o estado do robô.",
  )
  @checks.not_blacklisted()
  async def ping(self, context: Context) -> None:
    """
        Checa o estado do robô.
        
        :param context: The hybrid command context.
        """
    embed = discord.Embed(
      title="🏓 Pong!",
      description=f"A latência do robô é {round(self.bot.latency * 1000)}ms.",
      color=0x9C84EF)
    await context.send(embed=embed)

  @commands.hybrid_command(
    name="invite",
    description=
    "Obtenha o link de convite do robô e chame-o para outros servidores.",
  )
  @checks.not_blacklisted()
  async def invite(self, context: Context) -> None:
    """
        Obtenha o link de convite do robô e chame-o para outros servidores.
        
        :param context: The hybrid command context.
        """
    embed = discord.Embed(
      description=
      f"Convide-me clicando aqui (https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
      color=0xD75BF4)
    try:
      # Para saber quais permissões devem ser dadas a um robô, ver: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
      await context.author.send(embed=embed)
      await context.send("Enviei uma mensagem privada para você!")
    except discord.Forbidden:
      await context.send(embed=embed)

  @commands.hybrid_command(
    name="server",
    description="Convite para o servidor de suporte no discord.",
  )
  @checks.not_blacklisted()
  async def server(self, context: Context) -> None:
    """
        Convite para o servidor de suporte no discord.
        
        :param context: The hybrid command context.
        """
    embed = discord.Embed(
      description=
      f"Junte-se ao servidor de suporte para o robô clicando [aqui](https://discord.gg/mTBrXyWxAF).",
      color=0xD75BF4)
    try:
      await context.author.send(embed=embed)
      await context.send("Enviei uma mensagem privada para você!")
    except discord.Forbidden:
      await context.send(embed=embed)

  @commands.hybrid_command(
    name="8ball",
    description="Faça sua pergunta.",
  )
  @checks.not_blacklisted()
  @app_commands.describe(question="A questão que lhe intriga.")
  async def eight_ball(self, context: Context, *, question: str) -> None:
    """
        Ask any question to the bot.
        
        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
    answers = [
      ".Certamente", ".Pode contar com isso", ".Sem dúvidas",
      ".Sim - definitivamente", ".Por mim, sim", ".Provavelmente",
      ".Boas sensações sobre", ".Sim", ".Aparentemente, sim",
      ".Pergunta esquisita, tente novamente", ".Tente mais tarde",
      ".Melhor não dizer agora", ".Não posso prever agora",
      ".Não conte com isso", ".Digo que não", ".Minhas fontes dizem que não",
      ".Más sensações", ".Bastante duvidoso"
    ]
    embed = discord.Embed(title="**Minha resposta:**",
                          description=f"{random.choice(answers)}",
                          color=0x9C84EF)
    embed.set_footer(text=f"A pergunta foi: {question}")
    await context.send(embed=embed)

  '''@commands.hybrid_command(
    name="bitcoin",
    description="Preço atual do bitcoin.",
  )
  @checks.not_blacklisted()
  async def bitcoin(self, context: Context) -> None:
    """
        Preço atual do bitcoin.
        
        :param context: The hybrid command context.
        """
    # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
    async with aiohttp.ClientSession() as session:
      async with session.get(
          "https://api.coindesk.com/v1/bpi/currentprice/BTC.json") as request:
        if request.status == 200:
          data = await request.json(
            content_type="application/javascript"
          )  # For some reason the returned content is of type JavaScript
          embed = discord.Embed(
            title="Bitcoin: preço",
            description=
            f"O preço atual é {data['bpi']['USD']['rate']} :dollar:",
            color=0x9C84EF)
        else:
          embed = discord.Embed(
            title="Error!",
            description=
            "Algo errado com o API, tente novamente mais tarde.",
            color=0xE02B2B)
        await context.send(embed=embed)'''


async def setup(bot):
  await bot.add_cog(General(bot))
