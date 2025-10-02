from pathlib import Path
import unittest
from typing import get_args

from tyger.discipline.classes.class_type import ClassType
from tyger.discipline.classes.object_type import ObjectType
from tyger.discipline.simple.types import SimpleTypeSystem
from tyger.parser import Parser
from tyger.phases.type_check import TypingPhase


class ClassTypingCoreTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = Path(__file__).parent / "sources"
        cls.parser = Parser(str(cls.sources))

    def typecheck(self, filename: str):
        module = self.parser.parse(filename)
        phase = TypingPhase(SimpleTypeSystem(), file_path=self.parser.build_file_path(filename))
        env = phase.type_check_stmts(module.body)
        return phase, env

    def test_basic_class_definition(self):
        """Test basic class definition and environment."""
        phase, env = self.typecheck("simple_class.py")
        
        self.assertEqual([], phase.diagnostics)
        self.assertIn("Plain", env)
        
        plain_type = env["Plain"]
        self.assertIsInstance(plain_type, ClassType)
        self.assertEqual("Plain", plain_type.name)
        self.assertEqual([], plain_type.bases)
        
        self.assertEqual([int, str], plain_type.constructor_types)

        instance_type = plain_type.instance_type
        self.assertIsInstance(instance_type, ObjectType)
        self.assertEqual("Plain", instance_type.name)
        self.assertEqual([], instance_type.bases)

    def test_class_attributes_and_methods(self):
        """Test class attributes and method signatures."""
        phase, env = self.typecheck("simple_class.py")
        
        self.assertEqual([], phase.diagnostics)
        self.assertIn("Plain", env)
        
        plain_type = env["Plain"]
        self.assertIn("combine", plain_type.env)

    def test_inheritance_basic(self):
        """Test basic inheritance functionality."""
        phase, env = self.typecheck("simple_instantiation.py")
        
        self.assertEqual([], phase.diagnostics)
        self.assertIn("Base", env)
        self.assertIn("Child", env)
        
        base_type = env["Base"]
        child_type = env["Child"]
        
        self.assertEqual(["Base"], child_type.bases)

        self.assertEqual(["Base"], child_type.bases)

    def test_object_type_basic_properties(self):
        """Test basic ObjectType properties and structure."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        instance_type = plain_type.instance_type
        
        self.assertIsInstance(instance_type, ObjectType)
        self.assertEqual(instance_type.name, "Plain")
        self.assertEqual(instance_type.bases, [])
        self.assertIn("x", instance_type)
        self.assertIn("y", instance_type)
        self.assertEqual(instance_type["x"], int)
        self.assertEqual(instance_type["y"], str)

    def test_object_type_environment_operations(self):
        """Test ObjectType environment operations."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        instance_type = plain_type.instance_type
        
        self.assertIn("x", instance_type)
        self.assertIn("y", instance_type)
        self.assertNotIn("z", instance_type)

        self.assertEqual(int, instance_type["x"])
        self.assertEqual(str, instance_type["y"])

        self.assertEqual(int, instance_type.env["x"])
        self.assertEqual(str, instance_type.env["y"])

    def test_object_type_consistency_with_class_type(self):
        """Test that ObjectType is consistent with its corresponding ClassType."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        instance_type = plain_type.instance_type
        
        self.assertIs(instance_type, plain_type.instance_type)

        self.assertEqual(instance_type.name, plain_type.name)

        self.assertIn("x", instance_type.env)
        self.assertIn("y", instance_type.env)

    def test_constructor_type_inference(self):
        """Test that constructor types are properly inferred from __init__ methods."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        instance_type = plain_type.instance_type
        
        self.assertIn("x", instance_type)
        self.assertIn("y", instance_type)
        self.assertEqual(int, instance_type["x"])
        self.assertEqual(str, instance_type["y"])

    def test_method_signature_transformation(self):
        """Test that method signatures are properly transformed for instance access."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        instance_type = plain_type.instance_type
        
        self.assertIn("combine", instance_type)

        combine_sig = instance_type["combine"]
        dom, cod = get_args(combine_sig)
        self.assertEqual(1, len(dom))
        self.assertEqual(str, cod)

    def test_class_instantiation_readiness(self):
        """Test that classes are ready for instantiation."""
        phase, env = self.typecheck("simple_class.py")
        
        plain_type = env["Plain"]
        
        self.assertIsNotNone(plain_type.constructor_types)
        self.assertEqual([int, str], plain_type.constructor_types)

        instance_type = plain_type.instance_type
        self.assertIsNotNone(instance_type)
        self.assertIsInstance(instance_type, ObjectType)

        self.assertIn("x", instance_type)
        self.assertIn("y", instance_type)
