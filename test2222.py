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
        for i in range(self.cols - 1):
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
        # Set the width of the table and its columns
        self.table.setFixedWidth(1300)
        self.table.setColumnWidth(0, 175)  # Adjust as needed
        for col in range(1, self.cols):
            self.table.setColumnWidth(col, 220)  # Adjust as needed
        # Set the height of the rows above the table
        self.table.verticalHeader().setDefaultSectionSize(40)  # Adjust as needed
        layout.addWidget(self.table)

        # Process Button
        process_button = QPushButton("Process Data", self)
        process_button.setFont(self.font)
        process_button.clicked.connect(self.process_data)
        layout.addWidget(process_button)

        self.setLayout(layout)
        self.setWindowTitle('data analysis')
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
        print(f"display_result :\n self = {self} \n sorted_results = {sorted_results} \n headers = {headers} \n data = {data}\n")
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

    car_price, car_range, car_power, car_100, car_top_spd = main(car_data)

    cp_p, cr_p, cpp_p, c1_p, t_p = wight_inp(percentages)

    cp, cr, cpp, c1, t = calculate_input(cp_p, cr_p, cpp_p, c1_p, t_p, car_price, car_range, car_power, car_100, car_top_spd)

    qm, qx = shed(cp, cr, cpp, c1, t, preferences)

    bed = step4bad(qx, cp, cr, cpp, c1, t)

    good = step4good(qm, cp, cr, cpp, c1, t)

    fin = fin_num(good, bed)

    return fin, cp, cr, cpp, c1, t

def main(data):
    print(f"main:\n data = {data}\n")
    car_price = {}
    car_range = {}
    car_power = {}
    car_100 = {}
    car_top_spd = {}

    prc_sum = sum(map(float, data[list(data.keys())[1]]))
    for car, coast in zip(data[list(data.keys())[0]], data[list(data.keys())[1]]):
        car_price[car] = float(coast) / (prc_sum * 2) * 0.5

    range_sum = sum(map(float, data[list(data.keys())[2]]))
    for car, range in zip(data[list(data.keys())[0]], data[list(data.keys())[2]]):
        car_range[car] = float(range) / (range_sum * 2) * 0.5

    power_sum = sum(map(float, data[list(data.keys())[3]]))
    for car, power in zip(data[list(data.keys())[0]], data[list(data.keys())[3]]):
        car_power[car] = float(power) / (power_sum * 2) * 0.5

    to_100_sum = sum(map(float, data[list(data.keys())[4]]))
    for car, c100 in zip(data[list(data.keys())[0]], data[list(data.keys())[4]]):
        car_100[car] = float(c100) / (to_100_sum * 2) * 0.5

    top_speed_sum = sum(map(float, data[list(data.keys())[5]]))
    for car, top_spd in zip(data[list(data.keys())[0]], data[list(data.keys())[5]]):
        car_top_spd[car] = float(top_spd) / (top_speed_sum * 2) * 0.5

    return car_price, car_range, car_power, car_100, car_top_spd

def wight_inp(percentages):
    print(f" wight_inp:\n percentages = {percentages}\n")
    return tuple(float(p) for p in percentages)

def calculate_input(cp_p, cr_p, cpp_p, c1_p, t_p, car_price, car_range, car_power, car_100, car_top_spd):
    print(f"calculate_input :\n cp_p = {cp_p} \n cr_p = {cr_p} \n cpp_p = {cpp_p} \n c1_p = {c1_p} \n t_p = {t_p} \n car_price = {car_price} \n car_range = {car_range} \n car_power = {car_power} \n car_100 = {car_100} \n car_top = {car_top_spd}\n")
    cp = {k: (v * cp_p) / 100 for k, v in car_price.items()}
    cr = {k: (v * cr_p) / 100 for k, v in car_range.items()}
    cpp = {k: (v * cpp_p) / 100 for k, v in car_power.items()}
    c1 = {k: (v * c1_p) / 100 for k, v in car_100.items()}
    t = {k: (v * t_p) / 100 for k, v in car_top_spd.items()}
    return cp, cr, cpp, c1, t

def shed(cp, cr, cpp, c1, t, preferences):
    print(f"shed :\n cp = {cp} \n cr = {cr} \n cpp = {cpp} \n c1 = {c1} \n t = {t} \n preferences = {preferences}\n")
    q_min = {
        "price": min(cp.values()),
        "range": min(cr.values()),
        "power": min(cpp.values()),
        "acceleration": min(c1.values()),
        "speed": min(t.values())
    }

    q_max = {
        "price": max(cp.values()),
        "range": max(cr.values()),
        "power": max(cpp.values()),
        "acceleration": max(c1.values()),
        "speed": max(t.values())
    }

    bed_result = {}
    good_res = {}

    preference_map = {
        "price": preferences[1],
        "range": preferences[2],
        "power": preferences[3],
        "acceleration": preferences[4],
        "speed": preferences[5]
    }

    for key, value in preference_map.items():
        if value == "<":
            good_res[key] = q_min[key]
            bed_result[key] = q_max[key]
        elif value == ">":
            good_res[key] = q_max[key]
            bed_result[key] = q_min[key]

    return good_res, bed_result

def step4bad(bed_result, car_price, car_range, car_power, car_100, car_top_spd):
    print(f"step4bed \n badres = {bed_result} \n car_price = {car_price} \n car_range = {car_range} \n car_power {car_power} \n car_100 = {car_100} \n car_top = {car_top_spd}\n")
    cars = {}
    for pr in car_price:
        all_sum = 0
        if car_price[pr] > bed_result["price"]:
            all_sum = ((car_price[pr] - bed_result["price"]) * 2)   
        else:
            all_sum = ((bed_result["price"] - car_price[pr]) * 2)

        if car_range[pr] > bed_result["range"]:
            all_sum += ((car_range[pr] - bed_result["range"]) * 2)
        else:
            all_sum += ((bed_result["range"] - car_range[pr]) * 2)

        if car_power[pr] > bed_result["power"]:
            all_sum += ((car_power[pr] - bed_result["power"]) * 2)
        else:
            all_sum += ((bed_result["power"] - car_power[pr]) * 2)

        if car_100[pr] > bed_result["acceleration"]:
            all_sum += ((car_100[pr] - bed_result["acceleration"]) * 2)
        else:
            all_sum += ((bed_result["acceleration"] - car_100[pr]) * 2)

        if car_top_spd[pr] > bed_result["speed"]:
            all_sum += ((car_top_spd[pr] - bed_result["speed"]) * 2)
        else:
            all_sum += ((bed_result["speed"] - car_top_spd[pr]) * 2)

        cars[pr] = all_sum * 0.5
    return cars

def step4good(good_res, car_price, car_range, car_power, car_100, car_top_spd):
    print(f"step4good \n goodres = {good_res} \n car_price = {car_price} \n car_range = {car_range} \n car_power {car_power} \n car_100 = {car_100} \n car_top = {car_top_spd}\n")
    cars = {}
    for pr in car_price:
        all_sum = 0
        if car_price[pr] > good_res["price"]:
            all_sum = ((car_price[pr] - good_res["price"]) * 2)
        else:
            all_sum = ((good_res["price"] - car_price[pr]) * 2)

        if car_range[pr] > good_res["range"]:
            all_sum += ((car_range[pr] - good_res["range"]) * 2)
        else:
            all_sum += ((good_res["range"] - car_range[pr]) * 2)

        if car_power[pr] > good_res["power"]:
            all_sum += ((car_power[pr] - good_res["power"]) * 2)
        else:
            all_sum += ((good_res["power"] - car_power[pr]) * 2)

        if car_100[pr] > good_res["acceleration"]:
            all_sum += ((car_100[pr] - good_res["acceleration"]) * 2)
        else:
            all_sum += ((good_res["acceleration"] - car_100[pr]) * 2)

        if car_top_spd[pr] > good_res["speed"]:
            all_sum += ((car_top_spd[pr] - good_res["speed"]) * 2)
        else:
            all_sum += ((good_res["speed"] - car_top_spd[pr]) * 2)

        cars[pr] = all_sum * 0.5
    return cars

def fin_num(min_num, max_num):
    print(f"fin_num:\n min = {min_num} \n max_num = {max_num}")
    fin = {}
    for mi in min_num:
        fin_sum = max_num[mi] / (min_num[mi] + max_num[mi])
        fin[mi] = fin_sum
    sorted_values_desc = sorted(fin.items(), key=lambda x: x[1], reverse=True)
    return sorted_values_desc

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