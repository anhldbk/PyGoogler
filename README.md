PyGoogler
===================

PyGoogler is a Python library for scraping Google search results. 
It's a customized version of [xgoogle](https://pypi.python.org/pypi/xgoogle). 
Several bugs regarding encoding are fixed. PyGoogler is easier to use than [xgoogle](https://pypi.python.org/pypi/xgoogle).

Installation
-------------
> - Download the project
> - Make the project importable via sys.path.append() or anything else
> - Import the class and use it 

Example
-------------
```python
#!/usr/bin/python
from PyGoogler import Googler


def doSearch(googler):
    # googler: an instance of Googler
    print '-----------[ Instance %s ]--------------\n' % googler.__class__.__name__
    word = 'bigsonata'
    print 'Searching for %s...' % word
    results = googler.search(word, Googler.DOMAIN_VIETNAMESE)
    print 'Result(s) found: %s' % len(results)

    count = 0
    for result in results:
        count += 1
        print '%s. %s' % (count, result)


# Demo 1: Normal Googler
doSearch(Googler())

# Demo 2: A customized Googler with prohibited domains
class MyGoogler(Googler):
    def __init__(self):
        self.probihitedDomains = [
            'http://www.en.leander.cz',
            'http://performancecriticalapps.prelert.com'
        ]

    def parse(self, googleResult):
        """
        Parse a google result to see if it's matched your criteria.
        You should override this function in your subclass
        :param googleResult: an instance of GoogleResult
        :return: If it's matched, return True and this result will be 
                added to the overal search results. Otherwise, return False.
        """
        for prohibited in self.probihitedDomains:
            if prohibited in googleResult.url:
                return False
        return True

doSearch(MyGoogler())
```
License
-------------
Code is licensed under MIT license.

Permission is hereby granted, free of charge, to any person
Obtaining a copy of this software and associated documentation
Files (the "Software"), to deal in the Software without
Restriction, including without limitation the rights to use,
Copy, modify, merge, publish, distribute, sublicense, and/or sell
Copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
Conditions:

The above copyright notice and this permission notice shall be
Included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
