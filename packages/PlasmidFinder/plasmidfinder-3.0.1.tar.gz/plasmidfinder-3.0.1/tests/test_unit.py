import pytest
import src.plasmidfinder.functions as functions

functions.get_gene_note_acc

#create a hit object




def test_get_gene_note_acc():
    hit_ex_1_kma= dict(
    #based on the results from test_1_1.fq
            sbjct_length= 439,
            perc_coverage= 83.6,
            sbjct_string= "TATCAAGAGCCTTAAGGCGAAGATAAACCTTATAGTCAATCTGATAGAGCTCCTGAATCCGGGGATCTCCCTCTATCTCAATCTCATTGGTTTTTATGTTGTACCGTGCCCAGTTAATGAGGCCGGTCGTGAGGGTTGAATCTTCATTGCGGAACTGAAAAGTGACCATTTTCAGTTTAATCATCGAAGCATCGATACGTTGTTTCATGGGCTTATTCGACCTCGAGGGGTCAAACCCACAATTTTTAAGGAAGGTGCTAAAAGGAAGCTTAATCCTTCCTGAGTAATGGCCATGGTCATGTAATGAACGGACTATACCAAGCCATACACGGAAATCTGTCCCCATATCAAGACGAGGGCTGGATAGCGATATTTCTTTGTAGCCTTCACTGGATGCGATCTGCATATGCTGTAAATCGCGGGACACATCCATCGTAAC",
            query_string= "---------------GGCGAAGATAAACCTTATAGTCAATCTGATAGAGCTCCTGAATCCGGGGATCTCCCTCTATCTCAATCTCATTGGTTTTTATGTTGTACCGTGCCCAGTTAATGAGGCCGGTCGTGAGGGTTGAATCTTCATTGCGGAACTGAAAAGTGACCATTTTCAGTTTAATCATCGAAGCATCGATACGTTGTTTCATGGGCTTATTCGACCTCGAGGGGTCAAACCCACAATTTTTAAGGAAGGTGCTAAAAGGAAGCTTAATCCTTCCTGAGTAATGGCCATGGTCATGTAATGAACGGACTATACCAAGCCATACACGGAAATCTGTCCCCATATCAAGACGAGGGCTGGATAGCGATATTTCTTTGTA---------------------------------------------------------",
            homo_string= "_______________|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||_________________________________________________________",
            sbjct_header= "IncFIB(pNDM-Mar)_1__JN420336",
            #gene_note_acc
            perc_ident= 83.6,
            query_start= "NA",
            query_end= "NA",
            contig_name= "NA",
            HSP_length= 367,
            #alignment length
            cal_score= 0,
            depth= 4.44,
            p_value= 0
        )
    trial= functions.get_gene_note_acc(hit_ex_1_kma)
    print(trial [2])
    assert trial[0] =="IncFIB(pNDM-Mar)"
    assert trial[1] == ""
    assert trial [2] == "JN420336"


# def func(x):
#     return x + 1


# def test_answer():
#     assert func(3) == 5
    
#def compare_old_new_output(): what else to test?