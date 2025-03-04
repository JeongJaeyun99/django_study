import pandas as pd


def multiple(param1,param2):
    return param1 * param2

def average(x,y,z):
    return (x + y + z ) / 3


print("Hello World")




if __name__ == "__main__":

    data = [
        [93,93,89],
        [80, 50, 41],
        [87, 70, 73],
        [72, 63, 80],
        [40, 54, 99],
    ]

    df = pd.DataFrame(data, columns=["국어", "영어", "수학"])

    print(df)

    # df['평균'] = (df['국어'] + df['영어'] + df['수학']) / 3
    # df['평균'] = df.apply(lambda table : (table['국어'] + table['영어'] + table['수학']) / 3, axis=1)
    df['평균'] = df.apply(lambda table : average(table['국어'],table['영어'],table['수학']), axis=1)

    print(df)

    # print("Hello World!!!!")
    #
    # numb1 = list(range(1,11))
    # numb2 = list(range(11,21))
    # results = map(multiple,numb1,numb2)
    # for result in results:
    #     print(result)
    # for result in range(1,11):
    #     print(result)
    # print(range(1,11)) # 주소를 print함
    # print(list(results))