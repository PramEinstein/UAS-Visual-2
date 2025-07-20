import sys
import mysql.connector as mc
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi

class HalloPython(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi('mahasiswa.ui', self)
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

        self.pushButton.clicked.connect(self.insertmahasiswa)
        self.pushButton_2.clicked.connect(self.updatemahasiswa)
        self.pushButton_3.clicked.connect(self.deletemahasiswa)
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
            self.cursor.execute("SELECT * FROM mahasiswa ORDER BY npm ASC")
            result = self.cursor.fetchall()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        except mc.Error as err:
            self.showMessage("Error", "Gagal menampilkan data!")

    def insertmahasiswa(self):
        try:
            val = (
                self.lineEdit.text(),
                self.lineEdit_2.text(),
                self.lineEdit_3.text(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text(),
                self.lineEdit_6.text(),
                self.lineEdit_7.text(),
                self.lineEdit_8.text()
            )
            sql = "INSERT INTO mahasiswa (npm, nama_lengkap, nama_panggilan, telepon, email, kelas, matakuliah, lokasi_kampus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.cursor.execute(sql, val)
            self.mydb.commit()

            self.showMessage("Berhasil", "Data mahasiswa berhasil disimpan.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal menyimpan data mahasiswa!")

    def updatemahasiswa(self):
        try:
            val = (
                self.lineEdit_2.text(),
                self.lineEdit_3.text(),
                self.lineEdit_4.text(),
                self.lineEdit_5.text(),
                self.lineEdit_6.text(),
                self.lineEdit_7.text(),
                self.lineEdit_8.text(),
                self.lineEdit.text()
            )
            sql = "UPDATE mahasiswa SET nama_lengkap = %s, nama_panggilan = %s, telepon = %s, email = %s, kelas = %s, matakuliah = %s, lokasi_kampus = %s WHERE npm = %s"
            self.cursor.execute(sql, val)
            self.mydb.commit()

            self.showMessage("Berhasil", "Data mahasiswa berhasil diupdate.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal update data mahasiswa!")

    def deletemahasiswa(self):
        try:
            npm = self.lineEdit.text()
            sql = "DELETE FROM mahasiswa WHERE npm = %s"
            self.cursor.execute(sql, (npm,))
            self.mydb.commit()

            self.showMessage("Berhasil", "Data mahasiswa berhasil dihapus.")
            self.batal()
            self.sqlLoad()
        except mc.Error as err:
            self.showMessage("Gagal", "Gagal menghapus data mahasiswa!")

    def batal(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        self.lineEdit_5.clear()
        self.lineEdit_6.clear()
        self.lineEdit_7.clear()
        self.lineEdit_8.clear()

    def isiFormDariTabel(self, row, column):
        self.lineEdit.setText(self.tableWidget.item(row, 0).text())  
        self.lineEdit_2.setText(self.tableWidget.item(row, 1).text())  
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())  
        self.lineEdit_4.setText(self.tableWidget.item(row, 3).text())  
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())  
        self.lineEdit_6.setText(self.tableWidget.item(row, 5).text())  
        self.lineEdit_7.setText(self.tableWidget.item(row, 6).text())  
        self.lineEdit_8.setText(self.tableWidget.item(row, 7).text())  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = HalloPython()
    form.show()
    sys.exit(app.exec_())
