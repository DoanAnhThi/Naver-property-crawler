import sys
import json
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTableWidget, QTableWidgetItem, 
                             QLabel, QLineEdit, QComboBox, QPushButton)
from PySide6.QtCore import Qt

class NaverPropertyViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naver Property Viewer")
        self.setMinimumSize(1200, 800)
        
        # Load data
        self.load_data()
        
        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Create search and filter section
        filter_layout = QHBoxLayout()
        
        # Search box
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search properties...")
        self.search_input.textChanged.connect(self.filter_properties)
        filter_layout.addWidget(self.search_input)
        
        # Property type filter
        self.type_filter = QComboBox()
        self.type_filter.addItem("All Types")
        self.type_filter.addItems(sorted(set(item["realEstateTypeName"] for item in self.data["articleList"])))
        self.type_filter.currentTextChanged.connect(self.filter_properties)
        filter_layout.addWidget(self.type_filter)
        
        # Trade type filter
        self.trade_filter = QComboBox()
        self.trade_filter.addItem("All Trade Types")
        self.trade_filter.addItems(sorted(set(item["tradeTypeName"] for item in self.data["articleList"])))
        self.trade_filter.currentTextChanged.connect(self.filter_properties)
        filter_layout.addWidget(self.trade_filter)
        
        layout.addLayout(filter_layout)
        
        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Name", "Type", "Trade Type", "Price", "Area", 
            "Floor", "Direction", "Features"
        ])
        self.table.horizontalHeader().setStretchLastSection(True)
        layout.addWidget(self.table)
        
        # Populate table with data
        self.populate_table()
        
    def load_data(self):
        try:
            with open('naver_data.json', 'r', encoding='utf-8') as f:
                self.data = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
            self.data = {"articleList": []}
    
    def populate_table(self, filtered_data=None):
        data_to_show = filtered_data if filtered_data is not None else self.data["articleList"]
        self.table.setRowCount(len(data_to_show))
        
        for row, item in enumerate(data_to_show):
            self.table.setItem(row, 0, QTableWidgetItem(item["articleName"]))
            self.table.setItem(row, 1, QTableWidgetItem(item["realEstateTypeName"]))
            self.table.setItem(row, 2, QTableWidgetItem(item["tradeTypeName"]))

            rent_price = item.get('rentPrc', 'N/A')  # Nếu không có 'rentPrc', dùng 'N/A'
            self.table.setItem(row, 3, QTableWidgetItem(f"{item['dealOrWarrantPrc']}/{rent_price}"))

            # self.table.setItem(row, 3, QTableWidgetItem(f"{item['dealOrWarrantPrc']}/{item['rentPrc']}"))

            self.table.setItem(row, 4, QTableWidgetItem(f"{item['areaName']}㎡"))
            self.table.setItem(row, 5, QTableWidgetItem(item["floorInfo"]))
            self.table.setItem(row, 6, QTableWidgetItem(item["direction"]))
            self.table.setItem(row, 7, QTableWidgetItem(item["articleFeatureDesc"]))
    
    def filter_properties(self):
        search_text = self.search_input.text().lower()
        type_filter = self.type_filter.currentText()
        trade_filter = self.trade_filter.currentText()
        
        filtered_data = []
        for item in self.data["articleList"]:
            if (type_filter == "All Types" or item["realEstateTypeName"] == type_filter) and \
               (trade_filter == "All Trade Types" or item["tradeTypeName"] == trade_filter) and \
               (search_text in item["articleName"].lower() or \
                search_text in item["articleFeatureDesc"].lower() or \
                search_text in item["buildingName"].lower()):
                filtered_data.append(item)
        
        self.populate_table(filtered_data)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NaverPropertyViewer()
    window.show()
    sys.exit(app.exec()) 