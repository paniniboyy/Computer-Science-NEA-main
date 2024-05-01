import random
import numpy as np
import tkinter as tk
import PhotoElectricGUI as slider



class Metal():
    def __init__(self, MetalName, WorkFunctionEV, x, y, width = 6, height = 4):
        self.x = x #x is used to declare where the metal will be on the x-axis/horizontal direction
        self.y = y #y is used to delclare where the metal will be on the y-axis/vertical direction
        self.width = width #width of metal is constant value, 6
        self.height = height #height of metal is constant value, 4
        self.name = MetalName #takes the name of the metal as a string
        self.WorkFunctionEV = WorkFunctionEV #takes the work function of the metal in Electron Volts as a float value

    def ValidateFrequency(self, f, WorkFunctionEV):
        h = 6.63 * 10**-34 #Plancks constant
        E = WorkFunctionEV * (1.6 * 10**-19) #Converts the Work Function in electron volts into joules
        f = E/h #This is the threshold frequency for the metals
        return f
    
    def CalculateElectronKineticEnergy(self, frequency, WorkFunctionEV):
        h = 6.63 * 10**-34 #Plancks constant
        WorkFunctionJ = WorkFunctionEV * (1.6 * 10**-19) #Converts the Work Function in electron volts into joules
        KineticEnergy = (h * frequency) - WorkFunctionJ
        return KineticEnergy
        
#Each subsequent class inherits from the class Metal, keeping the same height, width, x and y dimensions but having different names and work functions

class MetalCaesium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Caesium" , 2.12)

class MetalIron(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Iron", 4.36)
        self.name = "Iron"
        self.WorkFunctionEV = 4.36

class MetalSodium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Sodium" , 2,27)
       
class MetalBarium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Barium" , 2.51)

class MetalSilver(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Silver", 4.28)

class MetalMagnesium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Magnesium", 3.46)

class MetalCadmium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Cadmium", 3.92)

class MetalAluminium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Aluminium", 3.74)

class MetalNickel(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Nickel", 4.84)

class MetalCopper(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Copper", 4.47)

class MetalTungsten(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Tungsten", 4.5)

class MetalChromium(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Chromium", 4.51)

class MetalZinc(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Zinc", 3.74)

class MetalGold(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Gold", 4.58)

class MetalLead(Metal):
    def __init__(self, x, y):
        super().__init__(x, y, "Lead", 4.02)

class Radiation():# This class represents a radiation source with its x and y coordinates, wavelength, and frequency.
    def __init__(self, x, y, wavelength, frequency):
        self.x = x #x coordinate of the radiation source
        self.y = y #y coordinate of the radiation source
        self.wavelength = wavelength #wavelength of radiation source given as a float value
        self.frequency = frequency #frequency of radiation source given as a float value

    




        
        

    