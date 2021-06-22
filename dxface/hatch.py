# class Hatch:
#     '''
#     hatch object
#     '''

#     END = '  0'
#     X1 = ' 10'
#     Y1 = ' 20'
#     X2 = ' 11'
#     Y2 = ' 21'
#     LAYER = '  8'

#     # nested data structure
#     class LineSeg:
#         '''
#         data structure for line segment of hatch entity
#         '''

#         # lineseg data structure takes in x1, y1, x2, y2 values
#         def __init__(self, x1, y1, x2, y2):

#             # initialise x1, y1, x2, y2 to inputted values
#             self.x1, self.x2 = x1, x2
#             self.y1, self.y2 = y1, y2

#     # hatch object takes in the dxf list and the line
#     # number where the hatch entity can be found
#     def __init__(self, dxf, start_line):

#         # initialise empty list of lines
#         self.lines = []

#         # initialise id attribute
#         self.id = None

#         # set current line number to input line number
#         line = start_line

#         # iterate over every line within the entity
#         while dxf[line] != self.END:

#             # if layer name found set id to layer name
#             if dxf[line] == self.LAYER:
#                 self.id = dxf[line + 1]

#             # if a line segment is found
#             if (dxf[line] == self.X1 and
#                 dxf[line + 2] == self.Y1 and
#                 dxf[line + 4] == self.X2 and
#                     dxf[line + 6] == self.Y2):

#                 # create a lineseg instance with the values
#                 lineseg = self.LineSeg(x1=float(dxf[line + 1]),
#                                        y1=float(dxf[line + 3]),
#                                        x2=float(dxf[line + 5]),
#                                        y2=float(dxf[line + 7]))

#                 # add line segment to this instance (self)
#                 self.lines.append(lineseg)

#             line += 1

#     def svg_shape(self, color):
#         '''
#         function takes in color and returns
#         svg polygon shape with given color
#         '''

#         # template svg polygon
#         svg = ('<polygon id="{id}" points="{points}" ' +
#                'fill="{fill}" />\n')

#         # convert list of lines to points string
#         points = ''
#         for l in self.lines:
#             points += '{},{} {},{} '.format(l.x1, -l.y1, l.x2, -l.y2)

#         # return svg polygon
#         return svg.format(points=points, fill=color, id=self.id)
