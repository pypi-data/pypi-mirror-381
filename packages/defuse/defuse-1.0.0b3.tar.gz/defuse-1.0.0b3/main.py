from defuse import ProjectAnalyzer

analyzer = ProjectAnalyzer()
analyzer.analyze_directory("/Users/antsticky/Desktop/korte")
analyzer.report()
analyzer.report_unused()
