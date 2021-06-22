from polyline import Polyline
from lwpolyline import Lwpolyline
from line import Line
from circle import Circle
from arc import Arc


class Entities:
    '''
    data structure for containing all graphical entities
    '''

    # entities data structure takes no inputs
    def __init__(self, dxf=None):

        # initialise empty lists to be populated with instances
        # of each type of graphical entity data structure

        self.lwpolylines = []
        self.lines = []
        self.circles = []
        self.polylines = []
        self.arcs = []

        # return as empty if dxf not provided
        if dxf == None:
            return

        # iterate over every line in the dxf entities section
        line = dxf.index('ENTITIES')
        while dxf[line] != 'ENDSEC':

            # if an entity is found, append an instance of the
            # entity to the corresponding list attribute of this
            # instance (self)

            if dxf[line] == 'LWPOLYLINE':
                self.lwpolylines.append(Lwpolyline(dxf, line))

            elif dxf[line] == 'CIRCLE':
                self.circles.append(Circle(dxf, line))

            elif dxf[line] == 'LINE':
                self.lines.append(Line(dxf, line))

            elif dxf[line] == 'POLYLINE':
                self.polylines.append(Polyline(dxf, line))

            elif dxf[line] == 'ARC':
                self.arcs.append(Arc(dxf, line))

            line += 1

    def svg(self, g=None, script=None, start=True, end=True):
        '''
        construct an svg document as a string
        using the objects from the entity lists
        '''

        # initialise svg string as start tag
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" ' +
               'xmlns:xlink="http://www.w3.org/1999/xlink">\n'
               if start else '')

        # if script name is present add script reference to svg
        if script is not None:
            svg += '<script xlink:href="{}" />\n'.format(script)

        # data list of object lists
        data = ((self.polylines, 'blue'),
                (self.lwpolylines, 'green'),
                (self.circles, 'black'),
                (self.arcs, 'magenta'),
                (self.lines, 'red'))

        # if group name is present add g tag to svg
        if g is not None:
            svg += '<g id="{}">\n'.format(g)

        # add svg shape of each object from each object list
        for li, color in data:
            svg += ''.join(map(lambda x: x.svg_shape(color), li))

        # return with closing tags
        svg += ('</g>\n' if g else '')
        return svg + ('</svg>' if end else '')
