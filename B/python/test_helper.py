# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        print 'OK got: %s' % repr(got)
    else:
        prefix = '  X '
        print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))
