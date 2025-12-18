# run_tests.py (in Video-Game-Hub/)
import sys
import os
import unittest
from time import sleep

def run_all_tests():
    """Run all tests in the test directory"""
    print("=" * 60)
    print("RUNNING ALL TESTS")
    print("=" * 60)
    
    # Add src to Python path
    src_dir = os.path.join(os.path.dirname(__file__), 'src')
    sys.path.insert(0, src_dir)
    
    # Discover tests
    loader = unittest.TestLoader()
    start_dir = os.path.join(os.path.dirname(__file__), 'test')
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Run tests
    sleep(2)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Exit with appropriate code
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    sys.exit(run_all_tests())