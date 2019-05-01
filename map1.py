#!/usr/bin/env python
import sys
def function(a):
    return {'ID':a[0],
            'DATE':a[1],
            'TYPE':a[2],
            'VALUE':a[3],
            'MFLAG':a[4],
            'QFLAG':a[5],
            'SFLAG':a[6],
            'OBSTIME':a[7]}
for l in sys.stdin:
    data = l.strip().upper().split(',')
    c = function(data)
    if 'TMAX' != c['TYPE'] and 'TMIN' != c['TYPE']:
        continue
    if c['VALUE'] == -9999:
        continue
    if c['SFLAG'] == '':
        continue
    if c['QFLAG'] != '':
        continue
    if c['MFLAG'] == 'P':
        contiune
    print '%s,%s,%s,%s,' % (c['DATE'],c['ID'],c['TYPE'],c['VALUE'])