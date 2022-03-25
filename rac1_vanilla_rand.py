from tkinter import *
from tkinter import font as tkFont
from PIL import ImageTk, Image
import pyglet, os
from randomize import randomize
import webbrowser

# If you have purchased SimianDisplay (the original rac1 font), you can
# Add the otf file to the fonts folder and change this to 1 (personal use only)
fontFree = 1


root = Tk()
root.title("R&C1 Vanilla Randomizer")
root.geometry("440x710")
root.minsize(440,710)
root.maxsize(440,710)
root['bg']='#000000'
root.iconbitmap("images/randoIcon.ico")

usefont = (1-fontFree)*'SimianDisplay' + (fontFree)*'Sansation'
if(fontFree):
    pyglet.font.add_file('fonts/'+usefont+'.ttf')
    pyglet.font.add_file('fonts/'+usefont+'-Bold.ttf')
else:
    pyglet.font.add_file('fonts/'+usefont+'.otf')

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = self.widget.winfo_pointerx() + 5
        y = self.widget.winfo_pointery() + 5
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT, fg='#586aa5',
                      bg="black", relief=RIDGE, borderwidth=3,
                      font=(usefont, "12", "normal"))
        label.pack(ipadx=6, ipady=4)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, textE, textD=''):
    toolTip = ToolTip(widget)
    def enter(event):
        if widget['state'] == DISABLED:
            toolTip.showtip(textD)
        else:
            toolTip.showtip(textE)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def YellowHighlight(widget):
    def enter(event):
        widget['fg'] = '#bab401'
    def leave(event):
        widget['fg'] = '#586aa5'
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

def bgColor():
    global btnPaint
    if(root['bg']=='#000000'):
        root['bg']='#ff00ff'
        btnPaint['bg']='#ff00ff'
        btnPaint['activebackground']='#ff00ff'
    else:
        root['bg']='#000000'
        btnPaint['bg']='#000000'
        btnPaint['activebackground']='#000000'

def alaLink():
    webbrowser.open_new("https://www.twitch.tv/alados5")


global packless, ilj_snflip, batalia_si, oltanis_mb, tree_skip
packless   = 0
ilj_snflip = 0
batalia_si = 0
tree_skip  = 0
oltanis_mb = 0

def toggleS1():
    global packless, btnS1, imgYN
    packless ^= 1
    btnS1['image']=imgYN[packless]
    btnS1['fg'] ='#bab401'*packless + '#586aa5'*(1-packless)

def toggleS2():
    global ilj_snflip, btnS2, imgYN
    ilj_snflip ^= 1
    btnS2['image']=imgYN[ilj_snflip]
    btnS2['fg'] ='#bab401'*ilj_snflip + '#586aa5'*(1-ilj_snflip)

def toggleS3():
    global batalia_si, btnS3, imgYN
    batalia_si ^= 1
    btnS3['image']=imgYN[batalia_si]
    btnS3['fg'] ='#bab401'*batalia_si + '#586aa5'*(1-batalia_si)

def toggleS4():
    global tree_skip, btnS4, imgYN
    tree_skip ^= 1
    btnS4['image']=imgYN[tree_skip]
    btnS4['fg'] ='#bab401'*tree_skip + '#586aa5'*(1-tree_skip)

def toggleS5():
    global oltanis_mb, btnS5, imgYN
    oltanis_mb ^= 1
    btnS5['image']=imgYN[oltanis_mb]
    btnS5['fg'] ='#bab401'*oltanis_mb + '#586aa5'*(1-oltanis_mb)

def init_rando():
    global packless, ilj_snflip, batalia_si, oltanis_mb, tree_skip, RNGsol
    for widget in root.winfo_children():
        widget.destroy()
    RNGsol = randomize(packless, ilj_snflip, batalia_si, tree_skip, oltanis_mb)
    root.quit()

def choose_strats():
    global imgYN, btnPaint
    virtual_img = PhotoImage(width=1, height=1)
    imgCRT = Image.open('images/crtFrame.png')
    imgCRTf = Image.open('images/crtFrameFlat.png')
    imgTitle = ImageTk.PhotoImage(Image.open('images/crtTitle.png'))
    imgInfo = ImageTk.PhotoImage(imgCRT.crop([3,0,348,120]).resize((350,80),Image.ANTIALIAS))
    imgStrat = ImageTk.PhotoImage(imgCRTf.resize((350,50),Image.ANTIALIAS))
    imgInit = ImageTk.PhotoImage(imgCRTf.resize((350,60),Image.ANTIALIAS))
    imgPaint = ImageTk.PhotoImage(file='images/paint.png')
    imgAla2 = ImageTk.PhotoImage(Image.open('images/alados5.png').resize((35,35),Image.ANTIALIAS))

    imgNo  = Image.open('images/radio_no.png').resize((24,24),Image.ANTIALIAS)
    imgYes = Image.open('images/radio_yes.png').resize((24,24),Image.ANTIALIAS)
    imgStratN = imgCRTf.crop([4,3,348,59]).resize((350,50),Image.ANTIALIAS)
    imgStratY = imgCRTf.resize((350,50),Image.ANTIALIAS)
    imgStratN.paste(imgNo, (313,13), mask=imgNo)
    imgStratY.paste(imgYes, (313,13), mask=imgYes)
    imgStratN = ImageTk.PhotoImage(imgStratN)
    imgStratY = ImageTk.PhotoImage(imgStratY)
    imgYN = [imgStratN, imgStratY]
    #banWi.paste(imgBan, (0,0), mask=imgBan)

    fontSz = 18-2*fontFree

    btnPaint = Button(root, image=imgPaint, relief=FLAT, bg='black', borderwidth=0,
                      activebackground='#000000', command=bgColor)
    btnPaint.place(width=35,height=35, x=5,y=5)
    CreateToolTip(btnPaint, 'Swap background color:\nBlack (#000000) / Magenta (#FF00FF)')

    btnAla2 = Button(root, image=imgAla2, relief=FLAT, bg='black', borderwidth=0,
                     activebackground='#000000', command=alaLink)
    btnAla2.place(width=35,height=35, x=400,y=670)
    CreateToolTip(btnAla2, 'Come say hi on Twitch! (Alados5)')

    btnTitle = Label(root, image=imgTitle, borderwidth=5, relief=RIDGE,
                     bg='#66684B', fg='#c4c4c4')
    btnTitle.place(width=350,height=120, x=45,y=45)

    btnInfo = Label(root, text="Which of these hard strats are\nyou willing to perform in a run?",
                    image=imgInfo, compound='c', borderwidth=5, relief=RIDGE,
                    font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                    bg='#66684B', fg='#586aa5')
    btnInfo.place(width=350,height=80, x=45,y=195)


    global btnS1, btnS1Box, btnS2, btnS2Box, btnS3, btnS3Box, btnS4, btnS4Box, btnS5, btnS5Box

    btnS1 = Button(root, text="Packless", image=imgStratN,
                   compound='c', borderwidth=5, relief=RIDGE, command=toggleS1,
                   font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                   bg='#66684B', fg='#586aa5')
    btnS1.place(width=350,height=50, x=45,y=285)
    CreateToolTip(btnS1, 'You might get all pack gadgets banned on any planet.\n'
                         'This is especially hard on Kerwan, Eudora and Rilgar.')

    btnS2 = Button(root, text="ILJs and Sinaflips", image=imgStratN,
                   compound='c', borderwidth=5, relief=RIDGE, command=toggleS2,
                   font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                   bg='#66684B', fg='#586aa5')
    btnS2.place(width=350,height=50, x=45,y=345)
    CreateToolTip(btnS2, 'You might have to do Infinite Long Jumps (ILJs)\n'
                         'or Sinaflips to progress, which can be hard to master.')

    btnS3 = Button(root, text="Batalia SIs", image=imgStratN,
                   compound='c', borderwidth=5, relief=RIDGE, command=toggleS3,
                   font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                   bg='#66684B', fg='#586aa5')
    btnS3.place(width=350,height=50, x=45,y=405)
    CreateToolTip(btnS3, 'You might have to do a long chain of Slope Intercepts (SIs)\n'
                         "on Batalia's mountains to get the Gaspar Infobot.")

    btnS4 = Button(root, text="Orxon 1 Tree Skip", image=imgStratN,
                   compound='c', borderwidth=5, relief=RIDGE, command=toggleS4,
                   font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                   bg='#66684B', fg='#586aa5')
    btnS4.place(width=350,height=50, x=45,y=465)
    CreateToolTip(btnS4, 'On Orxon 1 (Clank level), you might have to perform\n'
                         "the Tree Skip to then proxy to the end of the level.")

    btnS5 = Button(root, text="Oltanis Wall Magneboots", image=imgStratN,
                   compound='c', borderwidth=5, relief=RIDGE, command=toggleS5,
                   font=tkFont.Font(family=usefont, size=fontSz, weight='normal'),
                   bg='#66684B', fg='#586aa5')
    btnS5.place(width=350,height=50, x=45,y=525)
    CreateToolTip(btnS5, 'On Oltanis, you might need to continue using the Magneboots\n'
                         "to walk on the wall near the start (no PDA/Grindboots).")


    btnInit = Button(root, text="RANDOMIZE!", image=imgInit, command=init_rando,
                     compound='c', borderwidth=5, relief=RIDGE,
                     font=tkFont.Font(family=usefont, size=24, weight='bold'),
                     bg='#66684B', fg='#586aa5')
    btnInit.place(width=350,height=60, x=45,y=605)
    YellowHighlight(btnInit)

    root.mainloop()


choose_strats()

#----------
#  PAGE 2
#----------

# PREVIOUS AND NEXT
def prevP():
    global idxP
    idxP-=1
    if(idxP<0):
        idxP=len(imgP)-1
    if(idxP+1==18 and not KIII):
        idxP-=1
    btnP.config(image=imgP[idxP])
    btnPN.config(text=nameP[idxP])
    # Update Pools and Selections
    for w in range(16):
        btnW[w]['state'] = DISABLED
        banW[w].place(height=0,width=0)
    for w in PW[idxP+1]:
        btnW[w]['state'] = NORMAL
        if w not in RSW[idxP+1]:
            banW[w].place(height=50,width=50)
    for g in range(14):
        btnG[g]['state'] = DISABLED
        banG[g].place(height=0,width=0)
    for g in PG[idxP+1]:
        btnG[g-1]['state'] = NORMAL
        if g not in RSG[idxP+1]:
            banG[g-1].place(height=50,width=50)
    for c in range(2):
        btnC[c]['state'] = DISABLED
        banC[c].place(height=0,width=0)
    if idxP+1 in PC:
        for c in PC[idxP+1]:
            btnC[c-1]['state'] = NORMAL
            if c not in RSC[idxP+1]:
                banC[c-1].place(height=50,width=50)
    for gc in range(3):
        btnGC[gc]['state'] = DISABLED
        banGC[gc].place(height=0,width=0)
    if idxP+1 in PGC:
        for gc in PGC[idxP+1]:
            btnGC[gc-1]['state'] = NORMAL
            if gc not in RSGC[idxP+1]:
                banGC[gc-1].place(height=50,width=50)

def nextP():
    global idxP
    idxP+=1
    if(idxP>=len(imgP)):
        idxP=0
    if(idxP+1==18 and not KIII):
        idxP+=1
    btnP.config(image=imgP[idxP])
    btnPN.config(text=nameP[idxP])
    # Update Pools and Selections
    for w in range(16):
        btnW[w]['state'] = DISABLED
        banW[w].place(height=0,width=0)
    for w in PW[idxP+1]:
        btnW[w]['state'] = NORMAL
        if w not in RSW[idxP+1]:
            banW[w].place(height=50,width=50)
    for g in range(14):
        btnG[g]['state'] = DISABLED
        banG[g].place(height=0,width=0)
    for g in PG[idxP+1]:
        btnG[g-1]['state'] = NORMAL
        if g not in RSG[idxP+1]:
            banG[g-1].place(height=50,width=50)
    for c in range(2):
        btnC[c]['state'] = DISABLED
        banC[c].place(height=0,width=0)
    if idxP+1 in PC:
        for c in PC[idxP+1]:
            btnC[c-1]['state'] = NORMAL
            if c not in RSC[idxP+1]:
                banC[c-1].place(height=50,width=50)
    for gc in range(3):
        btnGC[gc]['state'] = DISABLED
        banGC[gc].place(height=0,width=0)
    if idxP+1 in PGC:
        for gc in PGC[idxP+1]:
            btnGC[gc-1]['state'] = NORMAL
            if gc not in RSGC[idxP+1]:
                banGC[gc-1].place(height=50,width=50)


def ArrowHover(widget,dir):
    imgDir  = [imgPrev,  imgNext]
    imgDirY = [imgPrevY, imgNextY]
    def enter(event):
        widget['image'] = imgDirY[dir]
    def leave(event):
        widget['image'] = imgDir[dir]
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# IMAGES
virtual_img = PhotoImage(width=1, height=1)
imgCRT = Image.open('images/crtFrame.png')
imgCRTf = Image.open('images/crtFrameFlat.png')
imgCRTt = Image.open('images/crtFrameTall.png')
imgBan = Image.open('images/banned.png')

#(60,90) (80,120)
imgPrev = ImageTk.PhotoImage(Image.open('images/arrowPrev.png').resize((80,120),Image.ANTIALIAS))
imgNext = ImageTk.PhotoImage(Image.open('images/arrowNext.png').resize((80,120),Image.ANTIALIAS))
imgPrevY = ImageTk.PhotoImage(Image.open('images/arrowPrevY.png').resize((80,120),Image.ANTIALIAS))
imgNextY = ImageTk.PhotoImage(Image.open('images/arrowNextY.png').resize((80,120),Image.ANTIALIAS))


# BLANK CRT FRAMES
imgCRTp = ImageTk.PhotoImage(imgCRT.crop([4,5,348,116]).resize((400,180),Image.ANTIALIAS))
btnCRTp = Label(root, image=imgCRTp, height=180, width=400,
              borderwidth=5, relief=RIDGE, bg='#2f2f2f')
btnCRTp.place(height=180, width=400, x=20,y=20)
imgCRTc = ImageTk.PhotoImage(imgCRT.crop([5,2,347,120]).resize((400,80),Image.ANTIALIAS))
btnCRTc = Label(root, image=imgCRTc, height=80, width=400,
              borderwidth=5, relief=RIDGE, bg='#2f2f2f')
btnCRTc.place(height=80, width=400, x=20,y=290)
imgCRTw = ImageTk.PhotoImage(imgCRTt.resize((190,300),Image.ANTIALIAS))
btnCRTw = Label(root, image=imgCRTw, height=300, width=190,
              borderwidth=5, relief=RIDGE, bg='#2f2f2f')
btnCRTw.place(height=300, width=190, x=20,y=390)
imgCRTg = ImageTk.PhotoImage(imgCRTt.resize((190,300),Image.ANTIALIAS))
btnCRTg = Label(root, image=imgCRTg, height=300, width=190,
              borderwidth=5, relief=RIDGE, bg='#2f2f2f')
btnCRTg.place(height=300, width=190, x=230,y=390)


# ARROWS
btnPrev = Button(root, image=imgPrev, borderwidth=0, relief=FLAT, command=prevP,
                 bg='black', activebackground='black')
btnPrev.place(height=120,width=80,x=50,y=50)
ArrowHover(btnPrev,0)

btnNext = Button(root, image=imgNext, borderwidth=0, relief=FLAT, command=nextP,
                 bg='black', activebackground='black')
btnNext.place(height=120,width=80,x=310,y=50)
ArrowHover(btnNext,1)


# ACTIVE PLANET INDEX
global idxP
idxP = 0

# ALL PLANETS
imgP = []
nameP = ["Veldin 1", "Novalis", "Kerwan", "Aridia", "Eudora",
         "Nebula G34", "Rilgar", "Umbris", "Batalia", "Orxon 1",
         "Gaspar", "Pokitaru", "Orxon 2", "Hoven", "Gemlik Base",
         "Oltanis", "Quartu", "Kalebo III", "Drek's Fleet", "Veldin 2"]
for btnPi in range(len(nameP)):
    filePi = 'images/P'+str(btnPi+1)+'.png'
    imgP.append(ImageTk.PhotoImage(file=filePi))

btnP = Label(root, image=imgP[idxP], borderwidth=0, relief=FLAT,
             bg='black', activebackground='black')
btnP.place(height=150,width=150,x=145,y=35)

imgPN = ImageTk.PhotoImage(imgCRT.resize((250,60),Image.ANTIALIAS))
btnPN = Label(root, text=nameP[idxP], image=imgPN, height=60, width=250,
              compound = 'c', borderwidth=5, relief=RIDGE,
              font=tkFont.Font(family=usefont, size=30-2*fontFree, weight='normal'),
              bg='#2f2f2f', fg='#586aa5')
btnPN.place(height=60, width=250, x=95,y=210)


# ALL WEAPONS
btnW = []
imgW = []
banW = []
bimgW = []
nameW = ["Bomb Glove", "Pyrocitor", "Blaster", "Glove of Doom", "Suck Cannon",
         "Taunter", "Mine Glove", "Devastator", "Visibomb Gun", "Walloper",
         "Decoy Glove", "Drone Device", "Tesla Claw", "Morph-o-Ray", "RYNO"]
for btnWi in range(len(nameW)):
    fileWi = 'images/W'+str(btnWi+1)+'.png'
    imgW.append(ImageTk.PhotoImage(file=fileWi))
    btnW.append(Label(root, image=imgW[btnWi], borderwidth=0, relief=FLAT, state=DISABLED))
    btnW[btnWi].place(height=50,width=50,x=35+55*(btnWi//5),y=405+55*(btnWi%5))
    banWi = Image.open(fileWi)
    banWi.paste(imgBan, (0,0), mask=imgBan)
    bimgW.append(ImageTk.PhotoImage(banWi))
    banW.append(Label(root, image=bimgW[btnWi], borderwidth=0, relief=FLAT))
    banW[btnWi].place(height=0,width=0,x=35+55*(btnWi//5),y=405+55*(btnWi%5))
    CreateToolTip(btnW[btnWi], ('The '+nameW[btnWi]+' is allowed!'), 'Unavailable (cannot be used on revisits!)')
    CreateToolTip(banW[btnWi], ('The '+nameW[btnWi]+' is banned!'), 'Unavailable (cannot be used on revisits!)')


# ALL GADGETS
btnG = []
imgG = []
banG = []
bimgG = []
nameG = ["Trespasser", "Hydrodisplacer", "Swingshot",
         "PDA", "Metal Detector", "Holo-Guise",
         "Heli-Pack", "Thruster-Pack", "Hydro-Pack",
         "O2 Mask", "Sonic Summoner", "Pilot's Helmet",
         "Grindboots", "Magneboots"]
for btnGi in range(len(nameG)):
    fileGi = 'images/G'+str(btnGi+1)+'.png'
    imgG.append(ImageTk.PhotoImage(file=fileGi))
    btnG.append(Label(root, image=imgG[btnGi], borderwidth=0, relief=FLAT, state=DISABLED))
    btnG[btnGi].place(height=50,width=50,x=245+55*(btnGi%3),y=405+55*(btnGi//3))
    banGi = Image.open(fileGi)
    banGi.paste(imgBan, (0,0), mask=imgBan)
    bimgG.append(ImageTk.PhotoImage(banGi))
    banG.append(Label(root, image=bimgG[btnGi], borderwidth=0, relief=FLAT))
    banG[btnGi].place(height=0,width=0,x=245+55*(btnGi%3),y=405+55*(btnGi//3))
    is_are = (btnGi-12<0)*' is ' + (btnGi-12>=0)*' are '
    CreateToolTip(btnG[btnGi], ('The '+nameG[btnGi]+is_are+'allowed!'), 'Unavailable (cannot be used on revisits!)')
    CreateToolTip(banG[btnGi], ('The '+nameG[btnGi]+is_are+'banned!'), 'Unavailable (cannot be used on revisits!)')

# WRENCH, CLANK, GIANT CLANK
nameW = ["Wrench"] + nameW
imgW = [ImageTk.PhotoImage(file='images/W0.png')] + imgW
btnW = [Label(root, image=imgW[0], borderwidth=0, relief=FLAT, state=DISABLED)] + btnW
btnW[0].place(height=50,width=50,x=35,y=305)
banWi = Image.open('images/W0.png')
banWi.paste(imgBan, (0,0), mask=imgBan)
bimgW = [ImageTk.PhotoImage(banWi)] + bimgW
banW = [Label(root, image=bimgW[0], borderwidth=0, relief=FLAT)] + banW
banW[0].place(height=0,width=0,x=35,y=305)
CreateToolTip(btnW[0], ('The '+nameW[0]+' is allowed!'), 'Unavailable (cannot be used on revisits!)')
CreateToolTip(banW[0], ('The '+nameW[0]+' is banned!'), 'Unavailable (cannot be used on revisits!)')

btnC = []
imgC = []
banC = []
bimgC = []
nameC = ["Clank", "Gadgebots"]
for btnCi in range(len(nameC)):
    fileCi = 'images/C'+str(btnCi+1)+'.png'
    imgC.append(ImageTk.PhotoImage(file=fileCi))
    btnC.append(Label(root, image=imgC[btnCi], borderwidth=0, relief=FLAT, state=DISABLED))
    btnC[btnCi].place(height=50,width=50,x=115+55*btnCi,y=305)
    banCi = Image.open(fileCi)
    banCi.paste(imgBan, (0,0), mask=imgBan)
    bimgC.append(ImageTk.PhotoImage(banCi))
    banC.append(Label(root, image=bimgC[btnCi], borderwidth=0, relief=FLAT))
    banC[btnCi].place(height=0,width=0,x=115+55*btnCi,y=305)
CreateToolTip(btnC[0], 'You can play as Clank!', 'No Clank section here')
CreateToolTip(banC[0], 'Playing as Clank is banned!')
CreateToolTip(btnC[1], 'Clank can use Gadgebots!', 'No Clank section here')
CreateToolTip(banC[1], 'Gadgebot attacks are banned!')

btnGC = []
imgGC = []
banGC = []
bimgGC = []
nameGC = ["Punches", "Missiles", "Bombs"]
for btnGCi in range(len(nameGC)):
    fileGCi = 'images/GC'+str(btnGCi+1)+'.png'
    imgGC.append(ImageTk.PhotoImage(file=fileGCi))
    btnGC.append(Label(root, image=imgGC[btnGCi], borderwidth=0, relief=FLAT, state=DISABLED))
    btnGC[btnGCi].place(height=50,width=50,x=245+55*btnGCi,y=305)
    banGCi = Image.open(fileGCi)
    banGCi.paste(imgBan, (0,0), mask=imgBan)
    bimgGC.append(ImageTk.PhotoImage(banGCi))
    banGC.append(Label(root, image=bimgGC[btnGCi], borderwidth=0, relief=FLAT))
    banGC[btnGCi].place(height=0,width=0,x=245+55*btnGCi,y=305)
    CreateToolTip(btnGC[btnGCi], ('Giant Clank can use '+nameGC[btnGCi]), 'Giant Clank unavailable')
    CreateToolTip(banGC[btnGCi], ('Giant Clank cannot use '+nameGC[btnGCi]))


global RNGsol
# return PW, PG, PC, PGC, RSW, RSG, RSC, RSGC

PW   = RNGsol[0]
PG   = RNGsol[1]
PC   = RNGsol[2]
PGC  = RNGsol[3]
RSW  = RNGsol[4]
RSG  = RNGsol[5]
RSC  = RNGsol[6]
RSGC = RNGsol[7]
KIII = RNGsol[8]

# DEBUGGING!
#print("Weapon pools: ", PW,  "\nSelected Weapons: ", RSW)
#print("Clank pools:  ", PC,  "\nSelected Clank:   ", RSC)
#print("GClank pools: ", PGC, "\nSelected GClank:  ", RSGC)
#print("Gadget pools: ", PG,  "\nSelected Gadgets: ", RSG)
#print("Kalebo III: ", KIII)

for w in PW[idxP+1]:
    btnW[w]['state'] = NORMAL
    if w not in RSW[idxP+1]:
        banW[w].place(height=50,width=50)

root.mainloop()








#
