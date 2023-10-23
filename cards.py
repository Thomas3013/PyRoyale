# GAME LOGIC / MECHANICS FOR EACH CARD IS YET TO BE WRITTEN
# troops, spells and buildings all use different vars
# target: 0 air ground & building !!  1 ground & building !! 2 building
# transport: 0 ground !! 1 air
hog_rider = {
    "name": "hog rider",
    "cost": 0,
    "hp": 1696,
    "dmg": 318,
    "splash": 0,
    "hit_speed": 1.6,
    "speed": 120,
    "deploy_time": 1,
    "range": 0.8,
    "target": 2,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (106, 36, 6)
}

ice_spirit = {
    "name": "ice spirit",
    "cost": 0,
    "hp": 230,
    "dmg": 318,
    "splash": 1.5,
    "hit_speed": 0.3,
    "speed": 120,
    "deploy_time": 1,
    "range": 2.5,
    "target": 0,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "suicide",
    "cc": "slow",
    "colors": (255, 255, 255)
}

musketeer = {
    "name": "musketeer",
    "cost": 0,
    "hp": 720,
    "dmg": 218,
    "splash": 0,
    "hit_speed": 1,
    "speed": 60,
    "deploy_time": 1,
    "range": 6,
    "target": 0,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

ice_golem = {
    "name": "ice golem",
    "cost": 0,
    "hp": 1197,
    "dmg": 84,
    "splash": 0,
    "hit_speed": 2.5,
    "speed": 45,
    "deploy_time": 1,
    "range": 0.75,
    "target": 2,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "slow on death",
    "cc": "none",
    "colors": (255, 255, 255)
}

skeletons = {
    "name": "skeletons",
    "cost": 0,
    "hp": 81,
    "dmg": 81,
    "splash": 0,
    "hit_speed": 1,
    "speed": 90,
    "deploy_time": 1,
    "range": 0.5,
    "target": 1,
    "count": 3,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

cannon = {
    "name": "cannon",
    "cost": 3,
    "hp": 824,
    "dmg": 212,
    "splash": 0,
    "hit_speed": 0.9,
    "lifetime": 30,
    "deploy_time": 1,
    "range": 5.5,
    "target": 1,
    "height": 10,
    "width": 10,
    "ability": "none",
    "colors": (255, 255, 255)
}

log = {
    "name": "the log",
    "cost": 2,
    "dmg": 290,
    "tower_dmg": 58,
    "speed": 200,
    "range": 10.1,
    "target": 1,
    "transport": 0,
    "height": 10,
    "width": 10,
    "kb": 12,
    "ability": "none",
    "dmg_counter": 1,
    "duration": 100,  # kill after x tiles moved
    "colors": (255, 255, 255)
}

fireball = {
    "name": "fireball",
    "cost": 4,
    "dmg": 689,
    "tower_dmg": 206,
    "speed": 0,
    "range": 2.5,
    "target": 0,
    "transport": 1,
    "height": 8,
    "width": 8,
    "kb": 12,
    "ability": "none",
    "dmg_counter": 1,
    "duration": 0.1,
    "colors": (255, 255, 255)
}

bandit = {
    "name": "bandit",
    "cost": 0,
    "hp": 907,
    "dmg": 193,
    "splash": 0,
    "hit_speed": 1,
    "speed": 90,
    "deploy_time": 1,
    "range": 0.75,
    "target": 1,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "bandit dash",
    "cc": "none",
    "colors": (255, 255, 255)
}

royal_ghost = {
    "name": "royal ghost",
    "cost": 0,
    "hp": 1210,
    "dmg": 261,
    "splash": 1,
    "hit_speed": 1.8,
    "speed": 90,
    "deploy_time": 1,
    "range": 1.2,
    "target": 1,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "invis",
    "cc": "none",
    "colors": (255, 255, 255)
}

minions = {
    "name": "minions",
    "cost": 0,
    "hp": 230,
    "dmg": 117,
    "splash": 0,
    "hit_speed": 1,
    "speed": 90,
    "deploy_time": 1,
    "range": 1.6,
    "target": 0,
    "count": 3,
    "transport": 1,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

pekka = {
    "name": "pekka",
    "cost": 0,
    "hp": 3760,
    "dmg": 816,
    "splash": 0,
    "hit_speed": 1.8,
    "speed": 45,
    "deploy_time": 1,
    "range": 1.2,
    "target": 1,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

poison = {
    "name": "poison",
    "cost": 4,
    "dmg": 91,  # hits 8 times
    "tower_dmg": 27,
    "speed": 0,
    "range": 3.5,
    "target": 0,
    "transport": 1,
    "height": 8,
    "width": 8,
    "kb": 0,
    "ability": "none",
    "dmg_counter": 8,
    "duration": 8,
    "colors": (255, 255, 255)
}

zap = {
    "name": "zap",
    "cost": 0,
    "dmg": 192,
    "tower_dmg": 57,
    "speed": 0,
    "range": 2.5,
    "target": 0,
    "transport": 1,
    "height": 8,
    "width": 8,
    "kb": 0,
    "ability": "zap",
    "dmg_counter": 1,
    "duration": 0.1,
    "colors": (255, 255, 255)
}

ewiz = {
    "name": "electro wizard",
    "cost": 0,
    "hp": 713,
    "dmg": 110,  # hits 2x
    "splash": 0,
    "hit_speed": 1.8,
    "speed": 90,
    "deploy_time": 1,
    "range": 5,
    "target": 0,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "zap",
    "cc": "zap",
    "colors": (255, 255, 255)
}

battle_ram = {
    "name": "battle ram",
    "cost": 0,
    "hp": 966,
    "dmg": 286,
    "splash": 0,
    "hit_speed": 1,
    "speed": 60,  # 120 when charging
    "deploy_time": 1,
    "range": 0.7,
    "target": 2,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "charge",
    "cc": "none",
    "colors": (255, 255, 255)
}

goblin_barrel = {
    "name": "goblin barrel",
    "cost": 0,
    "dmg": 0,
    "tower_dmg": 0,
    "speed": 0,
    "range": 1.5,
    "target": 0,
    "transport": 1,
    "height": 8,
    "width": 8,
    "kb": 0,
    "ability": "spawn 3 goblins",
    "dmg_counter": 1,
    "duration": 0.1,
    "colors": (255, 255, 255)
}

goblin_gang = {
    "name": "goblin gang",
    "cost": 0,
    "hp": 202,
    "dmg": 120,
    "splash": 0,
    "hit_speed": 1.1,
    "speed": 120,
    "deploy_time": 1,
    "range": 0.5,
    "target": 1,
    "count": 3,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "spawn 3x gang behind on spawn",
    "cc": "none",
    "colors": (255, 255, 255)
}

inferno_tower = {
    "name": "inferno tower",
    "cost": 0,
    "hp": 1749,
    "dmg": 42,
    "splash": 0,
    "hit_speed": 0.4,
    "lifetime": 30,
    "deploy_time": 1,
    "range": 6,
    "target": 0,
    "height": 8,
    "width": 8,
    "ability": "inferno dmg",
    "colors": (255, 255, 255)
}

knight = {
    "name": "knight",
    "cost": 0,
    "hp": 1607,
    "dmg": 202,
    "splash": 0,
    "hit_speed": 1.2,
    "speed": 60,
    "deploy_time": 1,
    "range": 1.2,
    "target": 1,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

princess = {
    "name": "princess",
    "cost": 0,
    "hp": 261,
    "dmg": 169,
    "splash": 1,
    "hit_speed": 3,
    "speed": 60,
    "deploy_time": 1,
    "range": 9,
    "target": 0,
    "count": 1,
    "transport": 0,
    "height": 8,
    "width": 8,
    "ability": "none",
    "cc": "none",
    "colors": (255, 255, 255)
}

rocket = {
    "name": "rocket",
    "cost": 6,
    "dmg": 1484,
    "tower_dmg": 371,
    "speed": 0,
    "range": 2,
    "target": 0,
    "transport": 1,
    "height": 8,
    "width": 8,
    "kb": 1,
    "ability": "none",
    "dmg_counter": 1,
    "duration": 0.1,
    "colors": (255, 255, 255)
}

unit = {
        "unit::hog_rider": hog_rider,
        "unit::ice_spirit": ice_spirit,
        "unit::musketeer": musketeer,
        "unit::ice_golem": ice_golem,
        "unit::skeletons": skeletons,
        "unit::bandit": bandit,
        "unit::royal_ghost": royal_ghost,
        "unit::minions": minions,
        "unit::pekka": pekka,
        "unit::ewiz": ewiz,
        "unit::battle_ram": battle_ram,
        "unit::goblin_gang": goblin_gang,
        "unit::knight": knight,
        "unit::princess": princess,
    }
