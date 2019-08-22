import pickle
with open('player_level.dat','rb') as a:
    player_level=pickle.load(a)

with open('player_rank.dat','rb') as b:
    player_rank=pickle.load(b)

with open('cor.dat','rb') as c:
    player_cor=pickle.load(c)

with open('player_credits.dat','rb') as d:
    player_credits=pickle.load(d)

levels_exp={
    'L2'  : 1000000    ,
    'L3'  : 2000000    ,
    'L4'  : 4000000    ,
    'L5'  : 8000000    ,
    'L6'  : 16000000   ,
    'L7'  : 32000000   ,
    'L8'  : 64000000   ,
    'L9'  : 128000000  ,
    'L10' : 256000000  ,
    'L11' : 512000000  ,
    'L12' : 1024000000 ,
    'L13' : 2048000000 ,
    'L14' : 4096000000 ,
    'L15' : 8192000000
}

