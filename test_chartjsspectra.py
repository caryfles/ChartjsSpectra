# test_chartjsspectra.py
"""
Tests for ChartjsSpectra module.
"""

import unittest
from chartjsspectra import ChartjsSpectra

class TestChartjsSpectra(unittest.TestCase):
    """Test cases for ChartjsSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChartjsSpectra()
        self.assertIsInstance(instance, ChartjsSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChartjsSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
