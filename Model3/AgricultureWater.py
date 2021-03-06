import Data
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt
from numpy import linspace
import Fit


years=range(2004, 2015)

def Expo(x,p):
    return p[0]+p[1]*(x-p[2])

def err(p, x, y):
    return Expo(x,p)-y

def para(datax,datay):
    x = [datax[t] for t in years]
    y = [datay[t] for t in years]
    return leastsq(err,[y[0],1e-8,x[0]],args=(x,y))[0]

def comparedata(datax,datay,xlabel,ylabel):
    Para = para(datax,datay)
    x = np.linspace(datax[years[0]],datax[years[-1]],100)
    y = Expo(x,Para)
    plt.figure()
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter([datax[t] for t in years],[datay[t] for t in years],marker="^",s=100)  
    plt.plot(x,y,'b-')
    plt.show()
    plt.close()

# comparedata(Data.Population,Data.WaterUseAgriculture,"Population/ 10k people","Agriculture Water Usage/ 100m m^3")
# comparedata(Data.PCGDP,Data.WaterUseAgriculture,"PCGDP/ CNY","Agreculture Water Usage/ 100m m^3")
# comparedata(Data.IrrigationArea,Data.WaterUseAgriculture,"Irrigation Area/ kha","Agreculture Water Usage/ 100m m^3")

pPara = para(Data.Population,Data.WaterUseAgriculture)
gPara = para(Data.PCGDP,Data.WaterUseAgriculture)
iPara = para(Data.IrrigationArea,Data.WaterUseAgriculture)

def AgricultureWater(time):
    pop = (Expo(Fit.PopulationFit(time),pPara)/Expo(Fit.PopulationFit(years[-1]),pPara))
    pcg = (Expo(Fit.PCGDPFit(time),gPara)/Expo(Fit.PCGDPFit(years[-1]),gPara))
    ira = (Expo(Fit.IrrigationAreaFit(time),iPara)/Expo(Fit.IrrigationAreaFit(years[-1]),iPara))
    return Data.WaterUseAgriculture[years[-1]]*(pop/3+pcg/3+ira/3)

def All(time):
    return (AgricultureWater(time)+ResidentWater.ResidentWater(time)+IndustWater.IndustWater(time))/Fit.PopulationFit(time)

x = np.linspace(years[0],years[-1],100)

plt.figure()
plt.xlabel("Population/ 10k people")
plt.ylabel("Agreculture Water Usage/ 100m m^3")
plt.scatter([Data.Population[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.PopulationFit(x),Expo(Fit.PopulationFit(x),pPara),'g-',label="Fit")
plt.legend()
plt.show()
plt.close()


plt.figure()
plt.xlabel("PCGDP/ CNY")
plt.ylabel("Agreculture Water Usage/ 100m m^3")
plt.scatter([Data.PCGDP[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.PCGDPFit(x),Expo(Fit.PCGDPFit(x),gPara),'g-',label="Fit")
plt.legend(loc=0)
plt.show()
plt.close()

plt.figure()
plt.xlabel("Irrigation Area/ kha" )
plt.ylabel("Agreculture Water Usage/ 100m m^3")
plt.scatter([Data.IrrigationArea[t] for t in years],[Data.WaterUseAgriculture[t] for t in years],marker="^",s=50,label='Raw Data')
plt.plot(Fit.IrrigationAreaFit(x),Expo(Fit.IrrigationAreaFit(x),iPara),'g-',label="Fit")
plt.legend(loc=0)
plt.show()
plt.close()
