import itertools


def assertEqual(x, y):
    """
    This method asserts that an object is equal to a control.

    >>> assertEqual(1, 1)
    >>> assertEqual(str(1), '1')
    """
    if not x == y:
        raise AssertionError("%s is not equal to %s" % (x, y))

def assertPrecision(object, amount):
    """
    Asserts an object has x amount of precision.

    >>> assertPrecision(1.111, 3)
    """
    if not len(str(format(object)).partition('.')[2]) == int(amount):
        raise AssertionError("%s does not have %s precision." % (str(object), str(amount)))


def assertEquals(x, y):
    """
    This method asserts that x is equal to y.
    
    >>> assertEquals(1, 1)
    >>> assertEquals(str(1), '1')
    """
    assertEqual(x, y)


def assertNotEqual(x, y):
    """
    This method asserts that x is not equal to y.
    
    >>> assertNotEqual(1, '1')
    >>> assertNotEqual(int("1"), '1')
    """
    if x == y:
        raise AssertionError("%s did not equal %s." % (x, y))


def assertNotEquals(object, control):
    """
    This method asserts that an object is not equal to a control.
    
    >>> assertNotEquals(1, '1')
    >>> assertNotEquals(int("1"), '1')
    """
    assertNotEqual(object, control)


def assertTrue(object):
    """
    This method asserts that an object or expression evaluates to True.
    
    >>> assertTrue(1)
    """
    if not bool(object):
        raise AssertionError("%s did not evaluate to True." % object)


def assertFalse(object):
    """
    This method asserts that an object or expression evaluates to False.

    >>> assertFalse(False)
    """
    if bool(object):
        raise AssertionError("%s did not evaluate to False." % object)


def assertIs(object, control):
    """
    This method asserts that an object evaluates to a control.

    >>> def x():
    ...     return 1
    >>>
    >>> y = x()
    >>> z = x()
    >>> assertIs(y, z)
    >>> assertIs(1, y)
    >>> assertIs(1, z)
    """
    if not object is control:
        raise AssertionError("%s is not %s" % (object, control))


def assertIsInstance(object, type):
    if not isinstance(object, type):
        raise AssertionError("%s is not an instance of %s" % (object, type))


def assertIsNotInstance(object, type):
    if isinstance(object, type):
        raise AssertionError("%s is an instance of %s" % (object, type))


def assertIsNot(object, control):
    if object is control:
        raise AssertionError("%s is %s" % (object, control))


def assertAlmostEqual(first, second, places=None, epsilon=None):
    """
    This method will assert that two objects are almost equal.\
    You can use either places or epsilon as an arg, but you can't\
    use both. `When using epsilon, be aware of \
    <http://docs.python.org/tutorial/floatingpoint.html>`_.
    
    >>> assertAlmostEqual(1.1, 1.111, places=2)
    >>> assertAlmostEqual(1.1, 1.11, epsilon=0.01)
    
    """
    if first == second:
        return
    if places and epsilon:
        raise TypeError("specify delta or places not both")
    if epsilon is not None:
        if abs(first - second) <= epsilon:
            raise AssertionError(
            '%s != %s within %s delta' % (first, second, epsilon))
    else:
        if round(abs(second - first), places) == 0:
            raise AssertionError(
            '%s != %s within %s places' % (first, second, places))


def assertNotAlmostEqual(first, second, places=None, epsilon=None):
    """
    This method will assert that two objects are not almost equal.\
    You can use either places or epsilon as an arg, but you can't\
    use both. `When using epsilon, be aware of \
    <http://docs.python.org/tutorial/floatingpoint.html>`_.
    
    >>> assertNotAlmostEqual(1.1, 1.12, places=5)
    >>> assertNotAlmostEqual(1.1, 1.11, epsilon=5)
    
    """
    if first != second:
        return
    if first == second:
        raise AssertionError('%s == %s' % (first, second))
    if places and epsilon:
        raise TypeError("specify delta or places not both")
    if epsilon is not None:
        if abs(first - second) >= epsilon:
            raise AssertionError(
            '%s == %s within %s delta' % (first, second, epsilon))
    else:
        if round(abs(second - first), places) != 0:
            raise AssertionError(
            '%s == %s within %s places' % (first, second, places))


def assertSequenceEqual(seq1, seq2, assert_seq_types=False):
    if assert_seq_types and type(seq1) != type(seq2):
        raise TypeError("type %s != type %s" % (type(seq1), type(seq2)))
    if len(seq1) != len(seq2):
        raise AssertionError("len(%s) of seq1 != len(%s) of seq2" % (len(seq1), len(seq2)))
    if not all(a == b for a, b in itertools.izip(seq1, seq2)):
        raise AssertionError("%s is not equal to %s" % (seq1, seq2))


def assertSequenceNotEqual(seq1, seq2, assert_seq_types=True):
    if assert_seq_types and type(seq1) == type(seq2):
        raise TypeError("type %s == type %s" % (type(seq1), type(seq2)))
    if all(a != b for a, b in itertools.izip(seq1, seq2)):
        raise AssertionError("%s is equal to %s" % (seq1, seq2))

def assertEither(control, x, y):
    """Assert that x evaluates to either y or z."""
    if control != this or control != z:
        raise AssertionError("{0} is neither {1} or {2}".format(control,x,y))

def assertNotEither(control, x, y):
    """Assert that x evaluates to either y or z."""
    if control == this or control == z:
        raise AssertionError("{0} is neither {1} or {2}".format(control,x,y))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
