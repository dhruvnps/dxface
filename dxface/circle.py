class Circle:
    '''
    circle object
    '''

    END = '  0'
    X = ' 10'
    Y = ' 20'
    Z = ' 30'
    RADIUS = ' 40'
    LAYER = '  8'

    # circle object takes in the dxf list and the line
    # number where the circle entity can be found
    def __init__(self, dxf, start_line):

        # initialise x, y, z, radius and id attributes
        self.x = self.y = self.z = self.radius = self.id = None

        # set current line number to input line number
        line = start_line

        # iterate over every line within the entity
        while dxf[line] != self.END:

            # if layer name found set id to layer name
            if dxf[line] == self.LAYER:
                self.id = dxf[line + 1]

            # if a coordinate is found set x, y, z values
            if (dxf[line] == self.X and
                dxf[line + 2] == self.Y and
                    dxf[line + 4] == self.Z):

                self.x = float(dxf[line + 1])
                self.y = float(dxf[line + 3])
                self.z = float(dxf[line + 5])

            # if radius is found set radius
            if (dxf[line] == self.RADIUS):
                self.radius = float(dxf[line + 1])

            line += 1

    def svg_shape(self, color):
        '''
        function takes in color and returns
        svg circle shape with given color
        '''

        # template svg circle
        svg = ('<circle id="{id}" cx="{cx}" cy="{cy}" r="{r}" ' +
               'stroke="{stroke}" stroke-width="50" ' +
               'fill="none" />\n')

        # return svg circle
        return svg.format(cx=self.x, cy=-self.y, r=self.radius,
                          stroke=color, id=self.id)
