'''
Task 
Read an integer N. For all non-negative integers i<N, print i^2. See the sample for details.

Input Format 
The first and only line contains N.

Constraints 
1≤N≤20

Output Format 
Print N lines, one corresponding to each i.
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(raw_input())
for i in range(0,n):
    print i*i
