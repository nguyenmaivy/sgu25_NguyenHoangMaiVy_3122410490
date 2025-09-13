import numpy as np
print("Tính chu vi và diện tích hình tròn")
r = float(input("Nhập bán kính r: "))
cv = 2 * np.pi * r
dt = np.pi * r ** 2
print(f"cv = 2\u03C0*{r} = {cv:.2f}, dt = \u03C0*{r}^2 = {dt:.2f}")
