import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

x=np.array( [1,2.1,3,4,5,6,7,8,9,1.20,1.1,1.22,13.2,14.5,30,-10] )
print(x)
indexx = np.arange(1,17,1)
print(indexx)

x = np.sort(x)
print(x)

dataSize  = np.shape(x)
print(dataSize)

# plt.boxplot(x)
# plt.show()

upperTile = (x.shape[0]+ 1)/4*3
upperTileData=0
# print(upperTile)
if(  abs(upperTile-math.floor(upperTile))  <0.001 ):
    upperTileData = x[math.ceil(upperTile)]
    print('upperTileData ',upperTileData)
else:
    upperTileData = np.interp(upperTile, indexx, x) 
    print('upperTileData ',upperTileData)

middleTile = (x.shape[0] + 1)/4*2
middleTileData=0
# print(middleTile)
if(  abs(middleTile-math.floor(middleTile))  <0.001 ):
    middleTileData = x[math.ceil(middleTile)]
    print('middleTileData ',middleTileData )
else:
    middleTileData =  np.interp(middleTile, indexx, x)
    print('middleTileData ',middleTileData )



lowerTile = (x.shape[0] + 1)/4*1
lowerTileData = 0
# print(lowerTile)
if(  abs(lowerTile-math.floor(lowerTile))  <0.001 ):
    lowerTileData = x[math.ceil(lowerTile)]
    print('lowerTileData is ', lowerTileData)
else:
    lowerTileData =  np.interp(lowerTile, indexx, x)
    print('lowerTileData is ', lowerTileData)

# IQR, inter-Quartile range
IQR = -lowerTileData + upperTileData
print('IQR is ',IQR)


minn = lowerTileData - IQR*1.5 
print('min is ',minn)
maxx = upperTileData + IQR*1.5
print('max is ',maxx)

sns.boxplot(y = x)
plt.title('sns boxplot')
plt.savefig('snsBoxplot.jpg')
plt.show()

plt.boxplot(x)
plt.title('pltBoxplt')
plt.savefig('pltBoxplt.jpg')
plt.show()

# 结论，sns boxplot 或者matplotlib plt  boxplot对于四分位数计算是基本正确的，但是对于min、max计算是不正确的