import ParserClass
from ParserClass import EdifactParser
"""
I've made the assumption for this question that I'm reading from a file.

"""


newEdifact = EdifactParser('./edifact_message.txt');
print(newEdifact.sec_third_segments)
