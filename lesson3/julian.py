from datetime import date
from jdcal import *
now = date.today()
jd = gcal2jd(now.year, now.month, now.day)
print('Calendar Date: {:d}'.format(now.isoformat()))
print('Julian Date: {:0.1f}'.format(jd[0]+jd[1]))
print('Modified Julian Date: {:s}'.format(jd))