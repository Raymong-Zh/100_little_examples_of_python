#!/usr/bin/python
#-*- coding:UTF-8 -*-

def output(s,l):
	if l==0:
		return
	print(s[l-1])
	output(s,l-1)

s=input('input a string:')
l=len(s)
output(s,l)
