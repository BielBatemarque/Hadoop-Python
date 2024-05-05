from mrjob.job import MRJob
from src.mapper import MRWordFrequencyCountMapper
from src.reducer import MRWordFrequencyCountReducer

class MRWordFrequencyCount(MRJob):

    def steps(self):
        return [
            self.mr(mapper=MRWordFrequencyCountMapper,
                    reducer=MRWordFrequencyCountReducer)
        ]

if __name__ == "__main__":
    MRWordFrequencyCount().run()