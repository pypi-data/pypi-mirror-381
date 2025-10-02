from pathlib import Path
import unittest
from typing import get_args

from tyger.discipline.classes.class_type import ClassType
from tyger.discipline.classes.object_type import ObjectType
from tyger.discipline.simple.types import SimpleTypeSystem
from tyger.parser import Parser
from tyger.phases.type_check import TypingPhase


class ClassTypingAdvancedTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = Path(__file__).parent / "sources"
        cls.parser = Parser(str(cls.sources))

    def typecheck(self, filename: str):
        module = self.parser.parse(filename)
        phase = TypingPhase(SimpleTypeSystem(), file_path=self.parser.build_file_path(filename))
        env = phase.type_check_stmts(module.body)
        return phase, env

    def test_nested_classes_basic(self):
        """Test basic nested class functionality."""
        phase, env = self.typecheck("nested_classes.py")
        
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]
        self.assertIsInstance(outer_type, ClassType)
        self.assertEqual([str], outer_type.constructor_types)
        
        self.assertIn("outer_attr", outer_type.env)
        self.assertEqual(int, outer_type.env["outer_attr"])

    def test_nested_class_environment_isolation(self):
        """Test that nested classes have proper environment isolation."""
        phase, env = self.typecheck("nested_classes.py")
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]
        
        self.assertIn("outer_attr", outer_type.env)
        self.assertIn("get_outer_name", outer_type.env)

    def test_nested_class_constructor_isolation(self):
        """Test that nested classes have isolated constructors."""
        phase, env = self.typecheck("nested_classes.py")
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]
        
        self.assertEqual([str], outer_type.constructor_types)

    def test_nested_class_method_signatures(self):
        """Test that nested class methods have proper signatures."""
        phase, env = self.typecheck("nested_classes.py")
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]
        
        self.assertIn("get_outer_name", outer_type.env)

    def test_complex_inheritance_basic(self):
        """Test basic inheritance without super() calls."""
        phase, env = self.typecheck("minimal_advanced.py")
        
        self.assertIn("SimpleInheritance", env)
        self.assertIn("Child", env)
        self.assertIn("MultipleInheritance", env)
        self.assertIn("Mixin", env)
        self.assertIn("Combined", env)

        child_type = env["Child"]
        self.assertIsInstance(child_type, ClassType)
        self.assertEqual(["SimpleInheritance"], child_type.bases)
        self.assertIn("get_name", child_type.env)
        self.assertIn("get_age", child_type.env)
        self.assertIn("get_info", child_type.env)

        child_instance = child_type.instance_type
        self.assertIn("name", child_instance)
        self.assertIn("age", child_instance)

        combined_type = env["Combined"]
        self.assertIsInstance(combined_type, ClassType)
        self.assertEqual(["MultipleInheritance", "Mixin"], combined_type.bases)
        self.assertIn("get_value", combined_type.env)
        self.assertIn("mixin_method", combined_type.env)
        self.assertIn("get_extra", combined_type.env)

        combined_instance = combined_type.instance_type
        self.assertIn("value", combined_instance)
        self.assertIn("extra", combined_instance)

    def test_multiple_inheritance_method_resolution(self):
        """Test method resolution in multiple inheritance scenarios."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Bat", env)
        self.assertIn("FlyingSquirrel", env)
        
        bat_type = env["Bat"]
        flying_squirrel_type = env["FlyingSquirrel"]
        
        self.assertEqual(["Mammal", "Bird"], bat_type.bases)
        self.assertEqual(["FlyingMammal", "GlidingMammal"], flying_squirrel_type.bases)
        
        self.assertIn("echolocate", bat_type.env)

    def test_inheritance_constructor_parameter_merging(self):
        """Test that constructor parameters are properly handled in inheritance."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Animal", env)
        self.assertIn("Mammal", env)
        self.assertIn("Bird", env)
        
        animal_type = env["Animal"]
        mammal_type = env["Mammal"]
        bird_type = env["Bird"]
        
        self.assertEqual([str], animal_type.constructor_types)
        self.assertEqual([str, bool], mammal_type.constructor_types)
        self.assertEqual([str, bool], bird_type.constructor_types)

    def test_inheritance_method_inheritance(self):
        """Test that methods are properly inherited in inheritance hierarchies."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Animal", env)
        self.assertIn("Mammal", env)
        self.assertIn("Bird", env)
        
        animal_type = env["Animal"]
        mammal_type = env["Mammal"]
        bird_type = env["Bird"]
        
        self.assertIn("speak", animal_type.env)
        self.assertIn("move", animal_type.env)
        self.assertIn("give_birth", mammal_type.env)
        self.assertIn("fly", bird_type.env)

    def test_local_classes_basic(self):
        """Test that local classes don't crash the type checker."""
        phase, env = self.typecheck("local_classes.py")
        
        self.assertIn("GlobalClass", env)
        global_type = env["GlobalClass"]
        self.assertIsInstance(global_type, ClassType)
        self.assertEqual([str], global_type.constructor_types)

    def test_advanced_methods_basic(self):
        """Test basic advanced method patterns."""
        phase, env = self.typecheck("minimal_advanced.py")

        self.assertIn("MethodVariations", env)
        method_var_type = env["MethodVariations"]
        self.assertIsInstance(method_var_type, ClassType)
        self.assertEqual([int], method_var_type.constructor_types)

        self.assertIn("SimplePropertyClass", env)
        prop_type = env["SimplePropertyClass"]
        self.assertIsInstance(prop_type, ClassType)
        self.assertEqual([int], prop_type.constructor_types)

        self.assertIn("MethodChaining", env)
        chain_type = env["MethodChaining"]
        self.assertIsInstance(chain_type, ClassType)
        self.assertEqual([int], chain_type.constructor_types)

    def test_edge_cases_basic(self):
        """Test basic edge cases."""
        phase, env = self.typecheck("minimal_advanced.py")

        self.assertIn("EmptyClass", env)
        empty_type = env["EmptyClass"]
        self.assertIsInstance(empty_type, ClassType)
        self.assertEqual([], empty_type.constructor_types)
        
        self.assertIn("ClassWithClassAttrs", env)
        attrs_type = env["ClassWithClassAttrs"]
        self.assertIn("class_attr", attrs_type.env)
        self.assertIn("name", attrs_type.env)
        self.assertEqual(int, attrs_type.env["class_attr"])
        self.assertEqual(str, attrs_type.env["name"])
        
        self.assertIn("ClassWithOnlyMethods", env)
        methods_type = env["ClassWithOnlyMethods"]
        self.assertIn("method1", methods_type.env)
        self.assertIn("method2", methods_type.env)
        self.assertIn("method3", methods_type.env)

    def test_object_type_inheritance_properties(self):
        """Test ObjectType inheritance and base class properties."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Animal", env)
        self.assertIn("Mammal", env)
        
        animal_type = env["Animal"]
        mammal_type = env["Mammal"]
        
        animal_instance = animal_type.instance_type
        mammal_instance = mammal_type.instance_type

        self.assertIsInstance(animal_instance, ObjectType)
        self.assertIsInstance(mammal_instance, ObjectType)

        self.assertEqual("Animal", animal_instance.name)
        self.assertEqual("Mammal", mammal_instance.name)

    def test_object_type_multiple_inheritance(self):
        """Test ObjectType with multiple inheritance."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Bat", env)
        self.assertIn("FlyingSquirrel", env)

        bat_type = env["Bat"]
        flying_squirrel_type = env["FlyingSquirrel"]

        bat_instance = bat_type.instance_type
        flying_squirrel_instance = flying_squirrel_type.instance_type

        self.assertIsInstance(bat_instance, ObjectType)
        self.assertIsInstance(flying_squirrel_instance, ObjectType)

        self.assertEqual("Bat", bat_instance.name)
        self.assertEqual("FlyingSquirrel", flying_squirrel_instance.name)

    def test_object_type_nested_class_instances(self):
        """Test ObjectType for nested class instances."""
        phase, env = self.typecheck("nested_classes.py")
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]

        outer_instance = outer_type.instance_type
        self.assertIsInstance(outer_instance, ObjectType)
        self.assertEqual("Outer", outer_instance.name)

    def test_object_type_nested_class_method_access(self):
        """Test ObjectType method access in nested classes."""
        phase, env = self.typecheck("nested_classes.py")
        
        self.assertIn("Outer", env)
        outer_type = env["Outer"]

        outer_instance = outer_type.instance_type
        self.assertIsInstance(outer_instance, ObjectType)

        self.assertIn("get_outer_name", outer_instance)

    def test_advanced_methods_complex(self):
        """Test complex advanced method patterns."""
        phase, env = self.typecheck("advanced_methods.py")
        
        self.assertIn("MethodVariations", env)
        method_var_type = env["MethodVariations"]
        self.assertIsInstance(method_var_type, ClassType)
        self.assertEqual([int], method_var_type.constructor_types)

        self.assertIn("PropertyClass", env)
        prop_type = env["PropertyClass"]
        self.assertIsInstance(prop_type, ClassType)
        self.assertEqual([int], prop_type.constructor_types)

        self.assertIn("MethodChaining", env)
        chain_type = env["MethodChaining"]
        self.assertIsInstance(chain_type, ClassType)
        self.assertEqual([int], chain_type.constructor_types)

        self.assertIn("OverloadedMethods", env)
        overload_type = env["OverloadedMethods"]
        self.assertIsInstance(overload_type, ClassType)
        self.assertEqual([str], overload_type.constructor_types)

    def test_complex_inheritance_patterns(self):
        """Test complex inheritance patterns."""
        phase, env = self.typecheck("complex_inheritance.py")
        
        self.assertIn("Animal", env)
        self.assertIn("Mammal", env)
        self.assertIn("Bird", env)
        self.assertIn("Bat", env)

        bat_type = env["Bat"]
        self.assertIsInstance(bat_type, ClassType)
        self.assertEqual(["Mammal", "Bird"], bat_type.bases)

        self.assertIn("FlyingMammal", env)
        self.assertIn("GlidingMammal", env)
        self.assertIn("FlyingSquirrel", env)

        flying_squirrel_type = env["FlyingSquirrel"]
        self.assertIsInstance(flying_squirrel_type, ClassType)
        self.assertEqual(["FlyingMammal", "GlidingMammal"], flying_squirrel_type.bases)

        self.assertIn("Shape", env)
        self.assertIn("Rectangle", env)
        self.assertIn("Square", env)

        square_type = env["Square"]
        self.assertIsInstance(square_type, ClassType)
        self.assertEqual(["Rectangle"], square_type.bases)

    def test_edge_cases_complex(self):
        """Test complex edge cases."""
        phase, env = self.typecheck("edge_cases.py")
        
        self.assertIn("EmptyClass", env)
        empty_type = env["EmptyClass"]
        self.assertIsInstance(empty_type, ClassType)
        self.assertEqual([], empty_type.constructor_types)

        self.assertIn("ClassWithOnlyAttributes", env)
        attrs_type = env["ClassWithOnlyAttributes"]
        self.assertIn("class_attr1", attrs_type.env)
        self.assertIn("class_attr2", attrs_type.env)
        self.assertIn("class_attr3", attrs_type.env)

        self.assertIn("ClassWithOnlyMethods", env)
        methods_type = env["ClassWithOnlyMethods"]
        self.assertIn("method1", methods_type.env)
        self.assertIn("method2", methods_type.env)

        self.assertIn("DeeplyNested", env)
        nested_type = env["DeeplyNested"]
        self.assertIsInstance(nested_type, ClassType)

        self.assertIn("ClassWithSpecialMethods", env)
        special_type = env["ClassWithSpecialMethods"]
        self.assertEqual([int], special_type.constructor_types)

        self.assertIn("ClassWithLambda", env)
        lambda_type = env["ClassWithLambda"]
        self.assertEqual([int], lambda_type.constructor_types)

        self.assertIn("ClassWithComplexTypes", env)
        complex_type = env["ClassWithComplexTypes"]
        self.assertIsInstance(complex_type, ClassType)
