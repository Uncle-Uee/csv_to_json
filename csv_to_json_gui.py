"""
Created By: Ubaidullah Effendi-Emjedi
Date: 27 October 2019
"""

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QFileDialog

from src.converters.csv_to_json import *

import sys
import os


class CsvToJsonWindow(QMainWindow):
    """
    CSV To JSON Window Class.
    """

    """ ORIENTATION """
    X_POSITION = 200
    Y_POSITION = 200

    WIDTH = 800
    HEIGHT = 600

    """ TITLE """
    TITLE = "Croissant - CSV to Json Converter"

    """ CSV FILE REFERENCE """
    csv_file = ""

    """ JSON FILE REFERENCE """
    json_file = ""

    """ CONSTRUCTOR """

    def __init__(self):
        super(CsvToJsonWindow, self).__init__()
        self.main_window_setup()
        self.menu_bar()
        self.ui()

    """ FUNCTIONS """

    def main_window_setup(self):
        """
        Adjust Main Window Parameters such as Geometry and Title etc
        :return:
        """
        self.setGeometry(self.X_POSITION, self.Y_POSITION, self.WIDTH, self.HEIGHT)
        self.setFixedSize(self.WIDTH, self.HEIGHT / 2)
        self.setWindowTitle(self.TITLE)
        self.setWindowIcon(QIcon("croissant.ico"))

    def ui(self):
        # File Dialogs
        self.open_csv_file_ui()
        self.save_json_file_ui()

        # Toggles
        self.allow_empty_strings_ui()
        self.allow_null_values_ui()
        self.use_unique_id_ui()
        self.root_data_ui()

        # CSV to Json Conversion
        self.convert_csv_to_json_ui()

    def open_csv_file_ui(self):
        """
        Open CSV File
        :return:
        """
        # CSV File Label
        self.csv_file_label = self.create_label(orientation=(25, 30, 625, 25), text="CSV File Location")

        # CSV File TextBox
        self.csv_file_text_box = self.create_text_box(orientation=(25, 55, 650, 25),
                                                      hint="CSV Filename or Location")
        # CSV File Button
        self.csv_file_button_open = self.create_button(orientation=(685, 55, 75, 25), text="Open")
        self.csv_file_button_open.clicked.connect(self.open_file_dialog)

    def open_file_dialog(self):
        """
        Select and Open a CSV File.
        :return:
        """
        self.csv_file = QFileDialog.getOpenFileName(self, "Open CSV File", os.curdir)
        self.csv_file = self.csv_file[0]
        self.csv_file_text_box.setText(self.csv_file)

    def save_json_file_ui(self):
        """
        Save Json File
        :return:
        """
        # Json File Label
        self.json_file_label = self.create_label(orientation=(25, 80, 625, 25), text="Json File Save Location")

        # Json File TextBox
        self.json_file_text_box = self.create_text_box(orientation=(25, 105, 650, 25),
                                                       hint="Json Filename or Save Location")

        # Json File Button
        self.json_file_button_save = self.create_button(orientation=(685, 105, 75, 25), text="Save")
        self.json_file_button_save.clicked.connect(self.save_file_dialog)

    def save_file_dialog(self):
        """
        Save the Json File.
        :return:
        """
        self.json_file = QFileDialog.getSaveFileName(self, "Save Json File", os.curdir)
        self.json_file = self.json_file[0]
        self.json_file_text_box.setText(self.json_file)

    def allow_empty_strings_ui(self):
        # Check Box
        self.allow_empty_strings = self.create_check_box(orientation=(25, 145, 250, 25),
                                                         text="Allow Empty Strings?")

        self.allow_empty_strings.toggle()
        print("Allow Empty Strings: " + str(self.allow_empty_strings.isChecked()) + "\n")

        self.allow_empty_strings.stateChanged.connect(self.allow_empty_strings_state_changed)

    def allow_empty_strings_state_changed(self):
        print("Allow Empty Strings State: " + str(self.allow_empty_strings.isChecked()) + "\n")

    def allow_null_values_ui(self):
        # Check Box
        self.allow_null_values = self.create_check_box(orientation=(165, 145, 250, 25),
                                                       text="Allow Null Values?")

        self.allow_null_values.toggle()
        print("Allow Null Values: " + str(self.allow_null_values.isChecked()) + "\n")

        self.allow_null_values.stateChanged.connect(self.allow_null_values_state_changed)

    def allow_null_values_state_changed(self):
        print("Allow Null Values State: " + str(self.allow_null_values.isChecked()) + "\n")

    def use_unique_id_ui(self):
        # Check Box
        self.use_unique_id = self.create_check_box(orientation=(25, 175, 250, 25),
                                                   text="Use CSV Column Tag as a Unique ID?")

        self.use_unique_id.stateChanged.connect(self.unique_id_ui)

        # Unique ID Text
        self.unique_id = self.create_text_box(orientation=(25, 200, 100, 25), hint="Column Tag")
        self.unique_id.setReadOnly(True)

        print("Use Unique ID's: " + str(self.use_unique_id.isChecked()) + "\n")

    def root_data_ui(self):
        # Check Box
        self.root_data = self.create_check_box(orientation=(250, 175, 250, 25),
                                               text="Root Json Data?")

        self.root_data.stateChanged.connect(self.root_key_ui)

        # Root Key Edit Text
        self.root_key = self.create_text_box(orientation=(250, 200, 100, 25), hint="Root Key")

        print("Root the Data: " + str(self.root_data.isChecked()) + "\n")

    def unique_id_ui(self):
        if self.use_unique_id.isChecked():
            self.unique_id.setReadOnly(False)
            print("Use Unique ID's: " + str(self.use_unique_id.isChecked()) + "\n")
        else:
            self.unique_id.setReadOnly(True)
            self.unique_id.setText("")
            print("Use Unique ID's: " + str(self.use_unique_id.isChecked()) + "\n")

    def root_key_ui(self):
        if self.root_data.isChecked():
            self.root_key.setReadOnly(False)
            print("Root the Data: " + str(self.root_data.isChecked()) + "\n")
        else:
            self.root_key.setReadOnly(True)
            print("Root the Data: " + str(self.root_data.isChecked()) + "\n")
            self.root_key.setText("")

    def convert_csv_to_json_ui(self):
        self.converter_button = self.create_button(orientation=(25, 245, 75, 30), text="Convert")

        self.converter_button.clicked.connect(self.convert_csv_to_json)

    def convert_csv_to_json(self):

        unique_id_value = self.unique_id.text()
        root_key_value = self.root_key.text()
        json_file_value = self.json_file_text_box.text()
        csv_file_value = self.csv_file_text_box.text()

        if json_file_value == "":
            json_file_value = os.path.basename(csv_file_value).replace('csv', 'json')

        if csv_file_value != "" and self.use_unique_id.isChecked() and self.root_data.isChecked():

            convert_csv_to_json_with_root_and_uid(csv_file_value, json_file_value, root_key_value, unique_id_value,
                                                  self.allow_empty_strings.isChecked(),
                                                  self.allow_null_values.isChecked())

        elif csv_file_value != "" and self.use_unique_id.isChecked():
            convert_csv_to_json_with_uid(csv_file_value, json_file_value, unique_id_value,
                                         self.allow_empty_strings.isChecked(),
                                         self.allow_null_values.isChecked())

        elif csv_file_value != "" and self.root_data.isChecked():
            convert_csv_to_json_with_root(csv_file_value, json_file_value, root_key_value,
                                          self.allow_empty_strings.isChecked(),
                                          self.allow_null_values.isChecked())
        elif csv_file_value != "":
            convert_csv_to_json(csv_file_value, json_file_value, self.allow_empty_strings.isChecked(),
                                self.allow_null_values.isChecked())

        else:
            print("Invalid Options!")

    def menu_bar(self):
        """
        Create a Menu Bar with Tabs and Actions
        :return:
        """

        # Create MenuBar
        bar = self.menuBar()

        # Create Root Menus
        file = bar.addMenu("File")

        # Create Actions for Menus
        open_action = QAction("Open", self)
        open_action.setShortcut("Ctrl+O")
        open_action.setStatusTip("Open a CSV File")

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")

        quit_action = QAction('Quit', self)
        quit_action.setShortcut("Ctrl+Q")

        # Add Actions
        file.addAction(open_action)
        file.addAction(save_action)
        file.addAction(quit_action)

        # Events
        open_action.triggered.connect(self.open_file_dialog)
        save_action.triggered.connect(self.save_file_dialog)
        quit_action.triggered.connect(lambda: (qApp.quit(), print("Quiting Application!")))

    def create_label(self, orientation=(0, 0, 0, 0), text=""):
        """
        Create a Label.
        :param orientation: Orientation of the label: X,Y Position and Width and Height
        :param text: Label Text
        :return: QTWidget Label
        """
        label = QtWidgets.QLabel(text, self)
        label.setGeometry(orientation[0], orientation[1], orientation[2], orientation[3])
        return label

    def create_button(self, orientation=(0, 0, 0, 0), text="button"):
        """
        Create a Button.
        :param orientation: Orientation of the button: X,Y Position and Width and Height
        :param text: Button Text
        :return: QTWidget Push Button
        """
        button = QtWidgets.QPushButton(text, self)
        button.setGeometry(orientation[0], orientation[1], orientation[2], orientation[3])
        return button

    def create_check_box(self, orientation=(0, 0, 0, 0), text=""):
        """
        Create a Check Box Option.
        :param orientation: Placement of the Check Box.
        :param text: Check Box Text.
        :return:
        """
        check_box = QtWidgets.QCheckBox(text, self)
        check_box.setGeometry(orientation[0], orientation[1], orientation[2], orientation[3])
        check_box.setText(text)
        check_box.adjustSize()
        return check_box

    def create_text_box(self, orientation=(0, 0, 0, 0), text="", hint=""):
        """
        Create a Text Box Input Field
        :param orientation: Placement of the Text Box Field.
        :param text: Text Box Text
        :param hint: Text Box Hint Text
        :return:
        """
        text_box = QtWidgets.QLineEdit(text, self)
        text_box.setGeometry(orientation[0], orientation[1], orientation[2], orientation[3])
        text_box.setPlaceholderText(hint)
        return text_box


def window():
    application = QApplication(sys.argv)
    win = CsvToJsonWindow()
    win.show()
    sys.exit(application.exec_())


if __name__ == "__main__":
    window()
