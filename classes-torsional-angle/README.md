
https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem

You are given four points A, B, C and D in a 3-dimensional Cartesian coordinate system. You are required to print the angle between the plane made by the points ABC and BCD in degrees(not radians). Let the angle be PHI

Cos(PHI) = (X.Y) / abs(X) abx(Y)

where

X = ABxBC
Y = BCxCD

Here, X.Y means the dot product of and X, Y and x means the cross product of vectors AB and BC . Also, AB = B - A

.

Input Format

(X, Y, Z)

One line of input containing the space separated floating number values of the
and

coordinates of a point.

Output Format

Output the angle correct up to two decimal places.

Sample Input

0 4 5
1 7 6
0 5 9
1 7 2

Sample Output

8.19



{has_any(s, "isalnum")}
{has_any(s, "isalpha")}
{has_any(s, "isdigit")}
{has_any(s, "islower")}
{has_any(s, "isupper")}