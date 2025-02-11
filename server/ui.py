import sys
import requests
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QMessageBox, QLineEdit
from PyQt5.QtCore import Qt, QThread, pyqtSignal

SERVER_URL = "http://127.0.0.1:5000"
DB_PATH = "inventory.db"

class WorkerThread(QThread):
    response_signal = pyqtSignal(str)

    def __init__(self, endpoint, payload=None):
        super().__init__()
        self.endpoint = endpoint
        self.payload = payload
        self._is_running = True

    def run(self):
        try:
            if self.payload:
                response = requests.post(f"{SERVER_URL}/{self.endpoint}", json=self.payload)
            else:
                response = requests.get(f"{SERVER_URL}/{self.endpoint}")

            if self.response_signal and self._is_running:
                if response.status_code == 200:
                    self.response_signal.emit(response.text)
                else:
                    self.response_signal.emit(f"Error: {response.status_code}")
        except Exception as e:
            if self.response_signal and self._is_running:
                self.response_signal.emit(f"Request Failed: {str(e)}")

    def stop(self):
        """Stop the thread safely"""
        self._is_running = False
        self.quit()
        self.wait()


class InventoryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Inventory Management")
        self.setGeometry(200, 200, 400, 300)

        self.layout = QVBoxLayout()

        # Inventory Table
        self.inventory_table = QTableWidget()
        self.inventory_table.setColumnCount(2)
        self.inventory_table.setHorizontalHeaderLabels(["Item", "Quantity"])
        self.layout.addWidget(self.inventory_table)

        # Refresh Button
        self.update_button = QPushButton("Refresh Inventory")
        self.update_button.clicked.connect(self.load_inventory)
        self.layout.addWidget(self.update_button)

        # Item Name Input
        self.item_name_input = QLineEdit(self)
        self.item_name_input.setPlaceholderText("Enter item name")
        self.layout.addWidget(self.item_name_input)

        # Quantity Input
        self.quantity_input = QLineEdit(self)
        self.quantity_input.setPlaceholderText("Enter quantity")
        self.layout.addWidget(self.quantity_input)

        # Add Button
        self.add_button = QPushButton("Add Item")
        self.add_button.clicked.connect(self.add_item)
        self.layout.addWidget(self.add_button)

        # Remove Button
        self.remove_button = QPushButton("Remove Item")
        self.remove_button.clicked.connect(self.remove_item)
        self.layout.addWidget(self.remove_button)

        self.setLayout(self.layout)
        self.load_inventory()

        self.worker = None

    def load_inventory(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name, quantity FROM inventory")
        rows = cursor.fetchall()
        conn.close()

        self.inventory_table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            self.inventory_table.setItem(i, 0, QTableWidgetItem(row[0]))
            self.inventory_table.setItem(i, 1, QTableWidgetItem(str(row[1])))

    def add_item(self):
        item_name = self.item_name_input.text()
        quantity = self.quantity_input.text()

        if not item_name or not quantity.isdigit():
            QMessageBox.warning(self, "Input Error", "Please provide a valid item name and quantity.")
            return

        self.worker = WorkerThread("add-item", {"name": item_name, "quantity": int(quantity)})
        self.worker.response_signal.connect(self.handle_response)
        self.worker.start()

    def remove_item(self):
        item_name = self.item_name_input.text()

        if not item_name:
            QMessageBox.warning(self, "Input Error", "Please provide a valid item name.")
            return

        self.worker = WorkerThread("remove-item", {"name": item_name})
        self.worker.response_signal.connect(self.handle_response)
        self.worker.start()

    def handle_response(self, response):
        QMessageBox.information(self, "Server Response", response)
        self.load_inventory()

    def closeEvent(self, event):
        if self.worker is not None:
            self.worker.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryApp()
    window.show()
    sys.exit(app.exec_())
cls