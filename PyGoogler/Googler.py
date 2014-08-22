#!/usr/bin/python
# encoding: utf-8
#
# Anh Le (anhldbk@gmail.com)
# http://bigsonata.com
#
#
# Code is licensed under MIT license.
#
# Permission is hereby granted, free of charge, to any person
# Obtaining a copy of this software and associated documentation
# Files (the "Software"), to deal in the Software without
# Restriction, including without limitation the rights to use,
# Copy, modify, merge, publish, distribute, sublicense, and/or sell
# Copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# Conditions:
#
# The above copyright notice and this permission notice shall be
# Included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
import time
import unicodedata

from search import GoogleSearch, SearchError


# noinspection PyPep8Naming
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
                    if not results or len(results) == 0:
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
