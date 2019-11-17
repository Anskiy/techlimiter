import random as rand
import multitechs as mt
Crono = ["Cyclone","Slash","Lightning","Spincut","Lightning2","Life","Confuse","Luminaire"]
Marle = ["Aura","Provoke","Ice","Cure","Haste","Ice2","Cure2","Life2"]
Lucca = ["FlameToss","HypnoWave","Fire","Napalm","Protect","Fire2","MegaBomb","Flare"]
Robo = ["RocketPunch","CureBeam","LaserSpin","RoboTackle","HealBeam","UzziPunch","AreaBomb","Shock"]
Frog = ["Slurp","SlurpCut","Water","Heal","LeapSlash","Water2","Cure2F","FrogSquash"]
Ayla = ["Kiss","RolloKick","CatAttack","RockThrow","Charm","TailSpin","DinoTail","TripleKick"]
Magus = ["Fire2M","Ice2M","Lightning2M","DarkBomb","MagicWall","DarkMist","BlackHole","DarkMatter"]
tech_lists = [Crono,Marle,Lucca,Robo,Frog,Ayla,Magus]
selected_list = []
iterator = 0
for char in tech_lists:
   while iterator < 3:
       x = 0
       y = 8
       if iterator < 2:
         if iterator < 1:
            y = 2
         else:
            x = 3
            y = 5
       temp = rand.choice(char[x:y])
       selected_list.append(temp)
       char.remove(temp)
       iterator += 1
   iterator = 0
tech_lists = ["Crono","Marle","Lucca","Robo","Frog","Ayla","Magus"]
f = open("techlist.txt","w+")
x = 0
y = 3
for char in tech_lists:
       temp_cleaned_list = selected_list[x:y]
       cleaned_list = str(temp_cleaned_list)
       cleaned_list = cleaned_list.replace("'","")
       x = x + 3
       y = y + 3
       f.write(char + "\n" + cleaned_list + "\n")
f.close()
mt.main()