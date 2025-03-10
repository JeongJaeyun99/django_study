import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sqlalchemy.dialects.mssql.information_schema import columns
from db.postgres_connect import create_table_customer, insert_into_table
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from tqdm import tqdm
tqdm.pandas()


def svd_model_martix(rating_df):
    origin_matrix = rating_df.pivot_table(index="user_id", columns='movie_id', values='rating', fill_value=0)
    matrix = origin_matrix.progress_apply(
        lambda col: col.replace(0, col[col != 0].mean()))  # 진행 바 표시  # 평균값이 들어간것이 안본 영화들

    sparse_matrix = csr_matrix(matrix)
    k = 3
    print("Computing SVD...")
    P, S, Qt = scipy.sparse.linalg.svds(sparse_matrix, k=k)
    S = np.diag(S)
    #svd_model = P @ S @ Qt

    # 축소된 사용자 표현
    reduced_matrix = P.dot(S)

    # k-최근접 이웃 모델 적용
    k_neighbors = 4  # 각 사용자별로 가장 유사한 4명만 저장
    nn_model = NearestNeighbors(metric='cosine', algorithm='brute', n_jobs=-1)
    nn_model.fit(reduced_matrix)

    # 각 사용자별 k개의 가장 가까운 이웃 찾기
    distances, indices = nn_model.kneighbors(reduced_matrix, n_neighbors=k_neighbors)

    user_ids = np.array(rating_df['user_id'].unique())
    neighbor_ids = user_ids[indices]  # `indices`를 실제 user_id로 매핑

    # 자기 자신을 제외한 유사 사용자만 남기기
    similarity_df = pd.DataFrame(neighbor_ids[:, 1:], index=user_ids,
                                 columns=[f"neighbor_{i}" for i in range(1, k_neighbors)])

    print("k-NN 기반 유사 사용자 탐색 완료!")
    return similarity_df,reduced_matrix


def plot_user_embeddings(reduced_matrix, user_ids):
    """ 사용자 임베딩을 t-SNE를 이용해 2D로 시각화 """
    tsne = TSNE(n_components=2, random_state=42)
    embeddings_2d = tsne.fit_transform(reduced_matrix)

    plt.figure(figsize=(8, 6))
    plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], alpha=0.6)

    for i, user_id in enumerate(user_ids[:30]):  # 일부만 표시
        plt.annotate(user_id, (embeddings_2d[i, 0], embeddings_2d[i, 1]), fontsize=8)

    plt.title("User Embeddings (t-SNE)")
    plt.xlabel("Dimension 1")
    plt.ylabel("Dimension 2")
    plt.show()
    # 숫자들끼리 붙어있을수록 비슷하다는 이야기!!

# 나와 유사한 유저의 영화를 추천
if __name__ == "__main__":
    # create_table_customer("similar_user")  # 첫 테이블 생성만

    names = ['movie_id', 'title', 'genre']
    movie_df = pd.read_csv("../data/movies.dat",
                           names=names,
                           sep="::",
                           engine='python'
                           )

    ratings_df = pd.read_pickle("../data/ratings.pkl")
    filtered_df = ratings_df[ratings_df.groupby("movie_id")["movie_id"].transform("count") >= 20000]
    filtered_df.reset_index(drop=True, inplace=True)

    similarity_df,reduced_matrix = svd_model_martix(filtered_df)

    user_id = 1 # user_id와 유사한 영화들을 뽑아야 하므로 타켓을 user_id에서 정해야함
    similar_users = similarity_df.loc[user_id]

    # 유사한 사용자를 similar_users에 저장했으니 유사한 사용자의 영화 상위 4개를 뽑아서 갖고온다.
    similar_movies = ratings_df[ratings_df['user_id'].isin(similar_users)]
    similar_movies = similar_movies.groupby('user_id').head(4) # 비슷한 사용자의 영화를 상위 4개만 뽑아옴

    # 유사한 사용자의 movie_id를 similar_movies에 저장했으니 이를 이용하여 영화 제목을 뽑아냄.
    similar_movies_with_titles = similar_movies.merge(movie_df[['movie_id', 'title']], on='movie_id', how='left')
    movie_titles = similar_movies_with_titles['title'] # >> title만 뽑아서 보여줌
    print(f"User {user_id}와 유사한 사용자들이 본 영화 제목들:\n{movie_titles}")

    # 유저의 그룹화를 시각화 하였음
    plot_user_embeddings(reduced_matrix, similarity_df.index)

    # new_rating = (
    #     svd_df.stack().reset_index().rename(columns={0: "rating"})
    # )
