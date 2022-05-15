import unittest
from damavis_challenge import numberOfAvailableDifferentPaths

class PruebasUnitarias(unittest.TestCase):
    def test1(self):
        board=(4,3)
        snake=[(2,2), (3,2), (3,1), (3,0), (2,0), (1,0), (0,0)]
        depth=3
        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), 7)
    
    def test2(self):
        board = (2,3)
        snake = [(0,2), (0,1), (0,0), (1,0), (1,1), (1,2)]
        depth=10
        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), 1)
    
    def test3(self):
        board=(10,10)
        snake=[(5,5), (5,4), (4,4), (4,5)]
        depth=4
        self.assertEqual(numberOfAvailableDifferentPaths(board, snake, depth), 81)
    

if __name__=='__main__':
    unittest.main()