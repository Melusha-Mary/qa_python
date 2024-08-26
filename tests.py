from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test

class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_valid_name_book(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")

        # проверяем, что книга добавляется, при валидном наименовании
        assert len(collector.books_genre) == 1

    def test_not_add_double_name_book(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_new_book("Винни Пух")

        # Повторное добавление, не должно увеличивать счетчик
        assert len(collector.books_genre) == 1


    @pytest.mark.parametrize("book_title, expected_count", [
        ("", 0),  # Пустое название, не добавится
        ("A" * 41, 0),  # Название более 40 символов, не добавится
    ])
    def test_not_add_invalid_name_book(self, book_title, expected_count):
        collector = BooksCollector()
        collector.add_new_book(book_title)

        # проверяем, что книга не добавляется, при невалидном наименовании
        assert len(collector.books_genre) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        # Проверяем, что жанр должен быть установлен корректно
        assert collector.get_book_genre("Винни Пух") == "Мультфильмы"


    @pytest.mark.parametrize("book_title, expected_genre", [
        ("Приключения", None),  # Проверка книги без установленного жанра
        ("Не существующая книга", None),  # Проверка на несуществующую книгу
    ])
    def test_get_book_genre_with_incorrect_date(self, book_title, expected_genre):
        collector = BooksCollector()
        collector.add_new_book("book_title")

        assert collector.get_book_genre(book_title) is None

    def test_get_books_with_specific_genre_cartoon(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        books = collector.get_books_with_specific_genre("Мультфильмы")
        # проверяем, что должны быть книги с жанром 'Мультфильмы'
        assert books == ["Винни Пух"]

    def test_not_get_books_with_specific_genre_fantastic(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        books = collector.get_books_with_specific_genre("Детективы")
        # проверяем, что Не должны быть книги с жанром 'Детективы'
        assert books == []

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        books_genre = collector.get_books_genre()
        # проверяем, что cловарь должен содержать существующие книги и их жанр
        assert books_genre == {"Винни Пух": "Мультфильмы"}

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        books = collector.get_books_for_children()
        # проверяем, что книги должны подходить для детей
        assert books == ["Винни Пух"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")

        # проверяем, что книга добавилась в Избранное
        assert "Винни Пух" in collector.favorites

    def test_not_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")
        # проверяем, что Книга не добавляется повторно в Избранное
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")
        collector.delete_book_from_favorites("Винни Пух")

        # проверяем, Книга должна быть удалена из Избранного
        assert "Винни Пух" not in collector.favorites

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_new_book("1926")
        collector.add_book_in_favorites("Винни Пух")
        collector.add_book_in_favorites("1926")

        favorites = collector.get_list_of_favorites_books()
        # проверяем, что список Избранных книг должен быть корректным
        assert sorted(favorites) == sorted(["Винни Пух", "1926"])
