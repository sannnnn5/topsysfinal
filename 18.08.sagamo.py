import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog,
    QSizePolicy, QHeaderView, QScrollArea
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class InputTableApp(QWidget):
    def __init__(self, rows, cols):
        super().__init__()
        
        self.rows = rows
        self.cols = cols
        self.result_window = None  # Reference to the result window

        # Set font for Georgian characters
        self.font = QFont("Sylfaen", 10)

        self.initUI()

    def initUI(self):
        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Create a widget to hold all content
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)

        # Add the "Interest Distribution" label at the top of the layout
        distribution_layout = QHBoxLayout()
        distribution_label = QLabel("Preferences and Percentages: ", self)
        distribution_label.setFont(self.font)
        distribution_layout.addWidget(distribution_label)
        distribution_layout.addStretch()  # Add a stretch to push the label to the left
        layout.addLayout(distribution_layout)

        # Interest Distribution and Preference stacked layout
        stacked_layout = QHBoxLayout()

        # Add an empty widget to align with the first header
        empty_widget = QWidget()
        empty_widget.setFixedWidth(220)
        stacked_layout.addWidget(empty_widget)

        # Calculate initial percentage
        initial_percentage = 100 / (self.cols - 1)

        # Stacked Percentage and Preference layouts
        self.percentage_entries = []
        self.preference_selectors = []
        for i in range(self.cols - 1):
            stacked_column = QVBoxLayout()

            # Preference selector
            combo = QComboBox(self)
            combo.setFont(self.font)
            combo.setFixedWidth(220)
            combo.addItems(["<", ">"])
            stacked_column.addWidget(combo)
            self.preference_selectors.append(combo)

            # Percentage entry
            entry = QLineEdit(self)
            entry.setFont(self.font)
            entry.setText(f"{initial_percentage:.10f}")  # Set the initial percentage
            entry.setFixedWidth(220)
            stacked_column.addWidget(entry)
            self.percentage_entries.append(entry)

            stacked_layout.addLayout(stacked_column)

        layout.addLayout(stacked_layout)

        # Header entries
        self.header_entries = []
        header_layout = QHBoxLayout()
        for i in range(self.cols):
            entry = QLineEdit(self)
            entry.setFont(self.font)
            entry.setFixedWidth(220)
            header_layout.addWidget(entry)
            self.header_entries.append(entry)

        layout.addLayout(header_layout)

        # Data entries
        self.table = QTableWidget(self.rows, self.cols, self)
        self.table.setFont(self.font)

        # Set all column widths to be equal and fixed
        for col in range(self.cols):
            self.table.setColumnWidth(col, 220)

        layout.addWidget(self.table)

        # Process Button
        process_button = QPushButton("Process Data", self)
        process_button.setFont(self.font)
        process_button.clicked.connect(self.process_data)
        layout.addWidget(process_button)

        # Set the content widget to the scroll area
        scroll_area.setWidget(content_widget)

        # Set the scroll area as the central widget of the main window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)
        self.setWindowTitle('Data Analysis')

        # Set a minimum size for the window, but allow it to be resized
        min_width = max(220 * min(self.cols, 6), 1300)  # Show at least 6 columns or 1300 wide
        self.setMinimumSize(min_width, 600)


    def process_data(self):
        try:
            # Get percentages, preferences, and headers
            percentages = [float(entry.text()) for entry in self.percentage_entries]

            # Adjust the percentages so that the total is 100
            total_percentage = sum(percentages)
            
            # Define a small tolerance for floating-point arithmetic errors
            tolerance = 1e-9

            if total_percentage > 100 + tolerance:
                QMessageBox.critical(self, "Error", "The sum of interest distributions cannot exceed 100.")
                return

            # Distribute any remaining percentage equally across all columns
            if total_percentage < 100:
                remaining_percentage = 100 - total_percentage
                equal_distribution = remaining_percentage / (self.cols - 1)
                for i in range(len(percentages)):
                    percentages[i] += equal_distribution

            # Update the percentage entries to reflect the adjusted values
            for i, entry in enumerate(self.percentage_entries):
                entry.setText(f"{percentages[i]:.10f}")  # Adjust the precision as needed

            # Get preferences and headers
            preferences = ["None"] + [combo.currentText() for combo in self.preference_selectors]
            headers = [entry.text() for entry in self.header_entries]

            # Get table data
            values = []
            for row in range(self.table.rowCount()):
                row_data = []
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item:
                        row_data.append(item.text().replace(",", "."))  # Replacing comma with dot for float conversion
                    else:
                        row_data.append("")
                values.append(row_data)

            # Convert data to dictionary format
            data = {headers[i]: [row[i] for row in values] for i in range(len(headers))}

            # Process data
            results = self.analyze_data(data, preferences, percentages)

            # Display results
            self.display_results(results, headers, data)
        except Exception as e:
            QMessageBox.critical(self, "Processing Error", str(e))

    def analyze_data(self, data, preferences, percentages):
        print(percentages)
        try:
            # Perform all steps of the analysis
            data1 = self.calculate_main(data)
            calc_o = self.calculate_input(data1, percentages)
            shed_mi, shed_mx = self.shed(calc_o, preferences)
            st_b = self.step4bed(calc_o, shed_mx)
            st_g = self.step4good(calc_o, shed_mi)
            sorted_results = self.final_calculation(st_g, st_b)
            return sorted_results
        except Exception as e:
            raise ValueError(f"Error during data analysis: {e}")

    def calculate_main(self, data):
        attributes = list(data.keys())[1:]  # Skip the first column, which is typically the main identifier
        results = []
        for attr in attributes:
            attribute_sum = sum(float(val) for val in data[attr])
            result = {car: float(value) / (attribute_sum * 2) * 0.5
                      for car, value in zip(data[list(data.keys())[0]], data[attr])}
            results.append(result)
        return tuple(results)

    def calculate_input(self, ddt, prcnt):
        ddol = []
        for i, e in zip(ddt, prcnt):
            ddo = {}
            for f, z in zip(i.values(), i.keys()):
                ssx = (f * e) / 100
                ddo[z] = ssx
            ddol.append(ddo)
        return ddol

    def shed(self, ddol, preference):
        minsc = []
        maxsc = []
        for i in ddol:
            minsc.append(min(i.values()))
            maxsc.append(max(i.values()))

        ggdrs = []
        bbdrs = []
        for i, (min_val, max_val) in enumerate(zip(minsc, maxsc)):
            if preference[i + 1] == "<":
                ggdrs.append(min_val)
                bbdrs.append(max_val)
            else:
                ggdrs.append(max_val)
                bbdrs.append(min_val)
        return ggdrs, bbdrs

    def step4bed(self, data, bed_results):
        snqs = {}
        for i, b in zip(data, bed_results):
            for z in i:
                n = abs((i[z] - b) * 2)
                if z in snqs:
                    snqs[z] += n
                else:
                    snqs[z] = n * 0.5
        return snqs

    def step4good(self, data, good_results):
        snqs = {}
        for i, b in zip(data, good_results):
            for z in i:
                n = abs((i[z] - b) * 2)
                if z in snqs:
                    snqs[z] += n
                else:
                    snqs[z] = n * 0.5
        return snqs

    def final_calculation(self, min_num, max_num):
        fin = {}
        for key in min_num.keys():
            fin[key] = max_num[key] / (max_num[key] + min_num[key])
        sorted_values_desc = sorted(fin.items(), key=lambda x: x[1], reverse=True)
        return sorted_values_desc

    def display_results(self, sorted_results, headers, data):
        if self.result_window is not None:
            self.result_window.close()  # Close any previous result window

        self.result_window = QWidget()
        self.result_window.setWindowTitle("Sorted Results")

        layout = QVBoxLayout()

        table = QTableWidget(len(sorted_results), len(headers) + 1)
        table.setFont(self.font)
        table.setHorizontalHeaderLabels(headers + ["Score"])

        for idx, (model, score) in enumerate(sorted_results):
            table.setItem(idx, 0, QTableWidgetItem(model))
            for j, header in enumerate(headers[1:], start=1):
                table.setItem(idx, j, QTableWidgetItem(str(data[header][data[headers[0]].index(model)])))
            table.setItem(idx, len(headers), QTableWidgetItem(str(round(score, 4))))

        layout.addWidget(table)
        self.result_window.setLayout(layout)
        self.result_window.resize(900, 800)
        self.result_window.show()


def setup_app():
    app = QApplication(sys.argv)
    num_rows, ok_rows = QInputDialog.getInt(None, "Setup Rows", "Enter number of rows:")
    if ok_rows:
        num_cols, ok_cols = QInputDialog.getInt(None, "Setup Columns", "Enter number of columns:")
        if ok_cols:
            ex = InputTableApp(num_rows, num_cols)
            ex.show()
            sys.exit(app.exec_())


if __name__ == '__main__':
    setup_app()
