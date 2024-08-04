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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    @pytest.mark.parametrize("book_title, expected_count", [
        ("Винни Пух", 1),  # Обычное название
        ("", 1),  # Пустое название, не добавится
        ("A" * 41, 1),  # Название более 40 символов, не добавится
        ("Винни Пух", 1),  # Повторное добавление, не должно увеличивать счетчик
    ])
    def test_add_new_book(self, book_title, expected_count):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_new_book(book_title)

        # проверяем, что количество книг должно соответствовать ожидаемому
        assert len(collector.books_genre) == expected_count

    @pytest.mark.parametrize("book_title, genre, expected_genre", [
        ("Винни Пух", "Мультфильмы", "Мультфильмы"),  # Допустимый жанр
        ("Винни Пух", "Неправильный жанр", ""),  # Неправильный жанр, не должен измениться
    ])
    def test_set_book_genre(self, book_title, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_title)
        # Устанавливаем жанр, даже если он неверный
        collector.set_book_genre(book_title, genre)

        # Проверяем, что жанр должен быть установлен корректно
        assert collector.get_book_genre(book_title) == expected_genre

    @pytest.mark.parametrize("book_title, expected_genre", [
        ("Винни Пух", "Мультфильмы"),  # Проверка успешного получения жанра
        ("Не существующая книга", None),  # Проверка на несуществующую книгу
    ])
    def test_get_book_genre(self, book_title, expected_genre):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")

        # проверяем, что жанр книги должен соответствовать ожидаемому
        assert collector.get_book_genre(book_title) == expected_genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.set_book_genre("Винни Пух", "Мультфильмы")
        collector.add_new_book("1926")
        collector.set_book_genre("1926", "Фантастика")

        books = collector.get_books_with_specific_genre("Мультфильмы")
        # проверяем, что должны быть книги с жанром 'Мультфильмы'
        assert books == ["Винни Пух"]

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
        collector.add_new_book("Ужасный детектив")
        collector.set_book_genre("Ужасный детектив", "Ужасы")

        books = collector.get_books_for_children()
        # проверяем, что книги должны подходить для детей
        assert books == ["Винни Пух"]

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Винни Пух")
        collector.add_book_in_favorites("Винни Пух")

        # проверяем, что книга должна быть в Избранном
        assert "Винни Пух" in collector.favorites

        collector.add_book_in_favorites("Винни Пух")
        # проверяем, что Книга не должна добавляться повторно в Избранное
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
