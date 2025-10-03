from __future__ import division
from tabulate import tabulate
import gzip




##########################################################################
# FUNCTIONS
##########################################################################


def text_table(headers, rows, empty_replace='-'):
    ''' Create text table

    USAGE:
        >>> from tabulate import tabulate
        >>> headers = ['A','B']
        >>> rows = [[1,2],[3,4]]
        >>> print(text_table(headers, rows))
        **********
          A     B
        **********
          1     2
          3     4
        ==========
    '''
    # Replace empty cells with placeholder
    rows = map(lambda row: map(lambda x: x if x else empty_replace, row), rows)
    # Create table
    table = tabulate(rows, headers, tablefmt='simple').split('\n')
    # Prepare title injection
    width = len(table[0])
    # Switch horisontal line
    table[1] = '*' * (width + 2)
    # Update table with title
    table = (("%s\n" * 3)
             % ('*' * (width + 2), '\n'.join(table), '=' * (width + 2)))
    return table


def is_gzipped(file_path):
    ''' Returns True if file is gzipped and False otherwise.
         The result is inferred from the first two bits in the file read
         from the input path.
         On unix systems this should be: 1f 8b
         Theoretically there could be exceptions to this test but it is
         unlikely and impossible if the input files are otherwise expected
         to be encoded in utf-8.
    '''
    with open(file_path, mode='rb') as fh:
        bit_start = fh.read(2)
    if(bit_start == b'\x1f\x8b'):
        return True
    else:
        return False


def get_file_format(input_files):
    """
    Takes all input files and checks their first character to assess
    the file format. Returns one of the following strings; fasta, fastq,
    other or mixed. fasta and fastq indicates that all input files are
    of the same format, either fasta or fastq. other indiates that all
    files are not fasta nor fastq files. mixed indicates that the inputfiles
    are a mix of different file formats.
    """

    # Open all input files and get the first character
    file_format = []
    invalid_files = []
    for infile in input_files:
        if is_gzipped(infile):
            f = gzip.open(infile, "rb")
            fst_char = f.read(1)
        else:
            f = open(infile, "rb")
            fst_char = f.read(1)
        f.close()
        # Assess the first character
        if fst_char == b"@":
            file_format.append("fastq")
        elif fst_char == b">":
            file_format.append("fasta")
        else:
            invalid_files.append("other")
    if len(set(file_format)) != 1:
        return "mixed"
    return ",".join(set(file_format))


def make_aln(file_handle, json_data, query_aligns, homol_aligns, sbjct_aligns):
    for dbs_info in json_data.values():
        for db_name, db_info in dbs_info.items():
            if isinstance(db_info, str):
                continue

            for gene_id, gene_info in sorted(db_info.items(),key=lambda x: (x[1]['plasmid'], x[1]['accession'])):

                seq_name = gene_info["plasmid"] + "_" + gene_info["accession"]
                hit_name = gene_info["hit_id"]

                seqs = ["", "", ""]
                seqs[0] = sbjct_aligns[db_name][hit_name]
                seqs[1] = homol_aligns[db_name][hit_name]
                seqs[2] = query_aligns[db_name][hit_name]

                write_align(seqs, seq_name, file_handle)


def write_align(seq, seq_name, file_handle):
    file_handle.write("# {}".format(seq_name) + "\n")
    sbjct_seq = seq[0]
    homol_seq = seq[1]
    query_seq = seq[2]
    for i in range(0, len(sbjct_seq), 60):
        file_handle.write("%-10s\t%s\n" % ("template:", sbjct_seq[i:i + 60]))
        file_handle.write("%-10s\t%s\n" % ("", homol_seq[i:i + 60]))
        file_handle.write("%-10s\t%s\n\n" % ("query:", query_seq[i:i + 60]))

def get_gene_note_acc(hit):
    header = hit["sbjct_header"]

    tmp = header.split("_")
    try:
        gene = tmp[0]
        note = tmp[2]
        acc = "".join(tmp[3:])
    except IndexError:
        gene = tmp
        note = ""
        acc = ""
    try:
        variant = tmp[3]
    except IndexError:
        variant = ""
    print("sbjct_header")
    print(header)
    return [gene, note, acc]

def write_old_json(contig_id, hit,json_results, db, db_name ):
    [gene, note, acc]= get_gene_note_acc(hit)
    identity = hit["perc_ident"]
    coverage = hit["perc_coverage"]
    sbj_length = hit["sbjct_length"]
    HSP = hit["HSP_length"]
    positions_contig = "%s..%s" % (hit["query_start"],
                                hit["query_end"])
    positions_ref = "%s..%s" % (hit["sbjct_start"], hit["sbjct_end"])
    contig_name = hit["contig_name"]

    json_results[db_name][db].update({contig_id: {}})
    json_results[db_name][db][contig_id] = {
                        "plasmid": gene,
                        "identity": round(identity, 2),
                        "HSP_length": HSP,
                        "template_length": sbj_length,
                        "position_in_ref": positions_ref,
                        "contig_name": contig_name,
                        "positions_in_contig": positions_contig,
                        "note": note,
                        "accession": acc,
                        "coverage": round(coverage, 2),
                        "hit_id": contig_id}
    return  json_results[db_name][db][contig_id]

#-------------------------------------------------------------------------
def write_new_json(contig_id, hit, plasmidfinder_results, method_obj, args ):
    [gene, note, acc]= get_gene_note_acc(hit)
     
    """     dict_query_str= {}
    for key, value in method_obj.gene_align_query.items():
        if len(value)>0:
            dict_query_str.update(value)
        
    dict_alignment_str= {}
    for key, value in method_obj.gene_align_homo.items():
        if len(value)>0:
            dict_alignment_str.update(value)

    dict_ref_str= {}
    for key, value in method_obj.gene_align_sbjct.items():
        if len(value)>0:
            dict_ref_str.update(value) """

    identity = hit["perc_ident"]
    coverage = hit["perc_coverage"]
    sbj_length = hit["sbjct_length"]
    HSP = hit["HSP_length"]
    contig_name = hit["contig_name"]
    depth= hit.get("depth")
    header = hit["sbjct_header"]

    if args.extended_output is True:
            
        query_string= hit['query_string']
        alignment_string= hit['homo_string']
        ref_string= hit["sbjct_string"]
    else:
        query_string= ""
        alignment_string= ""
        ref_string= ""
    plasmidfinder_results.add_class(cl="seq_regions", type="seq_region",
                                                    **{
                                                        "key": contig_id,
                                                        "gene": True,
                                                        "name": gene,
                                                        "identity": round(identity, 2),
                                                        "alignment_length": HSP,
                                                        "ref_gene_lenght": sbj_length,
                                                        "coverage": round(coverage, 2),
                                                        "depth": depth,
                                                        "ref_id": header,
                                                        "ref_acc": acc,
                                                        "ref_start_pos": hit["sbjct_start"],
                                                        "ref_end_pos":hit["sbjct_end"],
                                                        "query_id": contig_name ,
                                                        "query_start_pos":hit["query_start"],
                                                        "query_end_pos": hit["query_end"],
                                                        "ref_database": plasmidfinder_results.get_db_key("PlasmidFinder"),
                                                        "note": note,
                                                        #"query_string": dict_query_str[str(contig_id)],
                                                        #"alignment_string": dict_alignment_str[str(contig_id)],
                                                        #"ref_string":  dict_ref_str[str(contig_id)],
                                                        "query_string":query_string,
                                                        "alignment_string":alignment_string,
                                                        "ref_string": ref_string
                                                    })
    return plasmidfinder_results