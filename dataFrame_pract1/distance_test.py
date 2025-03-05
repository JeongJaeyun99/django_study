import seaborn as sns
import numpy as np

iris = sns.load_dataset('iris')
setosa = iris[iris['species'] == 'setosa']
setosa["species"] = 0
setosa_data = setosa[["sepal_length","sepal_width","petal_length","petal_width"]]
setosa_sample2 = setosa_data.sample(n=2, random_state=42)
setosa_remaining = setosa_data.drop(setosa_sample2.index)
setosa_mean = setosa_data.mean(axis=0) # setosa의 중심값

versicolor = iris[iris['species'] == 'versicolor']
versicolor["species"] = 1
versicolor_data = versicolor[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
versicolor_sample2 = versicolor_data.sample(n=2, random_state=42)
versicolor_remaining = versicolor_data.drop(versicolor_sample2.index)
versicolor_mean = versicolor_data.mean(axis=0)  #  versicolor의 중심값

virginica = iris[iris['species'] == 'virginica']
virginica["species"] = 2
virginica_data = virginica[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
virginica_sample2 = virginica_data.sample(n=2, random_state=42)
virginica_remaining = virginica_data.drop(virginica_sample2.index)
virginica_mean = virginica_data.mean(axis=0)  # virginica의 중심값

# print("setosa_mean : ",setosa_mean.values)
# print("versicolor_mean : ", versicolor_mean.values)
# print("virginica_mean : ", virginica_mean.values)
# ex > (50,4) 현재 이것인데 트랜스퍼 시켜서 (4,50)으로 만들고 (트랜스퍼)(4,50) @ 공분산의 역행렬(50,50) @ (50,4) == (4,4)

setosa_cov = ((setosa_remaining - setosa_mean).T @ (setosa_remaining - setosa_mean)).values # 공분산 = (setosa-평균).T 트랜스퍼 @ (setosa-평균) = (4,4)
setosa_cov_inv = np.linalg.inv(setosa_cov)
versicolor_cov = ((versicolor_remaining - versicolor_mean).T @ (versicolor_remaining - versicolor_mean)).values
versicolor_cov_inv = np.linalg.inv(versicolor_cov)
virginica_cov = ((virginica_remaining - virginica_mean).T @ (virginica_remaining - virginica_mean)).values
virginica_cov_inv = np.linalg.inv(virginica_cov)

# print(setosa_cov)

d0 = (virginica_sample2.values[1]-setosa_mean.values).T @ setosa_cov_inv @ (virginica_sample2.values[1]-setosa_mean.values)
# print(d0)
d1 = (virginica_sample2.values[1] - versicolor_mean.values).T @ versicolor_cov_inv @ (
                virginica_sample2.values[1] - versicolor_mean.values)
# print(d1)
d2 = (virginica_sample2.values[1] - virginica_mean.values).T @ virginica_cov_inv @ (
            virginica_sample2.values[1] - virginica_mean.values)
# print(d2)

if __name__ == "__main__":
    iris = sns.load_dataset('iris')
    # print(iris)
    # print(iris.keys())
    # print(iris['species'].unique())
    setosa = iris[iris['species'] == 'setosa']
    setosa["species"] = 0
    setosa_data = setosa[["sepal_length","sepal_width","petal_length","petal_width"]]
    setosa_sample2 = setosa_data.sample(n=2, random_state=42)
    setosa_remaining = setosa_data.drop(setosa_sample2.index)
    setosa_mean = setosa_data.mean(axis=0) # setosa의 중심값

    versicolor = iris[iris['species'] == 'versicolor']
    versicolor["species"] = 1
    versicolor_data = versicolor[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    versicolor_sample2 = versicolor_data.sample(n=2, random_state=42)
    versicolor_remaining = versicolor_data.drop(versicolor_sample2.index)
    versicolor_mean = versicolor_data.mean(axis=0)  #  versicolor의 중심값

    virginica = iris[iris['species'] == 'virginica']
    virginica["species"] = 2
    virginica_data = virginica[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    virginica_sample2 = virginica_data.sample(n=2, random_state=42)
    virginica_remaining = virginica_data.drop(virginica_sample2.index)
    virginica_mean = virginica_data.mean(axis=0)  # virginica의 중심값

    # print("setosa_mean : ",setosa_mean.values)
    # print("versicolor_mean : ", versicolor_mean.values)
    # print("virginica_mean : ", virginica_mean.values)
    # ex > (50,4) 현재 이것인데 트랜스퍼 시켜서 (4,50)으로 만들고 (트랜스퍼)(4,50) @ 공분산의 역행렬(50,50) @ (50,4) == (4,4)

    setosa_cov = ((setosa_remaining - setosa_mean).T @ (setosa_remaining - setosa_mean)).values # 공분산 = (setosa-평균).T 트랜스퍼 @ (setosa-평균) = (4,4)
    setosa_cov_inv = np.linalg.inv(setosa_cov)
    versicolor_cov = ((versicolor_remaining - versicolor_mean).T @ (versicolor_remaining - versicolor_mean)).values
    versicolor_cov_inv = np.linalg.inv(versicolor_cov)
    virginica_cov = ((virginica_remaining - virginica_mean).T @ (virginica_remaining - virginica_mean)).values
    virginica_cov_inv = np.linalg.inv(virginica_cov)

    # print(setosa_cov)

    d0 = (virginica_sample2.values[1]-setosa_mean.values).T @ setosa_cov_inv @ (virginica_sample2.values[1]-setosa_mean.values)
    print(d0)
    d1 = (virginica_sample2.values[1] - versicolor_mean.values).T @ versicolor_cov_inv @ (
                virginica_sample2.values[1] - versicolor_mean.values)
    print(d1)
    d2 = (virginica_sample2.values[1] - virginica_mean.values).T @ virginica_cov_inv @ (
            virginica_sample2.values[1] - virginica_mean.values)
    print(d2)
    # print(setosa)