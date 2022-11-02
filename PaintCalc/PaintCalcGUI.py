# this is a calculator that will show how much paint is needed to paint a surface

import tkinter as tk
from tkinter import ttk
from paintCalc import PaintCalc

# define window
root = tk.Tk()
rootWidth = 450
rootHeight = 520
root.geometry(f"{rootWidth}x{rootHeight}")
root.title("Paint calculator")

# resizes window when more buttons are added or removed
def resizeWindow():
    # will only make window smaller when number of walls are greater than or equal to 4
    if len(wallLenghtsEntries) - 4 > 0:
        rootHeight = 500 + (len(wallLenghtsEntries) - 4) * 50
        root.geometry(f"{rootWidth}x{rootHeight}")


# adds more entries and labels for wall lengths
def addWallEntries(numberOfRows):
    existingEntriesLength = len(wallLenghtsEntries)
    for i in range(numberOfRows):
        labelWall = tk.Label(root, text=f"Wall {1 + existingEntriesLength + i}", font="Calibri")
        labelWall.grid(row=6 + existingEntriesLength + i, column=0, pady=5, sticky="w")
        wallLenghtsLabels.append(labelWall)

        valueWall = tk.StringVar()
        valueWall.set("0")
        wallLengthsIntVars.append(valueWall)
        entryWall = ttk.Entry(root, textvariable=valueWall)
        entryWall.grid(row=6 + existingEntriesLength + i, column=1, pady=5)
        wallLenghtsEntries.append(entryWall)

        if numberOfRows == 1:
            adjustButtonPlacements()
            resizeWindow()


# removes entries for wall lengths
def removeWallEntries():
    # remove last entry widgets
    wallLenghtsEntries[-1].destroy()
    wallLenghtsLabels[-1].destroy()

    # remove last elements from list keeping track of wall length entries
    wallLengthsIntVars.pop()
    wallLenghtsEntries.pop()
    wallLenghtsLabels.pop()

    adjustButtonPlacements()
    resizeWindow()


# adjust buttons below entries when entries for wall lengths are added or subtracted
def adjustButtonPlacements():
    lastWallEntryPlacement = wallLenghtsEntries[-1].grid_info()
    row = lastWallEntryPlacement["row"]

    f1.grid(row=row+1)
    ButtonCalculate.grid(row=row+2)

    paintInLitersLabel.grid(row=row + 3)


# retrieves a list of all wall lengths
def getWallList():
    wallList = []
    for length in wallLengthsIntVars:
        wallList.append(float(length.get()))

    return wallList


# retrieves a string with minumum paint in liters
def calculatePaint():
    wallList = getWallList()
    numberOfDoors = valueDoors.get()
    numberOfWindows = valueWindows.get()
    wallHeight = float(valueHeight.get())
    paintLayers = valueLayers.get()


    paintCalc = PaintCalc(wallList, wallHeight, numberOfDoors, numberOfWindows, paintLayers)
    paintNeedInLiters = paintCalc.calculatePaintNeed()
    paintNeedText = f"You will need {paintNeedInLiters} liters of paint"

    paintInLitersLabel.config(text=paintNeedText)
    calculateButtonPlacement = ButtonCalculate.grid_info()
    row = calculateButtonPlacement["row"]
    paintInLitersLabel.grid(row=row+1, column=0)

# create layout
labelLayers = tk.Label(root, text="Paint layers", font="Calibri", fg="blue")
labelLayers.grid(row=1, column=0, pady = 10, sticky="w")

valueLayers = tk.IntVar()
entryLayers = ttk.Entry(root, textvariable=valueLayers)
entryLayers.grid(row=1, column=1, pady=10)

labelHeight = tk.Label(root, text="Height of wall", font="Calibri", fg="blue")
labelHeight.grid(row=2, column=0, pady=10, sticky="w")

valueHeight = tk.StringVar()
valueHeight.set("0")
entryHeight = ttk.Entry(root, textvariable=valueHeight)
entryHeight.grid(row=2, column=1, pady=10)

labelWindows = tk.Label(root, text="Number of windows", font="Calibri", fg="blue")
labelWindows.grid(row=3, column=0, pady=10, sticky="w")

valueWindows = tk.IntVar()
entryWindows = ttk.Entry(root, textvariable=valueWindows)
entryWindows.grid(row=3, column=1, pady=10)

labelDoors = tk.Label(root, text="Number of doors", font="Calibri", fg="blue")
labelDoors.grid(row=4, column=0, pady=10, sticky="w")

valueDoors = tk.IntVar()
entryDoors = ttk.Entry(root, textvariable=valueDoors)
entryDoors.grid(row=4, column=1, pady=10)

labelWallLengths = tk.Label(root, text="Wall lengths", font="Calibri", fg="blue")
labelWallLengths.grid(row=5, column=0, pady=10, columnspan=2)

wallLengthsIntVars = []
wallLenghtsEntries = []
wallLenghtsLabels = []
addWallEntries(4)

f1 = tk.Frame(root)
f1.grid(row=10, column=1)

ButtonPlus = tk.Button(f1, text="+", bg="magenta", width=1, command=lambda: addWallEntries(1))
ButtonPlus.grid(row=0, column=0, pady=5, padx=45)

ButtonMinus = tk.Button(f1, text="-", bg="red", width=1, command=removeWallEntries)
ButtonMinus.grid(row=0, column=1, pady=5, padx=45)

ButtonCalculate = tk.Button(root, text="Calculate", bg="green", command=calculatePaint)
ButtonCalculate.grid(row=11, column=1, pady=10)

# the "answer" widget will be blank until we hit calculate button
paintInLitersLabel = tk.Label(root, text="")
paintInLitersLabel.grid(row=12, column=0)

root.mainloop()