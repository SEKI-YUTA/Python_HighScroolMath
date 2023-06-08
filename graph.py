import numpy as np
import matplotlib.pyplot as plt
import math

# th = np.arange(0, 360)

# x = 2 *  np.cos(np.radians(th))
# y = 2 * np.sin(np.radians(th))

# r = 300
# x = np.arange(-300, 300 + 1)
# y = np.sqrt(r**2 - x**2)
# y2 = -y

# plt.plot(x, y)
# plt.plot(x, y2)
# plt.axis("equal")
# plt.grid(color="0.8")
# plt.savefig("out.png")

#
# x軸に線対象になるように移動
# p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1]])
# # 変換行列
# A = np.matrix([[-1,0], [0, -1]])
# p2 = A * p
# print(p2)
# p = np.array(p)
# p2 = np.array(p2)
# print("p: " + str(p))
# print("xxx: " + str(p[0]))
# plt.plot(p[0, :], p[1, :])
# plt.plot(p2[0, :], p2[1, :])
# plt.axis("equal")
# plt.grid(color='0.8')
# plt.show()
# plt.savefig("out.png")

#
# 三角形を拡大する
# p = np.matrix([[1, 1, 2, 1], [3, 1, 1, 3]])
# # 変換行列
# A = np.matrix([[3, 0], [0, 3]])

# p2 = A * p
# p = np.array(p)
# p2 = np.array(p2)
# plt.plot(p[0], p[1])
# plt.plot(p2[0], p2[1])
# plt.axis("equal")
# plt.grid(color="0.8")
# plt.show()
# plt.savefig("out.png")

# #
# # 四角形を反時計回りに回転
# # [[cos0, -sin0], [sin0, cos0]]
# p = np.matrix([[3, 3, 5, 5, 3], [3, 1, 1, 3, 3]])

# th = math.radians(45)
# # th = np.radians(30)
# A = np.matrix([[np.cos(th), np.sin(-th)], [np.sin(th), np.cos(th)]])

# p2 = A * p

# p = np.array(p)
# p2 = np.array(p2)
# plt.plot(p[0], p[1])
# plt.plot(p2[0], p2[1])
# plt.axis("equal")
# plt.grid(color="0.8")
# plt.show()

#
# # 図形の平行移動(同次座標を使う)
# p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1], [1, 1, 1, 1]])
# # 変換座標
# A = np.matrix([[1,0,2], [0, 1, 3], [0, 0, 1]])
# p2 = A * p
# p = np.array(p)
# p2 = np.array(p2)
# plt.plot(p[0], p[1])
# plt.plot(p2[0], p2[1])
# plt.axis("equal")
# plt.grid(color="0.8")
# plt.show()

#
# 図形を平行移動してから回転させる
p = np.matrix([[1, 3, 3, 1], [1, 1, 2, 1], [1, 1, 1, 1]])

A = np.matrix([[1, 0, 2], [0, 1, 3], [0, 0, 1]])
th = np.radians(90)
B = np.matrix([[np.cos(th), np.sin(-th), 0], [np.sin(th), np.cos(th), 0], [0, 0, 1]])

# p2 = A * B * p
X = B * A
p2 = X * p
p = np.array(p)
p2 = np.array(p2)

plt.plot(p[0], p[1])
plt.plot(p2[0], p2[1])
plt.axis("equal")
plt.grid(color="0.8")
plt.show()
