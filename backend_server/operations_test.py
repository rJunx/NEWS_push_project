import operations

def test_getOneNews_basic():
    news = operations.getOneNews()
    print(news)
    assert news is not None
    print("test_getOneNews_basic passed!")

def test_getNewsSummariesForUser_basic():
    news = operations.getNewsSummariesForUser('test', 1)
    assert len(news) > 0
    print('test_getNewsSummariesForUser_basic passed')

if __name__ == "__main__":
    test_getOneNews_basic()