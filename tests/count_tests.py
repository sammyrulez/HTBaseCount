import unittest
import os
import context
from countbases import count_reads_in_features

class TestCountFunctions(unittest.TestCase):

    def test_count_reads_in_features(self):
        fixture_data_dir = os.path.dirname(os.path.abspath(__file__)) + '/data'
        sam_file_name = "%s/yeast_RNASeq_excerpt.sam.gz" % (fixture_data_dir)
        gff_file_name = "%s/Saccharomyces_cerevisiae.SGD1.01.56.gtf.gz" % (fixture_data_dir)
        count_reads_in_features( sam_file_name, gff_file_name, "yes","union", "exon", "gene_id", True, 1,None )

if __name__ == '__main__':
    unittest.main()
