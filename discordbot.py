import asyncio
import discord

# 自分のBotのアクセストークンに置き換えてください
token = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # よろしくの項目
    if message.content == 'よろしく':
        await message.channel.send('よろしくお願いいたします。')

    if message.content == '宜しく':
        await message.channel.send('よろしくお願いいたします')

    if message.content == 'よろしくお願いいたします':
        await message.channel.send('よろしくお願いいたします')      
    if message.content == '/ms help':
        embed=discord.Embed(title="Minecraft Survival　公式botのヘルプです",description="基本コマンドの説明", color=0x2ecc71) #これを常にする0x2ecc71
        embed.add_field(name="```/ms help```", value= "このBOTで使えるコマンド一覧を表示します", inline=True)
        embed.add_field(name="```/ms 参加方法```", value= "本サーバー（ワールド）に参加する方法を表示します", inline=True)
        embed.add_field(name="```/ms サーバー状態```", value= "サーバー（ワールド）の状態を表示します", inline=True)
        embed.add_field(name="```削除されました```", value= "削除されました", inline=True)
        embed.add_field(name="```削除されました```", value= "削除されました", inline=True)
        embed.add_field(name="作成中", value= "そのほか機能追加中", inline=True)
        await message.channel.send(embed=embed)
    if message.content == '/ms サーバー状態':
        embed=discord.Embed(title="/ms サーバー状態の実行結果です",description="実行結果", color=0xe67e22)  #起動の場合は0xe67e22これ停止：0xdc0909
        embed.add_field(name="```起動中```", value= "tomokura0514が起動", inline=True)
        await message.channel.send(embed=embed)
    if message.content == '/ms 参加方法':
        embed=discord.Embed(title="/ms 参加方法の実行結果です",description="実行結果", color=0xdc0909)  
        embed.add_field(name="```入力したコマンドは見つかりませんでした```", value= "削除された可能性があります", inline=True)
        await message.channel.send(embed=embed)



@client.event
async def on_ready():
    while True:

        await client.change_presence(activity=discord.Game(name="マイクラ統合版の公式botです"))
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(name="更新時間：2020/8/11/16:51"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name="ヘルプ表示/ms help"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name="目標:サーバー参加者100人"))
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game(name="製作者:とも"))
        await asyncio.sleep(5)


# Botの起動とDiscordサーバーへの接続
bot.run(token)
