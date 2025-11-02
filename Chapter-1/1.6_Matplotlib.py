import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin & cos")
plt.legend()

# plt.show()
# 仮想環境上のせいか、WSLのせいなのか、GUIに制限が掛かってて表示できない。
# 代わりに画像を保存することで対応。
plt.savefig("result-2.png")
