def reverse(x: int) -> int:
    sx = str(x)
    minus = False
    if sx[0] == "-":
        sx = sx[1:]
        minus = True
    rsx = sx[::-1]
    if minus:
        rsx = "-" + rsx
    irsx = int(rsx)
    if irsx > 2 ** 31 - 1 or irsx < -2 ** 31:
        irsx = 0
    return irsx

reverse()