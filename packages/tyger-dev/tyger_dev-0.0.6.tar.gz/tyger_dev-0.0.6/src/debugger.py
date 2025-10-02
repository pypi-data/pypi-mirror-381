import sys
import linecache

# Global stepping state
state = {
    'mode': 'step',  # 'step', 'next', 'continue'
    'stopframe': None,
    'stopline': None,
}

def tracefunc(frame, event, arg):
    if event != 'line':
        return tracefunc

    filename = frame.f_code.co_filename
    lineno = frame.f_lineno
    line = linecache.getline(filename, lineno).strip()

    if should_pause_here(frame):
        print(f"\n🛑 {filename}:{lineno} -> {line}")
        print(f"Locals: {frame.f_locals}")
        user_cmd(frame)

    return tracefunc

def should_pause_here(frame):
    if state['mode'] == 'step':
        return True
    elif state['mode'] == 'next':
        return frame == state['stopframe'] and frame.f_lineno != state['stopline']
    elif state['mode'] == 'continue':
        return False
    return True

def user_cmd(frame):
    while True:
        cmd = input("(dbg) ").strip()
        if cmd in {'s', 'step'}:
            state['mode'] = 'step'
            return
        elif cmd in {'n', 'next'}:
            state['mode'] = 'next'
            state['stopframe'] = frame
            state['stopline'] = frame.f_lineno
            return
        elif cmd in {'c', 'continue'}:
            state['mode'] = 'continue'
            return
        elif cmd in {'p', 'print'}:
            print(f"Locals: {frame.f_locals}")
        elif cmd.startswith('p '):
            expr = cmd[2:]
            try:
                result = eval(expr, frame.f_globals, frame.f_locals)
                print(repr(result))
            except Exception as e:
                print(f"Error: {e}")
        elif cmd in {'q', 'quit'}:
            sys.exit(0)
        else:
            print("Commands: step (s), next (n), continue (c), print (p), quit (q)")

import ast

source = """
def main():
    x = y = 5
    return x
main()
"""

def as_load(node: ast.expr) -> ast.expr:
    if isinstance(node, ast.Name):
        return ast.Name(id=node.id, ctx=ast.Load())
    raise NotImplementedError("Only Name nodes supported for now.")

class MultiAssignRewriter(ast.NodeTransformer):
    def visit_Assign(self, node):
        self.generic_visit(node)

        # Rewrite only multi-target assignments
        if len(node.targets) > 1:
            new_nodes = []
            value = node.value
            for target in reversed(node.targets):
                new_assign = ast.Assign(
                    targets=[target],
                    value=value
                )
                #new_assign.lineno = node.lineno
                #new_assign.col_offset = node.col_offset
                new_nodes.insert(0, new_assign)
                value = as_load(target)  # Load version of the just-assigned target
            return reversed(new_nodes)

        return node

tree = ast.parse(source)
tree = MultiAssignRewriter().visit(tree)
ast.fix_missing_locations(tree)

# Compile and run
code = compile(tree, filename="<ast>", mode="exec")


# Optional: see modified code
print(ast.unparse(tree))

sys.settrace(tracefunc)
exec(code)
#def main():
#    y = 5
#    x = y
#    return x
#main()
sys.settrace(None)