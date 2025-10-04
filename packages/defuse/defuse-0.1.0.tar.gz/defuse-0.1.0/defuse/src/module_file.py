import ast
import os
import builtins
from collections import defaultdict


def is_virtual_env(path):
    return os.path.isfile(os.path.join(path, 'pyvenv.cfg'))


def annotate_parents(tree):
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            child.parent = node


class ProjectAnalyzer:
    def __init__(self):
        self.class_defs = {}
        self.func_defs = {}  # name → (file, lineno)
        self.method_defs = defaultdict(dict)  # class → method → (file, lineno)
        self.calls = defaultdict(set)  # key → set of (filename, lineno)
        self.aliases = {}
        self.instances = {}
        self.builtin_funcs = set(dir(builtins))

    def analyze_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            try:
                tree = ast.parse(f.read(), filename=filepath)
                annotate_parents(tree)
                self._visit(tree, filepath)
            except SyntaxError as e:
                print(f"⚠️ Skipping {filepath} due to syntax error: {e}")

    def _visit(self, tree, filepath):
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.aliases[alias.asname or alias.name] = alias.name

            elif isinstance(node, ast.ClassDef):
                self.class_defs[node.name] = {
                    "bases": [base.id for base in node.bases if isinstance(base, ast.Name)]
                }
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        self.method_defs[node.name][item.name] = (filepath, item.lineno)

            elif isinstance(node, ast.FunctionDef):
                if not isinstance(getattr(node, 'parent', None), ast.ClassDef):
                    self.func_defs[node.name] = (filepath, node.lineno)

            elif isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Call):
                    func = node.value.func
                    if isinstance(func, ast.Name):
                        class_name = self.aliases.get(func.id, func.id)
                        if class_name in self.class_defs:
                            for target in node.targets:
                                if isinstance(target, ast.Name):
                                    self.instances[target.id] = class_name
                                    self.calls[class_name].add((filepath, node.lineno))

            elif isinstance(node, ast.Call):
                self._track_call(node, filepath)

    def _track_call(self, node, filepath):
        lineno = getattr(node, 'lineno', '?')
        if isinstance(node.func, ast.Attribute):
            obj = node.func.value
            method = node.func.attr
            if isinstance(obj, ast.Name):
                instance = obj.id
                class_name = self.instances.get(instance)
                if class_name:
                    key = f"{class_name}.{method}"
                    self.calls[key].add((filepath, lineno))

        elif isinstance(node.func, ast.Name):
            name = node.func.id
            original = self.aliases.get(name, name)
            if original in self.class_defs:
                self.calls[original].add((filepath, lineno))
            elif name not in self.builtin_funcs:
                self.calls[name].add((filepath, lineno))

        elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            alias = node.func.value.id
            method = node.func.attr
            original = self.aliases.get(alias, alias)
            key = f"{original}.{method}"
            self.calls[key].add((filepath, lineno))

    def analyze_directory(self, root_dir):
        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [
                d for d in dirs
                if not is_virtual_env(os.path.join(root, d)) and d not in {'venv', '.venv', 'env', '.env', '__pycache__'}
            ]
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    self.analyze_file(filepath)

    def categorize_usage(self):
        init_calls = {}
        method_calls = {}
        function_calls = {}

        for key, locations in self.calls.items():
            if '.' in key:
                method_calls[key] = locations
            elif key[0].isupper():
                init_calls[key] = locations
            elif key not in self.builtin_funcs:
                function_calls[key] = locations

        return init_calls, method_calls, function_calls

    def report(self):
        print("\n📦 Classes:")
        for cls, info in self.class_defs.items():
            print(f"  - {cls} (inherits: {info['bases']})")

        print("\n🔧 Functions:")
        for func, (file, line) in sorted(self.func_defs.items()):
            print(f"  - {func} ({file}:{line})")

        print("\n🔧 Methods:")
        for cls, methods in self.method_defs.items():
            for method, (file, line) in sorted(methods.items()):
                print(f"  - {cls}.{method} ({file}:{line})")

        init_calls, method_calls, function_calls = self.categorize_usage()

        print("\n📊 Usage Breakdown:")

        print("\n🔹 Class Instantiations:")
        for key, locations in init_calls.items():
            print(f"  - {key} instantiated {len(locations)} time(s)")
            for file, line in sorted(locations):
                print(f"    • {file}:{line}")

        print("\n🔹 Method Calls:")
        for key, locations in method_calls.items():
            print(f"  - {key} called {len(locations)} time(s)")
            for file, line in sorted(locations):
                print(f"    • {file}:{line}")

        print("\n🔹 Function Calls:")
        for key, locations in function_calls.items():
            print(f"  - {key} called {len(locations)} time(s)")
            for file, line in sorted(locations):
                print(f"    • {file}:{line}")

    def report_unused(self):
        used_classes = {key.split('.')[0] for key in self.calls if '.' in key}
        used_classes |= {key for key in self.calls if key in self.class_defs}
        unused_classes = set(self.class_defs.keys()) - used_classes
        
        unused_methods = []
        for cls, methods in self.method_defs.items():
            for method in methods:
                key = f"{cls}.{method}"
                if key not in self.calls:
                    unused_methods.append(key)
        
        called_functions = {key for key in self.calls if '.' not in key}
        unused_functions = {
            name for name in self.func_defs
            if name not in called_functions and name not in self.builtin_funcs
        }
        
        if all([not unused_classes, not unused_methods, not unused_functions]):
            print("\nAll Element is used")
            return

        print("\nUnused Elements:")


        if unused_classes:
            print("\nUnused Classes:")
            for cls in sorted(unused_classes):
                print(f"  - {cls}")


        if unused_methods:
            print("\nUnused Methods:")
            for method in sorted(unused_methods):
                print(f"  - {method}")

        
        if unused_functions:
            print("\nUnused Functions:")
            for func in sorted(unused_functions):
                print(f"  - {func}")
