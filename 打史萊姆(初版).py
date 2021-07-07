import time
import random
wintimes=0
myatk=5
myfullhp=50
myhp=50
mydef=1
enemyatk=1
enemyfullhp=10
enemyhp=10
enemydef=0
while myhp>0:
    myhp=myfullhp
    enemyhp=enemyfullhp
    print("你的數值:攻擊{:.0f},生命值{:.0f},防禦{:.0f}".format(myatk,myhp,mydef))
    time.sleep(1)
    print("你遇見了史萊姆,攻擊{:.0f},生命值{:.0f},防禦{:.0f}".format(enemyatk,enemyhp,enemydef))
    time.sleep(2)
    mydamage=myatk**2/(myatk+enemydef)
    enemydamage=enemyatk**2/(enemyatk+mydef)
    mydamagemin=eval("{:.0f}".format(mydamage*0.7))+1
    mydamagemax=eval("{:.0f}".format(mydamage*1.3))+1
    enemydamagemin=eval("{:.0f}".format(enemydamage*0.7))+1
    enemydamagemax=eval("{:.0f}".format(enemydamage*1.3))+1
    while myhp>0 and enemyhp>0:
        mydamage=random.randint(mydamagemin,mydamagemax)
        enemydamage=random.randint(enemydamagemin,enemydamagemax)
        enemyhp-=mydamage
        if enemyhp<0:
            enemyhp=0
        print("你砍了史萊姆一劍，造成",mydamage,"點傷害，它的血量還剩",enemyhp,"點",sep="")
        time.sleep(1)
        if enemyhp>0:
            myhp-=enemydamage
            if myhp<0:
                myhp=0
            print("史萊姆咬了你一口，造成",enemydamage,"點傷害，你的血量還剩",myhp,"點",sep="")
            time.sleep(1)
    if myhp<=0:
        print("你輸了,你總共打贏",wintimes,"隻史萊姆",sep="")
    else:
        wintimes+=1
        print("1.攻擊加",wintimes*3,",2.生命值加",wintimes*10,",3.防禦加",wintimes*2,sep="")
        myplus=eval(input("請選擇加成(打編號)?"))
        if myplus==1:
            myatk+=wintimes*3
        elif myplus==2:
            myfullhp+=wintimes*10
        elif myplus==3:
            mydef+=wintimes*2
        enemyplus=random.randint(1,3)
        if enemyplus==1:
            enemyatk+=wintimes*2.5
        elif enemyplus==2:
            enemyfullhp+=wintimes*15
        elif enemyplus==3:
            enemydef+=wintimes*3