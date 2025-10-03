from qtpy.QtWidgets import QFrame, QVBoxLayout, QWidget, QTabWidget, QLabel, QPushButton
from qtpy.QtCore import Qt

from femora.components.Material.materialGUI import MaterialManagerTab
from femora.components.Mesh.meshPartGUI import MeshPartManagerTab
from femora.components.Assemble.AssemblerGUI import AssemblyManagerTab
from femora.components.Damping.dampingGUI import DampingManagerTab
from femora.components.Region.regionGUI import RegionManagerTab
from femora.components.Constraint.mpConstraintGUI import MPConstraintManagerTab
from femora.components.TimeSeries.timeSeriesGUI import TimeSeriesManagerTab
from femora.components.Constraint.spConstraintGUI import SPConstraintManagerTab
from femora.components.Pattern.patternGUI import PatternManagerTab
from femora.components.Recorder.recorderGUI import RecorderManagerTab
from femora.components.Analysis.analysisGUI import AnalysisManagerTab
from femora.components.Process.processGUI import ProcessGUI
from femora.components.DRM.combinedDRMGUI import CombinedDRMGUI
from femora.components.section.section_gui import SectionManagerTab
from femora.components.interface.interface_gui import InterfaceManagerTab

class LeftPanel(QFrame):
    '''
    Left panel of the main window containing various tabs.
    '''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumWidth(500)
        self.init_ui()
        
    def init_ui(self):
        # Add a layout for future widgets
        layout = QVBoxLayout(self)

        # Create a tab widget
        self.tabs = QTabWidget()
        # make the tabs vertical
        self.tabs.setTabPosition(QTabWidget.West)
        # make the tabs text horizontal
        self.tabs.setTabShape(QTabWidget.Triangular)

        self.tabs.setMovable(True)

        # make only the tab headers bold
        font = self.tabs.font()
        font.setBold(True)
        self.tabs.setTabsClosable(False)  # Disable tab closing
        self.tabs.tabBar().setFont(font)  # Apply bold font only to tab bar
        # make the order of the tabs from top to bottom
        self.tabs.setDocumentMode(True)


        layout.addWidget(self.tabs)

        # Create tabs
        self.create_tabs()
        self.setup_tab_contents()

    def create_tabs(self):
        self.material_tab = QWidget()
        self.mesh_tab = QWidget()
        self.interface_tab = QWidget()
        self.Assemble_tab = QWidget()
        self.drm_tab = QWidget()
        self.manage_tab = QWidget()

        # Add tabs to the tab widget
        self.tabs.addTab(self.material_tab, "Material && Section")
        self.tabs.addTab(self.mesh_tab, "Mesh")
        self.tabs.addTab(self.interface_tab, "Interface")
        self.tabs.addTab(self.Assemble_tab, "Assemble")
        self.tabs.addTab(self.drm_tab, "DRM Analysis")
        self.tabs.addTab(self.manage_tab, "Manage")



    

    def setup_tab_contents(self):
        # Material and  section tab
        self.material_tab.layout = QVBoxLayout()
        self.material_tab.layout.addWidget(MaterialManagerTab())
        self.material_tab.setLayout(self.material_tab.layout)
        # Section tab
        self.material_tab.layout.addWidget(SectionManagerTab())
        self.material_tab.setLayout(self.material_tab.layout)

        # Mesh tab
        self.mesh_tab.layout = QVBoxLayout()
        self.mesh_tab.layout.addWidget(MeshPartManagerTab())
        self.mesh_tab.setLayout(self.mesh_tab.layout)

        # Interface tab
        self.interface_tab.layout = QVBoxLayout()
        self.interface_tab.layout.addWidget(InterfaceManagerTab())
        self.interface_tab.setLayout(self.interface_tab.layout)

        # Assemble tab
        self.Assemble_tab.layout = QVBoxLayout()
        self.Assemble_tab.layout.addWidget(AssemblyManagerTab())
        self.Assemble_tab.setLayout(self.Assemble_tab.layout)


        # DRM tab
        self.drm_tab.layout = QVBoxLayout()
        self.drm_tab.layout.addWidget(CombinedDRMGUI())
        self.drm_tab.setLayout(self.drm_tab.layout)


        # # Process tab
        # self.analysis_tab.layout = QVBoxLayout()
        # self.analysis_tab.layout.addWidget(ProcessGUI())
        # self.analysis_tab.setLayout(self.analysis_tab.layout)

        # Manage Tab
        self.manage_tab.layout = QVBoxLayout()
        self.manage_tab.layout.setAlignment(Qt.AlignTop)

        # Helper function to create and add buttons
        def add_manage_button(label, callback):
            button = QPushButton(label)
            button.clicked.connect(callback)
            self.manage_tab.layout.addWidget(button)

        # Add buttons for managing different components
        add_manage_button("Manage Dampings", lambda: DampingManagerTab(parent=self).show())
        add_manage_button("Manage Regions", lambda: RegionManagerTab(parent=self).show())
        add_manage_button("Manage MP Constraints", lambda: MPConstraintManagerTab(parent=self).show())
        add_manage_button("Manage SP Constraints", lambda: SPConstraintManagerTab(parent=self).show())
        add_manage_button("Manage Time Series", lambda: TimeSeriesManagerTab(parent=self).show())
        add_manage_button("Manage Patterns", lambda: PatternManagerTab(parent=self).show())
        add_manage_button("Manage Recorders", lambda: RecorderManagerTab(parent=self).show())
        add_manage_button("Manage Analysis", lambda: AnalysisManagerTab(parent=self).show())
        add_manage_button("Manage Process", lambda: ProcessGUI(parent=self).show())
        self.manage_tab.setLayout(self.manage_tab.layout)
        


