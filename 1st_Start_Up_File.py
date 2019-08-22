import pickle
story={
    'tutorial_Done' :  False ,
    'ep1_done' : False ,
    'ep2_done' : False ,
    'ep3_done' : False ,
    'ep4_done' : False ,
    'ep5_done' : False
}

with open('story.dat','wb') as a:
    pickle.dump(story,a,pickle.HIGHEST_PROTOCOL)

cor={
    'xcor' : 0,
    'ycor' : 0
}

with open('cor.dat','wb') as b:
    pickle.dump(cor,b,pickle.HIGHEST_PROTOCOL)


player_rank={
    'player_rank'          : "Ensign",
    'player_ensign'        : True,
    'player_sublieutenant' : False,
    'player_lieutenant'    : False,
    'player_subcommander'  : False,
    'player_commander'     : False,
    'player_captain'       : False,
    'player_aftcommodore'  : False,
    'player_forecommodore' : False,
    'player_vicecommodore' : False,
    'player_commodore'     : False,
    'player_aftadmiral'    : False,
    'player_foreadmiral'   : False,
    'player_viceadmiral'   : False,
    'player_admiral'       : False,
    'player_fleetadmiral'  : False,
    'player_armadaadmiral' : False
}
with open('player_rank.dat','wb') as c:
    pickle.dump(player_rank,c,pickle.HIGHEST_PROTOCOL)
player_level={
    'player_level_int':1,
    'player_level_str':"1",
    'player_exp_int':0,
    'player_exp_str':"0"
}
with open('player_level.dat','wb') as d:
    pickle.dump(player_level,d,pickle.HIGHEST_PROTOCOL)

player_credits={
    'player_credits_int' : 10000,
    'player_credits_str' : "‡ 10000"
}
with open('player_credits.dat','wb') as e:
    pickle.dump(player_credits,e,pickle.HIGHEST_PROTOCOL)

