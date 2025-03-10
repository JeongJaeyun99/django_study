import pandas as pd
import numpy as np
import scipy.sparse.linalg
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import svds




if __name__ == "__main__":
    names = ['movie_id', 'title', 'genres']
    movies_df = pd.read_csv("../data/movies.dat",
                            names=names,
                            sep="::",
                            engine='python'
                            )
    # ratings_df = pd.read_csv("../data/ratings.csv")
    # names = ['user_id','movie_id','rating','date']
    # ratings_df = pd.read_csv("../data/ratings.dat",
    #                         names=names,
    #                         sep="::",
    #                         engine='python'
    #                         )
    ratings_df = pd.read_pickle("../data/ratings.pkl")
    # print(ratings_df['user_id'].nunique())
    # print(ratings_df['movie_id'].value_counts()) # value_counts는 값을 movie_id의 유니크한 값을 카운트 하는데 많은 순서대로!
    filtered_df= ratings_df[ratings_df.groupby("movie_id")["movie_id"].transform("count") >= 20000] #
    filtered_df.reset_index(drop=True,inplace=True)

    origin_matrix = pd.pivot_table(filtered_df,index="user_id",columns='movie_id',values='rating',fill_value=0)
    matrix = origin_matrix.apply(lambda col : col.replace(0,col[col!=0].mean())) # 평균값이 들어간것이 안본 영화들

    sparse_matrix = csr_matrix(matrix)
    k = 10 # 순위대로 나옴
    P, S, Qt = scipy.sparse.linalg.svds(sparse_matrix,k=k)
    S = np.diag(S)
    # print(P.shape)
    #print(P@S@Qt) # >>> 이게 모델(svd)
    svd_model = P@S@Qt
    new_df = pd.DataFrame(svd_model,index=matrix.index,columns=matrix.columns)
    movie_id_to_title = dict(zip(movies_df['movie_id'], movies_df['title']))
    new_df.columns = new_df.columns.map(movie_id_to_title)
    print(origin_matrix)
    # user1이 안본것중에서 4.5이상인 영화의 장르와 user1이 본 영화의 장르가 비슷하다! 비슷한지 보자

    user_id = 4

    # user_id가 안 본 영화들 중 추천 점수가 4.5 이상인 영화
    user_1_data = origin_matrix.loc[user_id]

    # user_1이 본 영화들의 movie_id
    user_1_watched_movie_ids = user_1_data[user_1_data != 0].index

    # movie_df에서 해당 movie_id에 대한 장르 정보 가져오기
    user_1_watched_movies_genres = movies_df[movies_df['movie_id'].isin(user_1_watched_movie_ids)]['genres']

    # 결과 출력
    print(f"User {user_id}이(가) 본 영화들의 장르:")
    print(user_1_watched_movies_genres)

    # user_1이 안 본 영화들의 movie_id (0으로 표시된 영화들)
    user_1_zeros = user_1_data[user_1_data == 0]

    # user_1_zeros의 movie_id를 제목으로 변환
    user_1_zeros_titles = user_1_zeros.index.map(movie_id_to_title)

    # user_1_zeros_titles로 추천 점수 추출 (new_df에서 user_1에 대한 열만 조회)
    user_1_zeros_recommendations = new_df.loc[user_id, user_1_zeros_titles]

    # 추천 점수가 4.5 이상인 영화들만 필터링
    recommended_movies = user_1_zeros_recommendations[user_1_zeros_recommendations >= 4.5]

    # 추천된 영화들 중 이미 본 영화는 제외
    recommended_movies = recommended_movies[~recommended_movies.index.isin(user_1_watched_movie_ids)]

    # 여러 개의 영화 추천하기 (상위 5개 추천)
    top_n = 5  # 추천할 영화 개수
    top_recommended_movies = recommended_movies.nlargest(top_n)

    # 추천된 영화들의 movie_id 추출
    recommended_movie_ids = top_recommended_movies.index.map(
        lambda title: movies_df[movies_df['title'] == title]['movie_id'].values[0])

    # 해당 영화들의 장르 정보 가져오기
    recommended_movie_genres = movies_df[movies_df['movie_id'].isin(recommended_movie_ids)]['genres']

    print(f"User {user_id}에게 추천된 상위 {top_n}개 영화의 장르:\n{recommended_movie_genres}")

    # ratings_df.iloc[:1000,:].to_csv("../data/ratings.csv")
    # exit()   # > > csv에 데이터 1000개만 잘라서 save
    # ratings_df.drop("Unnamed: 0", inplace=True, axis=1)
    movies_df['genres'] = movies_df['genres'].str.replace("|",",")

    merge_df = ratings_df.merge(movies_df[['movie_id', 'genres']], on='movie_id', how='left')

    pivot_df  = merge_df.pivot_table(index='user_id',columns='movie_id',values='rating',fill_value=0)
    #피벗팅을 해서 무비를 봣는지 봤는지
    #rating값의 평균값을 줘라
    print(merge_df)
    print(pivot_df)
    #print(ratings_df)
    #print()
    # movie_id