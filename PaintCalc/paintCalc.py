# this class will calculate minimum paint needed in liters

class PaintCalc:
    def __init__(self, wallLengths, wallHeight, numberOfDoors, numberOfWindows, paintLayers):
        self.wallLengths = wallLengths
        self.wallHeight = wallHeight
        self.numberOfDoors = numberOfDoors
        self.numberOfWindows = numberOfWindows
        self.paintLayers = paintLayers


    # calculates the minimum paint need in liters
    def calculatePaintNeed(self):
        paintLayers = self.paintLayers

        squareMetersPerLiterPaint = 9
        area = self.getArea()

        paintNeed = round(area / squareMetersPerLiterPaint, 1) * paintLayers

        # don't give negative values
        if paintNeed < 0:
            paintNeed = 0

        return str(paintNeed)


    # retrieves the area for the surface to be painted
    def getArea(self):
        height = self.wallHeight
        numberOfWindows = self.numberOfWindows
        numberOfDoors = self.numberOfDoors

        area = 0
        for wallLength in self.wallLengths:
            area += height * wallLength

        windowArea = 1.2
        area -= numberOfWindows * windowArea

        doorArea = 2
        area -= numberOfDoors * doorArea

        return area
