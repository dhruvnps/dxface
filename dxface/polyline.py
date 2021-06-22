class Polyline:
    '''
    polyline object
    '''

    END = 'SEQEND'
    X = ' 10'
    Y = ' 20'
    Z = ' 30'
    FLAG = ' 70'
    LAYER = '  8'

    # nested data structure
    class Vertex:
        '''
        data structure for vertex of polyline entity
        '''

        # vertex data structure takes in x, y, z values
        def __init__(self, x, y, z):

            # initialise x, y, z to inputted values
            self.x = x
            self.y = y
            self.z = z

    # polyline object takes in the dxf list and the line
    # number where the polyline entity can be found
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

            # if a vertex entity is found
            if dxf[line] == 'VERTEX':

                # iterate until a coordinate is found
                while (dxf[line] != self.X or
                       dxf[line + 2] != self.Y or
                       dxf[line + 4] != self.Z):
                    line += 1

                # create a vertex instance with the coordinate values
                vertex = self.Vertex(x=float(dxf[line + 1]),
                                     y=float(dxf[line + 3]),
                                     z=float(dxf[line + 5]))

                # add vertex to this instance (self)
                self.vertices.append(vertex)

            line += 1

    def svg_shape(self, color):
        '''
        function takes in color and returns
        svg polyline shape with given color
        '''

        # template svg polyline
        svg = ('<polyline id="{id}" points="{points}" ' +
               'stroke="{stroke}" stroke-width="50" fill="none" />\n')

        # convert list of vertices to points string
        points = ''
        for v in self.vertices:
            points += '{},{} '.format(v.x, -v.y)

        # if polyline is closed add another first vertex at end
        if self.flag in [1, 129]:
            v = self.vertices[0]
            points += '{},{} '.format(v.x, -v.y)

        # return svg polyline
        return svg.format(points=points, stroke=color, id=self.id)
