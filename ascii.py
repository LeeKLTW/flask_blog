# encoding: utf-8
"""
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl'
then your program should print
Longest substring in alphabetical order is: beggh
"""
import string
string.ascii_lowercase(1)
s = 'azcbobobegghakl'
s[1:]


def solution(s):
    ans = [s[0]]
    for char in s[1:]:
        if ord(ans[-1][-1])<=ord(char):
            ans[-1]+=char
        else:
            ans.append(char)
    return max(ans,key=len)

solution(s)