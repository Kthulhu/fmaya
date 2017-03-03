import unittest
from nose.plugins.attrib import attr

from .. import tf


# PURE

class Test_xyzAdd (unittest.TestCase):

    def test_xyzAdd_identities (self):
        self.assertEquals(tf.xyzAdd((0,0,0))((0,0,0)), (0,0,0))

    def test_xyzAdd_leftIdentity (self):
        self.assertEquals(tf.xyzAdd((0,0,0))((2,1,5)), (2,1,5))

    def test_xyzAdd_rightIdentity (self):
        self.assertEquals(tf.xyzAdd((3,2,5))((0,0,0)), (3,2,5))

    def test_xyzAdd_positives (self):
        self.assertEquals(tf.xyzAdd((3,2,5))((2,1,1)), (5,3,6))

    def test_xyzAdd_negatives (self):
        self.assertEquals(tf.xyzAdd((-2,-3,-1))((-2,-1,-3)), (-4,-4,-4))

    def test_xyzAdd_negativesAndPositives (self):
        self.assertEquals(tf.xyzAdd((-2,3,1))((2,-1,3)), (0,2,4))


class Test_xyzSub (unittest.TestCase):

    def test_xyzSub_identities (self):
        self.assertEquals(tf.xyzSub((0,0,0))((0,0,0)), (0,0,0))

    def test_xyzSub_noLeftIdentity (self):
        self.assertEquals(tf.xyzSub((0,0,0))((2,1,5)), (-2,-1,-5))

    def test_xyzSub_rightIdentity (self):
        self.assertEquals(tf.xyzSub((3,2,5))((0,0,0)), (3,2,5))

    def test_xyzSub_positives (self):
        self.assertEquals(tf.xyzSub((3,2,5))((2,1,1)), (1,1,4))

    def test_xyzSub_negatives (self):
        self.assertEquals(tf.xyzSub((-2,-3,-1))((-2,-1,-3)), (0,-2,2))

    def test_xyzSub_negativesAndPositives (self):
        self.assertEquals(tf.xyzSub((-2,3,1))((2,-1,3)), (-4,4,-2))


class Test_xyzMul (unittest.TestCase):

    def test_xyzMul_zeroes (self):
        self.assertEquals(tf.xyzMul((0,0,0))((0,0,0)), (0,0,0))

    def test_xyzMul_identities (self):
        self.assertEquals(tf.xyzMul((1,1,1))((1,1,1)), (1,1,1))

    def test_xyzMul_leftIdentity (self):
        self.assertEquals(tf.xyzMul((1,1,1))((2,1,5)), (2,1,5))

    def test_xyzMul_rightIdentity (self):
        self.assertEquals(tf.xyzMul((3,2,5))((1,1,1)), (3,2,5))

    def test_xyzMul_positives (self):
        self.assertEquals(tf.xyzMul((3,2,5))((2,1,1)), (6,2,5))

    def test_xyzMul_negatives (self):
        self.assertEquals(tf.xyzMul((-2,-3,-1))((-2,-1,-3)), (4,3,3))

    def test_xyzMul_negativesAndPositives (self):
        self.assertEquals(tf.xyzMul((-2,3,1))((2,-1,3)), (-4,-3,3))


class Test_xyzDiv (unittest.TestCase):

    def test_xyzDiv_dividingByZeroesRaises (self):
        self.assertRaises(ZeroDivisionError, lambda: tf.xyzDiv((1,1,1))((0,0,0)))

    def test_xyzDiv_identities (self):
        self.assertEquals(tf.xyzDiv((1,1,1))((1,1,1)), (1.0,1.0,1.0))

    def test_xyzDiv_noLeftIdentity (self):
        self.assertEquals(tf.xyzDiv((1,1,1))((2,1,5)), (0.5,1.0,0.2))

    def test_xyzDiv_rightIdentity (self):
        self.assertEquals(tf.xyzDiv((3,2,5))((1,1,1)), (3.0,2.0,5.0))

    def test_xyzDiv_allResultsPreservedAsOrPromotedToFloats (self):
        x, y, z = tf.xyzDiv((9,7,13))((3,3,4))
        self.assertTrue(type(x) == float and type(y) == float and type(z) == float)

    def test_xyzDiv_positives (self):
        self.assertEquals(tf.xyzDiv((3,2,5))((2,1,1)), (1.5,2.0,5.0))

    def test_xyzDiv_negatives (self):
        self.assertEquals(tf.xyzDiv((-2,-3,-3))((-2,-1,-3)), (1.0,3.0,1.0))

    def test_xyzDiv_negativesAndPositives (self):
        self.assertEquals(tf.xyzDiv((-2,3,3))((2,-1,3)), (-1.0,-3.0,1.0))


class Test_xyzScale (unittest.TestCase):

    def test_xyzScale_zeroZeroOut (self):
        self.assertEquals(tf.xyzScale(0)((-2,3,3)), (0,0,0))

    def test_xyzScale_hasIdentity (self):
        self.assertEquals(tf.xyzScale(1)((-2,3,1)), (-2,3,1))

    def test_xyzScale_scales (self):
        self.assertEquals(tf.xyzScale(3)((-2,3,1)), (-6,9,3))

    def test_xyzScale_inverseScales (self):
        self.assertEquals(tf.xyzScale(-1)((-2,3,1)), (2,-3,-1))


class Test_xyzAvg (unittest.TestCase):

    def test_xyzAvg_preservesIdentity (self):
        self.assertEquals(tf.xyzAvg([]), [])

    def test_xyzAvg_keepsSingletonElement (self):
        self.assertEquals(tf.xyzAvg([(2,1,-3)]), (2,1,-3))

    def test_xyzAvg_sameTriplesAverageToThemselves (self):
        self.assertEquals(tf.xyzAvg([(1,2,3)] * 35), (1,2,3))

    def test_xyzAvg_averagesSomeIntegers (self):
        self.assertEquals(tf.xyzAvg([(1,2,3),(2,3,1),(3,4,-3),(2,3,-1)]), (2,3,0))

