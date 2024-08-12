import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtGui import QFont

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
        layout = QVBoxLayout()

        # Interest Distribution
        distribution_layout = QHBoxLayout()
        distribution_label = QLabel("Interest Distribution:", self)
        distribution_label.setFont(self.font)
        distribution_layout.addWidget(distribution_label)

        self.percentage_entries = []
        for i in range(self.cols - 1):  # Adjusting for the dynamic number of columns
            entry = QLineEdit(self)
            entry.setFont(self.font)
            entry.setText("20")
            entry.setFixedWidth(40)
            distribution_layout.addWidget(entry)
            self.percentage_entries.append(entry)

        layout.addLayout(distribution_layout)

        # Preference selectors
        self.preference_selectors = []
        preference_layout = QHBoxLayout()
        preference_layout.addWidget(QLabel("", self))
        for i in range(self.cols - 1):
            combo = QComboBox(self)
            combo.setFont(self.font)
            combo.addItems(["<", ">"])
            preference_layout.addWidget(combo)
            self.preference_selectors.append(combo)
        layout.addLayout(preference_layout)

        # Header entries
        self.header_entries = []
        header_layout = QHBoxLayout()
        for i in range(self.cols):
            entry = QLineEdit(self)
            entry.setFont(self.font)
            header_layout.addWidget(entry)
            self.header_entries.append(entry)
        layout.addLayout(header_layout)

        # Data entries
        self.table = QTableWidget(self.rows, self.cols, self)
        self.table.setFont(self.font)
        self.table.setFixedWidth(1300)
        self.table.setColumnWidth(0, 175)
        for col in range(1, self.cols):
            self.table.setColumnWidth(col, 220)
        self.table.verticalHeader().setDefaultSectionSize(40)
        layout.addWidget(self.table)

        # Process Button
        process_button = QPushButton("Process Data", self)
        process_button.setFont(self.font)
        process_button.clicked.connect(self.process_data)
        layout.addWidget(process_button)

        self.setLayout(layout)
        self.setWindowTitle('Data Analysis')
        self.resize(1300, 800)

    def process_data(self):
        percentages = [entry.text() for entry in self.percentage_entries]
        preferences = ["None"] + [combo.currentText() for combo in self.preference_selectors]
        headers = [entry.text() for entry in self.header_entries]

        values = []
        for row in range(self.table.rowCount()):
            row_data = []
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item:
                    row_data.append(item.text().replace(",", "."))  # Replacing comma with dot
                else:
                    row_data.append("")
            values.append(row_data)

        total_percentage = sum(float(p) for p in percentages)
        if total_percentage > 100:
            QMessageBox.critical(self, "Error", "The sum of interest distributions cannot exceed 100.")
            return

        data = {headers[i]: [row[i] for row in values] for i in range(len(headers))}
        
        try:
            results, cp, cr, cpp, c1, t = all_a(data, preferences, percentages)
            self.display_results(results, headers, data)
        except Exception as e:
            QMessageBox.critical(self, "Processing Error", str(e))

    def display_results(self, sorted_results, headers, data):
        if self.result_window is not None:
            self.result_window.close()  # Close any previous result window

        self.result_window = QWidget()
        self.result_window.setWindowTitle("Sorted Results")

        layout = QVBoxLayout()

        table = QTableWidget(len(sorted_results), len(headers) + 1)
        table.setFont(self.font)
        table.setHorizontalHeaderLabels(headers + ["Score"])

        for idx, (model, score) in enumerate(sorted_results, start=1):
            table.setItem(idx - 1, 0, QTableWidgetItem(model))
            for j, header in enumerate(headers[1:], start=1):
                table.setItem(idx - 1, j, QTableWidgetItem(str(data[header][data[headers[0]].index(model)])))
            table.setItem(idx - 1, len(headers), QTableWidgetItem(str(round(score, 4))))

        layout.addWidget(table)
        self.result_window.setLayout(layout)
        self.result_window.resize(900, 800)
        self.result_window.show()

def all_a(data, preferences, percentages):
    car_data = data
    param_dicts = calculate_parameters(car_data)
    weighted_params = weight_inputs(percentages, param_dicts)
    qm, qx = shed(weighted_params, preferences)
    bad_scores = calculate_scores(qx, weighted_params)
    good_scores = calculate_scores(qm, weighted_params)
    final_scores = fin_num(good_scores, bad_scores)
    return final_scores, *weighted_params

def calculate_parameters(data):
    params = [dict() for _ in range(len(data.keys()) - 1)]
    sums = [sum(map(float, data[list(data.keys())[i+1]])) for i in range(len(params))]
    
    for i, param_dict in enumerate(params):
        for model, value in zip(data[list(data.keys())[0]], data[list(data.keys())[i+1]]):
            param_dict[model] = float(value) / (sums[i] * 2) * 0.5

    return params

def weight_inputs(percentages, param_dicts):
    return [{k: (v * float(percentages[i])) / 100 for k, v in param.items()} for i, param in enumerate(param_dicts)]

def shed(weighted_params, preferences):
    q_min = {f"param_{i}": min(param.values()) for i, param in enumerate(weighted_params)}
    q_max = {f"param_{i}": max(param.values()) for i, param in enumerate(weighted_params)}

    qx = {}
    qm = {}
    for i, pref in enumerate(preferences[1:]):
        if pref == "<":
            qx[f"param_{i}"] = q_min[f"param_{i}"]
        elif pref == ">":
            qx[f"param_{i}"] = q_max[f"param_{i}"]
        qm[f"param_{i}"] = sum(weighted_params[i].values()) / len(weighted_params[i])

    return qm, qx

def calculate_scores(reference, weighted_params):
    return {model: sum(abs(param[model] - reference[f"param_{i}"]) for i, param in enumerate(weighted_params)) for model in weighted_params[0].keys()}

def fin_num(good_scores, bad_scores):
    return sorted({model: good_scores[model] - bad_scores[model] for model in good_scores}.items(), key=lambda x: x[1], reverse=True)

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
