import pygame
import random
pygame.init()

Swidth=900
Sheight=600
screen=pygame.display.set_mode((Swidth,Sheight))

background1=background2=pygame.image.load('background.png')

loading_screen=loading=pygame.image.load('spaceshooter pic.png')

live1=live2=live3=pygame.image.load('live.png')
live_=pygame.image.load('live2.png')

speed_effect1=speed_effect2=pygame.image.load('effect.png')

player_sprite1=pygame.image.load('sprite1.png')
player_sprite2=pygame.image.load('sprite2.png')
player_sprite=player_sprite1

paused_menu_=pygame.image.load('paused.png')
paused_menu1=pygame.image.load('paused1.png')
paused_menu2=pygame.image.load('paused2.png')
paused_menu=paused_menu_

unit=dozen=hundred=thousand=dthousand=hthousand=billion=_0=pygame.image.load('0.png')
_1=pygame.image.load('1.png')
_2=pygame.image.load('2.png')
_3=pygame.image.load('3.png')
_4=pygame.image.load('4.png')
_5=pygame.image.load('5.png')
_6=pygame.image.load('6.png')
_7=pygame.image.load('7.png')
_8=pygame.image.load('8.png')
_9=pygame.image.load('9.png')
scoring=pygame.image.load('scoring.png')

boss_shot=boss_shot_=pygame.image.load('shot_.png')
boss_shot_p=pygame.image.load('shot_prepare.png')
boss_shot_s1=pygame.image.load('shot_shot.png')
boss_shot_s2=pygame.image.load('shot_shot2.png')
fireball_boss=pygame.image.load('fireball_boss.png')

boss_sprite=boss_sp_alive=pygame.image.load('boss11.png')
boss_sp_halfdead=pygame.image.load('boss112.png')
boss_sp_dead=pygame.image.load('boss12.png')
boss_hit_true=pygame.image.load('boss1_.png')
boss_hit_false=boss_hit=pygame.image.load('boss1__.png')

End_screen=End_screen2=pygame.image.load('end2.png')
End_screen1=pygame.image.load('end.png')

enemy1=enemy2=enemy3=enemy_off=pygame.image.load('fireball2.png')
enemy_on=pygame.image.load('fireball.png')

shot1=shot2=shot3=shot4=shot5=shot_off=pygame.image.load('shot2.png')
shot_on=pygame.image.load('shot.png')

#----pause menu----#

paused=False

#----enemies----#

x_ey1=900
y_ey1=0

x_ey2=900
y_ey2=0

x_ey3=900
y_ey3=0

ey1_on_set=False
ey2_on_set=False
ey3_on_set=False

#----Boss----#

x_boss=900
y_boss=600

y_laser=0

boss_on_set=False
boss_intro=False
boss_dead=False

paternx1=False
paternx2=False
paterny1=False
paterny2=False

attack1=False
attack2=False

laser_beam_prepare=False #preparer le lancement du laser appel de photo shot prepare
laser_beam_shot=False #lancer le laser appel des deux photo shot_shot et shot_shot2

boss_hitc=0

#----player----#

x_player=150#positionnement horizontal du joueur
y_player=300#positionnement verticale du joueur
x_player_save=x_player
y_player_save=y_player

hit1=False
hit2=False
hit3=False
GameOver=False

#----shots----#

x_shot1=-100
x_shot2=-100
x_shot3=-100
x_shot4=-100
x_shot5=-100
y_shot1=y_shot2=y_shot3=y_shot4=y_shot5=y_player+33

shot1_on=False
shot2_on=False
shot3_on=False
shot4_on=False
shot5_on=False

#----background----#

x_bkgd1=0
x_bkgd2=9000

x_sdet1=0
x_sdet2=1800

#----score----#

score=0
sc=[]

#----timer----#

timer_frame=0
timer_sec=1000
timer_save=timer_sec

#----game----#

clock=pygame.time.Clock()

done=False

#----music----#

ST1_playing=False
ST2_playing=False

#------------------------------------game script------------------------------------#

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()

    loading_screen=live_

    x_player_save=x_player
    y_player_save=y_player
    
    timer_frame=timer_frame+1

    boss_hit=boss_hit_false

    if GameOver:
        End_screen=End_screen1
        live1=live_
        if timer_frame>=200:
            done=True
        else:
            done=done
    else:

        #----music----#

        if not boss_on_set and not ST2_playing and not ST1_playing:
            pygame.mixer.music.load('detroit1.mp3')
            pygame.mixer.music.play(-1)
            ST1_playing=True
            ST2_playing=False
        elif not boss_on_set and ST2_playing and not ST1_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('ST_regards_from_.mp3')
            pygame.mixer.music.play(-1)
            ST1_playing=True
            ST2_playing=False
        elif boss_on_set and ST1_playing and not ST2_playing:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('ST_meeting_in_.mp3')
            pygame.mixer.music.play(-1)
            ST2_playing=True
            ST1_playing=False
        else:
            done=done

        #----pause menu----#
    

        if pressed[pygame.K_ESCAPE]:
            if paused:
                paused=False
                paused_menu=paused_menu_
            else:
                paused_menu=paused_menu1
                paused=True
            pygame.time.wait(100)
        else:
            done=done

        if not paused:

            #----score----#

            if hit1 and hit2:
                score=score+3
            elif hit1:
                score=score+2
            elif not hit1:
                score=score+1
            else:
                done=done

            score=str(score)

            sc=[]

            for i in range(len(score)):
                sc.append('_'+score[i])

            if len(sc)==1:
                units=eval(sc[0])
            elif len(sc)==2:
                units=eval(sc[1])
                dozen=eval(sc[0])
            elif len(sc)==3:
                units=eval(sc[2])
                dozen=eval(sc[1])
                hundred=eval(sc[0])
            elif len(sc)==4:
                units=eval(sc[3])
                dozen=eval(sc[2])
                hundred=eval(sc[1])
                thousand=eval(sc[0])
            elif len(sc)==5:
                units=eval(sc[4])
                dozen=eval(sc[3])
                hundred=eval(sc[2])
                thousand=eval(sc[1])
                dthousand=eval(sc[0])
            elif len(sc)==6:
                units=eval(sc[5])
                dozen=eval(sc[4])
                hundred=eval(sc[3])
                thousand=eval(sc[2])
                dthousand=eval(sc[1])
                hthousand=eval(sc[0])
            elif len(sc)>=7:
                units=eval(sc[6])
                dozen=eval(sc[5])
                hundred=eval(sc[4])
                thousand=eval(sc[3])
                dthousand=eval(sc[2])
                hthousand=eval(sc[1])
                billion=eval(sc[0])
            else:
                done=done


            score=int(score)
                    
            #----timer----#
            
            if timer_frame>=20:
                timer_sec=timer_sec-1
                timer_frame=0
            else:
                done=done
            paused_menu=paused_menu_

            #----lives----#

            if hit1 and hit2:
                GameOver==False
                live2=live_
            elif hit1:
                GameOver=False
                live3=live_
            else:
                done=done

            #----scrolling----#

            x_bkgd1=x_bkgd1-(1/3)
            x_bkgd2=x_bkgd2-(1/3)

            if x_bkgd1<=-9000:
                x_bkgd1=9000
            elif x_bkgd2<=-9000:
                x_bkgd2=9000
            else:
                done=done

            x_sdet1=x_sdet1-100
            x_sdet2=x_sdet2-100

            if x_sdet1<=-1800:
                x_sdet1=1800
            elif x_sdet2<=-1800:
                x_sdet2=1800
            else:
                done=done

            #----player----#

            if player_sprite==player_sprite1:
                player_sprite=player_sprite2
            elif player_sprite==player_sprite2:
                player_sprite=player_sprite1
            else:
                done=done

            #----shots----#.

            if pressed[pygame.K_SPACE]:
                if not shot1_on and (timer_frame>=19 or timer_frame==5 or timer_frame==10 or timer_frame==15):
                    shot1_on=True
                    shot1=shot_on
                    y_shot1=y_player+33
                    x_shot1=x_player+60
                elif not shot2_on and (timer_frame>=19 or timer_frame==5 or timer_frame==10 or timer_frame==15):
                    shot2_on=True
                    shot2=shot_on
                    y_shot2=y_player+33
                    x_shot2=x_player+60
                elif not shot3_on and (timer_frame>=19 or timer_frame==5 or timer_frame==10 or timer_frame==15):
                    shot3_on=True
                    shot3=shot_on
                    y_shot3=y_player+33
                    x_shot3=x_player+60
                elif not shot4_on and (timer_frame>=19 or timer_frame==5 or timer_frame==10 or timer_frame==15):
                    shot4_on=True
                    shot4=shot_on
                    y_shot4=y_player+33
                    x_shot4=x_player+60
                elif not shot5_on and (timer_frame>=19 or timer_frame==5 or timer_frame==10 or timer_frame==15):
                    shot5_on=True
                    shot5=shot_on
                    y_shot5=y_player+33
                    x_shot5=x_player+60
                else:
                    done=done
            else:
                done=done
            
            if shot1_on:
                if x_shot1>=900:
                    shot1_on=False
                    shot1=shot_off
                    x_shot1=-500
                else:
                    x_shot1=x_shot1+30
            else:
                done=done

            if shot2_on:
                if x_shot2>=900:
                    shot2_on=False
                    shot2=shot_off
                    x_shot2=-500
                else:
                    x_shot2=x_shot2+30
            else:
                done=done

            if shot3_on:
                if x_shot3>=900:
                    shot3_on=False
                    shot3=shot_off
                    x_shot3=-500
                else:
                    x_shot3=x_shot3+30
            else:
                done=done

            if shot4_on:
                if x_shot4>=900:
                    shot4_on=False
                    shot4=shot_off
                    x_shot4=-500
                else:
                    x_shot4=x_shot4+30
            else:
                done=done

            if shot5_on:
                if x_shot5>=900:
                    shot5_on=False
                    shot5=shot_off
                    x_shot5=-500
                else:
                    x_shot5=x_shot5+30
            else:
                done=done

            if (y_shot1>=y_ey1-70 and y_shot1<=y_ey1+70 and x_shot1>=x_ey1-70 and x_shot1<=x_ey1+70) or (x_shot2>=x_ey1-70 and y_shot2>=y_ey1-70 and y_shot2+5<=y_ey1+70 and x_shot2<=x_ey1+70) or (x_shot3>=x_ey1-70 and y_shot3>=y_ey1 and y_shot3+5<=y_ey1+70 and x_shot3<=x_ey1+70) or (y_shot4>=y_ey1-70 and y_shot4+5<=y_ey1+70 and x_shot4>=x_ey1 and x_shot4<=x_ey1+70) or (x_shot5>=x_ey1-70 and y_shot5>=y_ey1-70 and y_shot5+5<=y_ey1+70 and x_shot5<=x_ey1+70):
                ey1_on_set=False
                score=score+100
            else:
                done=done

            if (y_shot1>=y_ey2-70 and y_shot1<=y_ey2+70 and x_shot1>=x_ey2-70 and x_shot1<=x_ey2+70) or (x_shot2>=x_ey2-70 and y_shot2>=y_ey2-70 and y_shot2+5<=y_ey2+70 and x_shot2<=x_ey2+70) or (x_shot3>=x_ey2-70 and y_shot3>=y_ey2 and y_shot3+5<=y_ey2+70 and x_shot3<=x_ey2+70) or (y_shot4>=y_ey2-70 and y_shot4+5<=y_ey2+70 and x_shot4>=x_ey2 and x_shot4<=x_ey2+70) or (x_shot5>=x_ey2-70 and y_shot5>=y_ey2-70 and y_shot5+5<=y_ey2+70 and x_shot5<=x_ey2+70):
                ey2_on_set=False
                score=score+100
            else:
                done=done

            if (y_shot1>=y_ey3-70 and y_shot1<=y_ey3+70 and x_shot1>=x_ey3-70 and x_shot1<=x_ey3+70) or (x_shot2>=x_ey3-70 and y_shot2>=y_ey3-70 and y_shot2+5<=y_ey3+70 and x_shot2<=x_ey3+70) or (x_shot3>=x_ey3-70 and y_shot3>=y_ey3 and y_shot3+5<=y_ey3+70 and x_shot3<=x_ey3+70) or (y_shot4>=y_ey3-70 and y_shot4+5<=y_ey3+70 and x_shot4>=x_ey3 and x_shot4<=x_ey3+70) or (x_shot5>=x_ey3-70 and y_shot5>=y_ey3-70 and y_shot5+5<=y_ey3+70 and x_shot5<=x_ey3+70):
                ey3_on_set=False
                score=score+100
            else:
                done=done
            

            #----moves----#

            if pressed[pygame.K_UP]:
                y_player=y_player-10
            else:
                y_player=y_player
                
            if pressed[pygame.K_DOWN]:
                y_player=y_player+10
            else:
                y_player=y_player

            if pressed[pygame.K_LEFT]:
                x_player=x_player-10
            else:
                x_player=x_player

            if pressed[pygame.K_RIGHT]:
                x_player=x_player+10
            else:
                x_player=x_player

            #----limits----#

            if (x_player<=5 or x_player>=Swidth-(Swidth//3)) and (pressed[pygame.K_RIGHT] or pressed[pygame.K_LEFT]):
                x_player=x_player_save
            else:
                done=done
            if (y_player<=5 or y_player>=Sheight-50) and (pressed[pygame.K_UP] or pressed[pygame.K_DOWN]):
                y_player=y_player_save
            else:
                done=done

            
            #----enemies----#

            if not ey1_on_set:
                x_ey1=900
                if timer_frame>=19:
                    y_ey1=random.randrange(-15,675)
                    ey1_on_set=True
                else:
                    enemy1=enemy_off
            elif ey1_on_set:
                enemy1=enemy_on
                if x_ey1<=-60:
                    ey1_on_set=False
                    x_ey1=900
                else:
                    ey1_on_set=True
                    x_ey1=x_ey1-15
            else:
                done=done

            if not ey2_on_set:
                x_ey2=900
                if timer_frame>=13:
                    y_ey2=random.randrange(-15,675)
                    ey2_on_set=True
                else:
                    enemy2=enemy_off
            elif ey2_on_set:
                enemy2=enemy_on
                if x_ey2<=-60:
                    ey2_on_set=False
                    x_ey2=900
                else:
                    ey2_on_set=True
                    x_ey2=x_ey2-15
            else:
                done=done

            if not ey3_on_set:
                x_ey3=900
                if timer_frame>=5:
                    y_ey3=random.randrange(-15,675)
                    ey3_on_set=True
                else:
                    enemy3=enemy_off
            elif ey3_on_set:
                enemy3=enemy_on
                if x_ey3<=-60:
                    ey3_on_set=False
                    x_ey3=900
                else:
                    ey3_on_set=True
                    x_ey3=x_ey3-15
            else:
                done=done

            if y_ey1>=y_player-45 and y_ey1<=y_player+45:
                if x_ey1>=x_player-72 and x_ey1<=x_player+72:
                    ey1_on_set=False
                    if hit2:
                        hit3=True
                        GameOver=True
                    elif hit1:
                        hit2=True
                    else:
                        hit1=True
                else:
                    hit1=hit1
                    hit2=hit2
                    hit3=hit3
            else:
                hit1=hit1
                hit2=hit2
                hit3=hit3

            if y_ey2>=y_player-45 and y_ey2<=y_player+45:
                if x_ey2>=x_player-72 and x_ey2<=x_player+72:
                    ey2_on_set=False
                    if hit2:
                        hit3=True
                        GameOver=True
                    elif hit1:
                        hit2=True
                    else:
                        hit1=True
                else:
                    hit1=hit1
                    hit2=hit2
                    hit3=hit3
            else:
                hit1=hit1
                hit2=hit2
                hit3=hit3

            if y_ey3>=y_player-45 and y_ey3<=y_player+45:
                if x_ey3>=x_player-72 and x_ey3<=x_player+72:
                    ey3_on_set=False
                    if hit2:
                        hit3=True
                        GameOver=True
                    elif hit1:
                        hit2=True
                    else:
                        hit1=True
                else:
                    hit1=hit1
                    hit2=hit2
                    hit3=hit3
            else:
                hit1=hit1
                hit2=hit2
                hit3=hit3

            #----boss----#

            if boss_on_set and boss_intro:
                y_boss=-50
                if x_boss>=Swidth-400:
                    boss_intro=True
                    x_boss=x_boss-5
                else:
                    boss_intro=False
                    
            elif boss_on_set and not boss_dead:
                if x_shot1>=x_boss+170:
                    shot1_on=False
                    shot1=shot_off
                    x_shot1=-500
                    score=score+250
                    boss_hitc=boss_hitc+1
                    boss_hit=boss_hit_true
                else:
                    done=done
                if x_shot2>=x_boss+170:
                    shot2_on=False
                    shot2=shot_off
                    x_shot2=-500
                    score=score+250
                    boss_hitc=boss_hitc+1
                    boss_hit=boss_hit_true
                else:
                    done=done
                if x_shot3>=x_boss+170:
                    shot3_on=False
                    shot3=shot_off
                    x_shot3=-500
                    score=score+250
                    boss_hitc=boss_hitc+1
                    boss_hit=boss_hit_true
                else:
                    done=done
                if x_shot4>=x_boss+170:
                    shot4_on=False
                    shot4=shot_off
                    x_shot4=-500
                    score=score+250
                    boss_hitc=boss_hitc+1
                    boss_hit=boss_hit_true
                else:
                    done=done
                if x_shot5>=x_boss+170:
                    shot5_on=False
                    shot5=shot_off
                    x_shot5=-500
                    score=score+250
                    boss_hitc=boss_hitc+1
                    boss_hit=boss_hit_true
                else:
                    done=done
                
                if boss_hitc<150:
                    attack1=True
                    boss_sprite=boss_sp_alive
                elif boss_hitc>400:
                    boss_dead=True
                    attack2=False
                    boss_sprite=boss_sp_dead
                else:
                    attack1=False
                    attack2=True
                    boss_sprite=boss_sp_halfdead

                if attack1 or attack2:
                    enemy1=enemy2=enemy3=fireball_boss
                    if x_ey1<Swidth-100:
                        y_ey1=y_ey1
                    else:
                        y_ey1=y_player
                    if x_ey2<Swidth-100:
                        y_ey2=y_ey2
                    else:
                        y_ey2=y_player
                    if x_ey3<Swidth-100:
                        y_ey3=y_ey3
                    else:
                        y_ey3=y_player
                else:
                    done=done
                    
                if attack2 and not laser_beam_prepare and not laser_beam_shot:
                    y_laser=y_player-20
                    laser_beam_prepare=True
                    timer_save=timer_sec
                else:
                    done=done

                if laser_beam_prepare and timer_sec>=timer_save-3:
                    boss_shot=boss_shot_p
                elif laser_beam_prepare and timer_sec<timer_save-3:
                    laser_beam_prepare=False
                    laser_beam_shot=True
                    boss_shot=boss_shot_s1
                elif laser_beam_shot and timer_sec>timer_save-7:
                    if boss_shot==boss_shot_s1:
                        boss_shot=boss_shot_s2
                    else:
                        boss_shot=boss_shot_s1
                    if y_player<=y_laser+65 and y_player>=y_laser-45:
                        if hit2:
                            hit3=True
                            GameOver=True
                        elif hit1:
                            hit2=True
                        else:
                            hit1=True
                    else:
                        score=score+1
                else:
                    laser_beam_prepare=False
                    laser_beam_shot=False
                    
                    
                
                if paternx1:
                    if x_boss<=Swidth-430:
                        paternx1=False
                        paternx2=True
                    else:
                        x_boss=x_boss-3
                elif paternx2:
                    if x_boss>=Swidth-300:
                        paternx1=True
                        paternx2=False
                    else:
                        x_boss=x_boss+3
                else:
                    paternx1=True
                    
                if paterny1:
                    if y_boss<=-97:
                        paterny1=False
                        paterny2=True
                    else:
                        y_boss=y_boss-3
                elif paterny2:
                    if y_boss>=-3:
                        paterny1=True
                        paterny2=False
                    else:
                        y_boss=y_boss+3
                else:
                    paterny1=True

            elif boss_dead:
                boss_shot=boss_shot_
                boss_hit=boss_hit_false
                boss_on_set=False
                if x_boss<=900:
                    x_boss=x_boss+3
                else:
                    y_boss=600
            else:
                done=done

            if boss_on_set and not boss_intro:
                if x_player>=x_boss-62:
                    if hit2:
                        hit3=True
                        GameOver=True
                    elif hit1:
                        hit2=True
                    else:
                        hit1=True
                else:
                    done=done
            else:
                done=done
                

            #----level increase (level events schedules)----#

            if timer_sec<=905 and timer_sec>=899:
                ey1_on_set=False
                ey2_on_set=False
                ey3_on_set=False
                boss_on_set=True
                boss_intro=True
            elif timer_sec>995:
                loading_screen=loading
                score=0
                ey1_on_set=False
                ey2_on_set=False
                ey3_on_set=False
            elif timer_sec>987:
                ey1_on_set=False
                ey2_on_set=False
                ey3_on_set=False
            elif timer_sec>984:
                ey1_on_set=False
                ey2_on_set=False
            elif timer_sec>980:
                ey1_on_set=False
            else:
                done=done
                

    #----pause menu----#

        elif paused:
            if paused_menu==paused_menu2:
                if pressed[pygame.K_RETURN]:
                    done=True
                else:
                    done=False
            elif paused_menu==paused_menu1:
                if pressed[pygame.K_RETURN]:
                    paused=False
                else:
                    paused=True
            else:
                done=done
            if pressed[pygame.K_UP] or pressed[pygame.K_DOWN]:
                if paused_menu==paused_menu1:
                    paused_menu=paused_menu2
                elif paused_menu==paused_menu2:
                    paused_menu=paused_menu1
                else:
                    paused=True
                pygame.time.wait(100)
            else:
                done=done
        else :
            print('ERROR : an unknown error occured')

#----dev mode----#



    screen.fill((0,0,0))
    screen.blit(background1,(x_bkgd1,0))
    screen.blit(background2,(x_bkgd2,0))
    screen.blit(enemy1,(x_ey1,y_ey1))
    screen.blit(enemy2,(x_ey2,y_ey2))
    screen.blit(enemy3,(x_ey3,y_ey3))
    screen.blit(shot1,(x_shot1,y_shot1))
    screen.blit(shot2,(x_shot2,y_shot2))
    screen.blit(shot3,(x_shot3,y_shot3))
    screen.blit(shot4,(x_shot4,y_shot4))
    screen.blit(shot5,(x_shot5,y_shot5))
    screen.blit(boss_shot,(0,y_laser))
    screen.blit(boss_sprite,(x_boss,y_boss))
    screen.blit(boss_hit,(x_boss,y_boss))
    screen.blit(player_sprite,(x_player,y_player))
    screen.blit(speed_effect1,(x_sdet1,0))
    screen.blit(speed_effect2,(x_sdet2,0))
    screen.blit(live1,(10,5))
    screen.blit(live2,(60,5))
    screen.blit(live3,(110,5))
    screen.blit(scoring,(Swidth-330,8))
    screen.blit(unit,(Swidth-20,5))
    screen.blit(dozen,(Swidth-50,5))
    screen.blit(hundred,(Swidth-80,5))
    screen.blit(thousand,(Swidth-120,5))
    screen.blit(dthousand,(Swidth-150,5))
    screen.blit(hthousand,(Swidth-180,5))
    screen.blit(billion,(Swidth-220,5))
    screen.blit(paused_menu,((Swidth/2)-85,(Sheight/3)))
    screen.blit(End_screen,(150,(Sheight/2)-65))
    screen.blit(loading_screen,(0,0))
    clock.tick(20)
    pygame.display.flip()
    pygame.display.set_caption("space defense") 
