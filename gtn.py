if message.content.startswith(",start"): #command to start quessing game
        channel = message.channel
        await channel.send("Guess the number from 0-100 by writing number in this channel!") #message that tells about the start of the game

        number1 = random.randint(1,1000) #picking random number from 1 - 100 and printing it
        print(number1)
        
        number2 = str(number1) #converting int to str

        def check(m):
            return m.content == number2 and m.channel == channel #checking answers
        channel = bot.get_channel(819973480686420028)
        overwrite = channel.overwrites_for(message.guild.default_role)
        msg = await bot.wait_for('message', check=check)
        embed = discord.Embed(title = "Guess the Number Ended !", description = 'Hey, <a:6486_doge:752422466386788363> Buddy you won. The Prize will be sent to your account!\n Keep Playing.', color = discord.Color.blue())
        embed.add_field(name="True Value", value = f'{number1}')
        embed.add_field(name="Winner is", value = "{.author}".format(msg), inline = False)
        embed.set_footer(text="Pass me spaghetti#6599", icon_url='https://cdn.discordapp.com/avatars/485489178583498764/ae9dfda1d2d424bec82e35c3838da754.webp?size=1024')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/723406157724647495/725065082949730414/Final_animated_logo.gif')
        overwrite.send_messages = False
        await channel.set_permissions(message.guild.default_role, overwrite=overwrite)
        await channel.send(embed=embed)
        await channel.send('Channel locked.')
