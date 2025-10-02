from tyger.discipline.sectypes.types import L,unk
x: L = True
x_p: unk = x
y: L = True
y_pp: unk = y
z: L = True
z_p: unk = z
if x_p:
    y_p: L = False
if y_p:
    z_p = False
print(z_p)