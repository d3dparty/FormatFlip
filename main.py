# Создано d3dparty, лицензия AGPL-3.0, опубликовано на Github в 2024 году
#
# подключаем библиотеки
# subprocess - для запуска ffmpeg.exe
import subprocess
# os - для поиска пути, где находится ffmpeg.exe после запуска и очистки консоли
import os
# sys - также связано с поиском пути ffmpeg.exe
import sys
# time - чтобы использовать задержку time.sleep()
import time

# создаём класс Convert
class Convert():
    # метод инициализации
    def __init__(self):
        # inputFile хранит входной файл и путь к нему
        self.inputFile = ""
        # outputFile хранит выходной файл и путь к нему
        self.outputFile = ""
        # outputFormat хранит формат/расширение выходного файла
        self.outputFormat = ""
        # ffmpegPath хранит временный путь к ffmpeg.exe после запуска приложения
        self.ffmpegPath = os.path.join(sys._MEIPASS, 'ffmpeg.exe')

    # метод askInfo - спрашивает все необходимые данные для конвертации у пользователя
    def askInfo(self):
        # очищаем консоль
        os.system("cls")
        print("===============  Конвертер видео  ================", '\n')
        print("Выберите файл (укажите полный путь к файлу): ")
        # спрашиваем у пользователя входной файл/путь к нему и записываем как строку в UTF-8
        self.inputFile = input().encode("utf-8")
        print()

        print("Укажите путь, куда сохранить файл: ")
        # спрашиваем у пользователя выходной файл/путь к нему и записываем как строку в UTF-8
        self.outputFile = input().encode("utf-8")
        print()

        print("Укажите выходной формат файла (без точки): ")
        # спрашиваем у пользователя формат/расширение выходного файла и записываем как строку в UTF-8
        self.outputFormat = input().encode("utf-8")
        # складываем всё в полный путь к выходному файлу
        self.outputFile = self.outputFile + b"output" + b"." + self.outputFormat
    
    # метод convertion - конвертирует входной файл из выходного файла    
    def convertion(self):
        # очищаем консоль
        os.system("cls")
        print("===============  Конвертер видео  ================", '\n')
        print("Конвертируем...")
        # в конструкции try-except запускаем ffmpeg по пути ffmpegPath и передаем все нужные аргументы
        try:
            subprocess.run([self.ffmpegPath, "-i", self.inputFile, "-c:v", "copy", "-c:a", "copy", self.outputFile], check=True, stderr=subprocess.PIPE)
        # если ловим какую-либо ошибку
        except subprocess.CalledProcessError as e:
            # перехватываем stderr поток и выводим её в файл log.txt
            with open("log.txt", 'w') as f:
                f.write(e.stderr.decode())
        # проверяем существование выходного файла
        if os.path.exists(self.outputFile):
            # ЕСЛИ файл существует, то выводим сообщение
            print("Выполнено!", "Конвертированный файл сохранен")
            print(self.outputFile)
            # оставляем задержку в 5 секунд, чтобы пользователь успел прочитать сообщение
            time.sleep(5)
        else:
            # ИНАЧЕ выводим сообщение об ошибке
            print("Произошла ошибка!", "Для полной информации проверьте файл log.txt в директории программы")
            # оставляем задержку в 5 секунд, чтобы пользователь успел прочитать сообщение
            time.sleep(5)

# создаем экземляр vc класса Convert()
vc = Convert()
# вызываем метод askInfo()
vc.askInfo()
# вызываем метод convertion()
vc.convertion()
