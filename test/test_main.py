# test/test_main.py
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest

class TestMain(unittest.TestCase):
    
    def test_main_exists(self):
        """Test that main.py file exists and can be imported"""
        # Check if main.py file exists
        main_path = os.path.join(os.path.dirname(__file__), '..', 'src', 'main.py')
        self.assertTrue(os.path.exists(main_path), "main.py should exist in src/")
        
        # Try to import main module
        try:
            # We use importlib to avoid running the game when importing
            import importlib.util
            spec = importlib.util.spec_from_file_location("main", main_path)
            main_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(main_module)
            
            # If we get here, import succeeded
            self.assertTrue(True, "main.py should be importable")
        except Exception as e:
            self.fail(f"Failed to import main.py: {e}")

if __name__ == '__main__':
    unittest.main()