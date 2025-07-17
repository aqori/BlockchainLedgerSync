# test_blockchainledgersync.py
"""
Tests for BlockchainLedgerSync module.
"""

import unittest
from blockchainledgersync import BlockchainLedgerSync

class TestBlockchainLedgerSync(unittest.TestCase):
    """Test cases for BlockchainLedgerSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainLedgerSync()
        self.assertIsInstance(instance, BlockchainLedgerSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainLedgerSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
