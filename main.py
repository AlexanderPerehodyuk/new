import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QImage, QPen, QPainter
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QFileDialog


class mw(QMainWindow):
    def __init__(self):
        super().__init__()
        #устанавливаем размеры
        self.resize(500, 500)
        #устанавливаем название
        self.setWindowTitle
        ("MyPaintAnalog")
        #устанавливаем холст, его цвет
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        #устанавливаем, чтобы изанчальнно не рисовали
        self.drawing = False
        #устанавливаем размер кисточки
        self.brushSize = 2
        #цвет кисточки
        self.brushColor = Qt.black
        #последняя точка
        self.lastPoint = QPoint()
        #делаем menuBar чтобы там были элементы для изменения увета, размера кисточки, сохранения нарисованного и очистки 
        mainMenu = self.menuBar()
        #добавления меню для работы с файлом(сохранене, очистки)
        fileMenu = mainMenu.addMenu("File")

        #добавление меню для изменение размера кисточки
        brushMenu = mainMenu.addMenu("Brush Size")

        #добавление меню для измение цвета кисточки
        brushColor = mainMenu.addMenu("Brush Color")

        #создание кнопки для сохранения картинки
        saveAction = QAction("Save", self)
        #добавление ей быстрой клавиши
        saveAction.setShortcut("Cntrl+S")
        #добавление в меня для работы с файлом
        fileMenu.addAction(saveAction)
        #присваивание ей метода при нажатии
        saveAction.triggered.connect(self.save)

        #анологично как и для сохранение
        clearAction = QAction("Clear", self)
        clearAction.setShortcut("Cntrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        openAction = QAction("Open", self)
        openAction.setShortcut("Cntrl+O")
        fileMenu.addAction(openAction)
        openAction.triggered.connect(self.open)

        #тоже самое но без быстрой клавиши
        tpAction = QAction("Three pixel", self)
        brushMenu.addAction(tpAction)
        tpAction.triggered.connect(self.tp)

        #анологично как и для 3 пикселей
        fpAction = QAction("Five pixel", self)
        brushMenu.addAction(fpAction)
        fpAction.triggered.connect(self.fp)

        #анологично как и для 3 пикселей
        npAction = QAction("Nine pixel", self)
        brushMenu.addAction(npAction)
        npAction.triggered.connect(self.np)

        #анологично как и для 3 пикселей
        whiteAction = QAction("Стерка", self)
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.wColor)

        #анологично как и для 3 пикселей
        blackAction = QAction("Black", self)
        brushColor.addAction(blackAction)
        blackAction.triggered.connect(self.bColor)

        #анологично как и для 3 пикселей
        redAction = QAction("Red", self)
        brushColor.addAction(redAction)
        redAction.triggered.connect(self.rColor)

        #анологично как и для 3 пикселей
        GreenAction = QAction("Green", self)
        brushColor.addAction(GreenAction)
        GreenAction.triggered.connect(self.gColor)

        #анологично как и для 3 пикселей
        blueAction = QAction("Blue", self)
        brushColor.addAction(blueAction)
        blueAction.triggered.connect(self.bColor)

        #анологично как и для 3 пикселей
        yAction = QAction("Yellow", self)
        brushColor.addAction(yAction)
        yAction.triggered.connect(self.yColor)


    def mousePressEvent(self, event):
        #при нажатии на кнопку в последнию кнопку передается места где была нажата кнопка и рисование становиться True
          if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            

    def mouseMoveEvent(self, event):
        #рисование линиии и обновление экрана
          if self.drawing:
            painter = QPainter(self.image)
            
            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            
            self.update()
        
    def mouseReleazeEvent(self, event):
        #рисование становиться False чтобы при отпуске  кнопки линия переставала рисоваться
        if event.button() == Qt.LeftButton:
          self.drawing = False
            
    def paintEvent(self, event):
          canvaspainter = QPainter(self)
          canvaspainter.drawImage(self.rect(), self.image, self.image.rect())
        
    def save(self):
        #сохранение путя для сохранение фото и сохранение если путь указан
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
          return
        else:
          self.image.save(filePath)
    
    def open(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);; ALL Files(*.*)")
        if filePath == "":
          return
        else:
          self.image = QImage(filePath)
          
    def clear(self):
        #очищение холста и обновление экрана
        self.image.fill(Qt.white)
        self.update()

    def tp(self):
        #размер линии при рисовки будет 3 до следущего изменения
        self.brushSize = 3
        
    def fp(self):
        #размер линии при рисовки будет 5 до следущего изменения
        self.brushSize = 5
        
    def np(self):
        #размер линии при рисовки будет 9 до следущего изменения
        self.brushSize = 9

    def bColor(self):
      #цвет линии при рисовки будет черный до следущего изменения
        self.brushColor = Qt.black
        
    def wColor(self):
        #цвет линии при рисовки будет черный до следущего изменения
        self.brushColor = Qt.white
        
    def rColor(self):
        #цвет линии при рисовки будет красный до следущего изменения
        self.brushColor = Qt.red
        
    def gColor(self):
        #цвет линии при рисовки будет зеленый до следущего изменения
        self.brushColor = Qt.green
        
    def bColor(self):
        #цвет линии при рисовки будет синий до следущего изменения
        self.brushColor = Qt.blue
        
    def yColor(self):
        #цвет линии при рисовки будет желтый до следущего изменения
        self.brushColor = Qt.yellow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())
