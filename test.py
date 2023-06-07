import numpy as np
import math

#点と直線の距離
# pos = [1, 6]
# a = 3 / 4
# b = -1
# c = -1

# result = math.fabs(a*pos[0]+b*pos[1]+c) / math.sqrt(a**2 + b**2)
# print(result)

#円の公式
# x = [1, 3, 6]
# y = [5, 1, 4]

# a = math.sqrt((x[0]-x[1])**2 + (y[0]-y[1])**2)
# b = math.sqrt((x[2]-x[1])**2 + (y[2]-y[1])**2)
# c = math.sqrt((x[2]-x[0])**2 + (y[2]-y[0])**2)

# s = (a + b + c) / 2
# area = math.sqrt(s * (s-a)*(s-b)*(s-c))
# print(area)

#ベクトルの方向
# rad = math.atan2(math.sqrt(3), 1)
# deg = math.degrees(rad)
# print(deg)

###
# ２直線のなす角度（内積を使う）
# a = np.array([2,7])
# b = np.array([6, 1])
# c = np.array([2, 3])
# d = np.array([6, 5])

# # ベクトルの成分を作る
# va = b - a
# vb = d - c

# #ベクトルの大きさ
# norm_a = np.linalg.norm(va)
# norm_b = np.linalg.norm(vb)

# #ベクトルの内積
# dot_ab = np.dot(va, vb)
# print("内積: " + str(dot_ab))

# cos_th = dot_ab / (norm_a * norm_b)
# # print(cos_th)
# rad = math.acos(cos_th)
# degree = math.degrees(rad)
# print(degree)

# ベクトルの外積
# a = np.array([0, 1, 2])
# b = np.array([2, 0, 0])
# result = np.cross(a, b)
# print(result)

# ベクトルの外積を使って面積を求める
# a = np.array([2, 4])
# b = np.array([3, 1])
# cross_ab = np.cross(a, b)
# area = np.linalg.norm(cross_ab)
# print(area / 2)

# a = np.array([2, 4])
# a_size = np.linalg.norm(a)
# print(a_size)

# 行列の計算
# A = np.matrix([[50, 40], [10, 10]])
# B = np.matrix([[30, 100], [20, 15]])
# print(B + A)

# A = np.matrix([[1,3], [2, 1]])
# B = np.matrix([[145], [72]])
# 単位行列
# C = np.matrix([[1, 0], [0, 1]])
# print(C * A)

# 逆行列
# A = np.matrix([[5, 3], [2, 1]])
# B = np.linalg.inv(A)
# print(B)
# C = np.linalg.inv(B)
# print(A * B)

# 逆行列で連立方程式を解く
# 5x + 3y = 9
# 2x + y = 4
A = np.matrix([[5, 3], [2, 1]])
R = np.matrix([[9],[4]])
inv_a = np.linalg.inv(A)
result = inv_a * R
print(result)