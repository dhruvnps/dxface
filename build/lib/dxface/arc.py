from math import sin, cos, radians, pi


class Arc:
    '''
    arc object
    '''

    END = '  0'
    X = ' 10'
    Y = ' 20'
    Z = ' 30'
    RADIUS = ' 40'
    ANGLE_1 = ' 50'
    ANGLE_2 = ' 51'
    LAYER = '  8'

    # arc object takes in the dxf list and the line
    # number where the arc entity can be found
    def __init__(self, dxf, start_line):

        # initialise x, y, z, radius and id attributes
        self.x = self.y = self.z = self.radius = self.id = None

        # initialise start angle and end angle attributes
        self.angle_1 = self.angle_2 = None

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

            # if angles found set start angle and end angle
            if (dxf[line] == self.ANGLE_1 and
                    dxf[line + 2] == self.ANGLE_2):
                self.angle_1 = float(dxf[line + 1])
                self.angle_2 = float(dxf[line + 3])

            line += 1

    def svg_shape(self, color):
        '''
        function takes in color and returns
        svg path arc shape with given color
        '''

        # template svg path arc
        svg = ('<path id="{id}" d="M {x1} {y1} A {r} {r} 0 ' +
               '{largearc} {sweep} {x2} {y2}" stroke="{stroke}" ' +
               'stroke-width="50" fill="none" />\n')

        # calculate start and end points of the arc
        a1, a2 = radians(self.angle_1), radians(self.angle_2)
        x, y, r = self.x, self.y, self.radius
        x1, y1 = r * cos(a1) + x, r * sin(a1) + y
        x2, y2 = r * cos(a2) + x, r * sin(a2) + y

        # return svg path arc
        return svg.format(x1=x1, y1=-y1, x2=x2, y2=-y2,
                          r=r, stroke=color, id=self.id,
                          largearc=int((a2 - a1) % (2*pi) > pi),
                          sweep=0)
