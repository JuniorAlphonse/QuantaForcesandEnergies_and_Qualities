#This code's purpose is to enumerate gravity at the quantum level or as G(s) (Gravity of The ArcLength Sum).
import math
import cmath

s = 3;
m = s
r = s
c = (3.00 * (10 ** 8))
e = -1
def arclength_gravitation(s):
    G = .25 * (1 / (c ** 2)) * (e ** -10) * (-10 * (e ** 11) * (m ** 2))/(e ** ((.5 * (e ** 10)) + (.5 * (r ** 5))));

print(arclength_gravitation(s));

# Note that the result is that gravity of the quantum imaginary or the gravity of imaginary masses and radii is so small that the software yields none. To follow and get an numerical value, then consult wolframalpha.com.
