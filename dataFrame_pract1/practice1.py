

import pandas as pd
from map_practice import multiple








if __name__ == "__main__": # 현재 내가 쓰고 있는 스크립트 이름과 실행 파일 이름이 같아야지 실행된다!(여기는 테스트 하는곳)
    users =[
        {"user_id": 1, "name": "Alice", "email": "alice@example.com", "age": 28},
        {"user_id": 2, "name": "Bob", "email": "bob@example.com", "age": 34},
        {"user_id": 3, "name": "Charlie", "email": "charlie@example.com", "age": 25},
        {"user_id": 4, "name": "David", "email": "david@example.com", "age": 30},
        {"user_id": 5, "name": "Eva", "email": "eva@example.com", "age": 22},
    ]

    books = [
        {"book_id": 1, "title": "The Great Gatsby", "author": "author1", "publisher": "Scribner",
         "price": 10.99},
        {"book_id": 2, "title": "1984", "author": "author1", "publisher": "Secker & Warburg", "price": 15.99},
        {"book_id": 3, "title": "To Kill a Mockingbird", "author": "author2", "publisher": "J.B. Lippincott & Co.",
         "price": 12.49},
        {"book_id": 4, "title": "Moby-Dick", "author": "author2", "publisher": "Richard Bentley", "price": 18.50},
        {"book_id": 5, "title": "Pride and Prejudice", "author": "author3", "publisher": "T. Egerton", "price": 8.75},
    ]

    orders = [
        {"id": 1, "user_id": 1, "book_id": 1},
        {"id": 2, "user_id": 2, "book_id": 2},
        {"id": 3, "user_id": 3, "book_id": 3},
        {"id": 4, "user_id": 4, "book_id": 4},
        {"id": 5, "user_id": 5, "book_id": 5},
        {"id": 6, "user_id": 2, "book_id": 1},
        {"id": 7, "user_id": 3, "book_id": 2},
        {"id": 8, "user_id": 4, "book_id": 3},
        {"id": 9, "user_id": 5, "book_id": 5},
        {"id": 10, "user_id": 1, "book_id": 5}
    ]

    user_df = pd.DataFrame(users,columns=["user_id","name","email","age"])
    book_df = pd.DataFrame(books,columns=["book_id","title","author","publisher","price"])
    order_df = pd.DataFrame(orders,columns=["id","user_id","book_id"])

    group_df = book_df.groupby('author')['price'].mean()

    pivot_df = order_df.pivot_table(index='user_id'
                                    ,columns='book_id'
                                    ,values='id'
                                    ,aggfunc='count'
                                    ,fill_value=0)

    pivot_price = user_order_book_merge = pd.merge(
            pd.merge(user_df, order_df, on='user_id', how='inner'),
            book_df,
            on = 'book_id',
            how = 'inner'
        ).pivot_table(index="user_id",columns='book_id',values='price',aggfunc='sum',fill_value=0)

    print(pivot_price)

    # print(pivot_df)

    # print(pivot_df)
    # print(group_df)

    # for key,value in group_df:
    #     print("key" , key)
    #     print("value", value)

    # user_df['test1'] = 2

    # user_df['age*test1'] = user_df.apply(lambda x : multiple(x['age'],x['test1']),axis=1)
    # print(results)
    # print(user_df)
    # y = lambda x : 2*x + 2 # y = 2x+2


    # print(results)



    # print(user_df[user_df['age'] >= 30])
    # user_df.loc[4,"email"] = "John@example.com"
    # print(user_df.loc[4,"email"])
    # print(user_df)
    # user_df['test'] = 0
    # user_df['test2'] = 1
    # print(user_df)
    # user_df.drop(['test','test2'], axis=1, inplace=True) # axis = 1은 칼럼명
    # # print()
    # # user_df.drop('test', axis=1, inplace=True)
    # print(user_df)

    # user_order_merge = pd.merge(user_df,order_df,on = 'user_id', how='inner')
    # user_order_book_merge = pd.merge(
    #     pd.merge(user_df, order_df, on='user_id', how='inner'),
    #     book_df,
    #     on = 'book_id',
    #     how = 'inner'
    # )[['name','title','price']] # 갖고오고 싶은 필드명
    # # print(user_order_merge)
    # print(user_order_book_merge)

