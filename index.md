## (sort of) Recommender System for Tilling Windows Manager 
### Tilling Windows Manager
According to wikipedia:
> A tiling window manager is a window manager with an organization of the screen into mutually non-overlapping frames.

Mainly, this is done through *List-based* or *Tree-based* approaches.

#### List-based
In this method, windows are items in an ordered list. changing the position of windows in the list, rearrange windows. Different layouts could be applied. To illustrate this, consider a list of windows as *[1, 2, 3, 4, 5, ...]*. Then some layouts are depicted below.

* Stack
![Stack layout](/pic/stack.svg)
* hStack
![hStack layout](/pic/hstack.svg)
* Monocle
![Monocle layout](/pic/monocle.svg)
* Grid
![Grid layout](/pic/grid.svg)
* ...
#### Tree-based
in this method, windows are the leaves of a tree. and every internal node is a horizontal or vertical split that divides its own space among its children.

* Example 
