def oc(v0,i0,w0):
  import math
  npf=w0/(v0*i0)
  iw=i0*npf
  imu=i0*math.sqrt(1-npf**2)
  r0=v0/iw
  x0=v0/imu
  return r0,x0

def sc(vsc,isc,wsc):
  import math
  rhv=wsc/(isc**2)
  zhv=vsc/isc
  xhv=math.sqrt(zhv**2-rhv**2)
  return rhv,xhv

def eff(rating,w0,wsc,x,pf):
  e=(x*rating*pf)*100/((x*rating*pf)+w0+wsc*x*x)
  return e