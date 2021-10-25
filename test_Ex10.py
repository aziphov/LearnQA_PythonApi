class TestExample:
    def test_len(self):
        phrase = input("Set a phrase: ")
        assert len(phrase) < 15, "Фраза больше 15 символов"

