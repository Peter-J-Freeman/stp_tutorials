from pathlib import Path
import sys
import pytest
sys.path.append(str(Path(__file__).resolve().parent.parent))
from STP_Tutorials.modules import iteration, exceptions


def test_string_slice():
    transcript = "".join(""""
              CAAAAAGCTCGGGAAGTAGTGGACTGTTTTTACCCCTCCTGGGATCACCACTGACAGCATCCATGAAGTT
              CTGACAGAAGAACACACCAGGATGACAAAGTAGTGACTTTTAAAGAGCAGCCAACAACAAGCATATAGGG
              AATCTCTCAGCAAATACAGAATCCATCTGAGAATATGCTGCCACAAATACCCTTTTTGCTGCTAGTATCC
              TTGAACTTGGTTCATGGAGTGTTTTACGCTGAACGATACCAAATGCCCACAGGCATAAAAGGCCCACTAC
              CCAACACCAAGACACAGTTCTTCATTCCCTACACCATAAAGAGTAAAGGTATAGCAGTAAGAGGAGAGCA
              AGGTACTCCTGGTCCACCAGGCCCTGCTGGACCTCGAGGGCACCCAGGTCCTTCTGGACCACCAGGAAAA
              CCAGGCTACGGAAGTCCTGGACTCCAAGGAGAGCCAGGGTTGCCAGGACCACCGGGACCATCAGCTGTAG
              GGAAACCAGGTGTGCCAGGACTCCCAGGAAAACCAGGAGAGAGAGGACCATATGGACCAAAAGGAGATGT
              TGGACCAGCTGGCCTACCAGGACCCCGGGGCCCACCAGGACCACCTGGAATCCCTGGACCGGCTGGAATT
              TCTGTGCCAGGAAAACCTGGACAACAGGGACCCACAGGAGCCCCAGGACCCAGGGGCTTTCCTGGAGAAA
              AGGGTGCACCAGGAGTCCCTGGTATGAATGGACAGAAAGGGGAAATGGGATATGGTGCTCCTGGTCGTCC
              AGGTGAGAGGGGTCTTCCAGGCCCTCAGGGTCCCACAGGACCATCTGGCCCTCCTGGAGTGGGAAAAAGA
              GGTGAAAATGGGGTTCCAGGACAGCCAGGCATCAAAGGTGATAGAGGTTTTCCGGGAGAAATGGGACCAA
              TTGGCCCACCAGGTCCCCAAGGCCCTCCTGGGGAACGAGGGCCAGAAGGCATTGGAAAGCCAGGAGCTGC
              TGGAGCCCCAGGCCAGCCAGGGATTCCAGGAACAAAAGGTCTCCCTGGGGCTCCAGGAATAGCTGGGCCC
              CCAGGGCCTCCTGGCTTTGGGAAACCAGGCTTGCCAGGCCTGAAGGGAGAAAGAGGACCTGCTGGCCTTC
              CTGGGGGTCCAGGTGCCAAAGGGGAACAAGGGCCAGCAGGTCTTCCTGGGAAGCCAGGTCTGACTGGACC
              CCCTGGGAATATGGGACCCCAAGGACCAAAAGGCATCCCGGGTAGCCATGGTCTCCCAGGCCCTAAAGGT
              GAGACAGGGCCAGCTGGGCCTGCAGGATACCCTGGGGCTAAGGGTGAAAGGGGTTCCCCTGGGTCAGATG
                GAAAACCAGGGTACCCAGGAAAACCAGGTCTCGATGGTCCTAAGGGTAACCCAGGGTTACCAGGTCCAAA
                AGGTGATCCTGGAGTTGGAGGACCTCCTGGTCTCCCAGGCCCTGTGGGCCCAGCAGGAGCAAAGGGAATG
                CCCGGACACAATGGAGAGGCTGGCCCAAGAGGTGCCCCTGGAATACCAGGTACTAGAGGCCCTATTGGGC
                CACCAGGCATTCCAGGATTCCCTGGGTCTAAAGGGGATCCAGGAAGTCCCGGTCCTCCTGGCCCAGCTGG
                CATAGCAACTAAGGGCCTCAATGGACCCACCGGGCCACCAGGGCCTCCAGGTCCAAGAGGCCACTCTGGA
                GAGCCTGGTCTTCCAGGGCCCCCTGGGCCTCCAGGCCCACCAGGTCAAGCAGTCATGCCTGAGGGTTTTA
                TAAAGGCAGGCCAAAGGCCCAGTCTTTCTGGGACCCCTCTTGTTAGTGCCAACCAGGGGGTAACAGGAAT
                GCCTGTGTCTGCTTTTACTGTTATTCTCTCCAAAGCTTACCCAGCAATAGGAACTCCCATACCATTTGAT
                AAAATTTTGTATAACAGGCAACAGCATTATGACCCAAGGACTGGAATCTTTACTTGTCAGATACCAGGAA
                TATACTATTTTTCATACCACGTGCATGTGAAAGGGACTCATGTTTGGGTAGGCCTGTATAAGAATGGCAC
                CCCTGTAATGTACACCTATGATGAATACACCAAAGGCTACCTGGATCAGGCTTCAGGGAGTGCCATCATC
                GATCTCACAGAAAATGACCAGGTGTGGCTCCAGCTTCCCAATGCCGAGTCAAATGGCCTATACTCCTCTG
                AGTATGTCCACTCCTCTTTCTCAGGATTCCTAGTGGCTCCAATGTGAGTACACACAGAGCTAATCTAAAT
                CTTGTGCTAGAAAAAGCATTCTCTAACTCTACCCCACCCTACAAAATGCATATGGAGGTAGGCTGAAAAG
                AATGTAATTTTTATTTTCTGAAATACAGATTTGAGCTATCAGACCAACAAACCTTCCCCCTGAAAAGTGA
                GCAGCAACGTAAAAACGTATGTGAAGCCTCTCTTGAATTTCTAGTTAGCAATCTTAAGGCTCTTTAAGGT
                TTTCTCCAATATTAAAAAATATCACCAAAGAAGTCCTGCTATGTTAAAAACAAACAACAAAAAACAAACA
                ACAAAAAAAAAATTAAAAAAAAAAACAGAAATAGAGCTCTAAGTTATGTGAAATTTGATTTGAGAAACTC
                GGCATTTCCTTTTTAAAAAAGCCTGTTTCTAACTATGAATATGAGAACTTCTAGGAAACATCCAGGAGGT
                ATCATATAACTTTGTAGAACTTAAATACTTGAATATTCAAATTTAAAAGACACTGTATCCCCTAAAATAT
                TTCTGATGGTGCACTACTCTGAGGCCTGTATGGCCCCTTTCATCAATATCTATTCAAATATACAGGTGCA
                TATATACTTGTTAAAGCTCTTATATAAAAAAGCCCCAAAATATTGAAGTTCATCTGAAATGCAAGGTGCT
                TTCATCAATGAACCTTTTCAAACTTTTCTATGATTGCAGAGAAGCTTTTTATATACCCAGCATAACTTGG
                AAACAGGTATCTGACCTATTCTTATTTAGTTAACACAAGTGTGATTAATTTGATTTCTTTAATTCCTTAT
                TGAATCTTATGTGATATGATTTTCTGGATTTACAGAACATTAGCACATGTACCTTGTGCCTCCCATTCAA
                GTGAAGTTATAATTTACACTGAGGGTTTCAAAATTCGACTAGAAGTGGAGATATATTATTTATTTATGCA
                CTGTACTGTATTTTTATATTGCTGTTTAAAACTTTTAAGCTGTGCCTCACTTATTAAAGCACAAAATGTT
                TTACCTACTCCTTATTTACGACGCAATAAAATAACATCAATAGATTTTTAGGCTGAATTAATTTGAAAGC
                AGCAATTTGCTGTTCTCAACCATTCTTTCAAGGCTTTTCATTGTTCAAAGTTAATAAAAAAGTAGGACAA
                TAAAGTGATGGGTGGCTTTTA
                """.split())
    cds_start = 175
    cds_end = 2217
    return_value = iteration.get_cds(transcript, cds_start, cds_end)
    assert return_value == "".join("""
             atgctgccacaaataccctttttgctgctagtatccttgaacttggttcatggagtgttttacgctgaacgataccaaatgcccacaggcataaaaggcccactac
             ccaacaccaagacacagttcttcattccctacaccataaagagtaaaggtatagcagtaagaggagagcaaggtactcctggtccaccaggccctgctggacctcg
             agggcacccaggtccttctggaccaccaggaaaaccaggctacggaagtcctggactccaaggagagccagggttgccaggaccaccgggaccatcagctgtaggg
             aaaccaggtgtgccaggactcccaggaaaaccaggagagagaggaccatatggaccaaaaggagatgttggaccagctggcctaccaggaccccggggcccaccag
             gaccacctggaatccctggaccggctggaatttctgtgccaggaaaacctggacaacagggacccacaggagccccaggacccaggggctttcctggagaaaaggg
             tgcaccaggagtccctggtatgaatggacagaaaggggaaatgggatatggtgctcctggtcgtccaggtgagaggggtcttccaggccctcagggtcccacagga
             ccatctggccctcctggagtgggaaaaagaggtgaaaatggggttccaggacagccaggcatcaaaggtgatagaggttttccgggagaaatgggaccaattggcc
             caccaggtccccaaggccctcctggggaacgagggccagaaggcattggaaagccaggagctgctggagccccaggccagccagggattccaggaacaaaaggtct
             ccctggggctccaggaatagctgggcccccagggcctcctggctttgggaaaccaggcttgccaggcctgaagggagaaagaggacctgctggccttcctgggggt
             ccaggtgccaaaggggaacaagggccagcaggtcttcctgggaagccaggtctgactggaccccctgggaatatgggaccccaaggaccaaaaggcatcccgggta
             gccatggtctcccaggccctaaaggtgagacagggccagctgggcctgcaggataccctggggctaagggtgaaaggggttcccctgggtcagatggaaaaccagg
             gtacccaggaaaaccaggtctcgatggtcctaagggtaacccagggttaccaggtccaaaaggtgatcctggagttggaggacctcctggtctcccaggccctgtg
             ggcccagcaggagcaaagggaatgcccggacacaatggagaggctggcccaagaggtgcccctggaataccaggtactagaggccctattgggccaccaggcattc
             caggattccctgggtctaaaggggatccaggaagtcccggtcctcctggcccagctggcatagcaactaagggcctcaatggacccaccgggccaccagggcctcc
             aggtccaagaggccactctggagagcctggtcttccagggccccctgggcctccaggcccaccaggtcaagcagtcatgcctgagggttttataaaggcaggccaa
             aggcccagtctttctgggacccctcttgttagtgccaaccagggggtaacaggaatgcctgtgtctgcttttactgttattctctccaaagcttacccagcaatag
             gaactcccataccatttgataaaattttgtataacaggcaacagcattatgacccaaggactggaatctttacttgtcagataccaggaatatactatttttcata
             ccacgtgcatgtgaaagggactcatgtttgggtaggcctgtataagaatggcacccctgtaatgtacacctatgatgaatacaccaaaggctacctggatcaggct
             tcagggagtgccatcatcgatctcacagaaaatgaccaggtgtggctccagcttcccaatgccgagtcaaatggcctatactcctctgagtatgtccactcctctt
             tctcaggattcctagtggctccaatgtga
             """.split())



