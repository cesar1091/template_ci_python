from hello import hello, goodbye


def test_hello():
    assert "Hi" == hello()


def test_goodbye():
    assert "Bye" == goodbye()
