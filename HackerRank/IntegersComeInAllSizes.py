
'''
Task 
Read four numbers, a, b, c, and d, and print the result of ab+cd.

Input Format 
Four numbers are given on four lines.

Constraints 
1≤a≤1000 
1≤b≤1000 
1≤c≤1000 
1≤d≤1000

Output Format 
Print the result in one line.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
d = int(raw_input())

print pow(a,b) + pow(c,d)
