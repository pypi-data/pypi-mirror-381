from qtpy.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QComboBox, QPushButton, QTableWidget, QTableWidgetItem, 
    QDialog, QMessageBox, QHeaderView, QGridLayout,
    QFrame, QTextBrowser  
)

from qtpy.QtCore import Qt
from femora.components.Damping.dampingBase import DampingBase, DampingRegistry

class DampingManagerTab(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Main layout
        layout = QVBoxLayout(self)
        
        # Damping type selection
        type_layout = QGridLayout()
        self.damping_type_combo = QComboBox()
        self.damping_type_combo.addItems(DampingRegistry.get_available_types())
        
        create_damping_btn = QPushButton("Create New Damping")
        create_damping_btn.clicked.connect(self.open_damping_creation_dialog)
        
        type_layout.addWidget(QLabel("Damping Type:"), 0, 0)
        type_layout.addWidget(self.damping_type_combo, 0, 1, 1, 2)
        type_layout.addWidget(create_damping_btn, 1, 0, 1, 3)
        
        layout.addLayout(type_layout)
        
        # Dampings table
        self.dampings_table = QTableWidget()
        self.dampings_table.setColumnCount(5)  # Tag, Type, Name, Edit, Delete
        self.dampings_table.setHorizontalHeaderLabels(["Tag", "Type", "Name", "Edit", "Delete"])
        header = self.dampings_table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        
        layout.addWidget(self.dampings_table)
        
        # Refresh dampings button
        refresh_btn = QPushButton("Refresh Dampings List")
        refresh_btn.clicked.connect(self.refresh_dampings_list)
        layout.addWidget(refresh_btn)
        
        # Initial refresh
        self.refresh_dampings_list()

    def open_damping_creation_dialog(self):
        """Open dialog to create a new damping of selected type"""
        damping_type = self.damping_type_combo.currentText()
        dialog = DampingCreationDialog(damping_type, self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh_dampings_list()

    def refresh_dampings_list(self):
        """Update the dampings table with current dampings"""
        self.dampings_table.setRowCount(0)
        dampings = DampingBase._dampings
        
        self.dampings_table.setRowCount(len(dampings))
        # print(DampingBase.print_dampings())
        for row, (tag, damping) in enumerate(dampings.items()):
            # Tag
            tag_item = QTableWidgetItem(str(tag))
            tag_item.setFlags(tag_item.flags() & ~Qt.ItemIsEditable)
            self.dampings_table.setItem(row, 0, tag_item)
            
            # Damping Type
            type_item = QTableWidgetItem(damping.__class__.__name__)
            type_item.setFlags(type_item.flags() & ~Qt.ItemIsEditable)
            self.dampings_table.setItem(row, 1, type_item)
            
            # Name
            name_item = QTableWidgetItem(damping.name)
            name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
            self.dampings_table.setItem(row, 2, name_item)
            
            # Edit button
            edit_btn = QPushButton("Edit")
            edit_btn.clicked.connect(lambda checked, d=damping: self.open_damping_edit_dialog(d))
            self.dampings_table.setCellWidget(row, 3, edit_btn)
            
            # Delete button
            delete_btn = QPushButton("Delete")
            delete_btn.clicked.connect(lambda checked, t=tag: self.delete_damping(t))
            self.dampings_table.setCellWidget(row, 4, delete_btn)

    def open_damping_edit_dialog(self, damping):
        """Open dialog to edit an existing damping"""
        dialog = DampingEditDialog(damping, self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh_dampings_list()

    def delete_damping(self, tag):
        """Delete a damping from the system"""
        reply = QMessageBox.question(
            self, 'Delete Damping',
            f"Are you sure you want to delete damping with tag {tag}?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            DampingBase.remove_damping(tag)
            self.refresh_dampings_list()

class DampingCreationDialog(QDialog):
    def __init__(self, damping_type, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Create {damping_type} Damping")
        self.damping_type = damping_type.lower()
        
        # Main horizontal layout to split the dialog
        main_layout = QHBoxLayout(self)
        
        # Left side - Parameters
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Get damping class
        damping_class = DampingRegistry._damping_types[self.damping_type]
        
        # Parameter inputs
        self.param_inputs = {}
        parameters = damping_class.get_Parameters()
        
        # Create a grid layout for input fields
        params_group = QGridLayout()
        
        # Add label and input fields to the grid layout
        for row, (param, desc) in enumerate(parameters):
            label = QLabel(param)
            input_field = QLineEdit()
            description_label = QLabel(desc)
            description_label.setWordWrap(True)
            
            params_group.addWidget(label, row, 0)
            params_group.addWidget(input_field, row, 1)
            params_group.addWidget(description_label, row, 2)
            
            self.param_inputs[param] = input_field
        
        left_layout.addLayout(params_group)
        
        # Buttons at the bottom of left side
        btn_layout = QHBoxLayout()
        create_btn = QPushButton("Create Damping")
        create_btn.clicked.connect(self.create_damping)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        btn_layout.addWidget(create_btn)
        btn_layout.addWidget(cancel_btn)
        left_layout.addLayout(btn_layout)
        
        # make the left side be top aligned and left
        left_layout.addStretch()

        # Add left widget to main layout
        main_layout.addWidget(left_widget)

        
        # Vertical line separator
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        
        # Right side - Notes
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
                
        # Notes content using QTextEdit
        notes_display = QTextBrowser()
        notes_display.setReadOnly(True)  # Make it read-only
        notes_display.setOpenExternalLinks(True) 
        
        # Format notes content
        infotxt = ""
        infotxt += "<b>Notes:</b><br>"

        info = damping_class.get_Notes()
        notes = info.get("Notes", None)
        if notes:
            for i, note in enumerate(notes, 1):
                infotxt += f"{i}. {note}<br><br>"
        else:
            infotxt += "No notes available for this damping type.<br>"

        ref = info.get("References", None)
        if ref:
            infotxt += "<br><b>Reference:</b><br>"
            # Convert reference to clickable link
            for i, ref in enumerate(ref, 1):
                infotxt += f"{i}. <a href='{ref}'>{ref}</a><br>"

        notes_display.setHtml(infotxt)  # Use HTML formatting

        
        right_layout.addWidget(notes_display)
        
        right_layout.addStretch()
        
        # Add right widget to main layout
        main_layout.addWidget(right_widget)
        
        # Set the layout proportions
        main_layout.setStretch(0, 3)  # Left side takes 3/5 of the width
        main_layout.setStretch(2, 2)  # Right side takes 2/5 of the width

    def create_damping(self):
        try:
            # Collect parameters
            params = {}
            for param, input_field in self.param_inputs.items():
                value = input_field.text().strip() 
                if value == "" :
                    continue
                params[param] = value

            # Create damping
            DampingRegistry.create_damping(self.damping_type, **params)
            self.accept()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error",
                              f"Invalid input: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

class DampingEditDialog(QDialog):
    def __init__(self, damping, parent=None):
        super().__init__(parent)
        self.damping = damping
        self.setWindowTitle(f"Edit {damping.__class__.__name__} (Tag: {damping.tag})")
        
        
        # Main horizontal layout to split the dialog
        main_layout = QHBoxLayout(self)
        
        # Left side - Parameters
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Parameter inputs
        self.param_inputs = {}
        parameters = damping.__class__.get_Parameters()
        values = damping.get_values()
        
        # Create a grid layout for parameter inputs
        params_group = QGridLayout()
        
        # Add label and input fields to the grid layout
        for row, (param, desc) in enumerate(parameters):
            label = QLabel(param)
            input_field = QLineEdit()
            description_label = QLabel(desc)
            description_label.setWordWrap(True)
            
            # Set current value if available
            current_value = values.get(param, None)
            if current_value is not None:
                if isinstance(current_value, list):
                    input_field.setText(",".join(map(str, current_value)))
                else:
                    input_field.setText(str(current_value))
            
            params_group.addWidget(label, row, 0)
            params_group.addWidget(input_field, row, 1)
            params_group.addWidget(description_label, row, 2)
            
            self.param_inputs[param] = input_field
        
        left_layout.addLayout(params_group)
        
        # Buttons at the bottom of left side
        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save Changes")
        save_btn.clicked.connect(self.save_changes)
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(self.reject)
        
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)
        left_layout.addLayout(btn_layout)
        left_layout.addStretch()
        
        # Add left widget to main layout
        main_layout.addWidget(left_widget)
        
        # Vertical line separator
        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)
        
        # Right side - Notes
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
                
        # Notes content using QTextEdit
        notes_display = QTextBrowser()
        notes_display.setReadOnly(True)  # Make it read-only
        notes_display.setOpenExternalLinks(True) 
        
        # Format notes content
        infotxt = ""
        infotxt += "<b>Notes:</b><br>"

        info = damping.__class__.get_Notes()
        notes = info.get("Notes", None)
        if notes:
            for i, note in enumerate(notes, 1):
                infotxt += f"{i}. {note}<br><br>"
        else:
            infotxt += "No notes available for this damping type.<br>"

        ref = info.get("References", None)
        if ref:
            infotxt += "<br><b>Reference:</b><br>"
            # Convert reference to clickable link
            for i, ref in enumerate(ref, 1):
                infotxt += f"{i}. <a href='{ref}'>{ref}</a><br>"

        notes_display.setHtml(infotxt)  # Use HTML formatting

        
        right_layout.addWidget(notes_display)
        
        right_layout.addStretch()
        
        # Add right widget to main layout
        main_layout.addWidget(right_widget)

        # Set the layout proportions
        main_layout.setStretch(0, 3)  # Left side takes 3/5 of the width
        main_layout.setStretch(2, 2)  # Right side takes 2/5 of the width


    def save_changes(self):
        try:
            # Collect parameters
            params = {}
            for param, input_field in self.param_inputs.items():
                value = input_field.text().strip()
                params[param] = value

            # Update damping
            self.damping.update_values(**params)            

            self.accept()

        except ValueError as e:
            QMessageBox.warning(self, "Input Error",
                              f"Invalid input: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    import sys
    from qtpy.QtWidgets import QApplication
    from femora.components.Damping.dampingBase import RayleighDamping, ModalDamping
    RayleighDamping1 = RayleighDamping(alphaM=0.1, betaK=0.2, betaKInit=0.3, betaKComm=0.4)
    RayleighDamping2 = RayleighDamping(alphaM=0.5, betaK=0.6, betaKInit=0.7, betaKComm=0.8)
    ModalDamping1 = ModalDamping(numberofModes=2, dampingFactors="0.1,0.2")
    ModalDamping2 = ModalDamping(numberofModes=3, dampingFactors="0.3,0.4,0.5")
    app = QApplication(sys.argv)
    window = DampingManagerTab()
    window.show()
    sys.exit(app.exec_())