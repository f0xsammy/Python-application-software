# TODO Найдите количество книг, которое можно разместить на дискете

pages = 100
strings = 50
symbols = 25
size = 4

disk_b = 1.44 * 1024 * 1024
book = pages * strings * symbols * size
sum_books = int(disk_b // book)
print("Количество книг, помещающихся на дискету:", sum_books)
