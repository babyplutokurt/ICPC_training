from fractions import Fraction
a = input()
s = 0
for i in range(len(a)):
    s += int(a[-i - 1]) * ((3 / 2) ** i)

if s // 1 == s:
    print(int(s))
else:
    dec = s // 1
    fra = s - dec
    fra = Fraction(fra).limit_denominator()
    print(str(int(dec)), ' ', str(fra))
