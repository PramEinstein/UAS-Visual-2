import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('nilai.ui', self)
        self.setWindowTitle('PYTHON GUI TABLEWIDGET')

        try:
            self.mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="db_mahasiswa"
            )
            self.cursor = self.mydb.cursor()
        except mc.Error as err:
            self.showMessage("Koneksi Gagal", "Tidak dapat terhubung ke database!")
            sys.exit(1)

        self.pushButton.clicked.connect(self.insertnilai)
        self.pushButton_2.clicked.connect(self.updatenilai)
        self.pushButton_3.clicked.connect(self.deletenilai)
        self.pushButton_4.clicked.connect(self.batal)
        self.tableWidget.cellClicked.connect(self.isiFormDariTabel)
        self.sqlLoad()

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec()

    def sqlLoad(self):
        try:
            self.cursor.execute("SELECT * FROM nilai ORDER BY id ASC")
            result = self.cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as err:
            self.showMessage("Error", "Gagal menampilkan data!")

    def insertnilai(self):
        try:
            val = (
                self.lineEdit.text(),
                self.lineEdit_2.text(),
                self.lineEdit_3.text(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text(),
                self.lineEdit_6.text()
            )
            sql = "INSERT INTO nilai (id, id_mahasiswa, nilai_harian, nilai_tugas, nilai_uts, nilai_uas) VALUES (%s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, val)
            self.mydb.commit()

            self.showMessage("Berhasil", "Data nilai berhasil disimpan.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal menyimpan data nilai!")

    def updatenilai(self):
        try:
            val = (
                self.lineEdit_2.text(),
                self.lineEdit_3.text(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text(),
                self.lineEdit_6.text(),
                self.lineEdit.text()
            )
            sql = "UPDATE nilai SET id_mahasiswa = %s, nilai_harian = %s, nilai_tugas = %s, nilai_uts = %s, nilai_uas = %s WHERE id = %s"
            self.cursor.execute(sql, val)
            self.mydb.commit()

            self.showMessage("Berhasil", "Data nilai berhasil diupdate.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal update data nilai!")

    def deletenilai(self):
        try:
            id_mahasiswa = self.lineEdit.text()
            sql = "DELETE FROM nilai WHERE id_mahasiswa = %s"
            self.cursor.execute(sql, (id_mahasiswa,))
            self.mydb.commit()

            self.showMessage("Berhasil", "Data nilai berhasil dihapus.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal menghapus data nilai!")

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()

    def isiFormDariTabel(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())  
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())  
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())  
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())  
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text()) 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())
