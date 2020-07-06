import sys
import csv
import time
from datetime import datetime
import os
import multiprocessing as mlp
from main_window import Ui_MainWindow
from PySide2 import QtCore, QtWidgets


class Obj(QtCore.QObject):
    progress = QtCore.Signal(int)
    row = QtCore.Signal(int, int, list)
    head = QtCore.Signal(int)


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWin, self).__init__()
        self.setupUi(self)
        self.check = False
        self.button.setEnabled(False)
        self.login.setEnabled(False)
        self.time.setEnabled(False)
        self.login.toggled.connect(self.rdr_toggle)
        self.time.toggled.connect(self.rdr_toggle)
        self.anal_btn.clicked.connect(self.parsing)
        self.button.clicked.connect(self.main_click)
        self.save_btn.clicked.connect(self.save)
        self.save_btn.setEnabled(False)
        self.my_pool = mlp.Pool(1)
        self.obj = Obj()
        self.obj.progress.connect(self.progressBar.setValue)
        self.obj.row.connect(self.table_row)
        self.obj.head.connect(self.table_head)
        self.directory_btn.clicked.connect(self.get_directory)

    def get_directory(self) -> None:
        self.anal_btn.setEnabled(True)
        self.button.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.login.setEnabled(False)
        self.time.setEnabled(False)
        self.anal_btn.setText('Проверить папку')
        dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Выберите папку')
        self.path_txt.setText(dir)

    def work_with_data(self, logs) -> None:
        lim_1 = 0
        lim_2 = 99
        id = self.elems_cmb.currentIndex()
        count_box = self.elems_cmb.count()
        for i in range(count_box):
            if id == i:
                lim_1 = i * 100
                lim_2 = (i + 1) * 100 - 1
        mod = len(logs) % 100
        count_id = len(logs) - mod
        count_id = int(count_id / 100)
        self.table_head(logs[0])
        value = 10
        self.table.setRowCount(0)
        for i, row in enumerate(logs[1:]):
            value += 1
            self.obj.progress.emit(value)
            if lim_1 <= i <= lim_2:
                self.obj.row.emit(i, lim_1, row)

        if count_box > 1:
            self.elems_cmb.clear()
            self.elems_cmb.setCurrentIndex(0)
        for i in range(1, count_id):
            self.elems_cmb.addItem(f"{i} - ая ")
        self.elems_cmb.addItem("Последняя")
        if self.anal_btn.text() == 'Перейти на страницу':
            self.elems_cmb.setCurrentIndex(id)
        else:
            self.elems_cmb.setCurrentIndex(0)
        self.obj.progress.emit(value + 1)
        self.obj.progress.emit(0)
        self.save_array = list.copy(logs)
        self.check = True
        self.anal_btn.setText('Перейти на страницу')
        self.anal_btn.setEnabled(True)
        self.login.setEnabled(True)
        self.time.setEnabled(True)
        self.save_btn.setEnabled(True)
        if self.login.isChecked():
            self.button.setEnabled(True)
        elif self.time.isChecked():
            self.button.setEnabled(True)


    def rdr_toggle(self) -> None:
        self.info_txt.setText('')
        self.info_txt.setEnabled(False)
        self.dateTimeEdit.setEnabled(False)
        self.label_4.setText('')
        self.label_5.setText('')
        if self.login.isChecked():
            self.label_4.setText('Введите логин:')
            self.info_txt.setText('')
            self.info_txt.setEnabled(True)
            self.button.setText('Сортировать')
        if self.time.isChecked():
            self.label_5.setText('Введите время:')
            self.dateTimeEdit.setEnabled(True)
            self.button.setText('Сортировать')
        self.button.setEnabled(True)

    def main_click(self) -> None:
        self.button.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.anal_btn.setEnabled(False)
        self.anal_btn.setText('Прверить папку')
        if self.login.isChecked():
            login = self.info_txt.toPlainText()
            if login == '':
                self.massage_box('Введите логин!')
            else:
                self.sort_by_login(login)
        elif self.time.isChecked():
            date = self.dateTimeEdit.text()
            self.sort_by_date(date)
        self.button.setEnabled(True)
        self.save_btn.setEnabled(True)
        self.anal_btn.setEnabled(True)
        self.login.setChecked(False)
        self.time.setChecked(False)
        self.progressBar.setValue(0)

    def elems_manage(self, logs: []) -> None:
        id = self.elems_cmb.currentIndex()
        count_box = self.elems_cmb.count()
        lim_1 = id * 100
        lim_2 = (id + 1) * 100 - 1
        mod = len(logs) % 100
        count_id = len(logs) - mod
        count_id = int(count_id / 100)
        value = 0
        for i in range(len(logs)):
            value += 0.5
            self.obj.progress.emit(value)
            if lim_1 <= i <= lim_2:
                self.obj.row.emit(i, lim_1, logs[i])

        if count_box > 1:
            self.elems_cmb.clear()
            self.elems_cmb.addItem("1 - ая")
            self.elems_cmb.setCurrentIndex(0)
        for i in range(1, count_id):
            self.elems_cmb.addItem(f"{i} - ая ")
        if mod > 0 and len(logs) > 0:
            self.elems_cmb.addItem("Последняя")
        self.elems_cmb.setCurrentIndex(0)

    def sort_by_login(self, login: str) -> None:
        if self.check:
            clear = []
            self.table.setRowCount(0)
            self.table_head(self.save_array[0])
            value = 0
            for i in range(1, len(self.save_array)):
                value += 1
                log = self.save_array[i]
                self.obj.progress.emit(value)
                if login in log:
                    clear.append(log)
            if len(clear) > 0:
                self.elems_manage(clear)
                self.obj.progress.emit(100)
            else:
                self.massage_box('Такого логина не существует')
                self.obj.progress.emit(0)
                self.button.setText('Сортировать')
        else:
            self.massage_box('Нужно проверить папку')

    def sort_by_date(self, date: str) -> None:
        if self.check:
            norm_time = datetime.strptime(date, '%d.%m.%Y %H:%M:%S')
            unix_time = int(time.mktime(norm_time.timetuple()))
            unix_time = str(unix_time)
            self.table.setRowCount(0)
            self.table_head(self.save_array[0])
            clear = []
            value = 0
            for i in range(1, len(self.save_array)):
                row = self.save_array[i]
                value += 1
                self.obj.progress.emit(value)
                if unix_time == row[0]:
                    clear.append(row)

            if len(clear) > 0:
                self.elems_manage(clear)
                self.obj.progress.emit(100)
            else:
                self.massage_box('Такой даты не существует')
                self.button.setText('Сортировать')
                self.obj.progress.emit(0)
        else:
            self.massage_box('Нужно проверить папку')

    def save(self) -> None:
        head = ['begin', 'end', 'time interval', 'login', 'mac ab', 'ULSK1', 'BRAS ip', 'start count', 'alive count',
                'stop count', 'incoming', 'outcoming', 'error_count', 'code 0', 'code 1011', 'code 1100', 'code -3',
                'code -52', 'code -42', 'code -21', 'code -40', ' code -44', 'code -46', ' code -38']
        rowCount = self.table.rowCount()
        columCount = len(head)
        d = QtWidgets.QFileDialog.getSaveFileName(self, "Выберите куда сохранить", "/data", "*.csv")
        if d[0] == '':
            self.massage_box('Вы отменили сохранение')
            return 1
        value = 0
        with open(d[0], 'w', newline='') as file_csv:
            writer = csv.writer(file_csv)
            writer.writerow(head)
            for i in range(rowCount):
                save = []
                value += 1
                self.obj.progress.emit(value)
                for j in range(columCount):
                    p = self.table.item(i, j).text()
                    save.append(p)
                writer.writerow(save)
        self.obj.progress.emit(value + 1)
        self.obj.progress.emit(0)

    def table_row(self, i, miim, row) -> None:
        self.table.insertRow(self.table.rowCount())
        for j in range(len(row)):
            self.table.setItem((i - miim), j, QtWidgets.QTableWidgetItem(row[j]))

    def table_head(self, row) -> None:
        self.table.setColumnCount(len(row))
        self.table.setHorizontalHeaderLabels(row)

    def parsing(self) -> None:
        self.anal_btn.setEnabled(False)
        self.button.setEnabled(False)
        self.save_btn.setEnabled(False)
        self.login.setEnabled(False)
        self.time.setEnabled(False)
        self.button.setText('Сортировать')
        path_file = self.path_txt.toPlainText()
        if os.path.exists(path_file) is False:
            self.massage_box('Введите путь')
            self.path_txt.setText('')
            return
        list_dir = os.listdir(path_file)
        csv_files = []
        for i in range(len(list_dir)):
            get_path = os.path.join(path_file, list_dir[i])
            chek = os.path.isfile(get_path)
            if chek:
                sp_file = list_dir[i].split('.')
                if sp_file[-1] == 'csv':
                    csv_files.append(get_path)

        if len(csv_files) == 0:
            self.massage_box('В данной папке нет csv файлов')
        else:
            self.my_pool.apply_async(func=work_with_dir, args=(csv_files,), callback=self.work_with_data)
            self.progressBar.setValue(5)

    def massage_box(self, error: str) -> None:
        QtWidgets.QMessageBox.warning(self, 'Внимание', f'{error}', QtWidgets.QMessageBox.Ok)


def work_with_dir(csv_files) -> []:
    all_data = []
    for i in range(len(csv_files)):
        with open(csv_files[i], 'r')as csv_file:
            reader = csv.reader(csv_file)  # reader - список списсков
            data = list(reader)
        all_data.append(data)
    solo_data = list.copy(all_data[0])
    for i in range(1, len(all_data)):
        all_data[i].remove(all_data[i][0])
        solo_data += all_data[i]
    return solo_data


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())
