import discord
import os

client = discord.Client()


@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('소우야 도움말')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
        if message.content == "!핑":
            await message.channel.send("퐁!")

        if message.content == "소우야 도움말":
                embed = discord.Embed(title="도움말", description="---", color=0x00ff00)
                embed.add_field(name="도움 명령어: ", value="소우야 도움말",inline=False)
                embed.add_field(name="투표 명령어: ", value="s/투표 투표이름,투표내용,투표내용",inline=True)
                embed.add_field(name="청소 명령어: ", value="s/청소 (숫자)",inline=True)
                embed.add_field(name="초대: ", value="https://discord.com/api/oauth2/authorize?client_id=957257449285484604&permissions=0&scope=bot",inline=False)
                embed.set_footer(text="수정일 : 21/07/10")
                await message.channel.send(embed=embed)



        if message.content.startswith("s/투표"):
            vote = message.content[4:].split(",")
            await message.channel.send("투표 - " + vote[0])
            for i in range(1, len(vote)):
                choose = await message.channel.send("```" + vote[i] + "```")
                await choose.add_reaction('👍')
        

        if message.content == "소우야":
            await message.channel.send("네!")

        if message.content == "소우야!":
            await message.channel.send("네!")

        if message.content == "소우야?":
            await message.channel.send("네!")

        if message.content == "소우야 안녕":
            await message.channel.send(f"{message.author.mention}님, 하위!")

        if message.content == "소우야 안녕!":
            await message.channel.send(f"{message.author.mention}님, 하위!")

        if message.content == "소우야 안녕?":
            await message.channel.send(f"{message.author.mention}님, 하위!")

        if message.content == "소우야 사랑해":
            await message.channel.send("저도 사랑해요:heart:")

        if message.content == "소우야 사랑해!":
            await message.channel.send("저도 사랑해요:heart:")

        if message.content == "소우야 더워":
            await message.channel.send("저두 더워용ㅠㅠ")

        if message.content == "소우야 사랑해":
            await message.channel.send("저도 사랑해요:heart:")

        if message.content == "소우야 떡볶이":
            await message.channel.send("전 떡볶이 좋아해용!")

        if message.content == "소우야 똥":
            await message.channel.send("||뿌직||")

        if message.content == "소우야 뿌직":
            await message.channel.send("||똥||")

        if message.content == "소우야 좋아하는사람 있어?":
            await message.channel.send("음...전 당신을 좋아해요!")

        if message.content == "소우야 좋아 하는사람 있어?":
            await message.channel.send("음...전 당신을 좋아해요!")

        if message.content == "소우야 좋아 하는 사람 있어?":
            await message.channel.send("음...전 당신을 좋아해요!")

        if message.content == "소우야 좋아하는 사람 있어?":
            await message.channel.send("음...전 당신을 좋아해요!")

        if message.content == "소우야 해피 할로윈":
            await message.channel.send("오늘이 할로윈 인가요??")

        if message.content == "소우야 해피할로윈":
            await message.channel.send("오늘이 할로윈 인가요??")

        if message.content == "소우야 할로윈":
            await message.channel.send("오늘이 할로윈 인가요??")

        if message.content == "소우야 해피 크리스마스":
            await message.channel.send("오늘이 크리스마스 인가요??")

        if message.content == "소우야 해피크리스마스":
            await message.channel.send("오늘이 크리스마스 인가요??")

        if message.content == "소우야 크리스마스":
            await message.channel.send("오늘이 크리스마스 인가요??")

        if message.content == "소우야 새벽":
            await message.channel.send("무시무시 깜깜한 새벽..!!")

        if message.content == "소우야 아싸":
            await message.channel.send(f"{message.author.mention}님과 저는 아싸가 아니죠!")

        if message.content == "소우야 인싸":
            await message.channel.send(f"{message.author.mention}님과 저는 인싸죠!!")

        if message.content == "소우야 찐따":
            await message.channel.send("??")

        if message.content == "소우야 바부":
            await message.channel.send("나 바부 아닌데..ㅠ")

        if message.content == "소우야 바보":
            await message.channel.send("나 바보 아닌데..ㅠ")

        if message.content == "소우야 펭꾸 유튜브":
            await message.channel.send("펭바꾸보!!")

        if message.content == "소우야 펭꾸유튜브":
            await message.channel.send("펭바꾸보!!")

        if message.content == "소우야 김펭꾸":
            await message.channel.send("펭바꾸보!!")

        if message.content == "소우야 김펭꾸 유튜브":
            await message.channel.send("펭바꾸보!!")

        if message.content == "소우야 김펭꾸유튜브":
            await message.channel.send("펭바꾸보!!")

        if message.content == "소우야 김원토":
            await message.channel.send("귀요미 원토~")

        if message.content == "소우야 김원토 유튜브":
            await message.channel.send("귀요미 원토~")

        if message.content == "소우야 김원토유튜브":
            await message.channel.send("귀요미 원토~")

        if message.content == "소우야 원토 유튜브":
            await message.channel.send("귀요미 원토~")

        if message.content == "소우야 원토유튜브":
            await message.channel.send("귀요미 원토~")

        if message.content == "소우야 원토":
            await message.channel.send("귀요미 원토~")
            
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
