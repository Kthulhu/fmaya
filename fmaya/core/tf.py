try:
    import maya.cmds as cmds
except ImportError:
    print 'WARNING (%s): failed to load maya.cmds module.' % __file__

from .pure import uncurry


# PURE

xyzAdd = lambda (x,y,z): lambda (u,v,w): (x+u, y+v, z+w)
xyzSub = lambda (x,y,z): lambda (u,v,w): (x-u, y-v, z-w)
xyzMul = lambda (x,y,z): lambda (u,v,w): (x*u, y*v, z*w)
xyzDiv = lambda (x,y,z): lambda (u,v,w): (float(x)/float(u), float(y)/float(v), (z)/float(w))
xyzScale = lambda s: lambda (x,y,z): (s*x, s*y, s*z)
xyzAvg = lambda xs: [] if len(xs) == 0 else xyzScale(1.0/len(xs))(reduce(uncurry(xyzAdd), xs, (0,0,0)))

