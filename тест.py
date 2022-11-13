from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtWidgets import (QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGroupBox,QRadioButton,QPushButton,QLabel,QListWidget,QLineEdit)

class Mainwin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('Тест Руфье')
        self.set_apper() #интерфейс
        self.connect() #кнопки
        self.show() #окно
    

    def set_apper(self):
        #виджеты
        lable=QLabel("Добро пожаловать в программу по определению состояния здоровья!")
        lable1=QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                   'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
        self.button=QPushButton('Начать')
        v_line=QVBoxLayout()
        #добавление виджетов
        v_line.addWidget(lable)
        v_line.addWidget(lable1)
        v_line.addWidget(self.button)
        #ставим линию на экрвн
        self.setLayout(v_line)
    
    def connect(self):
        self.button.clicked.connect(self.next)

    def next(self):
        self.hide()
        tdni.show()

class Testwin(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle('Здоровье')
        self.set_apper() #интерфейс
        self.connect() #кнопки
        #self.show() #окно

    

    def set_apper(self):
        #таймер
        self.timer=QTimer()
        #виджеты
        lable=QLabel('Введите Ф.И.О.:')
        lable1=QLabel('инструкция')
        lable2=QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\n')
        lable3=QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\n'
        'чтобы запустить счетчик приседаний.')
        lable4=QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\n'
        'Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.\n'
        'Зелёным обозначены секунды, в течение которых необходимо \n'
        'проводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')
        self.time_label=QLabel('00:00:30')

        self.button=QPushButton('Начать первый тест')
        self.button2=QPushButton('Начать делать приседания')
        self.button3=QPushButton('Начать финальный тест')
        self.button4=QPushButton('Отправить результаты')

        line=QLineEdit("Ф.И.О.")
        line2=QLineEdit('0')
        line3=QLineEdit('0')
        line4=QLineEdit('0')
        line5=QLineEdit('0')
        
        v_line=QVBoxLayout()
        #добавление виджетов
        v_line.addWidget(lable)
        v_line.addWidget(line)
        v_line.addWidget(lable1)
        v_line.addWidget(line2)
        v_line.addWidget(lable2)
        v_line.addWidget(self.button)
        v_line.addWidget(line3)
        v_line.addWidget(lable3)
        v_line.addWidget(self.button2)
        v_line.addWidget(lable4)
        v_line.addWidget(self.button3)
        v_line.addWidget(line4)
        v_line.addWidget(line5)
        v_line.addWidget(self.time_label)
        v_line.addWidget(self.button4)
        #ставим линию на экрвн
        self.setLayout(v_line)

    def connect(self):
        self.button4.clicked.connect(self.next)
        self.button.clicked.connect(self.timer_test)
        self.button2.clicked.connect(self.timer_test1)
        self.button3.clicked.connect(self.timer_test2)

    def next(self):
        self.hide()
        #x.show()

    def timer_test(self):
        self.time=QTime(0,0,15)
        self.timer.timeout.connect(self.timeEdit1)
        self.timer.start(1000)

    def timeEdit1(self):
        self.time=self.time.addSecs(-1)
        self.time_label.setText(self.time.toString('hh:mm:ss'))
        if self.time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()

    def timer_test1(self):
        self.time=QTime(0,0,30)
        self.timer.timeout.connect(self.timeEdit1)
        self.timer.start(1000)

    def timeEdit2(self):
        self.time=self.time.addSecs(-1)
        self.time_label.setText(self.time.toString('hh:mm:ss')[6:8])
        if self.time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()

    def timer_test2(self):
        self.time=QTime(0,1,0)
        self.timer.timeout.connect(self.timeEdit1)
        self.timer.start(1000)

    def timeEdit3(self):
        self.time=self.time.addSecs(-1)
        self.time_label.setText(self.time.toString('hh:mm:ss'))
        if self.time.toString('hh:mm:ss')=='00:00:00':
            self.timer.stop()
        




















app=QApplication([])
tdni=Testwin()
inst=Mainwin()

app.exec_()
