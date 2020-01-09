import math
import turtle

class Spiro:
    def __init__(self,xc,yc,col,R,r,l):
        self.t = turtle.Turtle()
        self.t.shape('turtle')
        self.step = 5
        self.drawingComplete = False

        self.setparams(xc,yc,col,R,r,l)
        self.restart()

    def setparams(self,xc,yc,col,R,r,l):
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        gcdVal = gcd(self.r,self.R)
        self.nRot = self.r // gcdVal   #//代表整除
        self.k = r/float(R)
        self.t.color(*col)
        self.a = 0
    
    def restart(self):
        self.drawingComplete = False
        self.t.showturtle()
        self.t.up()
        R,k,l = self.R, self.k, self.l   #此处使用局部变量，使得下面的表达式保持简洁紧凑
        a = 0.0
        x = R*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc+x, self.yc+y)
        self.t.down()

    def draw(self):
        R, k, l = self.R, self.k, self.l  # 此处使用局部变量，使得下面的表达式保持简洁紧凑
        for i in range(0,360*self.nRot+1, self.step):
            a = math.radians(i)
            x = R*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
            y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
            self.t.setpos(self.xc+x, self.yc+y)
        self.t.hideturtle()

    def update(self):
        if self.drawingComplete:
            return
        self.a += self.step
        R, k, l = self.R, self.k, self.l  # 此处使用局部变量，使得下面的表达式保持简洁紧凑
        a = math.radians(self.a)
        x = R*((1-k)*math.cos(a)+l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a)-l*k*math.sin((1-k)*a/k))
        self.t.setpos(self.xc+x, self.yc+y)

        if self.a >= 360*self.nRot:
            self.drawingComplete = True
            self.t.hideturtle()
    
    




def main():
    

if __name__ == '__main__':
    main()
