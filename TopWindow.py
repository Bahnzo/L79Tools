# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\TopWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TopWindow(object):
    def setupUi(self, TopWindow):
        TopWindow.setObjectName("TopWindow")
        TopWindow.resize(605, 313)
        TopWindow.setMinimumSize(QtCore.QSize(605, 313))
        TopWindow.setMaximumSize(QtCore.QSize(605, 313))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        TopWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TopWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(TopWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.laps_label = QtWidgets.QLabel(self.centralwidget)
        self.laps_label.setGeometry(QtCore.QRect(10, 210, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.laps_label.setFont(font)
        self.laps_label.setObjectName("laps_label")
        self.fuel_used_last_lap_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fuel_used_last_lap_lcd.setGeometry(QtCore.QRect(10, 140, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fuel_used_last_lap_lcd.setFont(font)
        self.fuel_used_last_lap_lcd.setProperty("intValue", 0)
        self.fuel_used_last_lap_lcd.setObjectName("fuel_used_last_lap_lcd")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.race_laps = QtWidgets.QSpinBox(self.centralwidget)
        self.race_laps.setGeometry(QtCore.QRect(250, 30, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.race_laps.setFont(font)
        self.race_laps.setMaximum(200)
        self.race_laps.setObjectName("race_laps")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 10, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(380, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.fuel_needed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fuel_needed_lcd.setGeometry(QtCore.QRect(380, 30, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fuel_needed_lcd.setFont(font)
        self.fuel_needed_lcd.setObjectName("fuel_needed_lcd")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(180, 282, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(240, 282, 331, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 241, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 78, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 96, 61, 16))
        self.label_10.setObjectName("label_10")
        self.weather_type_label = QtWidgets.QLabel(self.groupBox)
        self.weather_type_label.setGeometry(QtCore.QRect(110, 20, 91, 16))
        self.weather_type_label.setText("")
        self.weather_type_label.setObjectName("weather_type_label")
        self.track_temp_label = QtWidgets.QLabel(self.groupBox)
        self.track_temp_label.setGeometry(QtCore.QRect(110, 60, 61, 16))
        self.track_temp_label.setText("")
        self.track_temp_label.setObjectName("track_temp_label")
        self.wind_dir_label = QtWidgets.QLabel(self.groupBox)
        self.wind_dir_label.setGeometry(QtCore.QRect(110, 78, 71, 16))
        self.wind_dir_label.setText("")
        self.wind_dir_label.setObjectName("wind_dir_label")
        self.wind_vel_label = QtWidgets.QLabel(self.groupBox)
        self.wind_vel_label.setGeometry(QtCore.QRect(110, 96, 61, 16))
        self.wind_vel_label.setText("")
        self.wind_vel_label.setObjectName("wind_vel_label")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(12, 42, 81, 16))
        self.label_13.setObjectName("label_13")
        self.air_temp_label = QtWidgets.QLabel(self.groupBox)
        self.air_temp_label.setGeometry(QtCore.QRect(110, 42, 61, 16))
        self.air_temp_label.setText("")
        self.air_temp_label.setObjectName("air_temp_label")
        self.avg_fuel_per_lap_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.avg_fuel_per_lap_lcd.setGeometry(QtCore.QRect(170, 140, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.avg_fuel_per_lap_lcd.setFont(font)
        self.avg_fuel_per_lap_lcd.setProperty("intValue", 0)
        self.avg_fuel_per_lap_lcd.setObjectName("avg_fuel_per_lap_lcd")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 120, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.laps_completed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.laps_completed_lcd.setGeometry(QtCore.QRect(10, 230, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.laps_completed_lcd.setFont(font)
        self.laps_completed_lcd.setProperty("intValue", 0)
        self.laps_completed_lcd.setObjectName("laps_completed_lcd")
        self.fuel_in_car_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.fuel_in_car_lcd.setGeometry(QtCore.QRect(320, 140, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.fuel_in_car_lcd.setFont(font)
        self.fuel_in_car_lcd.setProperty("intValue", 0)
        self.fuel_in_car_lcd.setObjectName("fuel_in_car_lcd")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.laps_left_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.laps_left_lcd.setGeometry(QtCore.QRect(470, 140, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.laps_left_lcd.setFont(font)
        self.laps_left_lcd.setProperty("intValue", 0)
        self.laps_left_lcd.setObjectName("laps_left_lcd")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(470, 120, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.version_label = QtWidgets.QLabel(self.centralwidget)
        self.version_label.setGeometry(QtCore.QRect(570, 0, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.version_label.setFont(font)
        self.version_label.setObjectName("version_label")
        self.time_label = QtWidgets.QLabel(self.centralwidget)
        self.time_label.setGeometry(QtCore.QRect(520, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 90, 121, 21))
        self.label_4.setObjectName("label_4")
        self.session_label = QtWidgets.QLabel(self.centralwidget)
        self.session_label.setGeometry(QtCore.QRect(370, 90, 71, 21))
        self.session_label.setText("")
        self.session_label.setObjectName("session_label")
        self.stint_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.stint_lcd.setGeometry(QtCore.QRect(468, 222, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.stint_lcd.setFont(font)
        self.stint_lcd.setProperty("intValue", 0)
        self.stint_lcd.setObjectName("stint_lcd")
        self.laps_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.laps_label_2.setGeometry(QtCore.QRect(474, 198, 97, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.laps_label_2.setFont(font)
        self.laps_label_2.setObjectName("laps_label_2")
        self.water_temp_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.water_temp_lcd.setGeometry(QtCore.QRect(336, 222, 85, 51))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.water_temp_lcd.setFont(font)
        self.water_temp_lcd.setDigitCount(3)
        self.water_temp_lcd.setProperty("intValue", 0)
        self.water_temp_lcd.setObjectName("water_temp_lcd")
        self.laps_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.laps_label_3.setGeometry(QtCore.QRect(330, 198, 97, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.laps_label_3.setFont(font)
        self.laps_label_3.setObjectName("laps_label_3")
        TopWindow.setCentralWidget(self.centralwidget)
        self.actionSettings = QtWidgets.QAction(TopWindow)
        self.actionSettings.setObjectName("actionSettings")

        self.retranslateUi(TopWindow)
        QtCore.QMetaObject.connectSlotsByName(TopWindow)

    def retranslateUi(self, TopWindow):
        _translate = QtCore.QCoreApplication.translate
        TopWindow.setWindowTitle(_translate("TopWindow", "iRacePal"))
        self.laps_label.setText(_translate("TopWindow", "Total Laps"))
        self.label_5.setText(_translate("TopWindow", "Fuel Used Last Lap"))
        self.label_6.setText(_translate("TopWindow", "Race Laps"))
        self.label_7.setText(_translate("TopWindow", "Fuel Needed"))
        self.label_8.setText(_translate("TopWindow", "Status:"))
        self.groupBox.setTitle(_translate("TopWindow", "Track Weather"))
        self.label.setText(_translate("TopWindow", "Weather Type:"))
        self.label_2.setText(_translate("TopWindow", "Track Temp:"))
        self.label_3.setText(_translate("TopWindow", "Wind Dir:"))
        self.label_10.setText(_translate("TopWindow", "Wind Vel:"))
        self.label_13.setText(_translate("TopWindow", "Air Temp"))
        self.label_9.setText(_translate("TopWindow", "Average Fuel Used"))
        self.label_11.setText(_translate("TopWindow", "Fuel Left"))
        self.label_12.setText(_translate("TopWindow", "Laps Until Empty"))
        self.version_label.setText(_translate("TopWindow", "v1.0"))
        self.time_label.setText(_translate("TopWindow", "TextLabel"))
        self.label_4.setText(_translate("TopWindow", "Session Remaining:"))
        self.laps_label_2.setText(_translate("TopWindow", "Laps in Stint"))
        self.laps_label_3.setText(_translate("TopWindow", "Water Temp"))
        self.actionSettings.setText(_translate("TopWindow", "Settings"))

