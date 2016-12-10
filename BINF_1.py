from Bio.Seq import Seq
seq_count = Seq("GCGCTGAGCCTATCAGCTTGACCCGGGTTTCTGGAGCAACTACGATCGCAAGATTCGCTGTGGGGATTCCGTTAAACAACGCTGAGTTGCCGCTCGGGCCAATTGAACCAACTAATTCGTTGATGCGAGGACCGCTATATGGATGGATCTAGAGGACGAGATATCTGATCTCTCACCGATTATTATCACGCCACCCAACCCAAAAGTCGCGGGCTTTGCTCTTCTATCTACCCTATTCAATAAGATGAATCACTACTAACTCTCACACTAACTTTCGACGTCTGCCTACGTGTTGCGGACGTGAAGCACGGTTTTTGCAATCCAACCCGCCATTAAGGGGCAGTAGTCATATACTTCGACTCTTCCCGATCTCAATGAGGCCACCCCCAGGTCTGAGGTTCTAGTATTGAGGCGCCAGGCAGATGACGAGCCAAAATGCACACATTTGGGCGGTCAAGAAGCGTTGGCGTTACTCGGTCCCATAGCAAAATACAAAAAGAGGCCCTGTGGACGAATGCAGCAGGTTAGTCGAAGGGTGCAGTACGGATGTTTGATCATGACCGGAATAGTCAGGTGAATCTGTAATTACCTTGAACAGCCAAAAAAGAGAACCGTATCTGCGCGAGCACACTACTGAAGCAAAATGACAATGGCCCGATATCGAGGGTTAATAACCGACAGCATGTTCTCAGTCCGTTCAGAATCCTGTCCCCTAACGGCTACACGTGGGCGACGTGGTTCATCCATTATACTTTCACCGTCGCGCTCCGGTCCGTCACGGAGTCGGTTGAAGAGGGGTTCCTGGACATCTGATGCCGCAGTAACTAGACTGTGTTCCGCCTCTTCCGCGAGAGAGCTCTGTACGTCGGCAGAGTACTGGCGGGGTGCC")
print seq_count.count("A")
print seq_count.count("C")
print seq_count.count("G")
print seq_count.count("T")