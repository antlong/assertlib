#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""assertlib is a library of standalone assertion methods.

  Examples:
    >>> import assertlib
    >>> assertlib.assertEither("a", "y", "a")
"""
import itertools
from types import StringType


def assertEqual(x, y):
    """Asserts that an object is equal to another.

    Examples:
      >>> assertEqual(1, 1)
      >>> assertEqual(str(1), '1')
    """
    if x == y:
        return
    else:
        raise AssertionError("%s is not equal to %s" % (x, y))


assertEquals = assertEqual


def assertPrecision(a, amount):
    """Asserts that an object has x amount of precision.

    Examples:
      >>> assertPrecision(1.111, 3)
    """
    if not len(str(format(a)).partition('.')[2]) == int(amount):
        raise AssertionError("{a} does not have {amount} precision.".format(
            str(a), str(amount))
    )


def assertNotEqual(a, b):
    """This method asserts that x is not equal to y.

    Examples:
      >>> assertNotEqual(1, '1')
      >>> assertNotEqual(int("1"), '1')
    """
    if a == b:
        raise AssertionError("%s did not equal %s." % (a, b))


assertNotEquals = assertNotEqual


def assertTrue(x):
    """Asserts that an object or expression evaluates to True.

    Examples:
      >>> assertTrue(1)
    """
    if not bool(x):
        raise AssertionError("{x} did not evaluate to True.".format(x))


def assertFalse(x):
    """
    This method asserts that an object or expression evaluates to False.

    Examples:
      >>> assertFalse(False)
    """
    if bool(x):
        raise AssertionError("%s did not evaluate to False." % x)


def assertIs(a, b):
    """
    This method asserts that an object evaluates to a control.

    Examples:
      >>> def x():
      ...     return 1
      >>>
      >>> y = x()
      >>> z = x()
      >>> assertIs( y, z )
      >>> assertIs( 1, y )
      >>> assertIs( 1, z )
    """
    if a is not b:
        raise AssertionError("{a} is not {b}".format(a, b))


def assertIsNot(a, b):
    """Asserts that a is not b

    Examples:
      >>> assertIsNot(1, 2)
    """
    if a is b:
        raise AssertionError("{a} is {b}".format(a, b))


def assertIsInstance(x, instanceof):
    """Assert an object is an instance of a type.

    Examples:
      >>> assertIsInstance("foo", StringType)
    """
    if not isinstance(x, instanceof):
        raise AssertionError("{} is not an instance of {}".format(x, instanceof))


def assertIsNotInstance(x, instanceof):
    """Asserts that an object is not an instance of a type.

    Examples:
      >>> assertIsNotInstance("x", int)
    """
    if isinstance(x, instanceof):
        raise AssertionError("{x} is an instance of {instanceof}".format(x, instanceof))


def assertAlmostEqual(a, b, places=None, epsilon=None):
    """Assert two things are almost equal.

    This method will assert that two objects are almost equal.\
    You can use either places or epsilon as an arg, but you can't\
    use both. `When using epsilon, be aware of \
    <http://docs.python.org/tutorial/floatingpoint.html>`_.

    Examples:
      >>> assertAlmostEqual(1.1, 1.111, places=2)
      >>> assertAlmostEqual(1.1, 1.11, epsilon=0.01)
    """
    if a == b:
        return
    if places and epsilon:
        raise TypeError("specify delta or places not both")
    if epsilon is not None:
        if abs(a - b) <= epsilon:
            raise AssertionError(
                '%s != %s within %s delta' % (a, b, epsilon))
    else:
        if round(abs(b - a), places) == 0:
            raise AssertionError(
                '%s != %s within %s places' % (a, b, places))


def assertNotAlmostEqual(a, b, places=None, epsilon=None):
    """
    This method will assert that two objects are not almost equal.\
    You can use either places or epsilon as an arg, but you can't\
    use both. `When using epsilon, be aware of \
    <http://docs.python.org/tutorial/floatingpoint.html>`_.
    
    >>> assertNotAlmostEqual(1.1, 1.12, places=5)
    >>> assertNotAlmostEqual(1.1, 1.11, epsilon=5)
    
    """
    if a != b:
        return
    if a == b:
        raise AssertionError('%s == %s' % (a, b))
    if places and epsilon:
        raise TypeError("specify delta or places not both")
    if epsilon is not None:
        if abs(a - b) >= epsilon:
            raise AssertionError(
                '%s == %s within %s delta' % (a, b, epsilon))
    else:
        if round(abs(b - a), places) != 0:
            raise AssertionError(
                '%s == %s within %s places' % (a, b, places))


def assertSequenceEqual(seq1, seq2, assert_seq_types=False):
    """Assers that a sequence is equal.

      >>> assertSequenceEqual([1,2,3], [1,2,3])
    """
    if assert_seq_types and type(seq1) != type(seq2):
        raise TypeError("type %s != type %s" % (type(seq1), type(seq2)))
    if len(seq1) != len(seq2):
        raise AssertionError("len(%s) of seq1 != len(%s) of seq2" % (len(seq1), len(seq2)))
    if not all(a == b for a, b in itertools.izip(seq1, seq2)):
        raise AssertionError("%s is not equal to %s" % (seq1, seq2))


def assertSequenceNotEqual(seq1, seq2, assert_seq_types=False):
    """Asserts that a swquence is not equal.

    Example:
      >>> assertSequenceNotEqual([1,2,3], [1,2,4])
    """
    if assert_seq_types and type(seq1) == type(seq2):
        raise TypeError("type %s == type %s" % (type(seq1), type(seq2)))
    if all(a != b for a, b in itertools.izip(seq1, seq2)):
        raise AssertionError("%s is equal to %s" % (seq1, seq2))


def assertEither(a, x, y):
    """Assert that a evaluates to either y or z.

    Examples:
      >>> a = 11
      >>> assertEither(a, 10, 11)
      >>> assertEither(str(a), "foo", "11")
      >>> x = ["foo"]
      >>> assertEither(x, ["bar"], ["foo"])
    """
    if a == x or a == y or a in x or a in y:
        return
    else:
        raise AssertionError("{0} is neither {1} or {2}".format(a, x, y))


def assertNotEither(a, x, y):
    """Assert that x does not evaluate to either y or z.

    Examples:
      >>> a = "A"
      >>> assertNotEither("a", "c", a)
      >>> assertNotEither("a", a, "1")
    """
    if a == x or a == y or a in x or a in y:
        raise AssertionError("{} is {} or {}".format(a, x, y))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
