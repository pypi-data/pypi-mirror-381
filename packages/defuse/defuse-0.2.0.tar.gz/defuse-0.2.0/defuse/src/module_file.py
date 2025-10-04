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

            elif isinstance(node, ast.Attribute):
                self._track_attribute_access(node, filepath)

    def _resolve_method_class(self, class_name, method):
        if method in self.method_defs.get(class_name, {}):
            return class_name
        for base in self.class_defs.get(class_name, {}).get("bases", []):
            resolved = self._resolve_method_class(base, method)
            if resolved:
                return resolved
        return None

    def _track_call(self, node, filepath):
        lineno = getattr(node, 'lineno', '?')

        if isinstance(node.func, ast.Attribute):
            obj = node.func.value
            method = node.func.attr
            if isinstance(obj, ast.Name):
                instance = obj.id
                class_name = self.instances.get(instance)
                if class_name:
                    resolved_class = self._resolve_method_class(class_name, method)
                    if resolved_class:
                        key = f"{resolved_class}.{method}"
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
            resolved_class = self._resolve_method_class(original, method)
            if resolved_class:
                key = f"{resolved_class}.{method}"
                self.calls[key].add((filepath, lineno))

    def _track_attribute_access(self, node, filepath):
        lineno = getattr(node, 'lineno', '?')
        attr = node.attr
        obj = node.value

        if isinstance(obj, ast.Name):
            name = obj.id

            # Instance-level access
            class_name = self.instances.get(name)
            if class_name:
                resolved_class = self._resolve_method_class(class_name, attr)
                if resolved_class:
                    key = f"{resolved_class}.{attr}"
                    self.calls[key].add((filepath, lineno))
                    self.calls[class_name].add((filepath, lineno))  # mark class as used
                    return

            # Class-level access
            original = self.aliases.get(name, name)
            if original in self.class_defs:
                resolved_class = self._resolve_method_class(original, attr)
                if resolved_class:
                    key = f"{resolved_class}.{attr}"
                    self.calls[key].add((filepath, lineno))
                    self.calls[original].add((filepath, lineno))  # mark class as used



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

    def get_unused_classes(self):
        used_classes = {key.split('.')[0] for key in self.calls if '.' in key}
        used_classes |= {key for key in self.calls if key in self.class_defs}
        return sorted(set(self.class_defs.keys()) - used_classes)

    def get_unused_methods(self):
        unused = []
        for cls, methods in self.method_defs.items():
            for method in methods:
                key = f"{cls}.{method}"
                if key not in self.calls:
                    unused.append(key)
        return sorted(unused)

    def get_unused_functions(self):
        called_functions = {key for key in self.calls if '.' not in key}
        return sorted({
            name for name in self.func_defs
            if name not in called_functions and name not in self.builtin_funcs
        })

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
        unused_classes = self.get_unused_classes()
        unused_methods = self.get_unused_methods()
        unused_functions = self.get_unused_functions()

        if all([not unused_classes, not unused_methods, not unused_functions]):
            print("\n✅ All elements are used.")
            return

        print("\n🧹 Unused Elements:")

        if unused_classes:
            print("\n🔸 Unused Classes:")
            for cls in unused_classes:
                print(f"  - {cls}")

        if unused_methods:
            print("\n🔸 Unused Methods:")
            for method in unused_methods:
                print(f"  - {method}")

        if unused_functions:
            print("\n🔸 Unused Functions:")
            for func in unused_functions:
                print(f"  - {func}")
