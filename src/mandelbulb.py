import taichi as ti
import taichi.math as tm

@ti.func
def mandelbulb(p,iter,scale):
   # go to spheric space
   p.xyz = p.xzy
   #declare variable Z with all coordonates
   z = p
   power = 8.
   #radial distance
   dr = 1.
   #norme of r
   r=0.

   for i in range(iter):
      r = tm.length(z)
      # if r>2 : point too far -> break
      if r > 2.:break
      #angle in X,Y plan
      theta = ti.atan2(z.y,z.x)
      # vertical angle 
      phi = tm.acos(z.z/r)

      # basic distance estimator of mandelbulb
      dr = power * (r**(power-1.)) * dr +1.

      # raising for next iteration
      r = r ** power
      theta *= power
      phi*=power

      # return in normal plan
      z = r* tm.vec3(tm.cos(theta)*tm.cos(phi),tm.sin(theta)*tm.cos(phi),tm.sin(phi))+p

   # final distance estimator
   return (.5*tm.log(r)*r / dr)*scale