from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QGroupBox, QButtonGroup
from PyQt5.QtGui import QFont, QIcon
import webbrowser
#function
def test_btn_function():
    line1.addWidget(start_text)
    RadioGroupBox.show()
    school_btn.hide()
    test_btn.hide()
    start_text.setText('Сейчас ты пройдёшь тест на 20 вопросов и узнаешь свой примерный уровень квалификации!🐍\nВопрос 1: Как расшифровывается ООП?')
    next_question_btn1.show()
#next que func
def next_question_btn1_function():
    if rbtn_2.isChecked():
        window.score += 1
        window.oop += 1
    elif rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass

    start_text.setText('Вопрос 2: Назовите основные принципы ООП')
    rbtn_1.setText('Инкапсуляция, полиморфизм, наследование')
    rbtn_2.setText('Делегирование, полиморфизм, абстракция')
    rbtn_3.setText('Разделение интерфейса, абстракция')
    rbtn_4.setText('Инкапсуляция, открытость/закрытость')
    next_question_btn1.hide()
    next_question_btn2.show()

def next_question_btn2_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.oop += 1

    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass

    start_text.setText('Вопрос 3: Этот принцип является способностью\nиспользовать общий интерфейс для нескольких форм')
    rbtn_1.setText('Инкапсуляция')
    rbtn_2.setText('Наследование')
    rbtn_3.setText('Абстракция')
    rbtn_4.setText('Полиморфизм')
    next_question_btn2.hide()
    next_question_btn3.show()

def next_question_btn3_function():
    if rbtn_4.isChecked():
        window.score += 1
        window.oop += 1
        
    elif rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_2.isChecked():
        pass
    
    start_text.setText('Вопрос 4: Какой из перечисленных вариантов\nявляется верным объявлением private поля?')
    rbtn_1.setText('field = 0')
    rbtn_2.setText('private field = 0')
    rbtn_3.setText('__field = 0')
    rbtn_4.setText('-field = 0')
    next_question_btn3.hide()
    next_question_btn4.show()
    
def next_question_btn4_function():
    if rbtn_3.isChecked():
        window.score += 1
        window.oop += 1
    elif rbtn_2.isChecked() or rbtn_1.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 5: Какой метод отвечает за удаление элемента списка')
    rbtn_1.setText('remove()')
    rbtn_2.setText('clear()')
    rbtn_3.setText('pop()')
    rbtn_4.setText('Такого нет')
    next_question_btn4.hide()
    next_question_btn5.show()

def next_question_btn5_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.spiski += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 6: Какой максимальный размер списка?')
    rbtn_1.setText('1 млн')
    rbtn_2.setText('10 млн')
    rbtn_3.setText('Лимита элементов нет')
    rbtn_4.setText('1 тыс.')
    next_question_btn5.hide()
    next_question_btn6.show()

def next_question_btn6_function():
    if rbtn_3.isChecked():
        window.score += 1
        window.spiski += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 7: При каких элементов списка метод sort()\nработает без ошибок?')
    rbtn_1.setText('Однотипных элементах')
    rbtn_2.setText('Любых типах')
    rbtn_3.setText('Строковых')
    rbtn_4.setText('Целочисленных')
    next_question_btn6.hide()
    next_question_btn7.show()

def next_question_btn7_function():
    if rbtn_4.isChecked():
        window.score += 1
        window.spiski += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_1.isChecked():
        pass
    start_text.setText('Вопрос 8: Какой метод добавляет элемент в конец списка?')
    rbtn_1.setText('extend()')
    rbtn_2.setText('append()')
    rbtn_3.setText('include()')
    rbtn_4.setText('add()')
    next_question_btn7.hide()
    next_question_btn8.show()

def next_question_btn8_function():
    if rbtn_2.isChecked():
        window.score += 1
        window.spiski += 1 
    elif rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 9: Что такое итерация?')
    rbtn_1.setText('Такого понятия нет')
    rbtn_2.setText('Однократное выполнение действия')
    rbtn_3.setText('Многократное выполнение действия')
    rbtn_4.setText('Переменная')
    next_question_btn8.hide()
    next_question_btn9.show()

def next_question_btn9_function():
    if rbtn_3.isChecked():
        window.score += 1
        window.whiles += 1
    elif rbtn_2.isChecked() or rbtn_1.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 10: Что из этого итерация?')
    rbtn_1.setText('from')
    rbtn_2.setText('list')
    rbtn_3.setText('class')
    rbtn_4.setText('while')
    next_question_btn9.hide()
    next_question_btn10.show()

def next_question_btn10_function():
    if rbtn_4.isChecked():
        window.score += 1
        window.whiles += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_1.isChecked():
        pass
    start_text.setText('Вопрос 11: Что делает break?')
    rbtn_1.setText('Останавливает цикл')
    rbtn_2.setText('Продолжает цикл')
    rbtn_3.setText('Такого не бывает')
    rbtn_4.setText('Останавливает программу')
    next_question_btn10.hide()
    next_question_btn11.show()

def next_question_btn11_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.whiles += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 12: Для чего else в циклах?')
    rbtn_1.setText('Проверяет работает ли цикл')
    rbtn_2.setText('Проверяет был ли сделан выход из цикла')
    rbtn_3.setText('Не используется')
    rbtn_4.setText('Создает условие')
    next_question_btn11.hide()
    next_question_btn12.show()

def next_question_btn12_function():
    if rbtn_2.isChecked():
        window.score += 1
        window.whiles += 1
    elif rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 13: Что выведет:\na = "2" + "2"\nprint(a)')
    rbtn_1.setText('22')
    rbtn_2.setText('2')
    rbtn_3.setText('4')
    rbtn_4.setText('ошибку')
    next_question_btn12.hide()
    next_question_btn13.show()

def next_question_btn13_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.stroki += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 14: Что выведет:\nb = "a" + "b"\nprint(b)')
    rbtn_1.setText('ошибку')
    rbtn_2.setText('ba')
    rbtn_3.setText('ab')
    rbtn_4.setText('a')
    next_question_btn13.hide()
    next_question_btn14.show()

def next_question_btn14_function():
    if rbtn_3.isChecked():
        window.score += 1
        window.stroki += 1
    elif rbtn_2.isChecked() or rbtn_1.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 15: Что выведет:\nd = "3" - "1"\nprint(d)')
    rbtn_1.setText('-3')
    rbtn_2.setText('3-1')
    rbtn_3.setText('2')
    rbtn_4.setText('ошибку')
    next_question_btn14.hide()
    next_question_btn15.show()

def next_question_btn15_function():
    if rbtn_4.isChecked():
        window.score += 1
        window.stroki += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_1.isChecked():
        pass
    start_text.setText('Вопрос 16: Что выведет:\ne = "a" + "1"\nprint(e)')
    rbtn_1.setText('a1')
    rbtn_2.setText('a11')
    rbtn_3.setText('1a')
    rbtn_4.setText('a')
    next_question_btn15.hide()
    next_question_btn16.show()

def next_question_btn16_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.stroki += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 17: Какой оператор означает правильность выполнения?')
    rbtn_1.setText('try')
    rbtn_2.setText('except')
    rbtn_3.setText('while')
    rbtn_4.setText('from')
    next_question_btn16.hide()
    next_question_btn17.show()

def next_question_btn17_function():
    if rbtn_1.isChecked():
        window.score += 1
        window.iskluchenia += 1
    elif rbtn_2.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 18: Какой оператор означает НЕПРАВИЛЬНОСТЬ выполнения?')
    rbtn_1.setText('import')
    rbtn_2.setText('try')
    rbtn_3.setText('except')
    rbtn_4.setText('begin')
    next_question_btn17.hide()
    next_question_btn18.show()

def next_question_btn18_function():
    if rbtn_3.isChecked():
        window.score += 1
        window.iskluchenia += 1
    elif rbtn_2.isChecked() or rbtn_1.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 19: После except можно ставить название ошибки?')
    rbtn_1.setText('Нет')
    rbtn_2.setText('Да')
    rbtn_3.setText('Только ValueError')
    rbtn_4.setText('Только SyntaxError')
    next_question_btn18.hide()
    next_question_btn19.show()

def next_question_btn19_function():
    if rbtn_2.isChecked():
        window.score += 1
        window.iskluchenia += 1
    elif rbtn_1.isChecked() or rbtn_3.isChecked() or rbtn_4.isChecked():
        pass
    start_text.setText('Вопрос 20: В try и except нужны отступы?')
    rbtn_1.setText('Только в try')
    rbtn_2.setText('Только в except')
    rbtn_3.setText('Везде нужны')
    rbtn_4.setText('Нигде не нужны')
    next_question_btn19.hide()
    next_question_btn20.show()

def result_test():
    if rbtn_3.isChecked():
        window.score += 1
        window.iskluchenia += 1
    elif rbtn_2.isChecked() or rbtn_1.isChecked() or rbtn_4.isChecked():
        pass
    
    line1.addWidget(start_text)
    start_text.setText('Колличество баллов: '+str(int(window.score))+' из 20🤔\nООП '+str(int(window.oop))+" из 4 👏"+'\nЦиклы '+str(int(window.whiles))+" из 4 👏"+'\nСтроки '+str(int(window.stroki))+" из 4 👏"+'\nИсключения '+str(int(window.iskluchenia))+" из 4 👏"+'\nСписки '+str(int(window.spiski))+" из 4 👏")
    RadioGroupBox.hide()
    next_question_btn20.hide()
    reset_btn.show()

    if int(window.score) == 20:
        result_test_k.show()
        result_test_k.setText('Примерный уровень подготовки: Senior😎\nВаши знания на высоком уровне, но в разделе База знаний Python вы можете найти что то новое и интересное!\nНапример Машинное Обучение и python.📔')

    elif int(window.score) < 20 and int(window.score) > 15:
        result_test_k.show()
        result_test_k.setText('Примерный уровень подготовки: Middle😜\nВы очень хорошо справились с тестом, но ошибки есть! В разделе База знаний Python вы можете найти и изучить что было непонятно!📔')

    elif int(window.score) < 15:
        result_test_k.show()
        result_test_k.setText('Примерный уровень подготовки: Junior😋\nРекомендуем вам подтянуть свои знания! В разделе База знаний Python есть все необходимые ссылки на источники информации!📔')
    
    result_test_r.show()
    if window.oop == 4 and window.spiski == 4 and window.whiles == 4 and window.stroki == 4 and window.iskluchenia == 4:
        result_test_r.setText('')
    if 2 >= window.oop:
        result_test_r.setText('Рекомендация:\nВам не мешает получше разобраться в теме "ООП" и в других темах которые вызвали у вас затруднение. Вы можете найти это в\nкниге "Изучаем программирование на Python".\nЭта и другие книги есть в Базе знаний в этом приложении!')
    if 2 >= window.spiski:
        result_test_r.setText('Рекомендация:\nВам не мешает получше разобраться в теме "Списки" и в других темах которые вызвали у вас затруднение. Вы можете найти это в\nкниге "Изучаем программирование на Python".\nЭта и другие книги есть в Базе знаний в этом приложении!')
    if 2 >= window.iskluchenia:
        result_test_r.setText('Рекомендация:\nВам не мешает получше разобраться в теме "Обработка исключений" и в других темах которые вызвали у вас затруднение. Вы можете найти это в\nкниге "Изучаем программирование на Python".\nЭта и другие книги есть в Базе знаний в этом приложении!')
    if 2 >= window.stroki:
        result_test_r.setText('Рекомендация:\nВам не мешает получше разобраться в теме "Действия со строками" и в других темах которые вызвали у вас затруднение. Вы можете найти это в\nкниге "Изучаем программирование на Python".\nЭта и другие книги есть в Базе знаний в этом приложении!')
    if 2 >= window.whiles:
        result_test_r.setText('Рекомендация:\nВам не мешает получше разобраться в теме "Циклы" и в других темах которые вызвали у вас затруднение. Вы можете найти это в\nкниге "Изучаем программирование на Python".\nЭта и другие книги есть в Базе знаний в этом приложении!')

def school_btn_function():
    start_text.setText('Здесь вы найдёте полезные ссылки и книги по языку программирования python🐍\nКаждый найдет здесь что то интересное😉Например Stackoverflow!\nЭто форум для программистов где вы можете задать вопрос и вам скорее всего ответят и объяснят код!\nИли например Хабр - это форум для программистов как\nи stackoverflow, но в нём также собраны полезные статьи по языкам программирования и библиотекам!\nИли github - это соц. сеть для разработчиков, где можно поделиться своми проектами\nи репозиториями с другими программистами!')
    school_btn.hide()
    test_btn.hide()
    web_btn1.show()
    web_btn2.show()
    web_btn3.show()
    web_btn4.show()
    reset_btn.show()

def reset_btn_function():
    start_text.setText('Привет😉 Это сервис для того чтобы: узнать свои уровень\nзнаний по языку программирования Python\nи обучиться новому в программировании на Python🐍!\nВыбери опцию ниже👇')
    start_text.show()
    school_btn.show()
    test_btn.show()
    RadioGroupBox.hide()
    web_btn1.hide()
    web_btn2.hide()
    web_btn3.hide()
    web_btn4.hide()
    result_test_k.hide()
    reset_btn.hide()
    result_test_r.hide()
    line1.addWidget(start_text, alignment=Qt.AlignCenter)
    rbtn_1.setText('Основы объект программирования')
    rbtn_2.setText('Объектно-ориентированное программирование')
    rbtn_3.setText('Отладка опенсорс проектов')
    rbtn_4.setText('Основные опорные программы')

def github():
    webbrowser.open('https://github.com/', new=2)
    start_text.setText('Ссылка открылась в вашем браузере!😉')

def habr():
    webbrowser.open('https://habr.com/ru/all/', new=2)
    start_text.setText('Ссылка открылась в вашем браузере!😉')

def stackoverflow():
    webbrowser.open('https://stackoverflow.com/', new=2)
    start_text.setText('Ссылка открылась в вашем браузере!😉')

def books():
    webbrowser.open('https://drive.google.com/drive/folders/1Jl8dP63LYRbHYt9nsSiWzD-wxD2zSI-g?usp=sharing', new=2)
    start_text.setText('Ссылка открылась в вашем браузере!😉')

#application and window
app = QApplication([])
window = QWidget()
window.resize(1000, 600)
window.setWindowTitle('Pydev')
window.setStyleSheet('background-color: beige')
start_text = QLabel('Привет😉 Это сервис для того чтобы: узнать свои уровень\nзнаний по языку программирования Python\nи обучиться новому в программировании на Python🐍!\nЕсли найдёте баг или ошибку пишите разработчику в телеграмм @stalnoy_alexander\nВыбери опцию ниже👇')
start_text.setFont(QFont('Calibri', 14))
school_btn = QPushButton('База знаний Python📔')
school_btn.setFont(QFont('Arial', 12))
test_btn = QPushButton('Тест на знание Python🤔')
test_btn.setFont(QFont('Arial', 12))
result_test_k = QLabel('')
reset_btn = QPushButton('👈Назад в меню')
reset_btn.setFont(QFont('Arial', 14))
result_test_k.setFont(QFont('Calibri', 14))
web_btn1 = QPushButton('Stackoverflow📙')
web_btn1.setFont(QFont('Arial', 12))
web_btn2 = QPushButton('Хабр👾')
web_btn2.setFont(QFont('Arial', 12))
web_btn3 = QPushButton('Гит Хаб🐱‍👤')
web_btn3.setFont(QFont('Arial', 12))
web_btn4 = QPushButton('Ссылка на книги (Google диск)📔')
web_btn4.setFont(QFont('Arial', 12))
result_test_r = QLabel('')
result_test_r.setFont(QFont('Calibri', 14))
#num
window.score = 0
window.oop = 0
window.spiski = 0 
window.whiles = 0
window.stroki = 0
window.iskluchenia = 0
#next que btn
next_question_btn1 = QPushButton('Следующий вопрос -->')
next_question_btn1.setFont(QFont('Arial', 12))
next_question_btn2 = QPushButton('Следующий вопрос -->')
next_question_btn2.setFont(QFont('Arial', 12))
next_question_btn3 = QPushButton('Следующий вопрос -->')
next_question_btn3.setFont(QFont('Arial', 12))
next_question_btn4 = QPushButton('Следующий вопрос -->')
next_question_btn4.setFont(QFont('Arial', 12))
next_question_btn5 = QPushButton('Следующий вопрос -->')
next_question_btn5.setFont(QFont('Arial', 12))
next_question_btn6 = QPushButton('Следующий вопрос -->')
next_question_btn6.setFont(QFont('Arial', 12))
next_question_btn7 = QPushButton('Следующий вопрос -->')
next_question_btn7.setFont(QFont('Arial', 12))
next_question_btn8 = QPushButton('Следующий вопрос -->')
next_question_btn8.setFont(QFont('Arial', 12))
next_question_btn9 = QPushButton('Следующий вопрос -->')
next_question_btn9.setFont(QFont('Arial', 12))
next_question_btn10 = QPushButton('Следующий вопрос -->')
next_question_btn10.setFont(QFont('Arial', 12))
next_question_btn11 = QPushButton('Следующий вопрос -->')
next_question_btn11.setFont(QFont('Arial', 12))
next_question_btn12 = QPushButton('Следующий вопрос -->')
next_question_btn12.setFont(QFont('Arial', 12))
next_question_btn13 = QPushButton('Следующий вопрос -->')
next_question_btn13.setFont(QFont('Arial', 12))
next_question_btn14 = QPushButton('Следующий вопрос -->')
next_question_btn14.setFont(QFont('Arial', 12))
next_question_btn15 = QPushButton('Следующий вопрос -->')
next_question_btn15.setFont(QFont('Arial', 12))
next_question_btn16 = QPushButton('Следующий вопрос -->')
next_question_btn16.setFont(QFont('Arial', 12))
next_question_btn17 = QPushButton('Следующий вопрос -->')
next_question_btn17.setFont(QFont('Arial', 12))
next_question_btn18 = QPushButton('Следующий вопрос -->')
next_question_btn18.setFont(QFont('Arial', 12))
next_question_btn19 = QPushButton('Следующий вопрос -->')
next_question_btn19.setFont(QFont('Arial', 12))
next_question_btn20 = QPushButton('Показать результат теста👀-->')
next_question_btn20.setFont(QFont('Arial', 12))
#group box
RadioGroupBox = QGroupBox("Варианты ответов")
RadioGroupBox.setFont(QFont('Calibri', 12))
rbtn_1 = QRadioButton('Основы объект программирования')
rbtn_1.setFont(QFont('Arial', 11))
rbtn_2 = QRadioButton('Объектно-ориентированное программирование')
rbtn_2.setFont(QFont('Arial', 11))
rbtn_3 = QRadioButton('Отладка опенсорс проектов')
rbtn_3.setFont(QFont('Arial', 11))
rbtn_4 = QRadioButton('Основные опорные программы')
rbtn_4.setFont(QFont('Arial', 11))
#layouts
boss_line = QVBoxLayout()
line1 = QVBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line1.addWidget(start_text, alignment=Qt.AlignCenter)
line2.addWidget(school_btn)
line2.addWidget(test_btn)
line2.addWidget(result_test_k) 
line3.addWidget(result_test_r) 
result_test_r.hide()
line4.addWidget(reset_btn)
reset_btn.hide()
line2.addWidget(web_btn1)
line2.addWidget(web_btn2)
line2.addWidget(web_btn3)
line2.addWidget(web_btn4)
web_btn1.hide()
web_btn2.hide()
web_btn3.hide()
web_btn4.hide()
result_test_k.hide()
layout_ans1 = QVBoxLayout() 
layout_ans2 = QVBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans1.addWidget(rbtn_1) 
layout_ans1.addWidget(rbtn_2)
layout_ans2.addWidget(rbtn_3) 
layout_ans2.addWidget(rbtn_4)
layout_ans3.addLayout(layout_ans1)
layout_ans3.addLayout(layout_ans2)
RadioGroupBox.setLayout(layout_ans3)
layout = QHBoxLayout()
#next que
layout.addWidget(next_question_btn1, stretch=3)
next_question_btn1.hide()
layout.addWidget(next_question_btn2, stretch=3)
next_question_btn2.hide()
layout.addWidget(next_question_btn3, stretch=3)
next_question_btn3.hide()
layout.addWidget(next_question_btn4, stretch=3)
next_question_btn4.hide()
layout.addWidget(next_question_btn5, stretch=3)
next_question_btn5.hide()
layout.addWidget(next_question_btn6, stretch=3)
next_question_btn6.hide()
layout.addWidget(next_question_btn7, stretch=3)
next_question_btn7.hide()
layout.addWidget(next_question_btn8, stretch=3)
next_question_btn8.hide()
layout.addWidget(next_question_btn9, stretch=3)
next_question_btn9.hide()
layout.addWidget(next_question_btn10, stretch=3)
next_question_btn10.hide()
layout.addWidget(next_question_btn11, stretch=3)
next_question_btn11.hide()
layout.addWidget(next_question_btn12, stretch=3)
next_question_btn12.hide()
layout.addWidget(next_question_btn13, stretch=3)
next_question_btn13.hide()
layout.addWidget(next_question_btn14, stretch=3)
next_question_btn14.hide()
layout.addWidget(next_question_btn15, stretch=3)
next_question_btn15.hide()
layout.addWidget(next_question_btn16, stretch=3)
next_question_btn16.hide()
layout.addWidget(next_question_btn17, stretch=3)
next_question_btn17.hide()
layout.addWidget(next_question_btn18, stretch=3)
next_question_btn18.hide()
layout.addWidget(next_question_btn19, stretch=3)
next_question_btn19.hide()
layout.addWidget(next_question_btn20, stretch=3)
next_question_btn20.hide()
#radio que
RadioGroupBox.hide()
#show app
boss_line.addLayout(line1)
boss_line.addLayout(line2)
boss_line.addLayout(line3)
boss_line.addLayout(line4)
boss_line.addWidget(RadioGroupBox)
boss_line.addLayout(layout)
test_btn.clicked.connect(test_btn_function)
#connect next
next_question_btn1.clicked.connect(next_question_btn1_function)
next_question_btn2.clicked.connect(next_question_btn2_function) 
next_question_btn3.clicked.connect(next_question_btn3_function) 
next_question_btn4.clicked.connect(next_question_btn4_function) 
next_question_btn5.clicked.connect(next_question_btn5_function) 
next_question_btn6.clicked.connect(next_question_btn6_function) 
next_question_btn7.clicked.connect(next_question_btn7_function) 
next_question_btn8.clicked.connect(next_question_btn8_function) 
next_question_btn9.clicked.connect(next_question_btn9_function)
next_question_btn10.clicked.connect(next_question_btn10_function)
next_question_btn11.clicked.connect(next_question_btn11_function)
next_question_btn12.clicked.connect(next_question_btn12_function)
next_question_btn13.clicked.connect(next_question_btn13_function)
next_question_btn14.clicked.connect(next_question_btn14_function)
next_question_btn15.clicked.connect(next_question_btn15_function)
next_question_btn16.clicked.connect(next_question_btn16_function)
next_question_btn17.clicked.connect(next_question_btn17_function)
next_question_btn18.clicked.connect(next_question_btn18_function)
next_question_btn19.clicked.connect(next_question_btn19_function)
reset_btn.clicked.connect(reset_btn_function)
school_btn.clicked.connect(school_btn_function)
next_question_btn20.clicked.connect(result_test)
web_btn1.clicked.connect(stackoverflow)
web_btn2.clicked.connect(habr)
web_btn3.clicked.connect(github)
web_btn4.clicked.connect(books)
school_btn.clicked.connect(school_btn_function)

#end
window.setLayout(boss_line)
window.show()
app.exec_()