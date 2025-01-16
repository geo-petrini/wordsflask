import os
import sys
from wordcloud import wordcloud

w = wordcloud.WordCloud()
w.generate_from_text( open('app.py').read() )
# w.background_color('white')
w.width = 500
w.height = 500
w.to_image()
w.to_file('app.png')
s =w.to_svg()
open('app.svg', 'w').write(s.encode('utf-8', 'ignore').decode())