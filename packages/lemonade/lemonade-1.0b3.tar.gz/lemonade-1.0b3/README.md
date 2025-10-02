# lemonade

Lemonade is a Python port of
[the LEMON Parser Generator](http://www.hwaci.com/sw/lemon/)
written by D. Richard Hipp.

Lemonade can be used in the traditional fashion to create a standalone
parser:

    lemonade gram.y

The above command generates `gram.py`, which you can include in your
project.

Since Python is a dynamic language, Lemonade could also enable client
software to generate a parser from a user-supplied `.y` file, and then
use the generated parser on the fly.

This is the beta release of Lemonade.  There is no documentation yet.
You may find
[the original LEMON documentation](http://www.hwaci.com/sw/lemon/lemon.html)
helpful.

However, many of LEMON's "%" directives are irrelevant in Python;
therefore, they have been eliminated in Lemonade.  Further, Lemonade
does not allow code fragments ("{}") within the grammar file.
Instead, the reduce actions are specified in a separate delegate
class.  See the `examples` directory for an example.
