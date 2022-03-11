import hikari
import lightbulb
import random

bot = lightbulb.BotApp(token='OTUxNzQ5MTI1NzM5Nzg2MzIw.Yir_cg.GUzGJP3q7hqsZul2Q068nWaFlFg', default_enabled_guilds=(489087224718032917))

#among us cock
@bot.command
@lightbulb.command('amoguscock', 'Among us Cock Text')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    await ctx.respond('⠀⠀‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎ ‎‎‎‎‎⠀⣠⣤⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⢰⡿⠋⠁⠀⠀⠈⠉⠙⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢀⣿⠇⠀⢀⣴⣶⡾⠿⠿⠿⢿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⣀⣀⣸⡿⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⣾⡟⠛⣿⡇⠀⠀⢸⣿⣿⣷⣤⣤⣤⣤⣶⣶⣿⠇⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀ ⢀⣿⠀⢀⣿⡇⠀⠀⠀⠻⢿⣿⣿⣿⣿⣿⠿⣿⡏⠀⠀⠀⠀⢴⣶⣶⣿⣿⣿⣆ ⢸⣿⠀⢸⣿⡇⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⣿⡇⣀⣠⣴⣾⣮⣝⠿⠿⠿⣻⡟ ⢸⣿⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠉⠀ ⠸⣿⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⠀⠀⠀⠀ ⠀⠻⣷⣶⣿⣇⠀⠀⠀⢠⣼⣿⣿⣿⣿⣿⣿⣿⣛⣛⣻⠉⠁⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⢸⣿⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀ ⠀⠀ ⠀⠀⠀⠀⢸⣿⣀⣀⣀⣼⡿⢿⣿⣿⣿⣿⣿⡿⣿⣿⡿⠀')


taopic_dict = {'cube': 'https://tao-archive.tumblr.com/post/678426687953895425/tao-cube',
                'pokerface': 'https://tao-archive.tumblr.com/post/678430032390209536/tao-pokerface',
               'carrot': 'https://tao-archive.tumblr.com/post/678430054228836352/tao-carrot',
               'hee': 'https://tao-archive.tumblr.com/post/678430075707899904/tao-hee',
                'ass': 'https://tao-archive.tumblr.com/post/678430267944419328/tao-ass',
                'tagieb': 'https://tao-archive.tumblr.com/post/678430317140492288/tao-tagieb',
               'thangmapraow': 'https://tao-archive.tumblr.com/post/678430355026542592/tao-thangmapraow',
               'stealhislook': 'https://tao-archive.tumblr.com/post/678430377841410048/tao-stealhislook',
               'dababy': 'https://tao-archive.tumblr.com/post/678430399629819904/tao-dababy',
               'sleep': 'https://tao-archive.tumblr.com/post/678430433435942912/tao-sleep',
               'phone': 'https://tao-archive.tumblr.com/post/678430455486447616/tao-phone',
               'aggressive': 'https://tao-archive.tumblr.com/post/678430476254445568/tao-aggressive',
               'picasso': 'https://tao-archive.tumblr.com/post/678430494942232576/tao-picasso',
               'demon': 'https://tao-archive.tumblr.com/post/678430515758530560/tao-demon',
                'cry': 'https://tao-archive.tumblr.com/post/678430534294257664/tao-cry',
               'cumjar': 'https://tao-archive.tumblr.com/post/678430557891379200/tao-cumjar',
               'wuhan': 'https://tao-archive.tumblr.com/post/678430578819973120/tao-wuhan',
               'melon': 'https://tao-archive.tumblr.com/post/678430601141977088/tao-melon',
               'cubeclassic': 'https://tao-archive.tumblr.com/post/678430626325610496/tao-cube-classic',
               'chocomilk': 'https://tao-archive.tumblr.com/post/678430648833310720/tao-chocomilk',
               'taxevasion': 'https://tao-archive.tumblr.com/post/678430677070479360/tao-tax-evasion',
               'wildrift': 'https://tao-archive.tumblr.com/post/678430706706399232/tao-wildrift',
               'dababy2': 'https://tao-archive.tumblr.com/post/678430734664515584/tao-dababy-2',
               'thug': 'https://tao-archive.tumblr.com/post/678431069222125569/tao-thug',
               }
taovid_dict = {'edm': 'https://tao-archive.tumblr.com/post/678426864703930368/tao-powpow',
                'boom': 'https://tao-archive.tumblr.com/post/678427068494708736/tao-boom',
               'nomorefortnite': 'https://tao-archive.tumblr.com/post/678427124862992384/tao-no-more-fortnite',
                'onetao': 'https://tao-archive.tumblr.com/post/678427227875098624/one-tao',
               'flip': 'https://tao-archive.tumblr.com/post/678430136222318592/tao-flip',
               'lore': 'https://tao-archive.tumblr.com/post/678430223152431104/tao-lore',
               'hotmilk': 'https://tao-archive.tumblr.com/post/678430817816543232/tao-hotmilk',
                'averagevsenjoyer': 'https://tao-archive.tumblr.com/post/678430925615431680/tao-average-vs-enjoyer',
               'aggressive 2': 'https://tao-archive.tumblr.com/post/678431011343925249/tao-aggressive-2',
                'damedane': 'https://tao-archive.tumblr.com/post/678431079308328960/tao-damedane',
               'okipullup': 'https://tao-archive.tumblr.com/post/678431160616075264/tao-ok-i-pull-up',
               'tumjai': 'https://tao-archive.tumblr.com/post/678431221446049792/tao-tumjai',
               '3d': 'https://tao-archive.tumblr.com/post/678431314108727296/tao-3d',
               'pvz': 'https://tao-archive.tumblr.com/post/678431380584136704/tao-pvz',
               'nomorefortnitex2': 'https://tao-archive.tumblr.com/post/678431433802530816/tao-no-more-fortnite-2x',
               'powpowx2': 'https://tao-archive.tumblr.com/post/678431517575430144/tao-pow-edm-2x',
               'snicker': 'https://tao-archive.tumblr.com/post/678431611315945472/tao-snicker'
               }
FB_pic = {'1': 'https://tao-archive.tumblr.com/post/678429545735553024/fb-1',
          '2': 'https://tao-archive.tumblr.com/post/678429579755520000/fb-2',
          '3': 'https://tao-archive.tumblr.com/post/678429618491031552/fb-3',
          '4': 'https://tao-archive.tumblr.com/post/678429647489400832/fb-4',
          '5': 'https://tao-archive.tumblr.com/post/678429675133992960/fb-5',
          '6': 'https://tao-archive.tumblr.com/post/678429700688887808/fb-6',
          '7': 'https://tao-archive.tumblr.com/post/678429724345843712/fb-7',
          '8': 'https://tao-archive.tumblr.com/post/678429757992550400/fb-8',
          '9': 'https://tao-archive.tumblr.com/post/678429780108099584/fb-9',
          '10': 'https://tao-archive.tumblr.com/post/678429802958569472/fb-10',
          '11': 'https://tao-archive.tumblr.com/post/678429831048888320/fb-11',
          '12': 'https://tao-archive.tumblr.com/post/678429859217866752/fb-12',
          '13': 'https://tao-archive.tumblr.com/post/678429892136861696/fb-13',
          '14': 'https://tao-archive.tumblr.com/post/678429923502850048/fb-14',
          '15': 'https://tao-archive.tumblr.com/post/678429950290837504/fb-15',
          '16': 'https://tao-archive.tumblr.com/post/678429973056471040/fb-16'
}
non_tao = {'egam': 'https://tao-archive.tumblr.com/post/678430291138953216/rak-egam',
           'rakspeedforce': 'https://tao-archive.tumblr.com/post/678429548854001664/rak-speedforce'
           }

def mergedict(taopic_dict, taovid_dict, FB_pic, non_tao):
    res = {**taopic_dict, **taovid_dict, **FB_pic, **non_tao}
    return res

merged = mergedict(taopic_dict, taovid_dict, FB_pic, non_tao)



#random
@bot.command
@lightbulb.command('random', 'Random meme pic and vid')
@lightbulb.implements(lightbulb.SlashCommand)
async def memerand(ctx):
    key, value = random.choice(list(merged.items()))
    await ctx.respond(value)


#tao pic group
@bot.command
@lightbulb.command('taopic', 'Tao pics command group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def taopic(ctx):
    pass
'''
keyList=sorted(taopic_dict.keys())
for x, v in enumerate(keyList):
    @taopic.child
    @lightbulb.command(v, v)
    @lightbulb.implements(lightbulb.SlashSubCommand)
    async def funcpic(ctx):
        await ctx.respond(taopic_dict[v])
        if x==0:
            globals()[x+1] = funcpic
    if x>1:
        globals()[x] = x-1
'''


#cube
@taopic.child
@lightbulb.command('cube', 'cube')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cube(ctx):
    await ctx.respond(taopic_dict['cube'])

#pokerface
@taopic.child
@lightbulb.command('pokerface', 'pokerface')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def pokerface(ctx):
    await ctx.respond(taopic_dict['pokerface'])


#tao vid group
@bot.command
@lightbulb.command('taovid', 'Tao videos command group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def taovid(ctx):
    pass

@taovid.child
@lightbulb.command('edm', 'Tao Pow Pow Edm')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def edm(ctx):
    await ctx.respond(taovid_dict['edm'])

@taovid.child
@lightbulb.command('boom', 'Tao boom vine')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def boom(ctx):
    await ctx.respond(taovid_dict['boom'])

@taovid.child
@lightbulb.command('nomorefortnite', 'Tao no more fortnite')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def nomorefortnite(ctx):
    await ctx.respond(taovid_dict['nomorefortnite'])

@taovid.child
@lightbulb.command('onetao', 'Tao one tao')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def onetao(ctx):
    await ctx.respond(taovid_dict['onetao'])

bot.run()

