import sys
import subprocess
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLabel
)
from PySide6.QtCore import Qt

class PropertyViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naver Property Data Viewer")
        self.resize(800, 600)

        self.status_label = QLabel("")
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(0)

        btn_fetch = QPushButton("Tải dữ liệu mới (Crawler)")
        btn_fetch.clicked.connect(self.fetch_data)

        btn_open = QPushButton("Mở file JSON")
        btn_open.clicked.connect(self.open_json)

        layout = QVBoxLayout()
        layout.addWidget(btn_fetch)
        layout.addWidget(btn_open)
        layout.addWidget(self.table)
        layout.addWidget(self.status_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def fetch_data(self):
        try:
            result = subprocess.run([sys.executable, 'naver-newer-crawler.py'], capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                self.status_label.setText("Đã tải dữ liệu mới thành công!")
            else:
                self.status_label.setText(f"Lỗi khi tải dữ liệu: {result.stderr}")
        except Exception as e:
            self.status_label.setText(f"Lỗi: {e}")

    def open_json(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Chọn file JSON", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.show_data(data)
                self.status_label.setText(f"Đã mở file: {file_path}")
            except Exception as e:
                self.status_label.setText(f"Lỗi khi đọc file: {e}")

    def show_data(self, data):
        items = data.get('data', [])
        if not items:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.table.setHorizontalHeaderLabels([])
            return
        # Lấy các keys của item đầu tiên làm header
        headers = list(items[0].keys())
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)
        self.table.setRowCount(len(items))
        for row, item in enumerate(items):
            for col, key in enumerate(headers):
                value = str(item.get(key, ""))
                self.table.setItem(row, col, QTableWidgetItem(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PropertyViewer()
    window.show()
    sys.exit(app.exec()) 