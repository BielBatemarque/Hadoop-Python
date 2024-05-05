
from mrjob.job import MRJob
import re

class MRWordFrequencyCountMapper(MRJob):

    def mapper(self, _, line):
        # Usa expressão regular para encontrar todas as palavras na linha
        for word in re.findall(r'\w+', line):
            # Emite cada palavra com contagem 1
            yield word.lower(), 1
