import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit
from scipy.linalg import lstsq  #最小二乘法拟合

UNIT_1 = 0.1
UNIT_2 = 1

def func(x,a,b,c):
    return a*np.exp(b*x)+c

def func_2(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

def draw(filepath,outpath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    y = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(1),encoding='utf-8')
    
    x_1 = x[0:101:1]
    x_2 = x[102:119:1]
    y_1 = y[0:101:1]*UNIT_1
    y_2 = y[102:119:1]*UNIT_2
    
    X = np.append(x_1,x_2)
    Y = np.append(y_1,y_2)
    
    cs = CubicSpline(X,Y)
    xin = np.arange(10,95,0.1)
    
    x_bound = []
    y_bound = []
    
    yin = cs(xin)
    flag = 0
    for i in range(len(xin)):
        if(i>=1):
            if((yin[i]-yin[i-1])<0):
                flag = 1
            if((yin[i]-yin[i-1])>0 and flag):
                flag = 0
                x_bound.append(xin[i-1])
                y_bound.append(yin[i-1])
                
    #del x_bound[0:2]
    #del y_bound[0:2]

    popt, pcov = curve_fit(func, x_bound, y_bound,bounds=(0, [1., 1., 0.5]))
    #popt, pcov = curve_fit(func_2, x_bound, y_bound)
    
    y_fit = [func(i,*popt) for i in x_bound]
    y_back = [func(i,*popt) for i in xin]
    
    y_off_back = yin - y_back
    
    flag_max=0
    flag_min=1
    y_min = []
    y_max = []
    for i in range(1,len(xin)):
        
        if(y_off_back[i]>y_off_back[i-1] and flag_min):
            y_min.append([y_off_back[i-1],i-1])
        if(y_off_back[i]<y_off_back[i-1] and flag_max):
            y_max.append([y_off_back[i-1],i-1])
        if(y_off_back[i]>y_off_back[i-1]):
            flag_max=1
            flag_min=0
            #y_max.append([max,i])
        if(y_off_back[i]<y_off_back[i-1]):
            flag_min=1
            flag_max=0
        pass
    
    print(y_min)
    print(y_max)

    x_average = []
    y_average = []
    for i in range(0,len(y_min)-1):
        aver_1 = (y_min[i][0]+y_max[i][0])/2
        aver_2 = (y_min[i+1][0]+y_max[i][0])/2
        x_min = y_min[i][0]
        x_max = y_max[i][0]
        y_1=0
        y_2=0
        for j in range(y_min[i][1],y_max[i][1]):
            if(np.abs(y_off_back[j]-aver_1)<np.abs(x_min-aver_1)):
                x_min=y_off_back[j];
                y_1=j
        for j in range(y_max[i][1],y_min[i+1][1]):
            if(np.abs(y_off_back[j]-aver_2)<np.abs(x_max-aver_2)):
                x_max=y_off_back[j];
                y_2=j
        x_average.append((xin[y_1]+xin[y_2])/2)
        y_average.append((x_min+x_max)/2)

    with open(outpath,'w') as out: # 参数为:写入文件路径,写入模式
        for i in range(len(x_average)):
            out.write("%5.4f\n"%(x_average[i])) #写入文件

    plt.plot(X,Y,'.',c='red',label='Original Data')
    plt.plot(xin,cs(xin),label='Cubic Spline Data')
    plt.plot(x_bound,y_bound,'o',c='blue',label='Minimum Data')
    plt.plot(xin,y_back,'g:',linewidth = 2,label='Background Curve')#:a=%5.5f, b=%5.3f, c=%5.3f' % tuple(popt))
    plt.plot(xin,y_off_back,c='violet',linestyle='--',label="Difference Curve")
    #plt.plot(x_bound,y_fit,'r--',label='fit: a=%5.6f, b=%5.3f, c=%5.3f' % tuple(popt))
    #plt.plot(x_bound,y_fit, 'p-',label='fit: a=%5.3f, b=%5.3f, c=%5.3f,d=%5.3f' % tuple(popt))
    #plt.plot([10,95],[-0.0000001,0.0000001])
    plt.plot(x_average,y_average,'x',label='Electric Potential at Peak')
    plt.legend(loc=2,framealpha=1, shadow=True)
    plt.title("Specific Data of $I_P$-$U_{G2K}$")
    plt.xlabel("$U_{G2K} / V$")
    plt.ylabel("$I_P / 0.1\mu A$")
    plt.show()
    pass

def analysis(filepath):
    x = np.loadtxt(filepath,dtype=np.float32,delimiter=",",usecols=(0),encoding='utf-8')
    
    l = []
    
    for i in range(len(x)):
        l.append(i+1)
    
    l_trans = np.array(l)
    
    A = np.vstack([l_trans**0,l_trans**1])
    sol,res,rank,s = lstsq(A.T,x)
    
    #print(res)
    
    m = 100
    l_1 = np.linspace(l[0],l[-1],m)
    y = sol[0] + sol[1] * l_1

    sum_1 =0 
    sum_2 = 0
    for i in range(len(l)):
        sum_1+=(l[i])**2
        sum_2+=l[i]
    
    Delta = len(l)*sum_1-sum_2**2

    sigma_b = np.sqrt(res/(len(l)-2)) * np.sqrt(len(l)/Delta)

    print(sigma_b)
    
    print(sigma_b/sol[1])

    #string1 = '$K=%0.4f$'%(sol[1])
    plt.plot(l,x,'x',c='red',label='Original Data')
    plt.plot(l_1,y,label='Least-square fit,K=%5.3f'%(sol[1]))
    plt.legend(loc=2,framealpha=1, shadow=True)
    plt.xlabel("$Peak \\ Number \\ (N)$")
    plt.ylabel("$U_{G2K}/V$")
    plt.title("$U_{G2K}$-$N$")
    plt.show()
    
#draw("./fh.csv","./fh_out.csv")
analysis("./fh_out.csv")