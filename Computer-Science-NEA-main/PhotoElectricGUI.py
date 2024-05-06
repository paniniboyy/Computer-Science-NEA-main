import tkinter as tk
import matplotlib.pyplot as plt
from PhotoElectricSim import Metal, MetalCaesium, MetalIron, MetalSodium, MetalBarium, MetalSilver, MetalMagnesium, MetalCadmium, MetalAluminium, MetalNickel, MetalCopper, MetalTungsten, MetalChromium, MetalZinc, MetalGold, MetalLead, Radiation

class PhotoElectricGUI:
    def __init__(self, master):
        self.master = master
        master.title("Photoelectric effect Simulation")

        # Metal selection
        self.metalLabel = tk.Label(master, text="Select Metal:")
        self.metalLabel.grid(row = 0, column = 0)
        self.metalVar = tk.StringVar()
        self.metalDropdown = tk.OptionMenu(master, self.metalVar, "Caesium", "Iron", "Sodium", "Barium", "Silver", "Magnesium", "Cadmium", "Aluminium", "Nickel", "Copper", "Tungsten", "Chromium", "Zinc", "Gold", "Lead")
        self.metalDropdown.grid(row = 0, column = 1)
        #Line 13 contains all the metals I have created subclasses for in the main file

        # Frequency input (Slider)
        self.frequencyLabel = tk.Label(master, text="Frequency (Hz):")
        self.frequencyLabel.grid(row = 1, column = 0)
        self.frequencyScale = tk.Scale(master, from_= 1e14, to = 1.5e15 , orient=tk.HORIZONTAL, resolution = 1e12, length = 300)
        self.frequencyScale.grid(row = 1, column = 1)   

        # Plot
        self.figure, self.ax = plt.subplots()
        self.ax.set_xlabel('Frequency (Hz)')
        self.ax.set_ylabel('Electron Kinetic Energy (J)')

        # Warning message
        self.warningVar = tk.StringVar()
        self.warningLabel = tk.Label(master, textvariable = self.warningVar, fg = "red")
        self.warningLabel.grid(row = 2, columnspan = 2)

        # Result display
        self.resultLabel = tk.Label(master, text = "Wavelength (m):")
        self.resultLabel.grid(row = 3, column = 0)
        self.resultVar = tk.StringVar()
        self.resultEntry = tk.Entry(master, state = 'readonly', textvariable = self.resultVar)
        self.resultEntry.grid(row = 3, column = 1)

        # Calculate button
        self.calculateButton = tk.Button(master, text = "Calculate", command = self.calculateWavelength)
        self.calculateButton.grid(row = 4, columnspan = 2 )

    def calculateWavelength(self):
        metalName = self.metalVar.get()
        frequency = self.frequencyScale.get()

    # Create Metal instance based on selection
        metalInstance = None
        if metalName == "Caesium":
            metalInstance = MetalCaesium("Caesium", 2.12, 0, 0)
        elif metalName == "Iron":
            metalInstance = MetalIron("Iron", 4.36, 0, 0)
        elif metalName == "Sodium":
            metalInstance = MetalSodium("Sodium", 2.27, 0, 0)
        elif metalName == "Barium":
            metalInstance = MetalBarium("Barium", 2.51, 0, 0)
        elif metalName == "Silver":
            metalInstance = MetalSilver("Silver", 4.28, 0, 0)
        elif metalName == "Magnesium":
            metalInstance = MetalMagnesium("Magnesium", 3.46, 0, 0)
        elif metalName == "Cadmium":
            metalInstance = MetalCadmium("Cadmium", 3.92, 0, 0)
        elif metalName == "Aluminium":
            metalInstance = MetalAluminium("Aluminium", 3.74, 0, 0)
        elif metalName == "Nickel":
            metalInstance = MetalNickel("Nickel", 4.84, 0, 0)
        elif metalName == "Copper":
            metalInstance = MetalCopper("Copper", 4.47, 0, 0)
        elif metalName == "Tungsten":
            metalInstance = MetalTungsten("Tungsten", 4.5, 0, 0)
        elif metalName == "Chromium":
            metalInstance = MetalChromium("Chromium", 4.51, 0, 0)
        elif metalName == "Zinc":
            metalInstance = MetalZinc("Zinc", 3.74, 0, 0)
        elif metalName == "Gold":
            metalInstance = MetalGold("Gold", 4.58, 0, 0)
        elif metalName == "Lead":
            metalInstance = MetalLead("Lead", 4.02, 0, 0)

        if metalInstance is not None:
            radiation = Radiation(0, 0, frequency, metalInstance)
            wavelength = radiation.FindWavelength()
            kineticEnergy = metalInstance.CalculateElectronKineticEnergy(frequency, metalInstance.WorkFunctionEV)
            wavelength = radiation.FindWavelength()
            self.resultVar.set(wavelength)

            # Update plot
            self.ax.plot(frequency, kineticEnergy, marker='o', linestyle='-', label=metalName)
            self.ax.legend()
            self.figure.canvas.draw()


            # Check if frequency is below threshold and show warning if necessary
            threshold_frequency = metalInstance.ValidateFrequency()
            if frequency < threshold_frequency:
                self.warningVar.set("Warning: Frequency is below the threshold frequency of the metal.")
            else:
                self.warningVar.set("")


def main():
    root = tk.Tk()
    root.geometry("1280x720")  #Sets window size
    app = PhotoElectricGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()


