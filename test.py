from bloomnames import  BloomNames
import unittest

class TestBloom(unittest.TestCase):

    def testBasic(self):
        import zlib
        bloom = BloomNames()
        bloom.add("bitworking")
        bloom.add("austin")    
          
        self.assertEqual(7016, len(hex(bloom.getfilter())))
        self.assertEqual(90, len(zlib.compress(hex(bloom.getfilter()))))


        self.assertTrue("bitworking" in bloom)
        self.assertTrue("austin" in bloom)
        self.assertFalse("fred" in bloom)

    def testFalsePositiveRate(self):
        import random
        random.seed(0L)

        # Make up 3000 long names
        members = {}
        while len(members) < 3000:
          members["".join([ random.choice("abcdef") for j in range(40)])] = 1
          
        # Make up another 3000 long names not in the first list
        nonmembers = {}
        while len(nonmembers) < 1000:
          name = "".join([ random.choice("abcdef") for j in range(40)])
          if not name in members and not name in nonmembers:
            nonmembers[name] = 1

        bl = BloomNames()
        for k in members.iterkeys():
          bl.add(k)

        false_positives = 0
        for k in nonmembers.iterkeys():
          if k in bl:
            false_positives += 1
          
        self.assertEqual(9, false_positives)




if __name__ == '__main__':
    unittest.main()
