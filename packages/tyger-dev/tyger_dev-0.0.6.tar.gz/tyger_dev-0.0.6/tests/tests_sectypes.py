import os
import typing
import unittest

from tyger.diagnostics.diagnostics import TygerDiagnostic
from tyger.diagnostics.errors import TypeMismatchError
from tyger.discipline.sectypes.ToAST import SecurityASTElaborator
from tyger.discipline.sectypes.types import SecurityTypeSystem, TypeException
from tyger.discipline.sectypes.evidence import RuntimeException
from tyger.runtime.wrapper import Wrapper
from tyger.phases.elaboration import ElaborationPhase
from tyger.phases.type_check import TypingPhase
from tyger.parser import Parser
from tyger.driver import Driver
import ast

class TestResult:
    def __init__(self, scope: typing.Optional[dict[str, typing.Any]], errors: list[TygerDiagnostic]):
        self.scope = scope
        self.errors = errors
    
    def __getitem__(self, item):
        return self.scope[item]

class TestSectypes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        tests_dir = os.path.abspath(os.path.dirname(__file__))
        sources = os.path.join(tests_dir, "sources", "sectypes")
        cls.parser = Parser(sources)
        cls.driver = Driver([TypingPhase(SecurityTypeSystem()), ElaborationPhase(SecurityASTElaborator())])

    def execute(self, program_ast: ast.Module):
        b, _, errors = self.driver.run_2(program_ast)
        if errors:
            return TestResult(None, errors)
        #print(ast.dump(ast.fix_missing_locations(b), indent=2))
        scope = dict()
        print(ast.unparse(ast.fix_missing_locations(b)))
        exec(compile(ast.fix_missing_locations(b), filename="<ast>", mode="exec"), scope)
        return TestResult(scope, errors)
    
    def assertMultipleDiagnostics(self, actual_errors: list[TygerDiagnostic], expected_errors: list[type]):
        for expected, actual in zip(expected_errors, actual_errors):
            self.assertIsInstance(actual, expected)
        
    def nativeEquals(self, a, b):
        return self.assertEqual(Wrapper.unwrap_value(a), Wrapper.unwrap_value(b))

    def test_assignments_transitivity_fail(self):
        program = self.parser.parse("assignments_transitivity_fail.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_binop1(self):
        program = self.parser.parse("binop1.py")
        result = self.execute(program)
        self.assertEqual(result['w'], 3)

    def test_binop2(self):
        program = self.parser.parse("binop2.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))


    def test_taint1(self):
        program = self.parser.parse("taint1.py")
        test_result = self.execute(program)
        self.assertMultipleDiagnostics(test_result.errors, [TypeMismatchError])

    def test_taint2(self):
        program = self.parser.parse("taint2.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_taint3(self):
        program = self.parser.parse("taint3.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_func(self):
        program = self.parser.parse("func.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_if_join_error(self):
        program = self.parser.parse("if_join_error.py")
        test_result = self.execute(program)
        self.assertMultipleDiagnostics(test_result.errors, [TypeMismatchError])

    def test_if_join_ok(self):
        program = self.parser.parse("if_join_ok.py")
        scope = self.execute(program)
        self.assertEqual(1, scope['x'])

    def test_references_and_pc1_error(self):
        program = self.parser.parse("references_and_pc1_error.py")
        self.assertRaises(TypeException, lambda: self.execute(program))

    def test_references_and_pc1_ok(self):
        program = self.parser.parse("references_and_pc1_ok.py")
        self.assertEqual(1, self.execute(program)['y'])

    def test_references_and_pc2_error(self):
        program = self.parser.parse("references_and_pc2_error.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_hofunction_ok(self):
        program = self.parser.parse("hofunction_ok.py")
        self.assertEqual(True, self.execute(program)['x'])

    def test_hofunction_error(self):
        program = self.parser.parse("hofunction_error.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_unknown_application(self):
        program = self.parser.parse("unknown_application.py")
        self.assertEqual(True, self.execute(program)['x'])

    def test_lambda_typed_ok(self):
        program = self.parser.parse("lambda_typed_ok.py")
        self.assertEqual(3, self.execute(program)['x'])

    def test_lambda_typed_error(self):
        program = self.parser.parse("lambda_typed_error.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))


    def test_lambda_modular_not_forgetful(self):
        program = self.parser.parse("lambda_modular_not_forgetful.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))


    def test_example_1_1(self):
        program = self.parser.parse("example_1_1.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_example_nsu_fennel_etal_ok(self):
        program = self.parser.parse("example_nsu_fennel_etal_ok.py")
        self.assertEqual(True, Wrapper.unwrap_value(self.execute(program)['z_p']))


    def test_example_nsu_fennel_etal_error(self):
        program = self.parser.parse("example_nsu_fennel_etal_error.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))

    def test_implicit_flow_runtime(self):
        #this program should fail as the evidence of the pc should be <H,H>, and the expected type is <L,L>
        program = self.parser.parse("implicit_flow_runtime.py")
        self.assertRaises(RuntimeException, lambda: self.execute(program))
