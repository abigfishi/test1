import math

N = 10000
with open("sin_table_1000.inc", "w") as f:
    for i in range(N):
        val = math.sin(2 * math.pi * i / N)
        f.write(f"{val:.6f}f")
        if i != N - 1:
            f.write(", ")
        if (i + 1) % 10 == 0:  # 每行10个方便阅读
            f.write("\n")
