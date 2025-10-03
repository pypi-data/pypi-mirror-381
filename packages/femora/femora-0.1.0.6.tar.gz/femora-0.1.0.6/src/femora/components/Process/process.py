from typing import List, Dict, Union, Optional
import weakref

# Import your existing component classes
from femora.components.Constraint.mpConstraint import mpConstraint
from femora.components.Constraint.spConstraint import SPConstraint
from femora.components.Pattern.patternBase import Pattern
from femora.components.Recorder.recorderBase import Recorder
from femora.components.Analysis.analysis import Analysis
from femora.components.Actions.action import Action

# Define a union type for all components that can be used in the process
ProcessComponent = Union[SPConstraint, mpConstraint, Pattern, Recorder, Analysis, Action]

class ProcessManager:
    """
    Singleton class to manage the sequence of operations in the structural analysis process.
    
    This class maintains a list of steps as weak references to component objects.
    Each step has only the object reference and an optional description.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProcessManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.steps = []
            self.current_step = -1
            self._initialized = True


    def __iter__(self):
        return iter(self.steps)
    

    def __len__(self):
        return len(self.steps)

    def add_step(self, component: ProcessComponent, description: str = "") -> int:
        """
        Add a step to the process
        
        Args:
            component: The component object to use in this step (must be one of the allowed component types)
            description: Description of the step
            
        Returns:
            int: Index of the added step
        """
        # Store a weak reference to the component
        if not isinstance(component, Action):
            # If the component is not an Action, store a weak reference
            component_ref = weakref.ref(component)
        elif isinstance(component, Action):
            # If the component is an Action, store a strong reference
            # This is because Actions are not expected to be weakly referenced
            # and should be kept alive for the duration of the process
            component_ref = component
        else:
            raise TypeError("Invalid component type. Must be one of the allowed types.")
        


        
        step = {
            "component": component_ref,
            "description": description
        }
        
        self.steps.append(step)
        return len(self.steps) - 1

    def insert_step(self, index: int, component: ProcessComponent, description: str = "") -> bool:
        """
        Insert a step at a specific position. Allows for negative indexing.
        
        Args:
            index: Position to insert the step (negative index allowed)
            component: The component object to use in this step (must be one of the allowed component types)
            description: Description of the step
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Adjust negative index to positive index
        if index < 0:
            index += len(self.steps) + 1

        if 0 <= index <= len(self.steps):

            if not isinstance(component, Action):
                # If the component is not an Action, store a weak reference
                component_ref = weakref.ref(component)
            elif isinstance(component, Action):
                # If the component is an Action, store a strong reference
                # This is because Actions are not expected to be weakly referenced
                # and should be kept alive for the duration of the process
                component_ref = component
            else:
                raise TypeError("Invalid component type. Must be one of the allowed types.")

            
            step = {
                "component": component_ref,
                "description": description
            }
            
            self.steps.insert(index, step)
            
            # Adjust current step if needed
            if index <= self.current_step:
                self.current_step += 1
                
            return True
        return False


    def remove_step(self, index: int) -> bool:
        """
        Remove a step at a specific position
        
        Args:
            index: Position of the step to remove
            
        Returns:
            bool: True if successful, False otherwise
        """
        if 0 <= index < len(self.steps):
            del self.steps[index]
            
            # Adjust current step if needed
            if index <= self.current_step:
                self.current_step -= 1
                
            return True
        return False

    def clear_steps(self) -> None:
        """Clear all steps"""
        self.steps.clear()
        self.current_step = -1

    def get_steps(self) -> List[Dict]:
        """Get all steps in the process"""
        return self.steps

    def get_step(self, index: int) -> Optional[Dict]:
        """
        Get a step at a specific position
        
        Args:
            index: Position of the step
            
        Returns:
            Optional[Dict]: The step or None if index is invalid
        """
        if 0 <= index < len(self.steps):
            return self.steps[index]
        return None
    
    def to_tcl(self):
        """Convert the process to a TCL script"""
        tcl_script = ""
        for step in self.steps:
            component = step["component"]
            if isinstance(component, weakref.ref):
                # If it's a weak reference, resolve it
                component = component()
            description = step["description"]
            tcl_script += f"# {description} ======================================\n\n"
            tcl_script += f"{component.to_tcl()}\n\n\n"
        return tcl_script