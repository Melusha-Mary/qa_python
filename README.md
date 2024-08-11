# qa_python
# 1* test_add_new_book_add_two_books - проверяем, что добавилось именно две книги.                   
# 2. test_add_valid_name_book - проверяем, что книга добавляется, при валидном наименовании.
# 3. test_not_add_double_name_book - проверяем, что  gовторное добавление, не должно увеличивать счетчик
# 4. test_not_add_invalid_name_book_none - проверяем, что книга не добавляется, при невалидном наименовании. Пустое название                                              
# 5. test_not_add_invalid_name_book_more_40_symbols - проверяем, что книга не добавляется, при невалидном наименовании. Название более 40 символов.
# 6. test_set_book_genre - Проверяем, что жанр должен быть установлен корректно.
# 7. test_get_book_genre_with_incorrect_date_without_ganre - Проверка книги без установленного жанра.
# 8. test_get_book_genre_with_incorrect_date_without_book_title - Проверка на несуществующую книгу  
# 9. test_get_books_with_specific_genre_cartoon - проверяем, что должны быть книги с жанром 'Мультфильмы'
# 10. test_not_get_books_with_specific_genre_fantastic - проверяем, что Не должны быть книги с жанром 'Детективы'
# 11. test_get_books_genre - проверяем, что cловарь должен содержать существующие книги и их жанр.                                                                                               
# 12. test_get_books_for_children -  проверяем, что книги должны подходить для детей.                                                                                        
# 13. test_add_book_in_favorites - проверяем, что добавляется книга в избранное.  
# 14. test_not_add_book_in_favorites - проверяем, что Книга не добавляется повторно в Избранное
# 15. test_delete_book_from_favorites - проверяем, что удаляется книга в избранное.                                                                                        
# 16. test_get_list_of_favorites_books - проверяем, что список избранных книг корректный.