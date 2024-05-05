from mrjob.job import MRJob

class MRWordFrequencyCountReducer(MRJob):

    def reducer(self, key, values):
        # Soma as contagens de cada palavra
        yield key, sum(values)