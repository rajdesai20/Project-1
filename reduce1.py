#!/usr/bin/env python
import sys
import operator

countmax = 0
countmin = 0
avgmax = 0
avgmin = 0
hot = []
cold = []
max = (-9999,'','')
min = (9999,'','')
currentyear = None
for l in sys.stdin:
    l = l.strip().split(',')

    date = l[0]
    year = date[:4]
    id = l[1]
    met = l[2]
    val = l[3]

    try:
        val = int(val)
    except ValueError:
        continue
    
    if currentyear is None:
        currentyear = year
    
    if currentyear != year:
        print 'Year: %s' % currentyear
        print 'Average TMAX: %s' % (avgmax * 0.1 / countmax)
        print 'Average TMIN: %s' % (avgmin * 0.1 / countmin)

        print 'Hottest Day: day: %s  val: %s  loc: %s' %(hot[0][2], hot[0][0], hot[0][1])
        print 'Coldest Day: day: %s  val: %s  loc: %s' %(cold[0][2], cold[0][0], cold[0][1])

        print 'Hottest Stations %s' % ([y[1] for y in hot])
        print 'Hottest Station Temperatures %s' % ([y[0] for y in hot])
        print 'Coldest Stations %s' % ([y[1] for y in cold])
        print 'Coldest Station Temperatures %s' % ([y[0] for y in cold])
        currentyear = year
        countmax = 0
        countmin = 0
        avgmax = 0
        avgmin = 0
        hot = []
        cold = []
    if met == 'TMAX':
        avgmax += val
        countmax += 1
        if max[0] < val:
            max = (val,id,date)

        hot.append((val,id,date))

        if len(hot) > 5:
            hot = sorted(hot, key=operator.itemgetter(0), reverse=True)
            hot.pop(len(hot) - 1)
    
    elif met == 'TMIN':
        avgmin += val
        countmin += 1
        if min[0] > val:
            min = (val,id,date)

        cold.append((val,id,date))

        if len(cold) > 5:
            cold = sorted(cold, key=operator.itemgetter(0))
            cold.pop(len(cold) - 1)


print 'Year: %s' % currentyear
print 'Average TMAX: %s' % (avgmax * 0.1 / countmax)
print 'Average TMIN: %s' % (avgmin * 0.1 / countmin)

print 'Hottest Day: day: %s  val: %s  loc: %s' %(hot[0][2], hot[0][0], hot[0][1])
print 'Coldest Day: day: %s  val: %s  loc: %s' %(cold[0][2], cold[0][0], cold[0][1])

print 'Hottest Stations %s' % ([y[1] for y in hot])
print 'Hottest Station Temperatures %s' % ([y[0] for y in hot])
print 'Coldest Stations %s' % ([y[1] for y in cold])
print 'Coldest Station Temperatures %s' % ([y[0] for y in cold])


print 'Max TMAX: %s | Station: %s' % (max[0],max[1])
print 'Min TMIN: %s | Station: %s' % (min[0],min[1])