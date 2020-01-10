import sys, os

dmgear = ["VladofSniper","EtechSniper","DahlSniper","HyperionShotgun","JakobsShotgun","TedioreShotgun","HyperionSmg",
    "DahlSmg","BanditSmg","TediorePistol","MaliwanPistol","EtechPistol","VladofPistol","TorguePistol","DahlGrenade","MaliwanGrenade",
    "BanditGrenade","PangolinShield","VladofShield","HyperionShield","DahlShield","VladofRpg","BanditRpg","TorgueRpg","JakobsAR",
    "VladofAR","EtechAR"]

while True:


    print ("\033[1;35;40m=================================================")
    print ("Please enter a Gun to be checked (q to quit) : ")
    print ("=================================================")


    gearname = input()

    os.system('cls' if os.name == 'nt' else 'clear')

    if gearname == "q" or gearname == "Q":
        sys.exit()
    
    if gearname == "showme":
        print ("\033[1;33;40m",dmgear)
           
            

    if gearname in dmgear:
        print("\033[1;31;40m ***That is DMMD's piece of gear! Hands OFF! D= ***")
    elif gearname == "showme":
        pass
    else:
        print("\033[1;31;40m ***That is Neko's piece of gear! Hands OFF! :3 ***")

    
