import seaborn as sns
import numpy as np
from distance_test import setosa_sample2,virginica_sample2,versicolor_sample2


if __name__ == "__main__":
    # pca 기법
    iris = sns.load_dataset('iris')
    iris_data = iris[["sepal_length","sepal_width","petal_length","petal_width"]]
    iris_mean = iris_data.mean(axis=0)
    # print(iris_mean)
    iris_conv = ((iris_data - iris_mean).T @ (iris_data - iris_mean)).values
    # iris_conv = ((iris_data - iris_mean).T @ (iris_data - iris_mean))
    # print(iris_conv)
    eigenvalues, eigenvectors = np.linalg.eig(iris_conv)

    # print("고유값 (Eigenvalues):\n", eigenvalues) # 가장 큰게 주성분을 이루고 있다는것을 알수있다.
    # print("\n고유벡터 (Eigenvectors):\n", eigenvectors)
    print(setosa_sample2 @ eigenvectors[0],"\n")
    print(versicolor_sample2 @ eigenvectors[0],"\n")
    print(virginica_sample2 @ eigenvectors[0])

    

