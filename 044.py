#!/usr/bin/python
# -*- coding:UTF-8 -*-

X=[[12,7,3],
   [4,5,6],
   [7,9,9]]

Y=[[5,8,1],
   [6,7,3],
   [4,5,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]


#line
for i in range(len(X)):
	#column
	for j in range(len(X[0])):
		result[i][j]=X[i][j]+Y[i][j]

for r in result:
	print(r)