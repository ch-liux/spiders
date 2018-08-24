import tushare as ts


def get_news():
    # 默认获取最近80条新闻数据，只提供新闻类型、链接和标题
    news = ts.get_latest_news()
    # 显示最新5条新闻，并打印出新闻内容
    news5 = ts.get_latest_news(top=5, show_content=True)
    print(news, news5)


def get_movie():
    # mov = ts.realtime_boxoffice()
    # print(mov.to_json())
    df = ts.day_cinema()  # 取上一日全国影院票房排行数据
    # df = ts.day_cinema('2015-12-24') #取指定日期的数据
    df.head(10)
    print(df.to_json())


if __name__ == "__main__":
    get_movie()