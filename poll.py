from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.graphics import Color, Ellipse

import random 
highee = Window.height
widhee = Window.width
muplay = False
class Menu(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        btn = Button(text = "|__•|",size_hint=(None,None),size = (200,100),pos=(0.22 * widhee ,0.7 * highee),font_size = 70,background_color=(0,0,0))
        btn.bind(on_press=self.start_game)
        self.add_widget(btn)
    def start_game(self,opj):
        muplay = True
        self.manager.current = "game"
      
class game(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        btn = Button(text="<][>",pos=(widhee * 0.88, highee*0.8 ) ,size_hint =(None,None), size= (widhee/8,highee/8) , font_size = 100,background_color=(0.1,0.1,0.1,0.6))
        btn.bind(on_press=self.sittng)
        self.add_widget(btn)
        self.xs = 700
        self.le = 1  
        self.ys = 1000
        self.sc = 0
        self.btnm = Button(text="menu" , pos=(widhee/2.66,highee/2.6),size_hint =(None,None) , size=(widhee/4,highee/10),font_size=(100),background_color=(0.1,0.1,0.1,0.7))        
        self.btnm.bind(on_press = self.mune)
        self.btnmus  = Button(text= "music", pos = ( widhee / 2.2 ,highee / 1.66),size_hint =(None,None) , size=(100,20) ,font_size=80,background_color=(0,0,0))                     
        self.btnmu1 = Button(text="-" , pos=(widhee/1.6,highee/1.9),size_hint =(None,None) , size=(widhee/8,highee/6),font_size=(120),background_color=(0.1,0.1,0.1,0.9))
        self.btnmu1.bind(on_press=self.soundm)          
        self.btnmu = Button(text="+" , pos=(widhee/4,highee/1.9),size_hint =(None,None) , size=(widhee/8,highee/6),font_size=(100),background_color=(0.1,0.1,0.1,0.8))
        self.btnmu.bind(on_press=self.soundp)
        self.btnrus = Button(text="rusem" , pos=(widhee/2.66,highee/1.55),size_hint =(None,None) , size=(widhee/4,highee/10),font_size=(100),background_color=(0.1,0.1,0.1,0.7))        
        
        self.btnrus.bind(on_press=self.rus)
        self.mu = SoundLoader.load("Krebo_Tel_-_otbobr_.mp3")
        if self.mu :
            self.mu.loop = True 
            
            self.mu.volume = 0.5
            if muplay == True :
                self.mu.play()
        self.stle = 0 + self.le 
        self.text = Label(text= "0", pos = (0.004 * widhee ,0.022 * highee) ,font_size = 40)
        self.textlo = Label(text="" , pos=(0.0 * widhee ,0.022 * highee),font_size = 200)
        self.textlv = Label(text="  LEVEL" + str(self.stle),center_x=widhee/200,top=highee/200,font_size = 200)
        self.add_widget(self.textlv)       
        self.dame = 1
        self.starda = False
        self.add_widget(self.text) 
        self.co1 = 1 
        self.shaf = 1
        self.trailr = [] 
        self.max_tra = 8
        self.trailr_canvas = []
        self.levb = 1 
        self.no = 1
        self.co = 4
        self.add_widget(self.textlo)
        self.px = 440      
        self.py = 100
        self.xb = 490
        self.yb = 140
        self.move__up = 0
        self.speed2 = 300 
        
        
        self.tooch = True 
        self.move_left = False
        self.move_right = False 
        self.re = False
        self.blocks = []
        self.spawn_blocks()
        self.lo = False        
        self.yc = 14
        xdl = random.choice([2,2,1,8,6])
        xdr = random.choice([-2,-2,-6])
        self.xc = random.choice([xdr])
        self.xy = [self.xb,self.yb]
        self.xcr = 0
        self.ycr = 0      
        self.Sqrb = []
        self.m = None 
    #    self.cr()
        Clock.schedule_interval(self.cr, 4)
       # self.sittng()
       # self.btnrus = Button(text="resm" , pos=(widhee/2.3,highee/1.6),size_hint =(None,None) , size=(widhee/8,highee/6),font_size=(100),background_color=(0,0,0))
        self.btnrus.bind(on_press=self.rus)
        #self.btnrus = None
        self.plso = 0.2
        self.namu = str(0)
        
        self.msa = False
        #self.m = None
        
        with self.canvas :
            self.cb = Color(1,1,1)
            self.rect2 = Ellipse(pos=(self.xb, self.yb), size=(50, 50))
           

            self.rect = Rectangle(pos=(self.px, self.py), size=(168, 40))
            self.ft = Clock.schedule_interval(self.update, 1/60)
            
    
    def soundm(self,opj):
        
        
        self.plso = 0.2
        self.mu.volume = max(0,self.mu.volume - self.plso)      
    def soundp(self,opj):
          
          
          self.plso = 0.2
          self.mu.volume = min(1,self.mu.volume + self.plso)
          

                                        
    def sittng(self,opj):
        
        if self.msa == True :
            self.remove_widget(self.btnrus)
            self.remove_widget(self.btnmu)
            self.remove_widget(self.btnmu1)
            self.remove_widget(self.btnm)
            self.remove_widget(self.btnmus)  
            self.msa = False
            if self.m  :
                self.canvas.after.remove(self.m)
                self.m = None
            
           # self.btnrus = None
        else :
            with self.canvas.after:
                self.ft.cancel()                
                self.add_widget(self.btnrus)  
                self.add_widget(self.btnmu) 
                self.add_widget(self.btnmu1) 
                self.add_widget(self.btnm) 
                self.add_widget(self.btnmus)       
                Color(1,1,1,0.4)
                self.m = Rectangle(pos=(widhee/4,highee/3), size=(widhee/2,highee/2))
                self.msa = True
        
    def rus(self,*args):
        self.ft = Clock.schedule_interval(self.update, 1/60)       
        self.msa = True 
        self.sittng(None)                        
                  
            #print("")
    def cr(self,dt) :
        for i in range(10) :
            with self.canvas :
                co = Color(1,1,1,0.5)
                self.xcr = random.randint(0,widhee)
                self.ycr = random.randint(highee,2400)
                self.si = random.randint(1,20)
                self.sqrb = Rectangle(pos= (self.xcr,self.ycr),size= (self.si,self.si))
                self.Sqrb.append(self.sqrb)
                
    def spawn_blocks(self) :
            
            
            if self.le == 6 :
                self.levb = 1 
                self.starda = True 
                
            for now in range(self.no + self.levb ):
                        for col in range(self.co):
                            xs = col * 290                           
                            ys = highee * 0.5 + now * 100
                            
                            if self.starda == True :
                                self.dame = 2
                               # self.co1 = 0
                                    
                         #   if self.dame == 2 :
                           #       self.co1 = 1
                                  
                                     
                                     
                                    
                                    
                            self.co1 = 1 / self.dame 
                           # block = {"rect": Rectangle(pos=(xs ,ys), size=(200 ,40),Color(1,1,1,1)),"dame":2}
                            with self.canvas :
                                
                            
                                color = Color(self.co1,self.co1,self.co1)
                                rect = Rectangle(pos=(xs, ys), size=(200, 40))
                            
                                block = { "color" : color ,
                                      "dame" : self.dame ,
                                      "rect" : rect 
                            }
                               # self.canvas.add(block["rect"])
                                self.blocks.append(block)
                         
           
                     
    def update_rect(self):
        self.rect.pos = (self.px, self.py)
        self.rect2.pos = (self.xb, self.yb)
        for sa in self.Sqrb [:]:
            sa.pos = (sa.pos[0] , sa.pos[1] - 0.6  )
            if sa.pos[1] < 0 :
               self.canvas.remove(sa)
               self.Sqrb.remove(sa)
       # self.rect3.pos = (self.xs, self.ys)
    
    #def vare(self):
        
        
    def update(self , dt ) :
        
        self.stle = self.le + 1
        
        if self.lo == True :
            self.textlo.text = "Game Over"
             
        if self.move_left :
            self.px -= 10
        if self.move_right :
            self.px += 10
        if self.move__up == 1 :
            self.yb += self.yc
            self.xb += self.xc
        if len(self.blocks) == 0:
            self.levb += 1
            self.le += 1
            self.spawn_blocks()
            self.tooch = True 
            self.text_cont()
            
        
        
        
        self.ycr -= 0.2

        self.wol()
        self.loes()
        self.text.text = str(self.sc)
       # self.cr      
        self.update_rect()
        
                    
    def text_cont(self):
        self.textlv.text = "LEVEL"+ str(self.stle)
        
    def on_touch_down(self , toch) :
        
            
        if toch.y > self.height / 5 and self.tooch == True :
            self.tooch = False 
            self.move__up = 1             
            
        if toch.x < self.width / 2 and self.lo == False  :
            self.move_left = 1
        if toch.x > self.width / 2 and self.lo == False :
            self.move_right = True
        return super().on_touch_down(toch)     
    def on_touch_up(self,toch):
        self.move_left = False 
        self.move_right = False
    def loes(self):
        if self.yb < 50 :
            self.lo = True
    def wol(self):
        
        for b in self.blocks [:] :
            rect = b["rect"]            
            if (self.xb < rect.pos[0] + 200 and self.xb + 40 > rect.pos[0] and self.yb < rect.pos[1] + 40 and self.yb + 40 > rect.pos[1] and self.re == False ):
                self.yc *= -1 
                #self.re = True
                
                
                b["dame"] -= 1
                co =  b["dame"] + 0.1                         
                b["color"].r= co
                b["color"].g= co
                b["color"].b= co                             
              #  b["color"].a =  0.8
                
                
                               
                
            if b["dame"] == 0 :
                self.canvas.remove(rect)
                self.blocks.remove(b) 
                self.sc = self.sc + 1
                    
       
            
        if (self.yb < self.py + 40 and self.xb > self.px and self.xb < self.px + 170):
           self.yc *= -1
           self.xc = random.choice([self.xc*-1,self.xc,self.xc,self.xc])
           
           
        
        if self.xb >= widhee :
            self.xc = self.xc * -1
            self.yc = random.choice([self.yc,self.yc,self.yc,self.yc,self.yc*-1,self.yc])
        
        if self.xb <= 0 :
            self.xc = self.xc * -1
            self.yc = random.choice([self.yc,self.yc,self.yc,self.yc*-1,self.yc  ])
        
        if self.yb > highee :
            self.yc = self.yc * -1
            print("su")            
        if self.px < 0:
            self.px = 0
        elif self.px > 0.88 * widhee:
                self.px = 0.88 * widhee
                
    
               
    def mune(self,opj):
        self.manager.current ="menu"                         
       
        self.reset_game()
        #self.msa = True
        #self.sittng(None)
        self.rus() 
       # self.m = None
         
    def reset_game(self):
         print("") 
         try:
           self.ft.cancel()
         except :
            pass                                         
         for b in self.blocks:
               try :
                  self.canvas.remove(b["rect"])
                  self.canvas.remove(b["color"])
               except:
                    pass                                                                               
         self.blocks.clear()
         
         self.dame = 1             
         #self.stle = 1 + self.le   
         self.sc = 0
         self.le = 0
         self.levb = 0
         self.stle = 1 + self.le  
         self.px = 440
         self.py = 100
         self.xb = 490
         self.yb = 140
         xdr = random.choice([-2,-2,-6])
         self.xc = random.choice([xdr])
         self.xy = [self.xb,self.yb]
         self.yc = 14
         self.move_left = False
         self.move_right = False
         self.move__up = 0
         self.lo = False
         self.starda = False
         self.text.text = "0"
         self.textlv.text = "LEVEL 1"
         self.textlo.text = ""
        # self.msa = False                                                                                                                                                                                                                                                                                                                                                  
class MyApp(App):

    def build(self):

        sm = ScreenManager()

        sm.add_widget(Menu(name="menu"))

        sm.add_widget(game(name="game"))

        sm.current = "menu"

        return sm
    
MyApp().run()


