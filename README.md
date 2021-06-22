# dxface
**Python interface for AutoCAD DXF.**

## Installation
Using **pip**:
```console
$ pip install dxface
```

## Supported Objects

> The following DXF graphical objects are supported:

- POLYLINE
- LWPOLYLINE
- CIRCLE
- ARC
- LINE


## Usage
Import the `Entities` object.

```python
from dxface import Entities
```

Create instance of `Entities` from DXF file.

```python
with open('drawing.dxf', 'r') as f:
  dxf = f.read().splitlines()
  entities = Entities(dxf)
```

Convert to **SVG**.

```python
svg = entities.svg()
with open('drawing.svg', 'w') as f:
  f.write(svg)
```

Access sublists containing DXF graphical objects

```python
polylines = entities.polylines
lwpolylines = entities.lwpolylines
circles = entities.circles
arcs = entities.arcs
lines = entities.lines
```

### UML diagram of `Entities` object

![Entities](https://github.com/dhruvnps/dxface/blob/master/images/uml.png?raw=true)