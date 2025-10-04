import ast
import os
from collections import defaultdict

class ProjectAnalyzer:
    def __init__(self):
        self.class_defs = {}
        self.func_defs = set()
        self.method_defs = defaultdict(set)
        self.calls = defaultdict(int)
        self.aliases = {}
        self.instances = {}

    def analyze_file(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read(), filename=filepath)
        self._visit(tree)

    def _visit(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.aliases[alias.asname or alias.name] = alias.name
            elif isinstance(node, ast.ClassDef):
                self.class_defs[node.name] = {
                    "methods": set(),
                    "bases": [base.id for base in node.bases if isinstance(base, ast.Name)]
                }
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        self.method_defs[node.name].add(item.name)
            elif isinstance(node, ast.FunctionDef):
                self.func_defs.add(node.name)
            elif isinstance(node, ast.Assign):
                if isinstance(node.value, ast.Call) and isinstance(node.value.func, ast.Name):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            self.instances[target.id] = node.value.func.id
            elif isinstance(node, ast.Call):
                self._track_call(node)

    def _track_call(self, node):
        if isinstance(node.func, ast.Attribute):
            obj = node.func.value
            method = node.func.attr
            if isinstance(obj, ast.Name):
                instance = obj.id
                class_name = self.instances.get(instance)
                if class_name:
                    key = f"{class_name}.{method}"
                    self.calls[key] += 1
        elif isinstance(node.func, ast.Name):
            self.calls[node.func.id] += 1
        elif isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name):
            alias = node.func.value.id
            method = node.func.attr
            original = self.aliases.get(alias, alias)
            key = f"{original}.{method}"
            self.calls[key] += 1

    def analyze_directory(self, root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith(".py"):
                    self.analyze_file(os.path.join(root, file))

    def report(self):
        print("\n📦 Classes:")
        for cls, info in self.class_defs.items():
            print(f"  - {cls} (inherits: {info['bases']})")

        print("\n🔧 Functions:")
        for func in sorted(self.func_defs):
            print(f"  - {func}")

        print("\n🔧 Methods:")
        for cls, methods in self.method_defs.items():
            for method in sorted(methods):
                print(f"  - {cls}.{method}")

        print("\n📊 Usage:")
        for key, count in self.calls.items():
            print(f"  - {key} called {count} time(s)")
