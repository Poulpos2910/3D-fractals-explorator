import taichi as ti
import taichi.math as tm

@ti.func
def sdfTriangle3(p, d):
   a,b,c = calcFromH(d)
   q = p

   #normals
   n0 = (b - a).cross(c - a)  # face ABC
   n1 = (c - a).cross(d - a)  # face ACD
   n2 = (d - a).cross(b - a)  # face ADB
   n3 = (d - b).cross(c - b)  # face BDC

   #plans
   d0 = (q - a).dot(n0) / ti.sqrt(n0.dot(n0))
   d1 = (q - a).dot(n1) / ti.sqrt(n1.dot(n1))
   d2 = (q - a).dot(n2) / ti.sqrt(n2.dot(n2))
   d3 = (q - b).dot(n3) / ti.sqrt(n3.dot(n3))

   return ti.max(ti.max(d0, d1), ti.max(d2, d3))




v3 = ti.Vector([.5,tm.sqrt(2/3),tm.sqrt(3)/6])


@ti.func
def calcFromH(h):
   #points
   a=ti.Vector([h.x-.5 ,h.y-tm.sqrt(2/3),h.z-tm.sqrt(3)/6])
   b=ti.Vector([h.x+.5 ,h.y-tm.sqrt(2/3) ,h.z-tm.sqrt(3)/6])
   c=ti.Vector([h.x ,h.y-tm.sqrt(2/3) ,h.z+tm.sqrt(3)/3])
   return a,b,c


@ti.func
def sierpinski(p, iterations,scaleN):
   d=v3
   q = p
   a, b, c = calcFromH(d)

   # scale = scaleN*.00001
   scale=scaleN
   for i in range(iterations):
      # distances²
      da = (q - a).dot(q - a)
      db = (q - b).dot(q- b)
      dc = (q - c).dot(q - c)
      dd = (q - d).dot(q - d)

      # searching for closest
      closest = a
      minDist = da

      if db < minDist:
            minDist = db
            closest = b
      if dc < minDist:
            minDist = dc
            closest = c
      if dd < minDist:
            closest = d

      # fractal transformation
      q = (q - closest) * 2.0 + closest

      scale *= 2.0

   return sdfTriangle3(q, d) / scale
