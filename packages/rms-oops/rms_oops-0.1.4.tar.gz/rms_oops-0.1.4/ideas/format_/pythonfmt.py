################################################################################
# oops/format_/pythonfmt.py: PythonFmt subclass of class Format
################################################################################

from oops.format_.format import Format

class PythonFmt(Format):
    """A PythonFormat is a format string defined using the default formatting
    mechanism in Python.
    """

    #===========================================================================
    def __init__(self, string):
        """The constructor for a Format object."""

        self.format = string

    def str(value):
        """Returns a character string indicating the value of a numeric quantity
        such as a coordinate.
        """

        return self.format % value

    def parse(string):
        """Returns a numeric value derived by parsing a character string."""

        return float(string)

################################################################################
# UNIT TESTS
################################################################################

import unittest

class Test_PythonFmt(unittest.TestCase):

    def runTest(self):
        pass

########################################
if __name__ == '__main__':
    unittest.main(verbosity=2)
################################################################################
