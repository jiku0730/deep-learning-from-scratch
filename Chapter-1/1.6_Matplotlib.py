import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 6, 0.1)
y = np.sin(x)

plt.plot(x, y)
# plt.show()
# 仮想環境上のせいか、WSLのせいなのか、GUIに制限が掛かってて表示できない。
# 代わりに画像を保存することで対応。
plt.savefig("result.png")
