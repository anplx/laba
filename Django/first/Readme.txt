WebDAV — набор расширений и дополнений к протоколу HTTP (протокол прикладного уровня передачи произвольных данных), 
поддерживающих совместную работу пользователей над редактированием файлов и управление файлами на удаленных веб-серверах.


127.0.0.1:port/ - вызовет метод перечисления файлов и папок в текущей директории

127.0.0.1:port/migrations - вызовет метод перечисления файлов и папок из папки migrations, находящейся в lab1

127.0.0.1:port/create/?fold=1 - вызовет метод создания пустой папки 1 в lab1 

127.0.0.1:port/delete/?fold=2 - вызовет метод удаления пустой папки 1 в lab1 

127.0.0.1:port/download/?file=admin.py - вызовет метод удаленного скачивания файла admin.py

Для проверки функций использовался браузер Microsoft Edge
