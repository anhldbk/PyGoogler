#!/usr/bin/python
import string
import time
import sys
import unicodedata

sys.path.append('.')
from xgoogle.search import GoogleSearch, SearchError


class GoogleResult:
    """
    Class representing a search result from Google
    """

    def __init__(self):
        """
        Constructor
        """
        self.title = ''
        self.url = ''
        self.description = ''

    def __str__(self):
        """
        Convert this instance into its String representation
        :return:
        """
        return 'Title: %s\nUrl: %s\nDescription: %s' % (self.title, self.url, self.description)

    def toAsciiString(self):
        """
        Convert this instance into its  Ascii string representation
        :return:
        """
        return 'Title: %s\nUrl: %s\nDescription: %s' % (
            self.__getAscii(self.title), self.__getAscii(self.url), self.__getAscii(self.description))

    def __getAscii(self, input):
        try:
            return unicodedata.normalize('NFKD', input).encode('ascii', 'ignore')
        except:
            return input


# noinspection PyClassHasNoInit
class Googler:
    """
    Class for googling
    """
    __RESULT_PER_PAGE = 50
    __USER_AGENT = 'Mozilla/5.0 (Windows NT 5.1; rv:31.0) Gecko/20100101 Firefox/31.0'  # Firefox

    DOMAIN_ENGLISH = '.com'
    DOMAIN_VIETNAMESE = '.com.vn'

    def parse(self, googleResult):
        """
        Parse a google result to see if it's matched your criteria.
        You should override this function in your subclass
        :param googleResult: an instance of GoogleResult
        :return: If it's matched, return True and this result will be added to the overal search results.
                Otherwise, return False.
        """
        return True

    def search(self, keyword, domain, numberOfResults=50):
        """
        Google for a specific keyword
        :param keyword: The keyword
        :param domain: Constants defined by Googler (DOMAIN_ENGLISH, DOMAIN_VIETNAMESE ...)
        :param numberOfResults: Number of results to return
        :return: List of GoogleResult instances
        """
        # a trick to make Google not ban us for requesting so often
        keyword = keyword.replace(' ', '+')

        gs = GoogleSearch(query=keyword, tld=domain)
        gs.results_per_page = Googler.__RESULT_PER_PAGE

        ret = []
        while True:
            try:
                while True:
                    results = gs.get_results()
                    if not results:
                        return ret

                    for result in results:
                        g = GoogleResult()
                        g.description = result.desc
                        g.url = result.url
                        g.title = result.title
                        if self.parse(g):
                            ret.append(g)
                            if len(ret) == numberOfResults:
                                return ret

                    # sleep before conducting another search
                    time.sleep(5)

            except SearchError as e:
                print "Search failed: %s" % e
                return ret


# alter spaces with plus signs to make Google not ban our IPs
googler = Googler()
word = 'Bkav'
print 'Searching for %s...' % word
results = googler.search(word, Googler.DOMAIN_VIETNAMESE)
print 'Result(s) found: %s' % len(results)

count = 0
for result in results:
    count += 1
    print '%s. %s' % (count, result)
