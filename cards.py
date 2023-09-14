# v BELOW IS ALL CARDS IN PEKKA BRIDGESPAM AND HOG 2.6 v
# GAME LOGIC / MECHANICS FOR EACH CARD IS YET TO BE WRITTEN
# troops, spells and buildings all use different vars
# target: 0 air ground & building !!  1 ground & building !! 2 building
# transport: 0 ground !! 1 air
hog_rider = {
    "cost" : 4,
    "hp" : 1696,
    "dmg" : 318,
    "splash" : 0,
    "hit_speed": 1.6,
    "speed" : 120,
    "deploy_time": 1,
    "range" : 0.8,
    "target" : 2,
    "count" : 1,
    "transport" : 0,
    "height" : 60,
    "width" : 36,
    "colors" : (106,36,6)
}
ice_spirit = {
    "cost" : 1,
    "hp" : 230,
    "dmg" : 318,
    "splash" : 1.5,
    "hit_speed": 0.3,
    "speed" : 120,
    "deploy_time": 1,
    "range" : 2.5,
    "target" : 0,
    "count" : 1,
    "transport" : 0,
    "height" : 24,
    "width" : 24,
    "colors" : (255,255,255)
}
musketeer = {
    "cost" : 4,
    "hp" : 720,
    "dmg" : 218,
    "splash" : 0,
    "hit_speed": 1,
    "speed" : 60,
    "deploy_time": 1,
    "range" : 6,
    "target" : 0,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 24,
    "colors" : (255,255,255)
}
ice_golem = {
    "cost" : 2,
    "hp" : 1197,
    "dmg" : 84,
    "splash" : 0,
    "hit_speed": 2.5,
    "speed" : 45,
    "deploy_time": 1,
    "range" : 0.75,
    "target" : 2,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 48,
    "colors" : (255,255,255)
}
skeletons = {
    "cost" : 1,
    "hp" : 81,
    "dmg" : 81,
    "splash" : 0,
    "hit_speed": 1,
    "speed" : 90,
    "deploy_time": 1,
    "range" : 0.5,
    "target" : 1,
    "count" : 3,
    "transport" : 0,
    "height" : 24,
    "width" : 24,
    "colors" : (255,255,255)
}
cannon = {
    "cost" : 3,
    "hp" : 824,
    "dmg" : 212,
    "splash" : 0,
    "hit_speed": 0.9,
    "lifetime" : 30,
    "deploy_time": 1,
    "range" : 5.5,
    "target" : 1,
    "height" : 48,
    "width" : 48,
    "colors" : (255,255,255)
}
log = {
    "cost" : 2,
    "dmg" : 290,
    "tower_dmg" : 58,
    "speed" : 200,
    "range" : 10.1,
    "target" : 1,
    "transport" : 0,
    "height" : 24,
    "width" : 72,
    "colors" : (255,255,255)
}
fireball = {
    "cost" : 4,
    "dmg" : 689,
    "tower_dmg" : 206,
    "speed" : 0,
    "range" : 2.5,
    "target" : 0,
    "transport" : 1,
    "height" : 96,
    "width" : 96,
    "colors" : (255,255,255)
}
bandit = {
    "cost" : 3,
    "hp" : 907,
    "dmg" : 193,
    "splash" : 0,
    "hit_speed": 1,
    "speed" : 90,
    "deploy_time": 1,
    "range" : 0.75,
    "target" : 1,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 24,
    "colors" : (255,255,255)
}
royal_ghost = {
    "cost" : 3,
    "hp" : 1210,
    "dmg" : 261,
    "splash" : 1,
    "hit_speed": 1.8,
    "speed" : 90,
    "deploy_time": 1,
    "range" : 1.2,
    "target" : 1,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 24,
    "colors" : (255,255,255)
}
minions = {
    "cost" : 3,
    "hp" : 230,
    "dmg" : 117,
    "splash" : 0,
    "hit_speed": 1,
    "speed" : 90,
    "deploy_time": 1,
    "range" : 1.6,
    "target" : 0,
    "count" : 3,
    "transport" : 1,
    "height" : 24,
    "width" : 24,
    "colors" : (255,255,255)
}
pekka = {
    "cost" : 7,
    "hp" : 3760,
    "dmg" : 816,
    "splash" : 0,
    "hit_speed": 1.8,
    "speed" : 45,
    "deploy_time": 1,
    "range" : 1.2,
    "target" : 1,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 96,
    "colors" : (255,255,255)
}
poison = {
    "cost" : 4,
    "dmg" : 91, # hits 8 times
    "tower_dmg" : 27,
    "speed" : 0,
    "range" : 3.5,
    "target" : 0,
    "transport" : 1,
    "height" : 168,
    "width" : 168,
    "colors" : (255,255,255)
}
zap = {
    "cost" : 2,
    "dmg" : 192,
    "tower_dmg" : 57,
    "speed" : 0,
    "range" : 2.5,
    "target" : 0,
    "transport" : 1,
    "height" : 120,
    "width" : 120,
    "colors" : (255,255,255)
}
ewiz = {
    "cost" : 4,
    "hp" : 713,
    "dmg" : 110, #hits 2x
    "splash" : 0,
    "hit_speed": 1.8,
    "speed" : 90,
    "deploy_time": 1,
    "range" : 5,
    "target" : 0,
    "count" : 1,
    "transport" : 0,
    "height" : 48,
    "width" : 24,
    "colors" : (255,255,255)
}
battle_ram = {
    "cost" : 4,
    "hp" : 966,
    "dmg" : 286, #hits 2x
    "splash" : 0,
    "hit_speed": 1, # hit speed is not given on wiki
    "speed" : 60, # 120 when charging
    "deploy_time": 1,
    "range" : 0.7,
    "target" : 2,
    "count" : 1,
    "transport" : 0,
    "height" : 72,
    "width" : 48,
    "colors" : (255,255,255)
}
