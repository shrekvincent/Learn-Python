'''
print("Hello World!")
import dexplot as dxp
import pandas as pd
airbnb = dxp.load_dataset('airbnb')
airbnb.head()
airbnb.shape
(4581, 12)
dxp.bar(x = 'neighborhood', y = 'price', data = airbnb, aggfunc = 'median')
dxp.line(x = 'neighborhood', y = 'price', data = airbnb, aggfunc = 'median')
'''

'''
a = 21
b = 10
c = 0
if ( a == b ):
    print ("1 - a 等于 b")
else:
    print ("1 - a 不等于 b")
if ( a != b ):
    print ("2 - a 不等于 b")
else:
    print("2 - a 等于 b")
'''

