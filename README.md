# ACSL2019-2020Problem
Code for a ACSL competition problem
Here is the problem:

Given a positive integer (call it N) and a position in that integer (call it P)
transform N. To transform N, find the Pth digit of N from the right. Replace each of the digits to
the left of the Pth digit with the sum of that digit and the Pth digit. If the sum is greater than 9, use
just the units digits (see the second example below). Replace each of the digits to the right of the
Pth digit by the absolute value of the difference between it and the Pth digit. Do not change the Pth digit.

Example input:

N = 4318672
P =  4

Output: 2198216


