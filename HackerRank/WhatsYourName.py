'''
Problem Statement

Let's learn the basics of Python! You are given the first name and the last name of a person. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
It's that simple!

In Python you can read a line as a string using

s = raw_input()
#here s reads the whole line.  
Input Format The first line contains the first name, and the second line contains the last name.

Constraints 
The length of the first and last name ≤ 10.

Output Format Print the output as mentioned above.
'''# Enter your code here. Read input from STDIN. Print output to STDOUT

s1 = raw_input()
s2 = raw_input()

print "Hello " + s1 + " " + s2 + "! You just delved into python."
