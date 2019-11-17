import sys

all_dual_techs = [
{
	'name': 'AuraWhirl',
	'prereqs': ['Cyclone', 'Aura'],
	'characters': ['Chrono', 'Marle']
},
{
	'name': 'IceSword',
	'prereqs': ['Spincut', 'Ice'],
	'characters': ['Chrono', 'Marle']
},
{
	'name': 'IceSword2',
	'prereqs': ['Confuse', 'Ice2'],
	'characters': ['Chrono', 'Marle']
},
{
	'name': 'FireWhirl',
	'prereqs': ['Cyclone', 'Flamethrower'],
	'characters': ['Chrono', 'Lucca']
},
{
	'name': 'FireSword',
	'prereqs': ['Spincut', 'Fire'],
	'characters': ['Chrono', 'Lucca']
},
{
	'name': 'FireSword2',
	'prereqs': ['Confuse', 'Fire2'],
	'characters': ['Chrono', 'Lucca']
},
{
	'name': 'RocketRoll',
	'prereqs': ['Cyclone', 'LaserSpin'],
	'characters': ['Chrono', 'Robo']
},
{
	'name': 'MaxCyclone',
	'prereqs': ['Spincut', 'LaserSpin'],
	'characters': ['Chrono', 'Robo']
},
{
	'name': 'SuperVolt',
	'prereqs': ['Lightning2', 'Shock'],
	'characters': ['Chrono', 'Robo']
},
{
	'name': 'X-Strike',
	'prereqs': ['Cyclone', 'SlurpCut'],
	'characters': ['Chrono', 'Frog']
},
{
	'name': 'SwordStream',
	'prereqs': ['Spincut', 'Water'],
	'characters': ['Chrono', 'Frog']
},
{
	'name': 'Spire',
	'prereqs': ['Lightning2', 'LeapSlash'],
	'characters': ['Chrono', 'Frog']
},
{
	'name': 'DrillKick',
	'prereqs': ['Cyclone', 'RolloKick'],
	'characters': ['Chrono', 'Ayla']
},
{
	'name': 'Volt Bite',
	'prereqs': ['Lightning', 'CatAttack'],
	'characters': ['Chrono', 'Ayla']
},
{
	'name': 'FalconHit',
	'prereqs': ['Spincut', 'RockThrow'],
	'characters': ['Chrono', 'Ayla']
},
{
	'name': 'Antipode',
	'prereqs': ['Ice', 'Fire'],
	'characters': ['Marle', 'Lucca']
},
{
	'name': 'Antipode2',
	'prereqs': ['Ice2', 'Fire2'],
	'characters': ['Marle', 'Lucca']
},
{
	'name': 'Antipode3',
	'prereqs': ['Ice2', 'Flare'],
	'characters': ['Marle', 'Lucca']
},
{
	'name': 'AuraBeam',
	'prereqs': ['Ice', 'CureBeam'],
	'characters': ['Marle', 'Robo']
},
{
	'name': 'IceTackle',
	'prereqs': ['Ice', 'RoboTackle'],
	'characters': ['Marle', 'Robo']
},
{
	'name': 'CureTouch',
	'prereqs': ['Cure2', 'HealBeam'],
	'characters': ['Marle', 'Robo']
},
{
	'name': 'IceWater',
	'prereqs': ['Ice', 'Water'],
	'characters': ['Marle', 'Frog']
},
{
	'name': 'Glacier',
	'prereqs': ['Ice2', 'Water2'],
	'characters': ['Marle', 'Frog']
},
{
	'name': 'Double Cure',
	'prereqs': ['Cure2', 'Cure2F'],
	'characters': ['Marle', 'Frog']
},
{
	'name': 'TwinCharm',
	'prereqs': ['Provoke', 'Charm'],
	'characters': ['Marle', 'Ayla']
},
{
	'name': 'IceToss',
	'prereqs': ['Ice', 'RockThrow'],
	'characters': ['Marle', 'Ayla']
},
{
	'name': 'CubeToss',
	'prereqs': ['Ice2', 'RockThrow'],
	'characters': ['Marle', 'Ayla']
},
{
	'name': 'FirePunch',
	'prereqs': ['Fire', 'RocketPunch'],
	'characters': ['Lucca', 'Robo']
},
{
	'name': 'FireTackle',
	'prereqs': ['Fire 2', 'RoboTackle'],
	'characters': ['Lucca', 'Robo']
},
{
	'name': 'DoublevBomb',
	'prereqs': ['MegaBomb', 'AreaBomb'],
	'characters': ['Lucca', 'Robo']
},
{
	'name': 'RedPin',
	'prereqs': ['Fire', 'LeapSlash'],
	'characters': ['Lucca', 'Frog']
},
{
	'name': 'LineBomb',
	'prereqs': ['MegaBomb', 'LeapSlash'],
	'characters': ['Lucca', 'Frog']
},
{
	'name': 'FrogFlare',
	'prereqs': ['Flare', 'FrogSquash'],
	'characters': ['Lucca', 'Frog']
},
{
	'name': 'FlameKick',
	'prereqs': ['Fire', 'RolloKick'],
	'characters': ['Lucca', 'Ayla']
},
{
	'name': 'FlameWhirl',
	'prereqs': ['Fire2', 'TailSpin'],
	'characters': ['Lucca', 'Ayla']
},
{
	'name': 'BlazeKick',
	'prereqs': ['Fire2', 'TripleKick'],
	'characters': ['Lucca', 'Ayla']
},
{
	'name': 'BladeToss',
	'prereqs': ['LaserSpin', 'SlurpCut'],
	'characters': ['Robo', 'Frog']
},
{
	'name': 'BubbleSnap',
	'prereqs': ['RoboTackle', 'Water'],
	'characters': ['Robo', 'Frog']
},
{
	'name': 'CureWave',
	'prereqs': ['HealBeam', 'Cure2F'],
	'characters': ['Robo', 'Frog']
},
{
	'name': 'Boogie',
	'prereqs': ['RoboTackle', 'Charm'],
	'characters': ['Robo', 'Ayla']
},
{
	'name': 'SpinKick',
	'prereqs': ['RoboTackle', 'RolloKick'],
	'characters': ['Robo', 'Ayla']
},
{
	'name': 'BeastToss',
	'prereqs': ['UzziPunch', 'RockThrow'],
	'characters': ['Robo', 'Ayla']
},
{
	'name': 'SlurpKiss',
	'prereqs': ['Slurp', 'Kiss'],
	'characters': ['Frog', 'Ayla']
},
{
	'name': 'BubbleHit',
	'prereqs': ['Water', 'RolloKick'],
	'characters': ['Frog', 'Ayla']
},
{
	'name': 'DropKick',
	'prereqs': ['LeapSlash', 'TripleKick'],
	'characters': ['Frog', 'Ayla']
},
]

all_triple_techs = [
{
	'name': 'DeltaForce',
	'prereqs': ['Lightning2', 'Ice2', 'Fire2'],
	'characters': ['Chrono', 'Marle', 'Lucca']
},
{
	'name': 'Lifeline',
	'prereqs': ['Cyclone', 'Life2', 'LaserSpin'],
	'characters': ['Chrono', 'Marle', 'Robo']
},
{
	'name': 'ArcImpulse',
	'prereqs': ['Spincut', 'Ice2', 'LeapSlash'],
	'characters': ['Chrono', 'Marle', 'Frog']
},
{
	'name': 'FinalKick',
	'prereqs': ['Lightning2', 'Ice2', 'TripleKick'],
	'characters': ['Chrono', 'Marle', 'Ayla']
},
{
	'name': 'FireZone',
	'prereqs': ['Spincut', 'Fire2', 'LaserSpin'],
	'characters': ['Chrono', 'Lucca', 'Robo']
},
{
	'name': 'DeltaStorm',
	'prereqs': ['Lightning2', 'Fire2', 'Water2'],
	'characters': ['Chrono', 'Lucca', 'Frog']
},
{
	'name': 'GatlingKick',
	'prereqs': ['Lightning2', 'Fire2', 'TripleKick'],
	'characters': ['Chrono', 'Lucca', 'Ayla']
},
{
	'name': 'TripleRaid',
	'prereqs': ['Cyclone', 'SlurpCut', 'RoboTackle'],
	'characters': ['Chrono', 'Robo', 'Frog']
},
{
	'name': 'Twister',
	'prereqs': ['Cyclone', 'LaserSpin', 'TailSpin'],
	'characters': ['Chrono', 'Robo', 'Ayla']
},
{
	'name': '3DAttack',
	'prereqs': ['Cyclone', 'SlurpCut', 'TripleKick'],
	'characters': ['Chrono', 'Frog', 'Ayla']
},
{
	'name': 'DarkEternal',
	'prereqs': ['DarkMatter', 'Ice2F', 'Fire2'],
	'characters': ['Magus', 'Frog', 'Lucca']
},
{
	'name': 'OmegaFlare',
	'prereqs': ['Flare', 'LaserSpin', 'DarkBomb'],
	'characters': ['Lucca', 'Robo', 'Magus']
},
{
	'name': 'SpinStrike',
	'prereqs': ['LeapSlash', 'RoboTackle', 'TailSpin'],
	'characters': ['Frog', 'Robo', 'Ayla']
},
{
	'name': 'PoyozoDance',
	'prereqs': ['Provoke', 'HypnoWave', 'TailSpin'],
	'characters': ['Marle', 'Lucca', 'Ayla']
},
{
	'name': 'GrandDream',
	'prereqs': ['FrogSquash', 'CureBeam', 'Life2'],
	'characters': ['Frog', 'Robo', 'Marle']
},
]

def main():
    single_techs = []
    with open('techlist.txt','r') as f:
        for line in f:
            line = line.strip()
            if line and line[0] != '[':
                continue
            line = line[1:line.find(']')]
            techs = line.split(',')
            single_techs.extend([t.strip() for t in techs])
    
    available_multi_techs = {}
    for t in all_dual_techs + all_triple_techs:
        if all(p in single_techs for p in t['prereqs']):
            chars = "+".join(sorted(t['characters']))
            a = available_multi_techs.get(chars, [])
            a.append(t['name'])
            available_multi_techs[chars] = a

    with open('techlistmulti.txt', 'w') as f:
        for k in available_multi_techs:
            f.write('{chars}\n{techs}\n'.format(chars=k, techs=str(available_multi_techs[k]).replace("'", "")))
    
    
if __name__ == "__main__":
    main()