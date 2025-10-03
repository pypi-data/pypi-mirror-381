import os
import subprocess
import sys

def main():
    # Path to the compiled binary installed with the package
    binary_path = os.path.join(os.path.dirname(__file__), '..', 'bin', 'insthost')
    binary_path = os.path.abspath(binary_path)

    if not os.path.exists(binary_path):
        print("Error: insthost binary not found.")
        sys.exit(1)

    # Forward all CLI args
    subprocess.run([binary_path] + sys.argv[1:])

if __name__ == "__main__":
    main()
