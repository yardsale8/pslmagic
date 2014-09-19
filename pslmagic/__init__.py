from IPython.core.magic import Magics, magics_class, line_cell_magic
from subprocess import check_output, STDOUT

EXE_ADDRESS = '/Users/tiverson/Desktop/osx-dist/bin/assignment1-osx'


@magics_class
class ParselTongueMagics(Magics):
    """Magic for the hylang lisp language
    """
    def __init__(self, shell):
        """
        Parameters
        ----------
        shell : IPython shell

        """
        super(ParselTongueMagics, self).__init__(shell)

    @line_cell_magic
    def psl(self, line,  cell=None, filename='<input>', symbol='single'):
        """ The is the line magic for parselTongue.  It will interpret a line of
        psl and print the resulting output. """
        source = cell if cell else line
        command = "echo '" + source + "' | " + EXE_ADDRESS + ' --interp'
        print "command is", command
        output = check_output(command, shell=True, stderr=STDOUT)
        #  The next list is a very dirty check for errors
        if ":" in output:
            raise SyntaxError(output)
        else:
            print output


def load_ipython_extension(ip):
    """Load the extension in IPython."""
    ip.register_magics(ParselTongueMagics)
