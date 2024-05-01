import random
import numpy as np
import tkinter as tk

class Metal():
    def __init__(self, MetalName, WorkFunctionEV, x, y, width = 6, height = 4):
        self.name = MetalName #takes the name of the metal as a string
        self.WorkFunctionEV = WorkFunctionEV #takes the work function of the metal in Electron Volts as a float value
        self.x = x #x is used to declare where the metal will be on the x-axis/horizontal direction
        self.y = y #y is used to delclare where the metal will be on the y-axis/vertical direction
        self.width = width #width of metal is constant value, 6
        self.height = height #height of metal is constant value, 4

    def ValidateFrequency(self):
        h = 6.63 * 10**-34
        E = self.WorkFunctionEV * (1.6 * 10**-19)
        f = E / h
        return f
    
    
    def CalculateElectronKineticEnergy(self, frequency, WorkFunctionEV):
        h = 6.63 * 10**-34 #Plancks constant
        WorkFunctionJ = WorkFunctionEV * (1.6 * 10**-19) #Converts the Work Function in electron volts into joules
        KineticEnergy = (h * frequency) - WorkFunctionJ
        return KineticEnergy
        
#Each subsequent class inherits from the class Metal, keeping the same height, width, x and y dimensions but having different names and work functions

class MetalCaesium(Metal):
    def __init__(self, MetalName , WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x , y, width=6, height=4)
        self.MetalName = "Caesium"
        self.WorkFunctionEV = 2.12


class MetalIron(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Iron"
        self.WorkFunctionEV = 4.36

class MetalSodium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Sodium"
        self.WorkFunctionEV = 2.27
       
class MetalBarium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Barium"
        self.WorkFunctionEV = 2.51

class MetalSilver(Metal):
    def __init__(self,MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Silver"
        self.WorkFunctionEV = 4.28

class MetalMagnesium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Magnesium"
        self.WorkFunctionEV = 3.46

class MetalCadmium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Cadmium"
        self.WorkFunctionEV = 3.92

class MetalAluminium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Aluminium"
        self.WorkFunctionEV = 3.74

class MetalNickel(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Nickel"
        self.WorkFunctionEV = 4.84

class MetalCopper(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Copper"
        self.WorkFunctionEV = 4.47

class MetalTungsten(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Tungsten"
        self.WorkFunctionEV = 4.5

class MetalChromium(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Chromium"
        self.WorkFunctionEV = 4.51

class MetalZinc(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Zinc"
        self.WorkFunctionEV = 3.74

class MetalGold(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Gold"
        self.WorkFunctionEV = 4.58

class MetalLead(Metal):
    def __init__(self, MetalName, WorkFunctionEV, x, y, width=6, height=4):
        super().__init__(MetalName, WorkFunctionEV, x, y, width=6, height=4)
        self.MetalName = "Lead"
        self.WorkFunctionEV = 4.02  

class Radiation():
    def __init__(self, x, y, frequency, metal=None, wavelength=None):
        self.x = x  # Sets the x coordinate for the radiation source
        self.y = y  # Sets the y coordinate for the radiation source
        self.frequency = frequency
        self.metal = metal  # Metal instance associated with the radiation source
        self.wavelength = wavelength

    def FindWavelength(self):
        if self.wavelength is None:
            if self.metal is not None:
                threshold_frequency = self.metal.ValidateFrequency()
                if self.frequency < threshold_frequency:
                    print("Warning: Frequency of the radiation is below the threshold frequency of the metal.")
            c = 3 * 10**8  # Speed of light
            self.wavelength = c / self.frequency
        return self.wavelength

    
caesium = MetalCaesium("Caesium", 2.12, 0 , 0)
radiationFrequency = float(input("Enter frequency: "))
radiation = Radiation(0 , 0, radiationFrequency, metal = caesium)
wavelengthValue = radiation.FindWavelength()
print("Wavelength: ", wavelengthValue)






    




        
        

    