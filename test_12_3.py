import test_12_2
import test_runner
import unittest


testRan = unittest.TestSuite()
testRan.addTest(unittest.TestLoader().loadTestsFromTestCase(test_runner.TestRunner))
testRan.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_2.TournamentTest))


runner = unittest.TextTestRunner(verbosity=2)
runner.run(testRan)

