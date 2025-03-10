import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
import pandas as pd
from sqlalchemy.dialects.mssql.information_schema import columns
from db.postgres_connect import create_table_customer, insert_into_table
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from tqdm import tqdm
tqdm.pandas()

def svd_model_martix(rating_df):
    origin_matrix = rating_df.pivot_table(index="user_id", columns='movie_id', values='rating', fill_value=0)
    #json = extract_rating_zero(origin_matrix)
    matrix = origin_matrix.progress_apply(lambda col: col.replace(0, col[col != 0].mean()))  # 진행 바 표시  # 평균값이 들어간것이 안본 영화들

    sparse_matrix = csr_matrix(matrix)
    k = 3  # 순위대로 나옴 # 고윳값 : 필드의 선호도
    print("Computing SVD...")
    P, S, Qt = scipy.sparse.linalg.svds(sparse_matrix, k=k)
    S = np.diag(S)
    # print(P.shape)
    # print(P@S@Qt) # >>> 이게 모델(svd)
    svd_model = P @ S @ Qt
    # 1번의 예측값
    new_df = pd.DataFrame(svd_model, index=matrix.index, columns=matrix.columns)
    print("SVD Completed!")
    # print(new_df)
    return new_df

def saw_and_not_saw(ratings_df,new_rating):
    saw_movies = ratings_df[ratings_df["rating"] > 0].groupby("user_id")["movie_id"].progress_apply(set)
    # print(saw_movies)

    unseen_movies = new_rating[
        ~new_rating.apply(lambda row: row["movie_id"] in saw_movies.get(row["user_id"], set()), axis=1)].progress_apply(
        lambda x: x)

    # pd.set_option('display.max_rows', None)  # 행 수 제한 없애기
    # pd.set_option('display.max_columns', None)  # 열 수 제한 없애기
    # pd.set_option('display.width', None)  # 자동 줄바꿈 없이 출력
    # pd.set_option('display.max_colwidth', None)  # 열 너비 제한 없애기

    return unseen_movies

if __name__ == "__main__":
    #create_table_customer("rating_result")  # 첫 테이블 생성만
    ratings_df = pd.read_pickle("../data/ratings.pkl")
    #ratings_df1 = ratings_df[:100]
    filtered_df = ratings_df[ratings_df.groupby("movie_id")["movie_id"].transform("count") >= 20000]  #
    filtered_df.reset_index(drop=True, inplace=True)

    new_df = svd_model_martix(filtered_df)

    new_rating = (
        new_df.stack().reset_index().rename(columns={0:"rating"})
    )
    #print(new_rating)

    unseen_movies = saw_and_not_saw(filtered_df,new_rating) # 본 영화를 먼저 추출 후 안 본 영화 추출
    print(unseen_movies)

    #insert_into_table(unseen_movies,"rating_result")



