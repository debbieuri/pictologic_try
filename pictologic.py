
import sys
import pygame
pygame.init()

class slider:
    def __init__(self,pos,length,valrange):
        self.pos=pos
        self.length=length
        self.valrange=valrange
        self.v=0
    def t(self):
        pos=pygame.mouse.get_pos()
        if pos[0]-self.pos[0]>=0 and pos[0]-self.pos[0]<self.length:
            if abs(pos[1]-self.pos[1])<10:
                self.v=pos[0]-self.pos[0]
    def getvalue(self):
        return int(self.valrange[0]+self.v*(self.valrange[1]-self.valrange[0])/self.length)
    def show(self,surf):
        pygame.draw.line(surf,(255,255,0),self.pos,(self.pos[0]+self.length,self.pos[1]),3)
        pygame.draw.rect(surf,(255,255,0),(self.pos[0]+self.v-2,self.pos[1]-5,4,10))


class game:
    def __init__(self):
        self.d=pygame.display.set_mode([1000,700],pygame.RESIZABLE,depth=10)
        pygame.display.set_caption('pictologic')
        self.font=pygame.font.Font('munro-narrow.ttf',40)
        self.clock=pygame.time.Clock()

    def show_text(self,surf,font,color,pos,msg):
        t=font.render(str(msg),True,color)
        surf.blit(t,pos)

    def start(self):
        a=pygame.rect.Rect(10,10,200,50)
        b=pygame.rect.Rect(10,70,200,50)
        while True:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.MOUSEBUTTONUP:
                    p=pygame.mouse.get_pos()
                    if a.collidepoint(p):
                        self.play()
                    if b.collidepoint(p):
                        self.makelevel()
            self.d.fill((0,0,0))
            pygame.draw.rect(self.d,(255,255,255),a)
            self.show_text(self.d,self.font,(255,0,0),(a[0]+5,a[1]),'PLAY')
            pygame.draw.rect(self.d,(255,255,255),b)
            self.show_text(self.d,self.font,(255,0,0),(b[0]+5,b[1]),'MAKE LEVEL')
            pygame.display.update()
            self.clock.tick(60)

    def makelevel(self):
        a=pygame.rect.Rect(10,10,300,50)
        b=pygame.rect.Rect(10,70,300,50)
        c=pygame.rect.Rect(10,130,300,50)
        self.d.fill((0,0,0))
        pygame.draw.rect(self.d,(255,255,255),a)
        self.show_text(self.d,self.font,(255,0,0),(a[0]+5,a[1]),'<---RETURN')
        pygame.draw.rect(self.d,(255,255,255),b)
        self.show_text(self.d,self.font,(255,0,0),(b[0]+5,b[1]),'DRAW LEVEL')
        pygame.draw.rect(self.d,(255,255,255),c)
        self.show_text(self.d,self.font,(255,0,0),(c[0]+5,c[1]),'FROM AN IMAGE FILE')
        pygame.display.update()
        while True:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.MOUSEBUTTONUP:
                    p=pygame.mouse.get_pos()
                    if a.collidepoint(p):
                        return
                    if b.collidepoint(p):
                        menu=False
                        self.drawlevel()
                        return
                    if c.collidepoint(p):
                        self.dalkjfdalkjfdalkjf()
                        return
            self.clock.tick(60)

    def sizeit(self,sizer,b):#b?
        self.sizer=sizer
        self.gfont=pygame.font.Font('munro-narrow.ttf',self.sizer)
        if b:
            self.checkmarkimg = pygame.transform.scale(pygame.image.load('check.png'),(self.sizer-4,self.sizer-4))
            self.clearimg = pygame.transform.scale(pygame.image.load('clear.png'),(self.sizer-4,self.sizer-4))
        else:
            self.checkmarkimg = pygame.transform.scale(pygame.image.load('check.png'),(self.sizer,self.sizer))
            self.clearimg = pygame.transform.scale(pygame.image.load('clear.png'),(self.sizer,self.sizer))

    def savelevel(self,level):
        if not self.levelpossible(level):
            if input('not possible/more than 1 solution. save anyway? yes for yes')!='yes':
                return
        c=str(len(level))+' '+str(len(level[0]))+' '
        for x in range(len(level)):
            for y in range(len(level[0])):
                if level[x][y]:
                    c=c+'1'
                else:
                    c=c+'0'
        f=open('saves.txt','a')
        levelname=input('name your level:')
        f.write('\n'+levelname+' '+c)
        f.close()
        print('saved!')

    def dalkjfdalkjfdalkjf(self):
        name=input('enter image filename with the end part too:')
        img=pygame.image.load(name)
        bimg=pygame.transform.scale(img,(300,img.get_width()/img.get_height()*300))
        buffer=[20,20]
        wslider=slider((buffer[0],bimg.get_height()+buffer[1]+20),300,[4,50])
        hslider=slider((buffer[0],bimg.get_height()+buffer[1]+40),300,[4,50])
        rslider=slider((buffer[0],bimg.get_height()+buffer[1]+80),300,[1,254])
        gslider=slider((buffer[0],bimg.get_height()+buffer[1]+100),300,[1,254])
        bslider=slider((buffer[0],bimg.get_height()+buffer[1]+120),300,[1,254])
        ri=pygame.rect.Rect(rslider.pos[0]+rslider.length+buffer[0],rslider.pos[1]-10,20,20)
        gi=pygame.rect.Rect(gslider.pos[0]+gslider.length+buffer[0],gslider.pos[1]-10,20,20)
        bi=pygame.rect.Rect(bslider.pos[0]+bslider.length+buffer[0],bslider.pos[1]-10,20,20)
        ii=[True,True,True]
        cc=[(255,0,0),(0,255,0)]
        checkmarkimg=pygame.transform.scale(pygame.image.load('check.png'),(50,50))
        self.sizeit(20,False)
        self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,self.d.get_height()-50-10,200,50)
        checkbutton=pygame.rect.Rect(self.returnbutton[0]-60,self.returnbutton[1],50,50)
        click=False
        self.m=[[0]]
        while True:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.WINDOWRESIZED:
                    self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,self.d.get_height()-50-10,200,50)
                    checkbutton=pygame.rect.Rect(self.returnbutton[0]-60,self.returnbutton[1],50,50)
                if e.type==pygame.MOUSEBUTTONDOWN:
                    click=True
                    p=pygame.mouse.get_pos()
                    if self.returnbutton.collidepoint(p):
                        if input('are you sure you want to leave? yes for yes')=='yes':
                            return
                    if checkbutton.collidepoint(p):
                        self.savelevel(self.m)
                    if ri.collidepoint(p):
                        ii[0]=not ii[0]
                    if gi.collidepoint(p):
                        ii[1]=not ii[1]
                    if bi.collidepoint(p):
                        ii[2]=not ii[2]
                if e.type==pygame.MOUSEBUTTONUP:
                    click=False
            if click:#pygame.mouse.getclicked ???d 
                wslider.t()
                hslider.t()
                rslider.t()
                gslider.t()
                bslider.t()
            self.d.fill((0,0,0))
            wslider.show(self.d)
            hslider.show(self.d)
            rslider.show(self.d)
            gslider.show(self.d)
            bslider.show(self.d)
            self.show_text(self.d,self.gfont,(255,255,0),(wslider.pos[0]+wslider.length+buffer[0]+10,wslider.pos[1]-10),str(wslider.getvalue()))
            self.show_text(self.d,self.gfont,(255,255,0),(hslider.pos[0]+hslider.length+buffer[0]+10,hslider.pos[1]-10),str(hslider.getvalue()))
            self.show_text(self.d,self.gfont,(255,255,0),(ri[0]+ri[2]+10,ri[1]),str(rslider.getvalue()))
            self.show_text(self.d,self.gfont,(255,255,0),(gi[0]+gi[2]+10,gi[1]),str(gslider.getvalue()))
            self.show_text(self.d,self.gfont,(255,255,0),(bi[0]+bi[2]+10,bi[1]),str(bslider.getvalue()))
            pygame.draw.rect(self.d,cc[ii[0]],ri)
            pygame.draw.rect(self.d,cc[ii[1]],gi)
            pygame.draw.rect(self.d,cc[ii[2]],bi)
            
            self.d.blit(bimg,buffer)

            n=self.getimgthing(img,wslider.getvalue(),hslider.getvalue())
            self.sizer=min(bimg.get_width()/wslider.getvalue(),bimg.get_height()/hslider.getvalue())
            for x in range(wslider.getvalue()):
                for y in range(hslider.getvalue()):
                    pygame.draw.rect(self.d,n[x][y],(x*self.sizer+buffer[0]+buffer[0]+bimg.get_width(),y*self.sizer+buffer[1],self.sizer,self.sizer))
            self.m=[[(((n[x][y][0]<rslider.getvalue())==ii[0]) and ((n[x][y][1]<gslider.getvalue())==ii[1]) and ((n[x][y][2]<bslider.getvalue())==ii[2])) for y in range(hslider.getvalue())] for x in range(wslider.getvalue())]
            for x in range(wslider.getvalue()):
                for y in range(hslider.getvalue()):
                    if self.m[x][y]:
                        pygame.draw.rect(self.d,(0,0,0),(x*self.sizer+buffer[0]+buffer[0]+buffer[0]+bimg.get_width()+bimg.get_width(),y*self.sizer+buffer[1],self.sizer,self.sizer))
                    else:
                        pygame.draw.rect(self.d,(255,255,255),(x*self.sizer+buffer[0]+buffer[0]+buffer[0]+bimg.get_width()+bimg.get_width(),y*self.sizer+buffer[1],self.sizer,self.sizer))

            self.d.blit(checkmarkimg,(checkbutton[0],checkbutton[1]))
            pygame.draw.rect(self.d,(255,255,255),self.returnbutton)
            self.show_text(self.d,self.font,(255,0,0),(self.returnbutton[0]+5,self.returnbutton[1]),'<---RETURN')
            pygame.display.update()
            self.clock.tick(60)

    def getimgthing(self,img,w,h):#useless..?
        n=[[0 for y in range(h)] for x in range(w)]
        for x in range(w):
            for y in range(h):
                n[x][y]=pygame.transform.average_color(img,(x*img.get_width()/w,y*img.get_height()/h,img.get_width()/w,img.get_height()/h))
        return n

    def drawlevel(self):#making...
        print('arrow keys to expand and despand')
        self.game=[[0 for y in range(10)] for x in range(10)]
        self.sizeit(30,False)
        buffer=[20,20]
        self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,10,200,50)
        self.placing=1
        click=False
        oldpos=[-1,-1]
        while True:
            self.d.fill((200,100,200))
            for x in range(len(self.game)):
                for y in range(len(self.game[0])):
                    if self.game[x][y]==0:
                        pygame.draw.rect(self.d,(255,255,255),(x*self.sizer+buffer[0],y*self.sizer+buffer[1],self.sizer,self.sizer))
                    else:
                        pygame.draw.rect(self.d,(0,0,0),(x*self.sizer+buffer[0],y*self.sizer+buffer[1],self.sizer,self.sizer))
            self.d.blit(self.checkmarkimg,(len(self.game)*self.sizer+buffer[0],(len(self.game[0])-1)*self.sizer+buffer[1]))
            pygame.draw.rect(self.d,(255,255,255),(len(self.game)*self.sizer+buffer[0],(len(self.game[0])-2)*self.sizer+buffer[1],self.sizer,self.sizer))
            pygame.draw.rect(self.d,(0,0,0),(len(self.game)*self.sizer+buffer[0],(len(self.game[0])-3)*self.sizer+buffer[1],self.sizer,self.sizer))
            pygame.draw.rect(self.d,(255,255,255),self.returnbutton)
            self.show_text(self.d,self.font,(255,0,0),(self.returnbutton[0]+5,self.returnbutton[1]),'<---RETURN')
            pygame.display.update()
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.WINDOWRESIZED:
                    self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,10,200,50)
                if e.type==pygame.KEYDOWN:
                    if e.key==pygame.K_LEFT:
                        if len(self.game)>4:##min
                            self.game.pop(-1)
                    if e.key==pygame.K_RIGHT:
                        if len(self.game)<100:##max
                            self.game.append([0 for i in range(len(self.game[0]))])
                    if e.key==pygame.K_UP:
                        if len(self.game[0])>4:##min
                            for i in range(len(self.game)):
                                self.game[i].pop(-1)
                    if e.key==pygame.K_DOWN:
                        if len(self.game[0])<100:##max
                            for i in range(len(self.game)):
                                self.game[i].append(0)
                    self.returnbutton=pygame.rect.Rect(buffer[0]+len(self.game)*self.sizer+self.sizer+buffer[0],buffer[1],200,50)
                if e.type==pygame.MOUSEBUTTONDOWN:
                    click=True
                    p=pygame.mouse.get_pos()
                    if self.returnbutton.collidepoint(p):
                        if input('are you sure you want to leave? yes for yes')=='yes':
                            return
                    p=[(p[0]-buffer[0])//self.sizer,(p[1]-buffer[1])//self.sizer]
                    if p[0]==len(self.game):
                        if p[1]==len(self.game[0])-1:
                            self.savelevel(self.game)
                        elif p[1]==len(self.game[0])-2:
                            self.placing=0
                        elif p[1]==len(self.game[0])-3:
                            self.placing=1
                if e.type==pygame.MOUSEBUTTONUP:
                    click=False
                    p=pygame.mouse.get_pos()
                    p=[(p[0]-buffer[0])//self.sizer,(p[1]-buffer[1])//self.sizer]
                    if p[0]>=0 and p[0]<len(self.game) and p[1]>=0 and p[1]<len(self.game[0]):
                        self.game[p[0]][p[1]]=self.placing
                    oldpos=[-1,-1]
            if click:
                p=pygame.mouse.get_pos()#v ??? nah.. +above
                p=[(p[0]-buffer[0])//self.sizer,(p[1]-buffer[1])//self.sizer]
                if p!=oldpos:
                    if p[0]>=0 and p[0]<len(self.game) and p[1]>=0 and p[1]<len(self.game[0]):
                        self.game[p[0]][p[1]]=self.placing
                    oldpos=p.copy()
            self.clock.tick(60)

    def levelpossible(self,level,draw=False):
        oldpg=[[0 for y in range(len(level[0]))] for x in range(len(level))]
        self.pg=[[0 for y in range(len(level[0]))] for x in range(len(level))]
        self.sidenums=self.set_widthways(level,False)
        self.topnums=self.set_heightways(level,False)
        while True:
            print('a')
            if draw:
                buffer=[20,20]
                for x in range(len(level)):
                    for y in range(len(level[0])):
                        if self.pg[x][y]==2:
                            pygame.draw.rect(self.d,(55,255,200),(x*self.sizer+buffer[0],y*self.sizer+buffer[1],self.sizer/2,self.sizer/2))
                        elif self.pg[x][y]==1:
                            pygame.draw.rect(self.d,(0,200,0),(x*self.sizer+buffer[0],y*self.sizer+buffer[1],self.sizer/2,self.sizer/2))
                pygame.display.update()
            for x in range(len(self.topnums)):
                m=self.pg[x].copy()
                q=self.getlines([],self.topnums[x].copy(),m)
                c=q[0]
                cc=[True for i in range(len(level[0]))]
                for i in q:
                    for ii in range(len(level[0])):
                        if i[ii]!=c[ii]:
                            cc[ii]=False
                for i in range(len(level[0])):
                    if cc[i]:
                        self.pg[x][i]=c[i]
            print('b')
            for y in range(len(self.sidenums)):
                m=[self.pg[x][y] for x in range(len(level))]
                q=self.getlines([],self.sidenums[y].copy(),m)
                c=q[0]
                cc=[True for i in range(len(level))]
                for i in q:
                    for ii in range(len(level)):
                        if i[ii]!=c[ii]:
                            cc[ii]=False
                for i in range(len(level)):
                    if cc[i]:
                        self.pg[i][y]=c[i]
            print('c')
            a=True
            b=True
            for x in range(len(level)):
                for y in range(len(level[0])):
                    if self.pg[x][y]==0:
                        a=False
                    if self.pg[x][y]!=oldpg[x][y]:
                        b=False
                        oldpg[x][y]=self.pg[x][y]
            if a:
                return True
            if b:
                return False

    def getlines(self,p,n,m):
        if n==[]:
            return [2 for i in range(len(m))]
        r=[]
        nn=n.pop(0)
        for i in range(len(m)-sum(n)-nn-len(n)-len(p)+1):
            pp=p.copy()
            a=True
            for ii in range(i):
                if m[len(pp)]==1:
                    a=False
                pp.append(2)
            for ii in range(nn):
                if m[len(pp)]==2:
                    a=False
                pp.append(1)
            if a:
                if len(n)==0:
                    if 1 in m[len(pp):]:
                        continue
                    while len(pp)<len(m):
                        pp.append(2)
                    r.append(pp.copy())
                else:
                    if m[len(pp)]==1:
                        continue
                    pp.append(2)
                    for x in self.getlines(pp,n.copy(),m):
                        r.append(x)
        return r

    def loadlevels(self):
        levels=[]
        f=open('saves.txt','r')
        for i in f.readlines():
            try:
                lvl=['','','','']
                x=0
                for ii in i:
                    if ii==' ':
                        x+=1
                    else:
                        lvl[x]=lvl[x]+ii
                levels.append([lvl[0],[[True if lvl[3][x*int(lvl[2])+y]=='1' else False for y in range(int(lvl[2]))] for x in range(int(lvl[1]))]])
            except Exception:#... slow..?
                pass
        f.close()
        return levels

    def play(self):
        levels=self.loadlevels()
        a=pygame.rect.Rect(10,10,300,50)
        buffer=80
        scroll=0
        if levels == []:
            surf=pygame.surface.Surface((self.d.get_width(),100))
            self.show_text(surf,self.font,(255,0,0),(5,5),'no games available. make your own!')
        else:
            surf=pygame.surface.Surface((self.d.get_width(),60*len(levels)+10))
            for i,j in enumerate(levels):
                pygame.draw.rect(surf,(255,255,255),(10,i*60,a[2],50))
                self.show_text(surf,self.font,(255,0,0),(a[0]+5,i*60),j[0])
        maxscroll=max(0,surf.get_height()+buffer-self.d.get_height())
        menu=True
        while menu:
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.MOUSEWHEEL:
                    scroll-=20*e.y
                    if scroll<0:
                        scroll=0
                    if scroll>maxscroll:
                        scroll=maxscroll
                if e.type==pygame.MOUSEBUTTONUP:
                    if e.button<4:
                        p=pygame.mouse.get_pos()
                        if a.collidepoint(p):
                            return
                        if p[0]-a[0]>=0 and p[0]-a[0]-a[2]<=0:
                            if p[1]-buffer+scroll>=0:
                                if (p[1]-buffer+scroll)%60<=50:
                                    menu=False
                                    self.game=levels[(p[1]-buffer+scroll)//60][1]
            self.d.fill((0,0,0))
            pygame.draw.rect(self.d,(255,255,255),a)
            self.show_text(self.d,self.font,(255,0,0),(a[0]+5,a[1]),'<---RETURN')
            ss=pygame.surface.Surface((self.d.get_width(),self.d.get_height()-buffer))
            ss.blit(surf,(0,-scroll))
            self.d.blit(ss,(0,buffer))
            pygame.display.update()
            self.clock.tick(60)

        self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,10,200,50)
        self.pg=[[0 for y in range(len(self.game[0]))] for x in range(len(self.game))]
        self.texth=self.set_heightways(self.game,True)
        self.textw=self.set_widthways(self.game,True)
        self.buffer=[0,0]###
        for a in self.texth:
            if len(a) > self.buffer[1]:
                self.buffer[1] = len(a)
        for a in self.textw:
            if len(a) > self.buffer[0]:
                self.buffer[0] = len(a)
        self.sizeit(30,True)
        click=False
        oldpos=[-1,-1]
        self.placing=1
        while True:
            self.display()
            for e in pygame.event.get():
                if e.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if e.type==pygame.WINDOWRESIZED:
                    self.returnbutton=pygame.rect.Rect(self.d.get_width()-200-10,10,200,50)
                if e.type==pygame.MOUSEBUTTONDOWN:
                    click=True
                    p=pygame.mouse.get_pos()
                    if self.returnbutton.collidepoint(p):
                        if input('are you sure you want to leave? yes for yes')=='yes':
                            return
                    p=[(p[0]-self.buffer[0]*self.sizer)//self.sizer,(p[1]-self.buffer[1]*self.sizer)//self.sizer]
                    if p[0]==len(self.game):
                        if p[1]==len(self.game[0])-1:
                            if self.checkforwin(self.game):
                                print('YOU GOT IT!')
                                #return####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#####################################################################################################################################################################
                        elif p[1]==len(self.game[0])-2:
                            if input('are yo sure yo want to clear this all??: yes for yes')=='yes':
                                self.pg=[[0 for y in range(len(self.game[0]))] for x in range(len(self.game))]
                        elif p[1]==len(self.game[0])-3:
                            self.placing=2
                        elif p[1]==len(self.game[0])-4:
                            self.placing=1
                        elif p[1]==len(self.game[0])-5:
                            self.placing=0
                if e.type==pygame.MOUSEBUTTONUP:
                    click=False
                    p=pygame.mouse.get_pos()
                    p=[(p[0]-self.buffer[0]*self.sizer)//self.sizer,(p[1]-self.buffer[1]*self.sizer)//self.sizer]
                    if p[0]>=0 and p[0]<len(self.game) and p[1]>=0 and p[1]<len(self.game[0]):
                        self.pg[p[0]][p[1]]=self.placing
                    oldpos=[-1,-1]
                    
            if click:
                p=pygame.mouse.get_pos()#v ??? nah.. +above
                p=[(p[0]-self.buffer[0]*self.sizer)//self.sizer,(p[1]-self.buffer[1]*self.sizer)//self.sizer]
                if p!=oldpos:
                    if p[0]>=0 and p[0]<len(self.game) and p[1]>=0 and p[1]<len(self.game[0]):
                        self.pg[p[0]][p[1]]=self.placing
                    oldpos=p.copy()
            self.clock.tick(60)

    def display(self):
        self.d.fill((200,200,200))
        for x in range(len(self.game)):
            for y in range(len(self.game[0])):
                if self.pg[x][y]==0:
                    pygame.draw.rect(self.d,(255,255,255),((x+self.buffer[0])*self.sizer,(y+self.buffer[1])*self.sizer,self.sizer,self.sizer))
                if self.pg[x][y]==1:
                    pygame.draw.rect(self.d,(0,0,0),((x+self.buffer[0])*self.sizer,(y+self.buffer[1])*self.sizer,self.sizer,self.sizer))
                if self.pg[x][y]==2:
                    pygame.draw.rect(self.d,(255,255,255),((x+self.buffer[0])*self.sizer,(y+self.buffer[1])*self.sizer,self.sizer,self.sizer))
                    pygame.draw.circle(self.d,(50,50,50),((x+self.buffer[0])*self.sizer+self.sizer/2,(y+self.buffer[1])*self.sizer+self.sizer/2),4)
        for x in range(len(self.game)):
            pygame.draw.line(self.d,(150,150,150),((x+self.buffer[0])*self.sizer,0),((x+self.buffer[0])*self.sizer,(len(self.game[0])+self.buffer[1])*self.sizer),4 if x%5==0 else 2)
        for y in range(len(self.game[0])):
            pygame.draw.line(self.d,(150,150,150),(0,(y+self.buffer[1])*self.sizer),((len(self.game)+self.buffer[0])*self.sizer,(y+self.buffer[1])*self.sizer),4 if y%5==0 else 2)
        for x in range(self.buffer[0]):
            pygame.draw.line(self.d,(150,150,150),((x)*self.sizer,0),((x)*self.sizer,(len(self.game[0])+self.buffer[1])*self.sizer),2)
        for y in range(self.buffer[1]):
            pygame.draw.line(self.d,(150,150,150),(0,(y)*self.sizer),((len(self.game)+self.buffer[0])*self.sizer,(y)*self.sizer),2)
        for n in range(len(self.texth)):
            for m in range(len(self.texth[n])):
                self.show_text(self.d,self.gfont,(255,0,0),(4+(n+self.buffer[0])*self.sizer,(self.buffer[1]-m-1)*self.sizer),self.texth[n][m])
        for n in range(len(self.textw)):
            for m in range(len(self.textw[n])):
                self.show_text(self.d,self.gfont,(255,0,0),(4+(self.buffer[0]-m-1)*self.sizer,(n+self.buffer[1])*self.sizer),self.textw[n][m])
        self.d.blit(self.checkmarkimg,(2+(self.buffer[0]+len(self.game))*self.sizer,2+(self.buffer[1]+len(self.game[0])-1)*self.sizer))
        self.d.blit(self.clearimg,(2+(self.buffer[0]+len(self.game))*self.sizer,2+(self.buffer[1]+len(self.game[0])-2)*self.sizer))
        pygame.draw.rect(self.d,(255,255,255),(2+(self.buffer[0]+len(self.game))*self.sizer,2+(self.buffer[1]+len(self.game[0])-3)*self.sizer,self.sizer-4,self.sizer-4))
        pygame.draw.circle(self.d,(50,50,50),(2+(self.buffer[0]+len(self.game))*self.sizer+self.sizer/2,2+(self.buffer[1]+len(self.game[0])-3)*self.sizer+self.sizer/2),4)
        pygame.draw.rect(self.d,(0,0,0),(2+(self.buffer[0]+len(self.game))*self.sizer,2+(self.buffer[1]+len(self.game[0])-4)*self.sizer,self.sizer-4,self.sizer-4))
        pygame.draw.rect(self.d,(255,255,255),(2+(self.buffer[0]+len(self.game))*self.sizer,2+(self.buffer[1]+len(self.game[0])-5)*self.sizer,self.sizer-4,self.sizer-4))
        pygame.draw.rect(self.d,(255,255,255),self.returnbutton)
        self.show_text(self.d,self.font,(255,0,0),(self.returnbutton[0]+5,self.returnbutton[1]),'<---RETURN')
        pygame.display.update()
        
    def set_widthways(self,level,r):
        numbers = []
        for a in range(len(level[0])):
            numbers.append([])
            temp = 0
            for b in range(len(level)):
                if level[b][a] == True:
                    temp+=1
                else:
                    if temp != 0:
                        numbers[a].append(temp)
                    temp = 0
            if temp != 0:
                numbers[a].append(temp)
            if numbers[a] == []:
                numbers[a].append(temp)
        if r:
            for i in numbers:
                i.reverse()
        return numbers

    def set_heightways(self,level,r):
        numbers = []
        for a in range(len(level)):
            numbers.append([])
            temp = 0
            for b in level[a]:
                if b == True:
                    temp+=1
                else:
                    if temp != 0:
                        numbers[a].append(temp)
                    temp = 0
            if temp != 0:
                numbers[a].append(temp)
            if numbers[a] == []:
                numbers[a].append(temp)
        if r:
            for i in numbers:
                i.reverse()
        return numbers

    def checkforwin(self,level):
        for x in range(len(level)):
            for y in range(len(level[0])):
                if self.pg[x][y]==1:
                    if not level[x][y]:
                        return False
                else:
                    if level[x][y]:
                        return False
        return True

g=game()
g.start()
