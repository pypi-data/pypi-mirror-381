"""
Uniaxial Section GUI Dialogs
Uses UniaxialSection class methods instead of hardcoding
"""

from qtpy.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFormLayout, QMessageBox, QGridLayout, QFrame, QTextBrowser, QGroupBox, QWidget
)
from qtpy.QtCore import Qt

from femora.components.section.section_opensees import UniaxialSection
from femora.components.section.section_gui_utils import setup_material_dropdown, get_material_by_combo_selection, set_combo_to_material

RESPONSE_CODES = ['P', 'Mz', 'My', 'Vy', 'Vz', 'T']

class UniaxialSectionCreationDialog(QDialog):
    """
    Dialog for creating new UniaxialSection sections using class methods
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create Uniaxial Section")
        self.setMinimumSize(600, 400)
        
        self.parameters = UniaxialSection.get_parameters()
        self.descriptions = UniaxialSection.get_description()
        
        main_layout = QHBoxLayout(self)
        
        # Left side - Parameters
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Section name group
        name_group = QGroupBox("Section Identification")
        name_layout = QFormLayout(name_group)
        self.user_name_input = QLineEdit()
        self.user_name_input.setPlaceholderText("Enter unique section name")
        name_layout.addRow("Section Name:", self.user_name_input)
        left_layout.addWidget(name_group)
        
        # Parameters group
        parameters_group = QGroupBox("Section Parameters")
        parameters_layout = QGridLayout(parameters_group)
        self.param_inputs = {}
        # Material
        param_label = QLabel("material:")
        self.material_combo = QComboBox()
        setup_material_dropdown(self.material_combo, lambda m: m.material_type == 'uniaxialMaterial', "Select Uniaxial Material")
        self.material_combo.setToolTip("Select uniaxial material")
        desc_label = QLabel(self.descriptions[0])
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: gray; font-size: 10px;")
        parameters_layout.addWidget(param_label, 0, 0)
        parameters_layout.addWidget(self.material_combo, 0, 1)
        parameters_layout.addWidget(desc_label, 0, 2)
        self.param_inputs['material'] = self.material_combo
        # Response code
        code_label = QLabel("response_code:")
        self.code_combo = QComboBox()
        self.code_combo.addItems(RESPONSE_CODES)
        self.code_combo.setToolTip("Select response code")
        desc_label2 = QLabel(self.descriptions[1])
        desc_label2.setWordWrap(True)
        desc_label2.setStyleSheet("color: gray; font-size: 10px;")
        parameters_layout.addWidget(code_label, 1, 0)
        parameters_layout.addWidget(self.code_combo, 1, 1)
        parameters_layout.addWidget(desc_label2, 1, 2)
        self.param_inputs['response_code'] = self.code_combo
        left_layout.addWidget(parameters_group)
        
        # Buttons
        btn_layout = QHBoxLayout()
        create_btn = QPushButton("Create Section")
        create_btn.clicked.connect(self.create_section)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(create_btn)
        btn_layout.addWidget(cancel_btn)
        left_layout.addLayout(btn_layout)
        left_layout.addStretch()
        main_layout.addWidget(left_widget)
        
        # Vertical line separator
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        
        # Right side - Help text from class
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        help_display = QTextBrowser()
        help_display.setHtml(UniaxialSection.get_help_text())
        right_layout.addWidget(help_display)
        main_layout.addWidget(right_widget)
        main_layout.setStretch(0, 3)
        main_layout.setStretch(2, 2)

    def create_section(self):
        try:
            user_name = self.user_name_input.text().strip()
            if not user_name:
                QMessageBox.warning(self, "Input Error", "Please enter a section name.")
                return
            try:
                existing_section = UniaxialSection.get_section_by_name(user_name)
                QMessageBox.warning(self, "Input Error", f"Section with name '{user_name}' already exists.")
                return
            except KeyError:
                pass
            material = get_material_by_combo_selection(self.material_combo)
            if not material:
                QMessageBox.warning(self, "Input Error", "Please select a uniaxial material.")
                return
            response_code = self.code_combo.currentText()
            params = {'material': material, 'response_code': response_code}
            try:
                validated_params = UniaxialSection.validate_section_parameters(**params)
            except ValueError as e:
                QMessageBox.warning(self, "Validation Error", str(e))
                return
            self.created_section = UniaxialSection(user_name=user_name, **params)
            QMessageBox.information(self, "Success", f"Uniaxial Section '{user_name}' created successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create section: {str(e)}")

class UniaxialSectionEditDialog(QDialog):
    """
    Dialog for editing existing UniaxialSection sections using class methods
    """
    def __init__(self, section, parent=None):
        super().__init__(parent)
        self.section = section
        self.setWindowTitle(f"Edit Uniaxial Section: {section.user_name}")
        self.setMinimumSize(600, 400)
        self.parameters = section.get_parameters()
        self.descriptions = section.get_description()
        main_layout = QHBoxLayout(self)
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        info_group = QGroupBox("Section Information")
        info_layout = QFormLayout(info_group)
        self.tag_label = QLabel(str(section.tag))
        self.user_name_label = QLabel(section.user_name)
        self.type_label = QLabel(section.section_name)
        info_layout.addRow("Tag:", self.tag_label)
        info_layout.addRow("Name:", self.user_name_label)
        info_layout.addRow("Type:", self.type_label)
        left_layout.addWidget(info_group)
        current_values = section.get_values(self.parameters)
        parameters_group = QGroupBox("Section Parameters")
        parameters_layout = QGridLayout(parameters_group)
        # Material
        param_label = QLabel("material:")
        self.material_combo = QComboBox()
        setup_material_dropdown(self.material_combo, lambda m: m.material_type == 'uniaxialMaterial', "Select Uniaxial Material")
        set_combo_to_material(self.material_combo, section.material)
        self.material_combo.setToolTip("Select uniaxial material")
        desc_label = QLabel(self.descriptions[0])
        desc_label.setWordWrap(True)
        desc_label.setStyleSheet("color: gray; font-size: 10px;")
        parameters_layout.addWidget(param_label, 0, 0)
        parameters_layout.addWidget(self.material_combo, 0, 1)
        parameters_layout.addWidget(desc_label, 0, 2)
        # Response code
        code_label = QLabel("response_code:")
        self.code_combo = QComboBox()
        self.code_combo.addItems(RESPONSE_CODES)
        self.code_combo.setCurrentText(current_values.get('response_code', 'P'))
        self.code_combo.setToolTip("Select response code")
        desc_label2 = QLabel(self.descriptions[1])
        desc_label2.setWordWrap(True)
        desc_label2.setStyleSheet("color: gray; font-size: 10px;")
        parameters_layout.addWidget(code_label, 1, 0)
        parameters_layout.addWidget(self.code_combo, 1, 1)
        parameters_layout.addWidget(desc_label2, 1, 2)
        left_layout.addWidget(parameters_group)
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.save_changes)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        left_layout.addLayout(btn_layout)
        left_layout.addStretch()
        main_layout.addWidget(left_widget)
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        help_display = QTextBrowser()
        help_display.setHtml(section.__class__.get_help_text())
        right_layout.addWidget(help_display)
        main_layout.addWidget(right_widget)
        main_layout.setStretch(0, 3)
        main_layout.setStretch(2, 2)
    def save_changes(self):
        try:
            material = get_material_by_combo_selection(self.material_combo)
            if not material:
                QMessageBox.warning(self, "Input Error", "Please select a uniaxial material.")
                return
            response_code = self.code_combo.currentText()
            update_values = {'material': material, 'response_code': response_code}
            self.section.update_values(update_values)
            QMessageBox.information(self, "Success", f"Section '{self.section.user_name}' updated successfully!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to update section: {str(e)}")



if __name__ == "__main__":
    from qtpy.QtWidgets import QApplication
    from femora.components.Material.materialsOpenSees import ElasticIsotropicMaterial, ElasticUniaxialMaterial
    import sys

    elas1 = ElasticIsotropicMaterial(user_name="Steel", E=210e9, nu=0.3)
    elas2 = ElasticUniaxialMaterial(user_name="Concrete", E=30e9, nu=0.2)

    app = QApplication(sys.argv)
    
    # Test creation dialog
    create_dialog = UniaxialSectionCreationDialog()
    if create_dialog.exec_() == QDialog.Accepted:
        print("Created section:", create_dialog.created_section)
    
    # Test edit dialog with a dummy section
    dummy_section = UniaxialSection(user_name="TestSection", material=None, response_code='P')
    edit_dialog = UniaxialSectionEditDialog(dummy_section)
    if edit_dialog.exec_() == QDialog.Accepted:
        print("Updated section:", dummy_section)

    sys.exit(app.exec_())
