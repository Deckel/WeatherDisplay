#!/usr/bin/env python
#C0de by DJ Dizzie Dec

  
import colorsys
import math
import time
import re
import ast
from random import randint
import pyowm
import gc

class Droplet:       
        def __init__(self, rainPosition, column, raining):
                self.rainPosition = rainPosition
                self.column = column
                self.raining = raining
        def rainMove(self, value):
                for instance in (obj for obj in gc.get_referrers(self.__class__) if isinstance(obj, self.__class__)):
                        instance.rainPosition -= value

import unicornhat as unicorn
unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.3)
while True:

        try:              

                print("Perspeculating weather!")

                # Setting the region data

                owm = pyowm.OWM('Your own key here')
                observation = owm.weather_at_place('miltonkeynes,uk')
                w = observation.get_weather()
                temp = w.get_temperature('celsius')
                status = w.get_status()
                print("The current weatheris: {}".format(status))
                print("The Tempreature at the moment is: {}".format(temp["temp"]))
                m = temp["temp"]
                t = round(m)
                end_counter = 0
                raindrops = 0

                #Getting current time

                currenttime = time.strftime("%H")
                currenttime = int(currenttime)
                print("The time in hours is: {}".format(currenttime))
                print("-----------------------------------")

                #------TESTING--------------
                #currenttime = 20
                #t = 12
                #status = 'Rain'
                              

                #Making it turn off at night
                if (8 < currenttime < 22):
                        unicorn.brightness(0.8)
                else:
                        unicorn.brightness(0)
                        print("THE BRIGHTNESS IS AT 0 AT THE MOMENT")

                #-------RAIN ARRAY---------------
                Drops = [Droplet(randint(7,14),randint(0,3),1) for i in range(0,15)]
                for i in range(0,15):
                        if (randint(0,10) > 2):
                                Drops[i].raining = 1
                                raindrops += 1                        

                def weather(str):
                                  
                        #----------------CLEAR---------------------------------------
                        if (str=='Clear' and t<=18 and 6 < currenttime < 18):
                                unicorn.set_pixel(7,0,244,241,66)
                                unicorn.set_pixel(7,1,244,241,66)
                                unicorn.set_pixel(6,0,244,241,66)
                                unicorn.set_pixel(6,1,244,241,66)
                                unicorn.show()
                                
                        
                        elif(str=='Clear' and t<=12):
                                unicorn.set_pixel(7,2,165,165,165)
                                unicorn.set_pixel(7,3,165,165,165)
                                unicorn.set_pixel(6,2,165,165,165)
                                unicorn.set_pixel(6,3,165,165,165)
                                unicorn.show()                              
                                
                        #-----------------CLOUDS---------------------------------------
                        if (str=='Clouds' and t<=18):
                                if (x % 2 == 0):
                                        #Clearing clouds
                                        for i in range(0,4):
                                                unicorn.set_pixel(6,i,0,0,0)
                                                unicorn.set_pixel(7,i,0,0,0)
                                        #Making clouds 1
                                        for i in range(1,4):
                                                unicorn.set_pixel(6,i,165,165,165)
                                        for i in range(0,3):
                                                unicorn.set_pixel(7,i,165,165,165)                                         
                                        unicorn.show()
                                        
                                else:
                                        #Clearing clouds
                                        for i in range(0,4):
                                                unicorn.set_pixel(6,i,0,0,0)
                                                unicorn.set_pixel(7,i,0,0,0)
                                        #Making clouds 2 
                                        for i in range(0,3):
                                                unicorn.set_pixel(6,i,165,165,165)
                                        for i in range(1,4):
                                                unicorn.set_pixel(7,i,165,165,165)
                                        unicorn.show()
                                        
                        #----------------RAIN-------------------------------------------
                        if (str=="Rain" and t<=18):
                                
                                #Set all rainPosition to 8 when it goes over the temp      
                                for i in range(0,15):
                                        if(Drops[i].rainPosition < pixel_pos):
                                                Drops[i].rainPosition = 8
                                                if (randint(0,10) > 2):
                                                        Drops[i].raining = 1
                                                else:
                                                        Drops[i].raining = 0
                                #Drawing rain
                                for i in range(0,15):
                                        if (Drops[i].raining == 1):                                
                                                unicorn.set_pixel(Drops[i].rainPosition,Drops[i].column, 0, 0, 255)

                                #Deleting non-diagonal rain
                                for i in range(0,15):
                                        if (Drops[i].raining == 1):
                                                unicorn.set_pixel(Drops[i].rainPosition+1,Drops[i].column, 0, 0, 0)
                                                unicorn.set_pixel(Drops[i].rainPosition,Drops[i].column+1, 0, 0, 0)
                                                unicorn.set_pixel(Drops[i].rainPosition,Drops[i].column-1, 0, 0, 0)
                                #Moves all the rain down one (trust me it works)
                                Drops[1].rainMove(1)
                                
                #Drawing tempreature pixels
                for x in range(0,int(t)):

                        #making color gradient
                        y = 14
                        r = 0 + y*x
                        b = 255 - y*x
                                                                  
                        #displaying the pixels
                        pixel_pos = int(round(x/3))
                        pixel_limit = int(round(t/3))                       
                        time.sleep(0.5)
                        weather(status)                  
                        for y in range(0,4):
                                unicorn.set_pixel(pixel_pos,y,r,0,b)
                                unicorn.show()
                                
                        #displayign the last row for an extened amount of time
                        if (x==t-1 or x==21):
                                while (end_counter < 2):
                                        x = x + 1
                                        weather(status)
                                        for i in range(1,5):
                                                unicorn.set_pixel(pixel_pos,i,r,0,b)
                                                unicorn.show()
                                        time.sleep(0.5)
                        
                                        if (x > 20):
                                                x = 0
                                                end_counter = end_counter + 1
                                print("REPEATING")
                                unicorn.clear()
                                break
                        
        #Restarts when connection goes down
        except:
                time.sleep(1)
                print("RESTARTING")
