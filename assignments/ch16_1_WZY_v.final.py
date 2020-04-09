import matplotlib.pyplot as plt
import numpy as np

#画一条线
def line(x1,y1,x2,y2,xlimmax,xlimmin,ylimmax,ylimmin):

    #计算显示坐标的x左右显示区域
    xlim=abs(xlimmax-xlimmin)
    #计算显示坐标的y左右显示区域
    ylim=abs(ylimmax-ylimmin)

    #x的值及其范围
    ran=np.arange(x1,x2,.01)

    #判断该函数是否垂直于坐标轴
    if y1-y2!=0 and x1-x2!=0:
        #计算一次函数的k值
        k=float((y1-y2)/(x1-x2))
        #计算一次函数的b值
        b=float(y1-x1*k)
        #整合函数
        y=k*ran+b
        #画出函数
        plt.plot(ran,y, 'c-', linewidth = 1)

    #如果函数垂直于x轴
    elif x1-x2==0:
        #ymin表示此线段最小值相对于整个坐标轴的绝对位置,ymax表示此线段最大值相对于整个坐标轴的的绝对位置
        plt.axvline(x=x1, ymin=abs(min(y1,y2)-ylimmin)/xlim,ymax=abs(max(y1,y2)-ylimmin)/xlim,linewidth=1,color='c')
    
    #如果函数垂直于y轴
    elif y1-y2==0:
        #xmin表示此线段最小值相对于整个坐标轴的绝对位置,xmax表示此线段最大值相对于整个坐标轴的的绝对位置
        plt.axhline(y=y1, xmin=abs(min(x1,x2)-xlimmin)/ylim,xmax=abs(max(x1,x2)-xlimmin)/ylim,linewidth=1,color='c')
    
    #其他输入就是非法的了
    else:
        print("what the hell did you put in?")

#确认坐标轴
xlimmax=12
xlimmin=-2
ylimmax=12
ylimmin=-2
plt.ylim(ylimmin,ylimmax)
plt.xlim(xlimmin,xlimmax)

#画出三角形
line(4,3,7,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(7,3,7,7,xlimmax,xlimmin,ylimmax,ylimmin)
line(4,3,7,7,xlimmax,xlimmin,ylimmax,ylimmin)

#画出5x5的正方形
line(0,6,4,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(0,6,3,10,xlimmax,xlimmin,ylimmax,ylimmin)
line(3,10,7,7,xlimmax,xlimmin,ylimmax,ylimmin)

#画出4x4的正方形
line(7,7,10,7,xlimmax,xlimmin,ylimmax,ylimmin)
line(10,7,10,3,xlimmax,xlimmin,ylimmax,ylimmin)
line(10,3,7,3,xlimmax,xlimmin,ylimmax,ylimmin)

#画出3x3的正方形
line(4,3,4,0,xlimmax,xlimmin,ylimmax,ylimmin)
line(4,0,7,0,xlimmax,xlimmin,ylimmax,ylimmin)
line(7,3,7,0,xlimmax,xlimmin,ylimmax,ylimmin)

#展示图形
plt.show()