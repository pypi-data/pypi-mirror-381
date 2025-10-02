from pathlib import Path
import unittest
from typing import get_args

from tyger.discipline.classes.class_type import ClassType
from tyger.discipline.classes.object_type import ObjectType
from tyger.discipline.simple.types import SimpleTypeSystem
from tyger.parser import Parser
from tyger.phases.type_check import TypingPhase


class ClassTypingInstantiationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.sources = Path(__file__).parent / "sources"
        cls.parser = Parser(str(cls.sources))

    def typecheck(self, filename: str):
        module = self.parser.parse(filename)
        phase = TypingPhase(SimpleTypeSystem(), file_path=self.parser.build_file_path(filename))
        env = phase.type_check_stmts(module.body)
        return phase, env

    def test_basic_class_definitions_for_instantiation(self):
        """Test that basic class definitions work for instantiation."""
        phase, env = self.typecheck("simple_instantiation.py")
        
        self.assertIn("SimpleClass", env)
        self.assertIn("ClassWithDefaults", env)
        self.assertIn("EmptyClass", env)
        self.assertIn("ClassWithClassAttrs", env)
        self.assertIn("Base", env)
        self.assertIn("Child", env)

        simple_type = env["SimpleClass"]
        self.assertIsInstance(simple_type, ClassType)
        self.assertEqual([int], simple_type.constructor_types)

        defaults_type = env["ClassWithDefaults"]
        self.assertEqual([int, str], defaults_type.constructor_types)

        empty_type = env["EmptyClass"]
        self.assertEqual([], empty_type.constructor_types)

        attrs_type = env["ClassWithClassAttrs"]
        self.assertEqual([str], attrs_type.constructor_types)

        base_type = env["Base"]
        child_type = env["Child"]
        self.assertEqual([int], base_type.constructor_types)
        self.assertEqual([int, str], child_type.constructor_types)
        self.assertEqual(["Base"], child_type.bases)

    def test_global_instantiated_objects_exist(self):
        """Test that instantiated objects exist in the global environment."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        self.assertEqual([], phase.diagnostics)

        expected_objects = ['obj_a', 'obj_b', 'obj_c', 'obj_empty', 'obj_parent', 'obj_child']
        for obj_name in expected_objects:
            self.assertIn(obj_name, env, f"Object {obj_name} should be in global environment")
            
        for obj_name in expected_objects:
            obj = env[obj_name]
            self.assertIsInstance(obj, ObjectType, f"Object {obj_name} should be ObjectType")

    def test_instantiated_object_subenvironments(self):
        """Test that instantiated objects have proper subenvironments."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_a = env["obj_a"]
        self.assertEqual("A", obj_a.name)
        self.assertEqual([], obj_a.bases)
        self.assertIn("x", obj_a.env)
        self.assertIn("get_x", obj_a.env)
        self.assertEqual(int, obj_a.env["x"])

        obj_b = env["obj_b"]
        self.assertEqual("B", obj_b.name)
        self.assertEqual([], obj_b.bases)
        self.assertIn("s", obj_b.env)
        self.assertIn("n", obj_b.env)
        self.assertIn("describe", obj_b.env)
        self.assertEqual(str, obj_b.env["s"])
        self.assertEqual(int, obj_b.env["n"])

        obj_c = env["obj_c"]
        self.assertEqual("C", obj_c.name)
        self.assertEqual([], obj_c.bases)
        self.assertIn("value", obj_c.env)
        self.assertIn("class_attr", obj_c.env)
        self.assertIn("get_both", obj_c.env)
        self.assertEqual(str, obj_c.env["value"])
        self.assertEqual(int, obj_c.env["class_attr"])

    def test_empty_class_instantiation_subenvironment(self):
        """Test that empty class instantiation has empty subenvironment."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_empty = env["obj_empty"]
        self.assertEqual("Empty", obj_empty.name)
        self.assertEqual([], obj_empty.bases)
        self.assertEqual(0, len(obj_empty.env), "Empty class should have empty environment")

    def test_inheritance_instantiation_subenvironments(self):
        """Test that inheritance instantiation has proper subenvironments."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_parent = env["obj_parent"]
        self.assertEqual("Parent", obj_parent.name)
        self.assertEqual([], obj_parent.bases)
        self.assertIn("p", obj_parent.env)
        self.assertEqual(int, obj_parent.env["p"])

        obj_child = env["obj_child"]
        self.assertEqual("Child", obj_child.name)
        self.assertEqual(["Parent"], obj_child.bases)
        self.assertIn("p", obj_child.env)
        self.assertIn("c", obj_child.env)
        self.assertEqual(int, obj_child.env["p"])
        self.assertEqual(str, obj_child.env["c"])

    def test_instantiated_object_method_signatures(self):
        """Test that instantiated objects have proper method signatures."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_a = env["obj_a"]
        get_x_sig = obj_a.env["get_x"]
        dom, cod = get_args(get_x_sig)
        self.assertEqual(0, len(dom))
        self.assertEqual(int, cod)

        obj_b = env["obj_b"]
        describe_sig = obj_b.env["describe"]
        dom, cod = get_args(describe_sig)
        self.assertEqual(0, len(dom))
        self.assertEqual(str, cod)

        obj_c = env["obj_c"]
        get_both_sig = obj_c.env["get_both"]
        dom, cod = get_args(get_both_sig)
        self.assertEqual(0, len(dom))

    def test_instantiated_objects_vs_class_types(self):
        """Test that instantiated objects are different from class types."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        class_a = env["A"]
        class_b = env["B"]
        class_c = env["C"]

        obj_a = env["obj_a"]
        obj_b = env["obj_b"]
        obj_c = env["obj_c"]

        self.assertIsInstance(class_a, ClassType)
        self.assertIsInstance(class_b, ClassType)
        self.assertIsInstance(class_c, ClassType)

        self.assertIsInstance(obj_a, ObjectType)
        self.assertIsInstance(obj_b, ObjectType)
        self.assertIsInstance(obj_c, ObjectType)

        self.assertIs(obj_a, class_a.instance_type)
        self.assertIs(obj_b, class_b.instance_type)
        self.assertIs(obj_c, class_c.instance_type)

    def test_instantiated_object_attribute_access(self):
        """Test that instantiated objects have proper attribute access."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_a = env["obj_a"]
        self.assertIn("x", obj_a)
        self.assertIn("get_x", obj_a)
        self.assertEqual(int, obj_a["x"])

        obj_b = env["obj_b"]
        self.assertIn("s", obj_b)
        self.assertIn("n", obj_b)
        self.assertIn("describe", obj_b)
        self.assertEqual(str, obj_b["s"])
        self.assertEqual(int, obj_b["n"])

        obj_c = env["obj_c"]
        self.assertIn("value", obj_c)
        self.assertIn("class_attr", obj_c)
        self.assertIn("get_both", obj_c)
        self.assertEqual(str, obj_c["value"])
        self.assertEqual(int, obj_c["class_attr"])

    def test_instantiated_object_environment_operations(self):
        """Test that instantiated objects support environment operations."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_a = env["obj_a"]
        
        self.assertIn("x", obj_a)
        self.assertIn("get_x", obj_a)
        self.assertNotIn("nonexistent", obj_a)

        self.assertEqual(int, obj_a["x"])

        self.assertIsInstance(obj_a.env, dict)
        self.assertIn("x", obj_a.env)
        self.assertIn("get_x", obj_a.env)

    def test_multiple_instantiations_same_class(self):
        """Test that multiple instantiations of the same class work correctly."""
        test_code = """
class Multi:
    def __init__(self, value: int):
        self.value = value

obj1 = Multi(1)
obj2 = Multi(2)
obj3 = Multi(3)
"""
        
        test_file = self.sources / "temp_multi_global.py"
        test_file.write_text(test_code)
        
        try:
            phase, env = self.typecheck("temp_multi_global.py")
            
            self.assertEqual([], phase.diagnostics)

            self.assertIn("obj1", env)
            self.assertIn("obj2", env)
            self.assertIn("obj3", env)

            obj1 = env["obj1"]
            obj2 = env["obj2"]
            obj3 = env["obj3"]

            self.assertIsInstance(obj1, ObjectType)
            self.assertIsInstance(obj2, ObjectType)
            self.assertIsInstance(obj3, ObjectType)

            class_multi = env["Multi"]
            self.assertIs(obj1, class_multi.instance_type)
            self.assertIs(obj2, class_multi.instance_type)
            self.assertIs(obj3, class_multi.instance_type)

            self.assertIs(obj1, obj2)
            self.assertIs(obj2, obj3)

            self.assertEqual(obj1.env, obj2.env)
            self.assertEqual(obj2.env, obj3.env)
            
        finally:
            if test_file.exists():
                test_file.unlink()

    def test_instantiated_object_type_consistency(self):
        """Test that instantiated objects maintain type consistency."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_a = env["obj_a"]
        class_a = env["A"]

        self.assertEqual(obj_a.name, class_a.name)

        self.assertEqual(obj_a.bases, class_a.instance_type.bases)

        self.assertIs(obj_a, class_a.instance_type)

        self.assertEqual(obj_a.env, class_a.instance_type.env)

    def test_instantiated_object_inheritance_consistency(self):
        """Test that instantiated objects maintain inheritance consistency."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        obj_child = env["obj_child"]
        class_child = env["Child"]
        
        self.assertEqual("Child", obj_child.name)
        self.assertEqual(["Parent"], obj_child.bases)

        self.assertIn("p", obj_child.env)
        self.assertIn("c", obj_child.env)

        self.assertEqual(int, obj_child.env["p"])
        self.assertEqual(str, obj_child.env["c"])

    def test_instantiated_object_global_environment_integration(self):
        """Test that instantiated objects are properly integrated into global environment."""
        phase, env = self.typecheck("instantiation_tests.py")
        
        expected_items = [
            "A", "B", "C", "Empty", "Parent", "Child",
            "obj_a", "obj_b", "obj_c", "obj_empty", "obj_parent", "obj_child"
        ]

        for item in expected_items:
            self.assertIn(item, env, f"Item {item} should be in global environment")

        class_a = env["A"]
        obj_a = env["obj_a"]

        self.assertIsInstance(class_a, ClassType)
        self.assertIsInstance(obj_a, ObjectType)

        self.assertIs(obj_a, class_a.instance_type)
