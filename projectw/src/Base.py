import numpy as np
from scipy.optimize import leastsq
import numpy.random as random

years = range(2004, 2015)

class Population(object):
    """Population"""
    def __init__(self, data):
        self.data = data
        self.coefs = self.para()
        self.var = self.variance()

    def fitfunc(self, t, p):
        return p[2]/(1+np.exp(-p[1]*(t-p[0])))

    def err(self, p, x, y):
        return self.fitfunc(x,p)-y

    def para(self):
        x = years
        y = [self.data[t] for t in years]
        return leastsq(self.err,[1950,0.01,160000],args=(x,y))[0]

    def variance(self):
        return np.mean([(self.data[i]-self.fitfunc(i,self.coefs))**2 for i in years])

    def __call__(self, time, intr=False):
        # return self.fitfunc(time, self.coefs)+10*np.sqrt(self.var)*random.randn()
        if time<=2014 or intr==False:
            return self.fitfunc(time, self.coefs)+10*np.sqrt(self.var)*random.randn()
        else:
            return 1/(1/(self.coefs[2])+(1/self.__call__(2014)-1/(self.coefs[2]))*np.exp(-self.coefs[1]*(time-2014)))+np.sqrt(self.var)*random.randn()

class PCGDP(object):
    """PCGDP"""
    def __init__(self, data):
        self.data = data
        self.coefs = self.para()
        self.var = self.variance()

    def fitfunc(self, t, p):
        return p[2]/(1+np.exp(-p[1]*(t-p[0])))
        
    def err(self, p, x, y):
        return self.fitfunc(x,p)-y

    def variance(self):
        return np.mean([(self.data[i]-self.fitfunc(i,self.coefs))**2 for i in years])

    def para(self):
        x = years
        y = [self.data[t] for t in years]
        return leastsq(self.err,[2050, 0.07, 200000],args=(x,y))[0]

    def __call__(self, time, intr=False):
        return self.fitfunc(time, self.coefs)+np.sqrt(self.var)*random.randn()


class IrrArea(object):
    """Irrigation Area"""
    def __init__(self, data):
        self.data = data
        self.coefs = self.para()
        self.var = self.variance()

    def fitfunc(self, t, p):
        return p[0]+p[1]*t+p[2]*t*t

    def err(self, p, x, y):
        return self.fitfunc(x,p)-y

    def para(self):
        x = years
        y = [self.data[t] for t in years]
        return leastsq(self.err,[1000,100,1],args=(x,y))[0]

    def variance(self):
        return np.mean([(self.data[i]-self.fitfunc(i,self.coefs))**2 for i in years])

    def __call__(self, time, intr=False):
        if time<2015 or intr==False:
            return self.fitfunc(time, self.coefs)+10*np.sqrt(self.var)*random.randn()
        else:
            return (self.coefs[0]+self.coefs[1]*time+self.coefs[2]*time*time)+np.sqrt(self.var)*random.randn()

class SteelProduct(object):
    """Steel Product"""
    def __init__(self, data):
        self.data = data
        self.coefs = self.para()
        self.var = self.variance()

    def fitfunc(self, t, p):
        return p[0]+p[1]*t+p[2]*t*t

    def err(self, p, x, y):
        return self.fitfunc(x,p)-y

    def para(self):
        x = years
        y = [self.data[t] for t in years]
        return leastsq(self.err,[1000,100,1],args=(x,y))[0]

    def variance(self):
        return np.mean([(self.data[i]-self.fitfunc(i,self.coefs))**2 for i in years])

    def __call__(self, time, intr=False):
        if time<2015 or intr==False:
            return self.fitfunc(time, self.coefs)+10*np.sqrt(self.var)*random.randn()
        else:
            return self.fitfunc(time, self.coefs)+np.sqrt(self.var)*random.randn()

class Electricity(object):
    """Electricity"""
    def __init__(self, data):
        self.data = data
        self.coefs = self.para()
        self.var = self.variance()

    def fitfunc(self, t, p):
        return p[0]+p[1]*t+p[2]*t*t 

    def err(self, p, x, y):
        return self.fitfunc(x,p)-y

    def para(self):
        x = years
        y = [self.data[t] for t in years]
        return leastsq(self.err,[30000,5000,1],args=(x,y))[0]

    def variance(self):
        return np.mean([(self.data[i]-self.fitfunc(i,self.coefs))**2 for i in years])

    def __call__(self, time, intr=False):
        return self.fitfunc(time, self.coefs)+np.sqrt(self.var)*random.randn()




#####################################################
# fit of Urban Engel

# def UrbanEngelFunction(t,p):
#     return p[1]/(t-p[0])

# def UrbanEngelResFunction(p):
#     return np.array([UrbanEngelFunction(t,p)-Data.UrbanEngel[t] for t in Data.UrbanEngel])

# UrbanEngelFitParam=leastsq(UrbanEngelResFunction,[1950,0.1])[0]

# def UrbanEngelFit(t):
#     return UrbanEngelFunction(t, UrbanEngelFitParam)*(1e-2*random.randn())

# # fit of Urban Engel

# def RuralEngelFunction(t,p):
#     return p[1]/(t-p[0])

# def RuralEngelResFunction(p):
#     return np.array([RuralEngelFunction(t,p)-Data.RuralEngel[t] for t in Data.RuralEngel])

# RuralEngelFitParam=leastsq(RuralEngelResFunction,[1950,0.1])[0]

# def RuralEngelFit(t):
#     return RuralEngelFunction(t, RuralEngelFitParam)*(1e-2*random.randn())
