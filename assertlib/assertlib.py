class Error(Exception):
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return repr(self.message)
    

def assertEqual(object, control):
    """
    This method asserts that an object is equal to a control.
    
    >>> assertEqual(1, 1)
    >>> assertEqual(str(1), '1')
    """
    message = []
    try:
        assert object == control
    except AssertionError:
        message.append("%s did not equal %s." % (repr(object), repr(control)))
        if type(object) != type(control):
            message.append("Additionally, %s did not equal %s" % (type(object), type(control)))
        raise Error(' '.join(message))


def assertEquals(object, control):
    """
    This method asserts that an object is equal to a control.
    
    >>> assertEquals(1, 1)
    >>> assertEquals(str(1), '1')
    """
    assertEqual(object, control)


def assertNotEqual(object, control):
    """
    This method asserts that an object is not equal to a control.
    
    >>> assertNotEqual(1, '1')
    >>> assertNotEqual(int("1"), '1')
    """
    message = []
    try:
        assert object != control
    except AssertionError:
        message.append("%s did not equal %s." % (repr(object), repr(control)))
        raise Error(' '.join(message))


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
    try:
        assert bool(object)
    except AssertionError:
        raise Error("%s did not evaluate to True." % object)


def assertFalse(object):
    """
    This method asserts that an object or expression evaluates to False.
    
    >>> assertFalse(False)
    """
    try:
        assert not bool(object)
    except AssertionError:
        raise Error("%s did not evaluate to False." % object)


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
    try:
        assert object is control
    except AssertionError:
        raise Error("%s is not %s" % (object, control))


def assertIsInstance(object, type):
    pass

def assertIsNot(object, control):
    try:
        assert object is not control
    except AssertionError:
        raise Error("%s is %s" % (object, control))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
