from abc import ABC, abstractmethod
from typing import List, Dict, Type, Optional, Any


class Material(ABC):
    """
    Base abstract class for all materials with simple sequential tagging
    """
    _materials = {}  # Class-level dictionary to track all materials
    _matTags = {}    # Class-level dictionary to track material tags
    _names = {}      # Class-level dictionary to track material names
    _next_tag = 1    # Class variable to track the next tag to assign
    _start_tag = 1   # Class variable to track the starting tag number

    def __init__(self, material_type: str, material_name: str, user_name: str):
        """
        Initialize a new material with a sequential tag
        
        Args:
            material_type (str): The type of material (e.g., 'nDMaterial', 'uniaxialMaterial')
            material_name (str): The specific material name (e.g., 'ElasticIsotropic')
            user_name (str): User-specified name for the material
        """
        if user_name in self._names:
            raise ValueError(f"Material name '{user_name}' already exists")
        
        self.tag = Material._next_tag
        Material._next_tag += 1
        
        self.material_type = material_type
        self.material_name = material_name
        self.user_name = user_name
        
        # Register this material in the class-level tracking dictionaries
        self._materials[self.tag] = self
        self._matTags[self] = self.tag
        self._names[user_name] = self

    @classmethod
    def delete_material(cls, tag: int) -> None:
        """
        Delete a material by its tag and retag all remaining materials sequentially
        
        Args:
            tag (int): The tag of the material to delete
        """
        if tag in cls._materials:
            # Remove the material from tracking dictionaries
            material_to_delete = cls._materials[tag]
            cls._names.pop(material_to_delete.user_name)
            cls._matTags.pop(material_to_delete)
            cls._materials.pop(tag)

            # Retag all remaining materials
            cls.retag_all()

    @classmethod
    def get_material_by_tag(cls, tag: int) -> 'Material':
        """
        Retrieve a specific material by its tag.
        
        Args:
            tag (int): The tag of the material
        
        Returns:
            Material: The material with the specified tag
        
        Raises:
            KeyError: If no material with the given tag exists
        """
        if tag not in cls._materials:
            raise KeyError(f"No material found with tag {tag}")
        return cls._materials[tag]

    @classmethod
    def get_material_by_name(cls, name: str) -> 'Material':
        """
        Retrieve a specific material by its user-specified name.
        
        Args:
            name (str): The user-specified name of the material
        
        Returns:
            Material: The material with the specified name
        
        Raises:
            KeyError: If no material with the given name exists
        """
        if name not in cls._names:
            raise KeyError(f"No material found with name {name}")
        return cls._names[name]

    @classmethod
    def clear_all(cls):
        """
        Reset all class-level tracking and start tags from 1 again
        """
        cls._materials.clear()
        cls._matTags.clear()
        cls._names.clear()
        cls._next_tag = cls._start_tag

    @classmethod
    def set_tag_start(cls, start_number: int):
        """
        Set the starting number for material tags globally
        
        Args:
            start_number (int): The first tag number to use
        """
        if start_number < 1:
            raise ValueError("Tag start number must be greater than 0")
        cls._start_tag = start_number
        cls._next_tag = cls._start_tag
        cls.retag_all()


    @classmethod
    def retag_all(cls):
        """
        Retag all materials sequentially starting from 1
        """
        sorted_materials = sorted(
            [(tag, material) for tag, material in cls._materials.items()],
            key=lambda x: x[0]
        )

        # Clear existing dictionaries
        cls._materials.clear()
        cls._matTags.clear()

        # Rebuild dictionaries with new sequential tags
        for new_tag, (_, material) in enumerate(sorted_materials, start=cls._start_tag):
            material.tag = new_tag # Update the material's tag
            cls._materials[new_tag] = material # Update materials dictionary
            cls._matTags[material] = new_tag   # Update matTags dictionary
        
        # Update next tag
        cls._next_tag = cls._start_tag + len(cls._materials)



    @classmethod
    def get_all_materials(cls) -> Dict[int, 'Material']:
        """
        Retrieve all created materials.
        
        Returns:
            Dict[int, Material]: A dictionary of all materials, keyed by their unique tags
        """
        return cls._materials


    @classmethod
    def get_material_by_name(cls, name: str) -> 'Material':
        """
        Retrieve a specific material by its user-specified name.
        
        Args:
            name (str): The user-specified name of the material
        
        Returns:
            Material: The material with the specified name
        
        Raises:
            KeyError: If no material with the given name exists
        """
        return cls._names[name]
    
    @classmethod  
    @abstractmethod
    def get_parameters(cls) -> List[str]:
        """
        Get the list of parameters for this material type.
        
        Returns:
            List[str]: List of parameter names
        """
        pass

    @classmethod  
    @abstractmethod
    def get_description(cls) -> List[str]:
        """
        Get the list of descriptions for the parameters of this material type.
        
        Returns:
            List[str]: List of parameter descriptions
        """
        pass

    def __str__(self) -> str:
        """
        String representation of the material.
        
        Returns:
            str: Formatted material definition string
        """
        str = f"Material :"
        str += f"\tname:{self.material_name}\n"
        str += f"\ttype:{self.material_type}\n"
        str += f"\ttag:{self.tag}\n"
        str += f"\tuser_name:{self.user_name}\n"
        str += f"\tparameters:"
        for key in self.get_parameters():
            str += f"\t\t{str(key)}: {self.params[key]}"

    @staticmethod
    def validate(params: Dict[str, Any]) -> None:
        """
        Validate the material parameters for all instances.
        
        Args:
            params (Dict[str, Any]): Dictionary of parameter names and values to validate
        
        Raises:
            ValueError: If any parameter is invalid
        """
        pass
    
    @abstractmethod
    def to_tcl(self) -> str:
        """
        Convert the material to a TCL string for OpenSees.
        
        Returns:
            str: TCL representation of the material
        """
        pass

    def get_values(self, keys: List[str]) -> Dict[str, float]:
        """
        Default implementation to retrieve values for specific parameters.
        
        Args:
            keys (List[str]): List of parameter names to retrieve
        
        Returns:
            Dict[str, float]: Dictionary of parameter values
        """
        return {key: self.params.get(key) for key in keys}
    

    def update_values(self,**kwargs) -> None:
        """
        Default implementation to update material parameters.
        
        Args:
            values (Dict[str, float]): Dictionary of parameter names and values to update
        """
        self.params.clear()
        params = self.validate(**kwargs)
        self.params = params if params else {}
        

    def get_param(self, key: str)-> Any:
        """
        Get the value of a specific parameter.
        
        Args:
            key (str): The parameter name
        
        Returns:
            float: The value of the parameter
        """
        return self.params[key]

    @classmethod
    def clear_all_materials(cls):
        """
        Clear all materials and reset tags to starting value
        """
        cls.clear_all()

    def updateMaterialStage(self, state: str)-> str:
        """
        Update the material stage.
        
        Args:
            state (str): The new state of the material
        """
        return ""


class MaterialRegistry:
    """
    A registry to manage material types and their creation.
    """
    _material_types = {}

    @classmethod
    def register_material_type(cls, material_category: str, name: str, material_class: Type[Material]):
        """
        Register a new material type for easy creation.
        
        Args:
            material_category (str): The category of material (nDMaterial, uniaxialMaterial)
            name (str): The name of the material type
            material_class (Type[Material]): The class of the material
        """
        if material_category not in cls._material_types:
            cls._material_types[material_category] = {}
        cls._material_types[material_category][name] = material_class

    @classmethod
    def get_material_categories(cls):
        """
        Get available material categories.
        
        Returns:
            List[str]: Available material categories
        """
        return list(cls._material_types.keys())

    @classmethod
    def get_material_types(cls, category: str):
        """
        Get available material types for a given category.
        
        Args:
            category (str): Material category
        
        Returns:
            List[str]: Available material types for the category
        """
        return list(cls._material_types.get(category, {}).keys())

    @classmethod
    def create_material(cls, material_category: str, material_type: str, user_name: str = "Unnamed", **kwargs) -> Material:
        """
        Create a new material of a specific type.
        
        Args:
            material_category (str): Category of material (nDMaterial, uniaxialMaterial)
            material_type (str): Type of material to create
            user_name (str): User-specified name for the material
            **kwargs: Parameters for material initialization
        
        Returns:
            Material: A new material instance
        
        Raises:
            KeyError: If the material category or type is not registered
        """
        if material_category not in cls._material_types:
            raise KeyError(f"Material category {material_category} not registered")
        
        if material_type not in cls._material_types[material_category]:
            raise KeyError(f"Material type {material_type} not registered in {material_category}")
        
        return cls._material_types[material_category][material_type](user_name=user_name, **kwargs)
    
    
    def updateMaterialStage(self, state: str)-> str:
        """
        Update the material stage.
        
        Args:
            state (str): The new state of the material
        """
        return ""

from femora.components.Material.materialsOpenSees import *
class MaterialManager:
    """
    Singleton class for managing mesh materials and properties
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MaterialManager, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance


    def _initialize(self):
        """Initialize the singleton instance"""
        # Add nd and uniaxial managers for autocompletion and access
        from .nd_uniaxial_manager import NDMaterialManager, UniaxialMaterialManager
        self.nd = NDMaterialManager()
        self.uniaxial = UniaxialMaterialManager()


    def create_material(self, 
                       material_category: str, 
                       material_type: str, 
                       user_name: str, 
                       **material_params) -> Material:
        """
        Create a new material with the given parameters
        
        Args:
            material_category (str): Category of material (e.g., 'nDMaterial')
            material_type (str): Type of material (e.g., 'Concrete')
            user_name (str): Unique name for the material
            **material_params: Material-specific parameters
            
        Returns:
            Material: The created material instance
            
        Raises:
            KeyError: If material category or type doesn't exist
            ValueError: If material name already exists
        """
        return MaterialRegistry.create_material(
            material_category=material_category,
            material_type=material_type,
            user_name=user_name,
            **material_params
        )

    @staticmethod
    def get_material(identifier: Any) -> Material:
        """
        Get material by either tag or name
        
        Args:
            identifier: Either material tag (int) or user_name (str)
            
        Returns:
            Material: The requested material
            
        Raises:
            KeyError: If material not found
            TypeError: If identifier type is invalid
        """
        if isinstance(identifier, int):
            return Material.get_material_by_tag(identifier)
        elif isinstance(identifier, str):
            return Material.get_material_by_name(identifier)
        else:
            raise TypeError("Identifier must be either tag (int) or name (str)")


    def update_material_params(self, 
                             identifier: Any, 
                             new_params: Dict[str, float]) -> None:
        """
        Update parameters of an existing material
        
        Args:
            identifier: Either material tag (int) or user_name (str)
            new_params: Dictionary of parameter names and new values
            
        Raises:
            KeyError: If material not found
        """
        material = self.get_material(identifier)
        material.update_values(new_params)


    def delete_material(self, identifier: Any) -> None:
        """
        Delete a material by its identifier
        
        Args:
            identifier: Either material tag (int) or user_name (str)
            
        Raises:
            KeyError: If material not found
        """
        if isinstance(identifier, str):
            material = Material.get_material_by_name(identifier)
            Material.delete_material(material.tag)
        elif isinstance(identifier, int):
            Material.delete_material(identifier)
        else:
            raise TypeError("Identifier must be either tag (int) or name (str)")


    def get_all_materials(self) -> Dict[int, Material]:
        """
        Get all registered materials
        
        Returns:
            Dict[int, Material]: Dictionary of all materials keyed by their tags
        """
        return Material.get_all_materials()


    def get_available_material_types(self, category: Optional[str] = None) -> Dict[str, List[str]]:
        """
        Get available material types, optionally filtered by category
        
        Args:
            category (str, optional): Specific category to get types for
            
        Returns:
            Dict[str, List[str]]: Dictionary of categories and their material types
        """
        if category:
            return {category: MaterialRegistry.get_material_types(category)}
        
        return {
            cat: MaterialRegistry.get_material_types(cat)
            for cat in MaterialRegistry.get_material_categories()
        }


    def set_material_tag_start(self, start_number: int) -> None:
        """
        Set the starting number for material tags
        
        Args:
            start_number (int): Starting tag number (must be > 0)
            
        Raises:
            ValueError: If start_number < 1
        """
        Material.set_tag_start(start_number)


    def clear_all_materials(self) -> None:
        """Clear all registered materials and reset tags"""
        Material.clear_all()


    @classmethod
    def get_instance(cls, **kwargs):
        """
        Get the singleton instance of MaterialManager
        
        Args:
            **kwargs: Keyword arguments to pass to the constructor
            
        Returns:
            MaterialManager: The singleton instance
        """
        if cls._instance is None:
            cls._instance = cls(**kwargs)
        return cls._instance






if __name__ == "__main__":
# Example concrete material class for testing
    class ConcreteMaterial(Material):
        def __init__(self, user_name: str, fc: float = 4000, E: float = 57000*pow(4000, 0.5)):
            super().__init__('nDMaterial', 'Concrete', user_name)
            self.params = {'fc': fc, 'E': E}
        
        @classmethod
        def get_parameters(cls) -> List[str]:
            return ['fc', 'E']
        
        @classmethod
        def get_description(cls) -> List[str]:
            return ['Concrete strength', "Young's modulus"]
        
        def __str__(self) -> str:
            return f"nDMaterial Concrete {self.tag} {self.params['fc']} {self.params['E']}"

    # Register the concrete material
    MaterialRegistry.register_material_type('nDMaterial', 'Concrete', ConcreteMaterial)

    def print_material_info():
        """Helper function to print current material information"""
        print("\nCurrent Materials:")
        for tag, mat in Material.get_all_materials().items():
            print(f"Tag: {tag}, Name: {mat.user_name}, Material: {mat}")
        print("-" * 50)

    # Test 1: Basic material creation and sequential tagging
    print("Test 1: Basic material creation and sequential tagging")
    try:
        mat1 = ConcreteMaterial(user_name="Concrete1")
        mat2 = ConcreteMaterial(user_name="Concrete2")
        mat3 = ConcreteMaterial(user_name="Concrete3")
        print_material_info()
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: Deleting a material and checking retag
    print("\nTest 2: Deleting a material and checking retag")
    try:
        Material.delete_material(2)  # Delete middle material
        print("After deleting material with tag 2:")
        print_material_info()
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: Setting custom start tag
    print("\nTest 3: Setting custom start tag")
    try:
        Material.clear_all()  # Clear existing materials
        Material.set_tag_start(100)  # Start tags from 100
        mat1 = ConcreteMaterial(user_name="HighTagConcrete1")
        mat2 = ConcreteMaterial(user_name="HighTagConcrete2")
        print_material_info()
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: Error handling for duplicate names
    print("\nTest 4: Error handling for duplicate names")
    try:
        mat_duplicate = ConcreteMaterial(user_name="HighTagConcrete1")
        print("Should not reach here - duplicate name allowed!")
    except ValueError as e:
        print(f"Expected error caught: {e}")

    # Test 5: Material retrieval by tag and name
    print("\nTest 5: Material retrieval by tag and name")
    try:
        mat_by_tag = Material.get_material_by_tag(100)
        print(f"Retrieved by tag 100: {mat_by_tag.user_name}")
        
        mat_by_name = Material.get_material_by_name("HighTagConcrete2")
        print(f"Retrieved by name 'HighTagConcrete2': Tag = {mat_by_name.tag}")
    except Exception as e:
        print(f"Test 5 failed: {e}")

    # Test 6: Registry functionality
    print("\nTest 6: Registry functionality")
    try:
        # Get available categories and types
        categories = MaterialRegistry.get_material_categories()
        print(f"Available categories: {categories}")
        
        types = MaterialRegistry.get_material_types('nDMaterial')
        print(f"Available nDMaterial types: {types}")
        
        # Create material through registry
        registry_mat = MaterialRegistry.create_material(
            'nDMaterial',
            'Concrete',
            user_name="RegistryMaterial",
            fc=5000,
            E=4000000
        )
        print(f"Created through registry: {registry_mat}")
    except Exception as e:
        print(f"Test 6 failed: {e}")

    # Final state
    print("\nFinal state of materials:")
    print_material_info()