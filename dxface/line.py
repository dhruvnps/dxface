class Line:
    '''
    line object
    '''

    END = '  0'
    X1, X2 = ' 10', ' 11'
    Y1, Y2 = ' 20', ' 21'
    Z1, Z2 = ' 30', ' 31'
    LAYER = '  8'

    # line object takes in the dxf list and the line
    # number where the line entity can be found
    def __init__(self, dxf, start_line):

        # initialise first point
        self.x1 = self.y1 = self.z1 = None

        # initialise second point
        self.x2 = self.y2 = self.z2 = None

        # initialise id attribute
        self.id = None

        # set current line number to input line number
        line = start_line

        # iterate over every line within the entity
        while dxf[line] != self.END:

            # if layer name found set id to layer name
            if dxf[line] == self.LAYER:
                self.id = dxf[line + 1]

            # if first point is found set x1, y1, z1 values
            if (dxf[line] == self.X1 and
                dxf[line + 2] == self.Y1 and
                    dxf[line + 4] == self.Z1):

                self.x1 = float(dxf[line + 1])
                self.y1 = float(dxf[line + 3])
                self.z1 = float(dxf[line + 5])

            # if second point is found set x2, y2, z2 values
            if (dxf[line] == self.X2 and
                dxf[line + 2] == self.Y2 and
                    dxf[line + 4] == self.Z2):

                self.x2 = float(dxf[line + 1])
                self.y2 = float(dxf[line + 3])
                self.z2 = float(dxf[line + 5])

            line += 1

    def svg_shape(self, color):
        '''
        function takes in color and returns
        svg line shape with given color
        '''

        # template svg line
        svg = ('<line id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" ' +
               'y2="{y2}" stroke="{stroke}" stroke-width="50" />\n')

        # return blank if line has no attributes (some have none)
        if self.x1 is None:
            return ''

        # return svg line
        return svg.format(x1=self.x1, y1=-self.y1, x2=self.x2,
                          y2=-self.y2, stroke=color, id=self.id)
