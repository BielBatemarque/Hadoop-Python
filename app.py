from mrjob.job import MRJob
import re

class MRWordFrequencyCount(MRJob):

    def mapper(self, _, line):
        # Usa expressão regular para encontrar todas as palavras na linha
        for word in re.findall(r'\w+', line):
            # Emite cada palavra com contagem 1
            yield word.lower(), 1

    def reducer(self, key, values):
        # Soma as contagens de cada palavra
        yield key, sum(values)

if __name__ == "__main__":
    MRWordFrequencyCount().run()