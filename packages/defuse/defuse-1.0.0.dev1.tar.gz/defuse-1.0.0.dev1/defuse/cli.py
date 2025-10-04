import argparse
from defuse import ProjectAnalyzer

def main():
    parser = argparse.ArgumentParser(description="Defuse: Python usage analyzer")
    parser.add_argument("check", nargs="?", help="Run usage analysis")
    parser.add_argument("--path", required=True, help="Path to the Python project")
    parser.add_argument("--fail-on-unused", action="store_true", help="Exit with error if unused code is found")

    args = parser.parse_args()

    analyzer = ProjectAnalyzer()
    analyzer.analyze_directory(args.path)
    analyzer.report()

    if args.fail_on_unused:
        unused = []
        unused.extend(analyzer.get_unused_classes())
        unused.extend(analyzer.get_unused_methods())
        unused.extend(analyzer.get_unused_functions())
        if unused:
            print("\n❌ Unused code detected. Failing as requested.")
            exit(1)

    analyzer.report_unused()

if __name__ == "__main__":
    main()
