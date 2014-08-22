__author__ = 'anhld'
# -- coding: utf-8 --
from xgoogle.html2text import  *
a = u'4 Tháng M&#432;&#7901;i M&#7897;t 2013   ...    Sau khi yêu c&#7847;u gia h&#7841;n &#273;&#432;&#7907;c   BkavCA    ti&#7871;p nh&#7853;n, b&#7841;n hãy th&#7921;c hi&#7879;n theo các     @@b&#432;&#7899;c sau &#273;ây &#273;&#7875; s&#7917; d&#7909;ng ch&#7919; ký s&#7889; v&#7899;i th&#7901;i h&#7841;n m&#7899;i &#273;&#432;&#7907;c gia&nbsp;... '
a = html2text(a).replace('\n', ' ')

print a