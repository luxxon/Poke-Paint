#pokepaint.py
#Marissa Jun
#it's a pokemon-themed paint program!

from random import *
from pygame import *
from math import *
from tkinter import *
import os

#this centers the window on the screen
os.environ['SDL_VIDEO_WINDOW_POS']='50,50'

#this keeps that annoying Tk box from popping up
root=Tk()                                 
root.withdraw()

#setting up the top part and the font
font.init()
typeface=font.SysFont("Calibri",18)
pokeball=image.load("images/pokeball.png")
display.set_icon(pokeball)
display.set_caption(("Poke-Paint v2.0"))
screen=display.set_mode((1200,750))
#------------------------------------
#throwing down some basic colors
white=(255,255,255)
black=(0,0,0)
grey=(200,200,200)
red=(233,114,114)
#------------------------------------
#importing all the images
background=image.load("images/background.png")
pokepaintlogo=image.load("images/pokepaint logo.png")
colorpicker=image.load("images/color picker.png")
pikachu=image.load("images/pikachu.png")
bulbasaur=image.load("images/bulbasaur.png")

#moving them a bit so they look nice
bulbasaur=transform.flip(bulbasaur,True,False)
pikachu=transform.smoothscale(pikachu,(152,140))

rocketlogo=image.load("images/rocket logo.png")
aqualogo=image.load("images/aqua logo.png")
magmalogo=image.load("images/magma logo.png")
galacticlogo=image.load("images/galactic logo.png")
plasmalogo=image.load("images/plasma logo.png")
flarelogo=image.load("images/flare logo.png")
pokeball2=image.load("images/pokeball2.png")
greatball=image.load("images/great ball.png")
ultraball=image.load("images/ultra ball.png")
masterball=image.load("images/master ball.png")

pencilclip=image.load("images/pencil clip.png")
eraserclip=image.load("images/eraser clip.png")
fillclip=image.load("images/fill clip.png")
lineclip=image.load("images/line clip.png")
ovalclip=image.load("images/oval clip.png")
rectangleclip=image.load("images/rectangle clip.png")
dropperclip=image.load("images/dropper clip.png")
sprayclip=image.load("images/spray clip.png")

pencildesc=image.load("images/pencil desc.png")
eraserdesc=image.load("images/eraser desc.png")
filldesc=image.load("images/fill desc.png")
linedesc=image.load("images/line desc.png")
ovaldesc=image.load("images/oval desc.png")
rectangledesc=image.load("images/rectangle desc.png")
dropperdesc=image.load("images/dropper desc.png")
spraydesc=image.load("images/spray desc.png")
stampdesc=image.load("images/stamp desc.png")

#some have to be resized so they don't touch the borders of their rects
sprayclip=transform.smoothscale(sprayclip,(90,90))
dropperclip=transform.smoothscale(dropperclip,(85,85))
rectangleclip=transform.smoothscale(rectangleclip,(85,85))
lineclip=transform.smoothscale(lineclip,(85,85))
ovalclip=transform.smoothscale(ovalclip,(85,85))

#all resized to be the same size
pencildesc=transform.smoothscale(pencildesc,(375,90))
eraserdesc=transform.smoothscale(eraserdesc,(375,90))
filldesc=transform.smoothscale(filldesc,(375,90))
linedesc=transform.smoothscale(linedesc,(375,90))
ovaldesc=transform.smoothscale(ovaldesc,(375,90))
rectangledesc=transform.smoothscale(rectangledesc,(375,90))
dropperdesc=transform.smoothscale(dropperdesc,(375,90))
spraydesc=transform.smoothscale(spraydesc,(375,90))
stampdesc=transform.smoothscale(stampdesc,(375,90))
#------------------------------------
#setting up the layout

#basic stuff
screen.blit(background,(0,0))
screen.blit(pokepaintlogo,(10,10))

canvas=Rect(260,10,750,510)
draw.rect(screen,white,canvas)

#dividers (just for appearance)
draw.line(screen,red,(130,70),(130,520),2)
draw.line(screen,red,(10,519),(250,519),2)
draw.line(screen,red,(130,600),(130,740),2)
draw.line(screen,white,(620,530),(620,580),2)
draw.line(screen,white,(870,530),(870,580),2)

#the tools
pencil=Rect(10,70,95,95)
draw.rect(screen,white,pencil,2)
screen.blit(pencilclip,(10,70))

eraser=Rect(155,70,95,95)
draw.rect(screen,red,eraser,2)
screen.blit(eraserclip,(155,70))

fill=Rect(10,180,95,95)
draw.rect(screen,red,fill,2)
screen.blit(fillclip,(10,180))

line=Rect(155,180,95,95)
draw.rect(screen,red,line,2)
screen.blit(lineclip,(160,185))

oval=Rect(10,290,95,95)
draw.rect(screen,red,oval,2)
screen.blit(ovalclip,(15,295))

rectangle=Rect(155,290,95,95)
draw.rect(screen,red,rectangle,2)
screen.blit(rectangleclip,(160,295))

dropper=Rect(10,400,95,95)
draw.rect(screen,red,dropper,2)
screen.blit(dropperclip,(15,405))

spraypaint=Rect(155,400,95,95)
draw.rect(screen,red,spraypaint,2)
screen.blit(sprayclip,(157,402))

#the stamps
rocket=Rect(260,530,50,50)
screen.blit(rocketlogo,(260,530))

aqua=Rect(320,530,50,50)
screen.blit(aqualogo,(320,530))

magma=Rect(380,530,50,50)
screen.blit(magmalogo,(380,530))

galactic=Rect(440,530,50,50)
screen.blit(galacticlogo,(440,530))

plasma=Rect(500,530,50,50)
screen.blit(plasmalogo,(500,530))

flare=Rect(560,530,50,50)
screen.blit(flarelogo,(560,530))

pokeballstamp=Rect(631,530,50,50)
screen.blit(pokeball2,(631,530))

greatballstamp=Rect(691,530,50,50)
screen.blit(greatball,(691,530))

ultraballstamp=Rect(751,530,50,50)
screen.blit(ultraball,(751,530))

masterballstamp=Rect(811,530,50,50)
screen.blit(masterball,(811,530))

#the current tool description
screen.blit(bulbasaur,(260,600))
screen.blit(pencildesc,(450,600))
screen.blit(pikachu,(858,600))

#the color-related stuff
colorpick=Rect(1020,10,170,664)
colorpreview=Rect(1020,684,170,56)
cproutline=Rect(1020,684,170,56)

screen.blit(colorpicker,(1020,10))
draw.rect(screen,grey,cproutline,5)

#the width-related stuff
woptbg=Rect(880,530,130,20)
sizebg=Rect(880,550,130,30)
draw.rect(screen,grey,woptbg)
draw.rect(screen,white,sizebg)

wopt=typeface.render(("Width Options"),True,black)
xsmall=typeface.render(("XS"),True,red)
small=typeface.render(("S"),True,red)
medium=typeface.render(("M"),True,black)
large=typeface.render(("L"),True,red)
xlarge=typeface.render(("XL"),True,red)

#the undo/redo functions
undo=typeface.render(("UNDO"),True,black)
redo=typeface.render(("REDO"),True,black)

#the save/load functions
save=typeface.render(("SAVE"),True,black)
load=typeface.render(("LOAD"),True,black)

#the flip horizontally/vertically functions
flip=typeface.render(("FLIP"),True,black)
inversion=typeface.render(("INVERT"),True,black)

#boxes had to be made since the renders can't be collidepoint-ed. :(
xsmallbox=Rect(885,555,17,19)
smallbox=Rect(912,555,8,19)
mediumbox=Rect(930,555,16,19)
largebox=Rect(956,555,8,19)
xlargebox=Rect(974,555,17,19)

undobox=Rect(10,600,95,40)
redobox=Rect(155,600,95,40)
flipbox=Rect(10,650,95,40)
invertbox=Rect(155,650,95,40)
savebox=Rect(10,700,95,40)
loadbox=Rect(155,700,95,40)
#------------------------------------
#setting up the default tool. starts out with a black, medium pencil.
#the stamp variable is for later so i don't have to repeat a section as much.
color=(0,0,0)
tool="pencil"
width=4
stamp="off"
#------------------------------------
#these two are stuff for undo/redo; first canvascop is the blank canvas
undolist=[screen.subsurface(canvas).copy()]
redolist=[]

running=True
while running:
    #click and keypress is a flag for the undo/redo/flip/invert
    click=False
    keypress=False
    for e in event.get():
        if e.type==QUIT:
            running=False
        #this section is to get the pos of the mouse when clicked
        #to be used for the circle, line, and rectangle
        #and the undo/redo
        if e.type==KEYDOWN:
            keypress=True
        if e.type==MOUSEBUTTONDOWN:
            if e.button==1:
                click=True
                sx,sy=e.pos
                canvascop=screen.subsurface(canvas).copy()
        if e.type==MOUSEBUTTONUP and canvas.collidepoint(e.pos):
                undolist.append(screen.subsurface(canvas).copy())
    #--------------------------------------------
    #mouse position and what's clicked or pressed
    mx,my=mouse.get_pos()
    mp=mouse.get_pressed()
    keys=key.get_pressed()

    #changing tools
    #all those rects change the outline color to show the tool selected
    if mp[0]==1 and pencil.collidepoint(mx,my):
        stamp="off"
        tool="pencil"
        draw.rect(screen,white,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)
        
    if mp[0]==1 and eraser.collidepoint(mx,my):
        tool="eraser"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,white,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)

    if mp[0]==1 and fill.collidepoint(mx,my):
        tool="fill"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,white,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)
        
    if mp[0]==1 and line.collidepoint(mx,my):
        tool="line"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,white,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)

    if mp[0]==1 and oval.collidepoint(mx,my):
        tool="oval"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,white,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)

    if mp[0]==1 and rectangle.collidepoint(mx,my):
        tool="rectangle"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,white,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)

    if mp[0]==1 and dropper.collidepoint(mx,my):
        tool="dropper"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,white,dropper,2)
        draw.rect(screen,red,spraypaint,2)

    if mp[0]==1 and spraypaint.collidepoint(mx,my):
        tool="spraypaint"
        stamp="off"
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,white,spraypaint,2)

    #changing colors
    #i'm also putting the dropper tool under here
    #since it too affects the color
    if colorpick.collidepoint((mx,my)) and mp[0]==1:
        color=screen.get_at((mx,my))
    if tool=="dropper" and canvas.collidepoint((mx,my)) and mp[0]==1:
        color=screen.get_at((mx,my))

    #put this here since it depends on the color.
    draw.rect(screen,color,colorpreview)

    #changing width
    #put this here since these also change colors when clicked
    #color change indicates the current width
    screen.blit(wopt,(885,532))
    screen.blit(xsmall,((885,555)))
    screen.blit(small,((912,555)))
    screen.blit(medium,((930,555)))
    screen.blit(large,((956,555)))
    screen.blit(xlarge,((974,555)))

    if xsmallbox.collidepoint((mx,my)) and mp[0]==1:
        width=1
        xsmall=typeface.render(("XS"),True,black)
        small=typeface.render(("S"),True,red)
        medium=typeface.render(("M"),True,red)
        large=typeface.render(("L"),True,red)
        xlarge=typeface.render(("XL"),True,red)

    if smallbox.collidepoint((mx,my)) and mp[0]==1:
        width=2
        xsmall=typeface.render(("XS"),True,red)
        small=typeface.render(("S"),True,black)
        medium=typeface.render(("M"),True,red)
        large=typeface.render(("L"),True,red)
        xlarge=typeface.render(("XL"),True,red)
        
    if mediumbox.collidepoint((mx,my)) and mp[0]==1:
        width=4
        xsmall=typeface.render(("XS"),True,red)
        small=typeface.render(("S"),True,red)
        medium=typeface.render(("M"),True,black)
        large=typeface.render(("L"),True,red)
        xlarge=typeface.render(("XL"),True,red)
        
    if largebox.collidepoint((mx,my)) and mp[0]==1:
        width=6
        xsmall=typeface.render(("XS"),True,red)
        small=typeface.render(("S"),True,red)
        medium=typeface.render(("M"),True,red)
        large=typeface.render(("L"),True,black)
        xlarge=typeface.render(("XL"),True,red)
        
    if xlargebox.collidepoint((mx,my)) and mp[0]==1:
        width=8
        xsmall=typeface.render(("XS"),True,red)
        small=typeface.render(("S"),True,red)
        medium=typeface.render(("M"),True,red)
        large=typeface.render(("L"),True,red)
        xlarge=typeface.render(("XL"),True,black)
         
    #using the tools
    if canvas.collidepoint(mx,my) and mp[0]==1:
        screen.set_clip(canvas)
        
        if tool=="pencil":
            draw.line(screen,color,(omx,omy),(mx,my),width)
            #a marker feature integrated into the pencil because im lazy
            #and don't want to make it a seperate tool
            #also its technically a calligraphy tool and not a marker but
            #yknow marker is quicker to type
            if mp[2]==1:
                draw.line(screen,color,(mx+10,my-10),(mx-10,my+10),width)

        if tool=="eraser":
            draw.circle(screen,white,(mx,my),(width*2))

        if tool=="fill":
            draw.rect(screen,color,canvas)

        if tool=="line":
            screen.blit(canvascop,(260,10))
            draw.line(screen,color,(sx,sy),(mx,my),width)
        
        if tool=="rectangle":
            screen.blit(canvascop,(260,10))
            #the min chooses if sx or mx is smaller and then uses that
            #so that the rect doesnt get drawn opposite direction as mouse
            #and the abs is absolute value
            temprect=Rect(min(sx,mx),min(sy,my),abs(sx-mx),abs(sy-my))
            draw.rect(screen,color,temprect,width)
            if mp[2]==1:
                draw.rect(screen,color,temprect,0)

        if tool=="oval":
            screen.blit(canvascop,(260,10))
            #same deal as what's going on with the rectangle
            temprect=Rect(min(sx,mx),min(sy,my),abs(sx-mx),abs(sy-my))
            #if the unfilled ellipse has greater width than diameter, it crashes
            #with filled it's not a problem since there is no width
            if abs(sx-mx)>=width*2 and abs(sy-my)>=width*2:
                draw.ellipse(screen,color,temprect,width)
            if mp[2]==1 or (abs(sx-mx)<=8 and abs(sx-my)<=8):
                draw.ellipse(screen,color,temprect,0)

        if tool=="spraypaint":
            for i in range(10):
                sprayx=(randint(-(width*2),width*2))
                sprayy=(randint(-(width*2),width*2))
                spraypot=hypot(sprayx,sprayy)
                if spraypot<width*2:
                    screen.set_at((mx+sprayx,my+sprayy),color)
                
        screen.set_clip(None)

    #gets the mx,my from the loop before
    omx,omy=mx,my
    
    #selecting the stamps
    #have to still use tool, otherwise it'll use the tool function
    #along with the selected stamp
    if rocket.collidepoint(mx,my) and mp[0]==1:
        tool="rocket"
        stamp="on"
        
    if aqua.collidepoint(mx,my) and mp[0]==1:
        tool="aqua"
        stamp="on"
        
    if magma.collidepoint(mx,my) and mp[0]==1:
        tool="magma"
        stamp="on"
        
    if galactic.collidepoint(mx,my) and mp[0]==1:
        tool="galactic"
        stamp="on"
        
    if plasma.collidepoint(mx,my) and mp[0]==1:
        tool="plasma"
        stamp="on"
        
    if flare.collidepoint(mx,my) and mp[0]==1:
        tool="flare"
        stamp="on"
        
    if pokeballstamp.collidepoint(mx,my) and mp[0]==1:
        tool="pokeball"
        stamp="on"
        
    if greatballstamp.collidepoint(mx,my) and mp[0]==1:
        tool="greatball"
        stamp="on"
        
    if ultraballstamp.collidepoint(mx,my) and mp[0]==1:
        tool="ultraball"
        stamp="on"
        
    if masterballstamp.collidepoint(mx,my) and mp[0]==1:
        tool="masterball"
        stamp="on"

    #using just the stamp variable means i only have to paste this once
    #instead of for every individual stamp!
    if stamp=="on":
        draw.rect(screen,red,pencil,2)
        draw.rect(screen,red,eraser,2)
        draw.rect(screen,red,fill,2)
        draw.rect(screen,red,line,2)
        draw.rect(screen,red,oval,2)
        draw.rect(screen,red,rectangle,2)
        draw.rect(screen,red,dropper,2)
        draw.rect(screen,red,spraypaint,2)
        
    #using the stamps
    #didn't make rects here because they looked ugly
    #had to blit canvascop since otherwise, the stamp would drag when mp[0]==1
    if canvas.collidepoint(mx,my) and mp[0]==1:
        screen.set_clip(canvas)
        
        if tool=="rocket":
            screen.blit(canvascop,(260,10))
            screen.blit(rocketlogo,(mx-25,my-25))
            
        if tool=="aqua":
            screen.blit(canvascop,(260,10))
            screen.blit(aqualogo,(mx-25,my-25))
            
        if tool=="magma":
            screen.blit(canvascop,(260,10))
            screen.blit(magmalogo,(mx-25,my-25))
            
        if tool=="galactic":
            screen.blit(canvascop,(260,10))
            screen.blit(galacticlogo,(mx-25,my-25))
            
        if tool=="plasma":
            screen.blit(canvascop,(260,10))
            screen.blit(plasmalogo,(mx-25,my-25))
            
        if tool=="flare":
            screen.blit(canvascop,(260,10))
            screen.blit(flarelogo,(mx-25,my-25))
            
        if tool=="pokeball":
            screen.blit(canvascop,(260,10))
            screen.blit(pokeball2,(mx-25,my-25))
            
        if tool=="greatball":
            screen.blit(canvascop,(260,10))
            screen.blit(greatball,(mx-25,my-25))
            
        if tool=="ultraball":
            screen.blit(canvascop,(260,10))
            screen.blit(ultraball,(mx-25,my-25))
            
        if tool=="masterball":
            screen.blit(canvascop,(260,10))
            screen.blit(masterball,(mx-25,my-25))

        screen.set_clip(None)

    #the current tool description
    if tool=="pencil":
        screen.blit(pencildesc,(450,600))
        
    if tool=="eraser":
        screen.blit(eraserdesc,(450,600))
        
    if tool=="fill":
        screen.blit(filldesc,(450,600))
        
    if tool=="line":
        screen.blit(linedesc,(450,600))
        
    if tool=="oval":
        screen.blit(ovaldesc,(450,600))
        
    if tool=="rectangle":
        screen.blit(rectangledesc,(450,600))
        
    if tool=="dropper":
        screen.blit(dropperdesc,(450,600))
        
    if tool=="spraypaint":
        screen.blit(spraydesc,(450,600))
        
    if stamp=="on":
        screen.blit(stampdesc,(450,600))
    
    #using the functions
    #have to draw all this before the text or the boxes will be on top
    draw.rect(screen,red,undobox)
    draw.rect(screen,red,redobox)
    draw.rect(screen,red,flipbox)
    draw.rect(screen,red,invertbox)
    draw.rect(screen,red,savebox)
    draw.rect(screen,red,loadbox)

    #undo/redo functions
    #unfortunately if the cursor is off the canvas when mousebuttonup
    #then that line isn't counted in the undo/redo lists
    #nor does the redolist get deleted once the drawing continues
    if undobox.collidepoint((mx,my)):
        draw.rect(screen,white,undobox)
        draw.rect(screen,red,redobox)
        
    if (undobox.collidepoint((mx,my)) and click==True) or (keys[K_z] and keys[K_LCTRL] and keypress==True):
        if len(undolist)>1:
            redolist.append(undolist[-1])
            del undolist[-1]
            screen.blit(undolist[-1],(260,10))
        
    if redobox.collidepoint((mx,my)):
        draw.rect(screen,red,undobox)
        draw.rect(screen,white,redobox)
        
    if (redobox.collidepoint((mx,my)) and click==True) or (keys[K_y] and keys[K_LCTRL] and keypress==True):
        if len(redolist)>0:
            undolist.append(redolist[-1])
            screen.blit(redolist[-1],(260,10))
            del redolist[-1]

    #this has to be blitted on top of the boxes, therefore afterwards
    screen.blit(undo,(32,612))
    screen.blit(redo,(177,612))

    #flip functions
    if flipbox.collidepoint((mx,my)):
        draw.rect(screen,white,flipbox)
        draw.rect(screen,red,invertbox)
        
    if (mp[0]==1 and flipbox.collidepoint((mx,my))) or (keys[K_LCTRL] and (keys[K_LEFT] or keys[K_RIGHT])):
        if click==True or keypress==True:
            flipcopy=transform.flip(screen.subsurface(canvas),True,False)
            screen.blit(flipcopy,(260,10))
        
    if invertbox.collidepoint((mx,my)):
        draw.rect(screen,red,flipbox)
        draw.rect(screen,white,invertbox)
        
    if (mp[0]==1 and invertbox.collidepoint((mx,my))) or (keys[K_LCTRL] and (keys[K_UP] or keys[K_DOWN])):
        if click==True or keypress==True:
            invertcopy=transform.flip(screen.subsurface(canvas),False,True)
            screen.blit(invertcopy,(260,10))
        
    screen.blit(flip,(32,662))
    screen.blit(inversion,(177,662))
    
    #save/load functions
    if savebox.collidepoint((mx,my)):
        draw.rect(screen,white,savebox)
        draw.rect(screen,red,loadbox)
        
    if (mp[0]==1 and savebox.collidepoint((mx,my))) or (keys[K_s] and keys[K_LCTRL]):
        savename=filedialog.asksaveasfilename(defaultextension=".png")
        if savename!="":
            image.save(screen.subsurface(canvas),savename)
        
    if loadbox.collidepoint((mx,my)):
        draw.rect(screen,red,savebox)
        draw.rect(screen,white,loadbox)
        
    if (mp[0]==1 and loadbox.collidepoint((mx,my))) or (keys[K_v] and keys[K_LCTRL]):
        loadname=filedialog.askopenfilename(filetypes=[("Images","*.png")])
        if loadname!="":
            loadnameimage=image.load(loadname)
            loadnamewidth=loadnameimage.get_width()
            loadnameheight=loadnameimage.get_height()
            #if the height or width is bigger than the canvas the image resizes
            #if only the height is bigger the height is changed, same with widrh
            #but if both are bigger the whole image is resized
            #unfortunately it skews the image, but I couldn't understand
            #the code necessary to resize with the aspect ratio intact.
            if loadnamewidth>750:
                loadnameimage=transform.smoothscale(loadnameimage,(750,loadnameheight))
            if loadnameheight>510:
                loadnameimage=transform.smoothscale(loadnameimage,(loadnamewidth,510))
            if loadnamewidth>750 and loadnameheight>510:
                loadnameimage=transform.smoothscale(loadnameimage,(750,510))
            screen.blit(loadnameimage,(260,10))
        
    screen.blit(save,(32,712))
    screen.blit(load,(177,712))
    #--------------------------------------------
    display.flip()
    
font.quit()
del typeface
quit()
