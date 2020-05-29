import matplotlib.pyplot as plt
import numpy as np

xlimmax=12
xlimmin=-2
ylimmax=12
ylimmin=-2

def line(x1,y1,x2,y2,xlimmax,xlimmin,ylimmax,ylimmin):
    xlim=abs(xlimmax-xlimmin)
    ylim=abs(ylimmax-ylimmin)
    ran=np.arange(x1,x2,.01)
    if y1-y2!=0 and x1-x2!=0:
        k=float((y1-y2)/(x1-x2))
        b=float(y1-x1*k)
        y=k*ran+b
        plt.plot(ran,y, 'c-', linewidth = 1)
    elif x1-x2==0:
        plt.axvline(x=x1, ymin=abs(min(y1,y2)-ylimmin)/xlim,ymax=abs(max(y1,y2)-ylimmin)/xlim,linewidth=1,color='c')
    elif y1-y2==0:
        plt.axhline(y=y1, xmin=abs(min(x1,x2)-xlimmin)/ylim,xmax=abs(max(x1,x2)-xlimmin)/ylim,linewidth=1,color='c')
    else:
        print("what the hell did you put in?")


line(4,3,7,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(7,3,7,7,xlimmax,xlimmin,ylimmax,ylimmin)
line(4,3,7,7,xlimmax,xlimmin,ylimmax,ylimmin)

line(0,6,4,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(0,6,3,10,xlimmax,xlimmin,ylimmax,ylimmin)
line(3,10,7,7,xlimmax,xlimmin,ylimmax,ylimmin)

line(7,7,10,7,xlimmax,xlimmin,ylimmax,ylimmin)
line(10,7,10,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(10,3,7,3,xlimmax,xlimmin,ylimmax,ylimmin)

line(4,3,4,0,xlimmax,xlimmin,ylimmax,ylimmin)
line(4,0,7,0,xlimmax,xlimmin,ylimmax,ylimmin)
line(7,3,7,0,xlimmax,xlimmin,ylimmax,ylimmin)


plt.ylim(ylimmin,ylimmax)
plt.xlim(xlimmin,xlimmax)
plt.show()