import luigi


class GenerateWords(luigi.Task):
    def output(self):
        return luigi.LocalTarget('words.txt')

    def run(self):
        # write a dummy list of words to output file﻿
        words = ['apple', 'banana', 'grapefruit']
        with self.output().open('w') as f:
            for word in words:
                f.write('{word}\n'.format(word=word))


class CountLetters(luigi.Task):
    def requires(self):
        return GenerateWords()

    def output(self):
        return luigi.LocalTarget('letter_counts.txt')

    def run(self):
        # read in file as list﻿
        with self.input().open('r') as infile:
            words = infile.read().splitlines()
        # write each word to output file with letter count﻿
        with self.output().open('w') as outfile:
            for word in words:
                outfile.write(
                    '{word} | {letter_count}\n'.format(
                        word=word, letter_count=len(word)
                    )
                )
