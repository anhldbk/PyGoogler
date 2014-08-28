#!/usr/bin/python
from PyGoogler import Googler



def doSearch(googler):
    # googler: an instance of Googler
    print '\n-----------[ Instance %s ]--------------\n' % googler.__class__.__name__
    word = '"cách mạng"'
    print 'Searching for %s...' % word
    results = googler.search(word, Googler.DOMAIN_VIETNAMESE, maxRequest=2)
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
        :return: If it's matched, return True and this result will be added to the overal search results.
                Otherwise, return False.
        """
        for prohibited in self.probihitedDomains:
            if prohibited in googleResult.url:
                return False
        return True

# doSearch(MyGoogler())