#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__=='__main__':
	a=[1,4,6,9,13,16,19,28,40,100,0]
	print('the original list:')
	for i in range(len(a)):
		print(a[i]),
	number=int(input('\nplease input a nubmer:\n'))
	end=a[9]
	if number>end:
		a[10]=number
	else:
		for i in range(10):
			if a[i]>number:
				temp1=a[i]
				a[i]=number
				for j in range (i+1,11):
					temp2=a[j]
					a[j]=temp1
					temp1=temp2
				break #why
	print ('the list after sorting.')
	for i in  range(11):
		print(a[i]),