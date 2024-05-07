import tkinter as tk
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PhotoElectricSim import Metal, MetalCaesium, MetalIron, MetalSodium, MetalBarium, MetalSilver, MetalMagnesium, MetalCadmium, MetalAluminium, MetalNickel, MetalCopper, MetalTungsten, MetalChromium, MetalZinc, MetalGold, MetalLead, Radiation
import numpy as np



class PhotoElectricGUI:
    def __init__(self, master):
        self.master = master
        master.title("Photoelectric effect Simulation")

        # Metal selection
        self.metalLabel = tk.Label(master, text="Select Metal:")
        self.metalLabel.grid(row=0, column=0)
        self.metalVar = tk.StringVar()
        self.metalDropdown = tk.OptionMenu(master, self.metalVar, "Caesium", "Iron", "Sodium", "Barium", "Silver", "Magnesium", "Cadmium", "Aluminium", "Nickel", "Copper", "Tungsten", "Chromium", "Zinc", "Gold", "Lead")
        self.metalDropdown.grid(row=0, column=1)

        # Frequency input (Slider)
        self.frequencyLabel = tk.Label(master, text="Frequency (Hz):")
        self.frequencyLabel.grid(row=1, column=0)
        self.frequencyScale = tk.Scale(master, from_=1e14, to=1.5e15, orient=tk.HORIZONTAL, resolution=1e12, length=300)
        self.frequencyScale.grid(row=1, column=1)

        #Initialize plot
        self.figure, self.ax = plt.subplots() # Create a figure and axis for the plot
        self.ax.set_xlabel('Frequency / (Hz)') # Set the label for the x-axis
        self.ax.set_ylabel('Electron Kinetic Energy / (J)') # Set the label for the y-axis
        self.plot, = self.ax.plot([], [], marker='o', linestyle='-') # Create an empty plot line with markers

        # Embed Matplotlib figure in Tkinter window
        self.canvas = FigureCanvasTkAgg(self.figure, master=master) # Create a canvas for the figure
        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=5) # Place the canvas in the Tkinter window

        # Initalize metalInstance attribute to None
        self.metalInstance = None

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
        self.calculateButton = tk.Button(master, text="Calculate", command=self.updatePlotWrapper)
        self.calculateButton.grid(row = 4, columnspan = 2)

        # Metal graphics
        self.metal_graphics = tk.Canvas(master, width=100, height=100)
        self.metal_graphics.grid(row=20, column=1, rowspan=5)
        # Draw metal
        self.drawMetal()
        
        # Background color selection
        self.colorLabel = tk.Label(master, text="Select Background Color:")
        self.colorLabel.grid(row=4, column=3) 
        self.colorVar = tk.StringVar()
        self.colorVar.set("White")  # Default color
        self.colorDropdown = tk.OptionMenu(master, self.colorVar, "White", "Gray", "Black")
        self.colorDropdown.grid(row=4, column=4)  

        # Apply button to change background color
        self.applyButton = tk.Button(master, text="Apply", command=self.changeBackgroundColor)
        self.applyButton.grid(row=4, column=5)  

    def changeBackgroundColor(self):
        color = self.colorVar.get()
        if color == "White":
            self.canvas.get_tk_widget().configure(background="white")
        elif color == "Gray":
            self.canvas.get_tk_widget().configure(background="gray")
        elif color == "Black":
            self.canvas.get_tk_widget().configure(background="black")

    def drawMetal(self):
    # Draw metal graphic
        self.metal_graphics.create_rectangle(10, 10, 90, 90, fill="gray", outline="black")
    
    def updatePlotWrapper(self):
        value = self.frequencyScale.get()
        frequency = float(value)
        self.updatePlot(value)
        self.emitElectron(frequency)  # Pass the frequency to emitElectron
        self.metalInstance = None


    def updatePlot(self, value): 
        print("Updating plot with value:", value) #Debug Statement
        frequency = float(value)
        #All instances of metal called here
        metalName = self.metalVar.get()
        if metalName == "Caesium":
            self.metalInstance = MetalCaesium("Caesium", 2.12, 0, 0)
        elif metalName == "Iron":
            self.metalInstance = MetalIron("Iron", 4.36, 0, 0)
        elif metalName == "Sodium":
            self.metalInstance = MetalSodium("Sodium", 2.27, 0, 0)
        elif metalName == "Barium":
            self.metalInstance = MetalBarium("Barium", 2.51, 0, 0)
        elif metalName == "Silver":
            self.metalInstance = MetalSilver("Silver", 4.28, 0, 0)
        elif metalName == "Magnesium":
            self.metalInstance = MetalMagnesium("Magnesium", 3.46, 0, 0)
        elif metalName == "Cadmium":
            self.metalInstance = MetalCadmium("Cadmium", 3.92, 0, 0)
        elif metalName == "Aluminium":
            self.metalInstance = MetalAluminium("Aluminium", 3.74, 0, 0)
        elif metalName == "Nickel":
            self.metalInstance = MetalNickel("Nickel", 4.84, 0, 0)
        elif metalName == "Copper":
            self.metalInstance = MetalCopper("Copper", 4.47, 0, 0)
        elif metalName == "Tungsten":
            self.metalInstance = MetalTungsten("Tungsten", 4.5, 0, 0)
        elif metalName == "Chromium":
            self.metalInstance = MetalChromium("Chromium", 4.51, 0, 0)
        elif metalName == "Zinc":
            self.metalInstance = MetalZinc("Zinc", 3.74, 0, 0)
        elif metalName == "Gold":
            self.metalInstance = MetalGold("Gold", 4.58, 0, 0)
        elif metalName == "Lead":
            self.metalInstance = MetalLead("Lead", 4.02, 0, 0)
        else:
            self.metalInstance = None

    def emitElectron(self, frequency):
        if self.metalInstance is not None:
        # Check if frequency exceeds the threshold
            threshold_frequency = self.metalInstance.ValidateFrequency()
            if frequency >= threshold_frequency:
            # Emit electron graphic from the metal
                self.metal_graphics.create_oval(40, 0, 60, 10, fill="yellow")  # Oval representing electron
        else:
        # Handle the case when metal instance is None
            print("Error: No metal instance available")


        if self.metalInstance is not None:
        # Check threshold frequency
            thresholdFrequency = self.metalInstance.ValidateFrequency()
            if frequency < thresholdFrequency:
                self.warningVar.set("Warning: Frequency is below the threshold frequency of the metal.")
            else:
                self.warningVar.set("")  # Clear the warning message if frequency is within threshold

        # Calculate electron kinetic energy
            kineticEnergy = self.metalInstance.CalculateElectronKineticEnergy(frequency, self.metalInstance.WorkFunctionEV)
            print("Calculated kinetic energy:", kineticEnergy)  # Print calculated kinetic energy
        
        # Plot point on the graph
            plot_data_x = np.concatenate([self.plot.get_xdata(), [frequency]])
            plot_data_y = np.concatenate([self.plot.get_ydata(), [kineticEnergy]])
            print("Plot data x:", plot_data_x)  # Debug statement
            print("Plot data y:", plot_data_y)  # Debug statement
            self.plot.set_data(plot_data_x, plot_data_y)

            self.ax.relim()
            self.ax.autoscale_view()
            self.canvas.draw()

        # Print x-axis and y-axis limits
            print("X-axis limits:", self.ax.get_xlim()) # Debug statement
            print("Y-axis limits:", self.ax.get_ylim()) # Debug statement

        # Calculate and display wavelength
            radiation = Radiation(0, 0, frequency, self.metalInstance)
            wavelength = radiation.FindWavelength()
            self.resultVar.set(wavelength)
        else:
            self.warningVar.set("Error: Metal selection not recognized.")  # Set warning message for unrecognized metal selection





def main():
    root = tk.Tk()
    root.geometry("1280x720")  #Sets window size
    app = PhotoElectricGUI(root)
    root.mainloop() 


if __name__ == "__main__":
    main()


