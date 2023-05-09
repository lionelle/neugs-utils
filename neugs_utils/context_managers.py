from io import StringIO 
import sys

#inspired by https://stackoverflow.com/questions/16571150/how-to-capture-stdout-output-from-a-python-function-call
class Capturing(list):
    """Context capture class, that focuses on capturing output and allowing
    for StringIO input. 

    output is a list is list that contains every line of output as an item.

    Example:
        with Capturing("hello") as output:
            some_func()
        self.assertEqual(output[0], "hello")
    """
    def __init__(self, input = None):
        """Setups the context. Allows for an optional input string. 

        Args:
            input (str or StringIO(), optional): Can be a string, or StringIO(), 
            replaces sys.in context. Defaults to None which means sys.in is not modified.
        """
        if input is not None:
            if type(input) == str:
                input =StringIO(input)
            self._input = input
        else:
            self._input = None

    def __enter__(self):
        self._stdout = sys.stdout
        if self._input is not None:
            self._stdin = sys.stdin
            sys.stdin = self._input
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout
        if self._input is not None:
            sys.stdin = self._stdin
