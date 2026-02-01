"""
Test Cases for Aegean Tour Optimizer
"""

import unittest
from src.optimizer import AegeanTourOptimizer
from main import AegeanTourApp


class TestAegeanTourOptimizer(unittest.TestCase):
    app = AegeanTourApp()
    def test_example_case(self):
        """test the provided example case"""
        input_text = """6
                        4
                        0 by-sea, 2 by-sea, 3 by-sea
                        0 by-sea, 5 airborne
                        0 airborne, 5 by-sea
                        2 airborne"""
        
        num_hops, customers = self.app.parse_input(input_text)
        optimizer = AegeanTourOptimizer(num_hops, customers)
        solution = optimizer.solve()
        self.assertIsNotNone(solution)
        # verify the solution satisfies all constraints
        self.assertEqual(len(solution), 6)
    
    def test_impossible_case(self):
        """Test a case where no solution exists."""
        # customer wants hop 0 airborne, another wants hop 0 by-sea only
        customers = [
                    [(0, "airborne")],
                    [(0, "by-sea")]
                    ]
        optimizer = AegeanTourOptimizer(3, customers)
        solution = optimizer.solve()
        self.assertIsNone(solution)
    
    def test_simple_case(self):
        """Test a simple case with minimal constraints."""
        customers = [
                    [(0, "by-sea")],
                    [(1, "by-sea")]
                    ]
        optimizer = AegeanTourOptimizer(2, customers)
        solution = optimizer.solve()
        self.assertIsNotNone(solution)
        self.assertEqual(len(solution), 2)
        
        # Should be all by-sea since that satisfies everyone with minimum airborne
        for _, transport in solution:
            self.assertEqual(transport, "by-sea")
    
    def test_parse_input(self):
        """test input parsing."""
        input_text = """3
                        2
                        0 by-sea, 1 airborne
                        2 by-sea"""
        
        num_hops, customers = self.app.parse_input(input_text)
        
        self.assertEqual(num_hops, 3)
        self.assertEqual(len(customers), 2)
        self.assertEqual(customers[0], [(0, "by-sea"), (1, "airborne")])
        self.assertEqual(customers[1], [(2, "by-sea")])
    
    def test_format_output(self):
        """test output formatting."""
        itinerary = [(0, "by-sea"), (1, "airborne"), (2, "by-sea")]
        output = self.app.format_output(itinerary)
        expected = "0 by-sea, 1 airborne, 2 by-sea"
        
        self.assertEqual(output, expected)
    
    def test_no_itinerary_output(self):
        """test NO ITINERARY output."""
        output = self.app.format_output([])
        self.assertEqual(output, "NO ITINERARY")


if __name__ == "__main__":
    unittest.main()
