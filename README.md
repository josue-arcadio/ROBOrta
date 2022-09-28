# ROBOrta

assim:

        embed.set_footer(
            text=f"Created at: {context.guild.created_at}"
        )
        await context.send(embed=embed)
   
    @comands.hybrid_command(
      name="Imagens",
      description="Envia imagem aleatória da obra em questão.",
    )
    @check.not_blacklisted()
    async def imagens(self, context: Context) -> None:
      prefix = self.bot.config("prefix")
      embed = discord.Embed(title="NGE", img_aleat= random.choice(glob.glob("imagens yotsu/*.jpg")), description=img_aleat))
      await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
