"""
MicroDAG CLI - Command line interface entry point for PyPI installation
"""

def main():
    """Main CLI entry point for PyPI console_scripts"""
    from .cli.interface import CLI
    cli = CLI()
    cli.run()

if __name__ == "__main__":
    main()
