#!/usr/bin/env python3
"""hmm CLI - Simple entry point"""

import os
import sys
import subprocess

def main():
    """Main entry point for hmm CLI"""
    # Call the actual hmm script in bin/
    script_path = os.path.join(os.path.dirname(__file__), 'bin', 'hmm')
    if os.path.exists(script_path):
        subprocess.call([sys.executable, script_path] + sys.argv[1:])
    else:
        # Fallback - try to find it in installed location
        import importlib.resources
        print("hmm CLI")
        print("Run: hmm install, hmm uninstall, or hmm status")

if __name__ == '__main__':
    main()

