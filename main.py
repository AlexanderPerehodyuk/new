import sys
from math import cos, pi, sin, radians

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QMouseEvent, QImage, QPen, QPainter, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QMenuBar, QMenu, QAction, QFileDialog, QSlider, QColorDialog, QPushButton


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
        self.pixmap = QPixmap.fromImage(self.image)
        self.label = QLabel(self)
        self.label.resize(500, 500)
        self.label.setPixmap(self.pixmap)
        #устанавливаем, чтобы изанчальнно не рисовали
        self.drawing = False
        #устанавливаем размер кисточки
        self.brushSize = 3
        #цвет кисточки
        self.brushColor = Qt.black
        #последняя точка
        self.currentPoint = self.lastPoint = QPoint()
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
        tpAction = QAction("Выбрать толщину", self)
        brushMenu.addAction(tpAction)
        tpAction.triggered.connect(self.tp)

        #анологично как и для выбора тощины
        whiteAction = QAction("Стерка", self)
        brushColor.addAction(whiteAction)
        whiteAction.triggered.connect(self.wColor)

        #анологично как и для 3 пикселей
        colorAction = QAction("Выбрать цвет", self)
        brushColor.addAction(colorAction)
        colorAction.triggered.connect(self.bColor)

    def mousePressEvent(self, event):
        #при нажатии на кнопку в последнию кнопку передается места где была нажата кнопка и рисование становиться True
          if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            self.currentPoint = event.pos()
            self.repaint()
            

    def mouseMoveEvent(self, event):
        #предача текущего значения местоположения курсора если мы рисуем
        if self.drawing:
            self.currentPoint = event.pos()


    def mouseReleazeEvent(self, event):
        #рисование становиться False чтобы при отпуске  кнопки линия переставала рисоваться
        if event.button() == Qt.LeftButton:
          self.drawing = False
            
    def paintEvent(self, event):
          canvaspainter = QPainter(self)
          canvaspainter.drawImage(self.rect(), self.image, self.image.rect())
          if self.drawing:
            self.drawLine()

    def drawLine(self):
        painter = QPainter(self.image)
        painter.begin(self.image)
        painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, self.currentPoint)
        self.lastPoint = self.currentPoint
        self.pixmap = QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmap)
        painter.end()
        self.update()

    def save(self):
        #сохранение путя для сохранение фото и сохранение если путь указан
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if filePath == "":
          return
        else:
          self.image.save(filePath)
    
    def open(self):
        filePath, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg)")
        if filePath == "":
          return
        else:
          self.image = QImage(filePath)
        self.pixmap = QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmap)
          
    def clear(self):
        #очищение холста и обновление экрана
        self.image.fill(Qt.white)
        self.update()

    def tp(self):
        #размер линии при рисовки будет 3 до следущего изменения
        self.brushSize = 3
        bs = BrushSize()
        bs.show()

    def bColor(self):
      #вызывается диалоговое окно, там пользователь выбирает цвет и если он выбран без ошибок устанавливается для кисточки
        col = QColorDialog.getColor()
        if col.isValid():
          self.brushColor = col

        
    def wColor(self):
        #цвет линии при рисовки будет черный до следущего изменения
        self.brushColor = Qt.white
    
    def setSize(self, value):
      self.brushize = value

    def c(self):
      return self.brushColor
    
    def s(self):
      return self.brushSize


class BrushSize(QWidget):
  def __init__(self):
    super().__init__()
    self.move(50,0)
    self.resize(50, 100)
    self.slider = QSlider(Qt.Horizontal, self)
    self.slider.setMaximum(20)
    self.slider.valueChanged[int].connect(self.changeValue)
    self.m = mw()
    self.brushSize = self.m.s()
    self.brushColor = self.m.c()
    self.btn = QPushButton(self)
    self.btn.resize(20, 20)
    self.btn.setText("Ok")
    self.btn.move(0, 75)
    self.btn.clicked.connect(self.ok)
  
  def ok(self):
    self.m.setSize(self.slider.value)
    self.hide()

  def changeValue(self, value):
    self.brushSize = value
    self.update()
  
  def paintEvent(self, e):
    painter = QPainter(self)
    painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
    painter.drawLine(0, 50, 100, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = mw()
    ex.show()
    sys.exit(app.exec())