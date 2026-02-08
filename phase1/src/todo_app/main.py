"""
Main entry point for the Todo Application.

This module contains the main function that starts the console-based
todo application.
"""


def main():
    """
    Main function to start the todo application.
    """
    # Import here to avoid issues when running as module
    from .cli_interface import run_cli

    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try restarting the application.")


if __name__ == "__main__":
    # Import differently when run directly
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from cli_interface import run_cli

    try:
        run_cli()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try restarting the application.")