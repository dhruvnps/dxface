from math import sqrt


class Lwpolyline:
    '''
    lwpolyline object
    '''

    END = '  0'
    X = ' 10'
    Y = ' 20'
    BULGE = ' 42'
    FLAG = ' 70'
    LAYER = '  8'

    # nested data structure
    class Vertex:
        '''
        data structure for vertex of lwpolyline entity
        '''

        # vertex data structure takes in x and y values
        # bulge value is optional, and defaults to None
        def __init__(self, x, y, bulge=None):

            # initialise x, y, bulge to inputted values
            self.x = x
            self.y = y
            self.bulge = bulge

    # lwpolyline object takes in the dxf list and the line
    # number where the lwpolyline entity can be found
    def __init__(self, dxf, start_line):

        # initialise empty list of vertices
        self.vertices = []

        # initialise polyline flag and id attributes
        self.flag = self.id = None

        # set current line number to input line number
        line = start_line

        # iterate over every line within the entity
        while dxf[line] != self.END:

            # if layer name found set id to layer name
            if dxf[line] == self.LAYER:
                self.id = dxf[line + 1]

            # if polyline flag found set flag attribute
            if dxf[line] == self.FLAG and self.flag is None:
                self.flag = int(dxf[line + 1])

            # if a coordinate is found
            if dxf[line] == self.X and dxf[line + 2] == self.Y:

                # create a vertex instance with the coordinate values
                vertex = self.Vertex(x=float(dxf[line + 1]),
                                     y=float(dxf[line + 3]))

                # search for bulge until next coordinate or end hit
                while dxf[line + 4] not in [self.X, self.END]:

                    # if bulge found add bulge attribute to vertex
                    if dxf[line + 4] == self.BULGE:
                        vertex.bulge = dxf[line + 5]
                        break

                    line += 1

                # add vertex to this instance (self)
                self.vertices.append(vertex)

            line += 1

    def get_arc(self, v1, v2):
        '''
        function to create arc command string for path
        v1 is previous vertex, v2 is current vertex
        '''

        # if not bulge return straight line command
        if v1.bulge is None or not float(v1.bulge):
            return 'L {} {} '.format(v2.x, -v2.y)

        # get distance between vertex and previous vertex
        dist = sqrt((v1.x - v2.x)**2 + (v1.y - v2.y)**2)

        # get radius using bulge -> radius equation
        bulge = float(v1.bulge)
        radius = dist * ((1 + bulge**2) / abs(4 * bulge))

        # return arc command
        return ('A {r} {r} 0 {largearc} {sweep} {x} {y} '
                ).format(r=radius, largearc=int(bulge > 1),
                         sweep=int(bulge < 0), x=v2.x, y=-v2.y)

    def svg_shape(self, color):
        '''
        function takes in color and returns
        svg path shape with given color
        '''

        # template svg path
        svg = ('<path id="{id}" d="{d}" stroke="{stroke}" ' +
               'stroke-width="50" fill="none" />\n')

        # initialise d string with move to command to first vertex
        v = self.vertices[0]
        d = 'M {} {} '.format(v.x, -v.y)

        # iterate over other vertices and add segments to d string
        for idx, v in enumerate(self.vertices[1:]):
            d += self.get_arc(self.vertices[idx], v)

        # close path if lwpolyline is closed
        if self.flag in [1, 129]:
            d += self.get_arc(self.vertices[-1], self.vertices[0])

        # return svg path
        return svg.format(d=d, stroke=color, id=self.id)
