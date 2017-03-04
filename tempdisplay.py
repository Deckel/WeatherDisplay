#!/usr/bin/env python
while True:
          
        import colorsys
        import math
        import time
        import re
        import ast
        from random import randint
        import pyowm
        

        import unicornhat as unicorn
        unicorn.set_layout(unicorn.PHAT)
        unicorn.brightness(0.4)



        while True:

                try:

                        print("Perspeculating weather!")

                        # Setting the region data

                        owm = pyowm.OWM('####YOUR OWN PYOOWM KEY HERE######')
                        observation = owm.weather_at_place('canterbury,uk')
                        w = observation.get_weather()
                        temp = w.get_temperature('celsius')
                        status = w.get_status()
                        print("The current weatheris: {}".format(status))
                        print("The Tempreature at the moment is: {}".format(temp["temp"]))
                        m = temp["temp"]
                        t = round(m)

                        #Getting current time

                        currenttime = time.strftime("%H")
                        currenttime = int(currenttime)
                        print("The time in hours is: {}".format(currenttime))

                        #Making it turn off at night

                        if (8 < currenttime < 22):
                                unicorn.brightness(0.8)
                        else:
                                unicorn.brightness(0)
                                print("THE BRIGHTNESS IS AT 0 AT THE MOMENT")

                        

                        #------TESTING--------------
                        #currenttime = 20
                        #t = 20
                        #status = 'Clear'
                        
                        def weather(str):
                                #----------------CLEAR---------------------------------------
                                if (str=='Clear' and t<=12 and 6 < currenttime < 18):
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
                                if (str=='Clouds' and t<=12):
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
                                                
                                #---------------------------------------------------------------
                        for x in range(0,int(t)):

                                #making color gradient
                                y = 16
                                r = 0 + y*x
                                b = 255 - y*x
                                                                               
                                #displaying the pixels
                                weather(status)
                                time.sleep(0.5)
                                for y in range(0,4):
                                        unicorn.set_pixel((x/2),y,r,0,b)
                                        unicorn.show()
                                print(x)
                                #displayign the last row for an extened amount of time
                                if (x==t-1) or x==16:
                                        for i in range(1,5):
                                                unicorn.set_pixel((x/2),i,r,0,b)
                                        unicorn.show()
                                        for x in range(1,20):
                                                weather(status)
                                                time.sleep(0.5)
                                                unicorn.show()
                                        unicorn.clear()
                                        break
                except:
                        time.sleep(1)
                        print("RESTARTING")
