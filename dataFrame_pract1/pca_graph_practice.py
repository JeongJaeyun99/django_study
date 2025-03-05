import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

# 1️⃣ 아이리스 데이터 로드
iris = load_iris()
X = iris.data  # 특성 데이터
y = iris.target  # 품종 레이블
target_names = iris.target_names  # 품종 이름

# 2️⃣ PCA 적용 (2차원으로 축소)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# 3️⃣ 시각화 (산점도)
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b']  # 품종별 색상

for i, target_name in enumerate(target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1],
                label=target_name, alpha=0.7, edgecolors='k', color=colors[i])

plt.xlabel("PCA Component 1")
plt.ylabel("PCA Component 2")
plt.title("Iris Dataset PCA Scatter Plot")
plt.legend()
plt.grid(True)
plt.show()