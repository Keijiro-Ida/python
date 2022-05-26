import math

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

BAx, BAy = ax-bx, ay-by
BCx, BCy = cx-bx, cy-by
CAx, CAy = ax-cx, ay-cy
CBx, CBy = bx-cx, by-cy

pattern = 2
if BAx * BCx + BAy * BCy < 0:
    pattern = 1
if CAx * CBx + CAy * CBy < 0:
    pattern = 3

if pattern == 1:
    answer = math.sqrt(BAx**2 + BAy**2)
if pattern == 3:
    answer = math.sqrt(CAx**2 + CAy**2)
if pattern == 2:
    S = abs(BAx*CAy - BAy*CAx)
    BClength = math.sqrt(BCx**BCy**2)
    answer = S / BClength

print("%.12f" % answer )
