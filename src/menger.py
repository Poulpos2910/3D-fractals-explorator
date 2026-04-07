import taichi as ti
import taichi.math as tm



@ti.func
def cubeSDF(p, cote):
    q = abs(p) - cote
    return tm.length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0)

@ti.func
def menger(p,iter,scaleN):
    d = cubeSDF(p,tm.vec3(1.)) #cube
    scale = scaleN
    for i in range(iter):

        #set to scale
        a = tm.mod(p*scale,2.)-1.
        scale*=3.
        r = abs(1. - 3.*ti.abs(a))

        #remove cross 
        da = max(r.x,r.y)
        db = max(r.y,r.z)
        dc = max(r.z,r.x)
        c = (min(da,min(db,dc))-1.)/scale
        d = max(d,c)
    return d



