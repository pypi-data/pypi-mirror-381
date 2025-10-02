from __future__ import division
from argparse import ArgumentParser
from cgecore.blaster import Blaster
from cgecore.cgefinder import CGEFinder
from cgecore.output.result import Result
from shutil import which
import sys
import os
import time
import json
import pprint

from .cge.config import Config

from plasmidfinder.functions import text_table, get_file_format, make_aln, write_new_json, write_old_json
from .__init__ import __version__



##########################################################################
# TODO list
##########################################################################
# 1) A lot of output files are opened while creating output and not closed
#    until the end. This creates unecessary I/O pressure on the servers.
#    SOLUTION: create output in string variables and write all output to
#    each file only once.







def main():
    ##########################################################################
    # PARSE COMMAND LINE OPTIONS
    ##########################################################################

    parser = ArgumentParser()
    _ = parser.add_argument("-i", "--infile",
                        help="FASTA or FASTQ input files.",
                        nargs="+",
                        required=True)
    _ = parser.add_argument("-o", "--outputPath",
                        dest="outdir",
                        help="Path to blast output",
                        default='.')
    _ =parser.add_argument("-tmp", "--tmp_dir",
                        help=("Temporary directory for storage of the results "
                            "from the external software."))
    _ = parser.add_argument("-mp", "--methodPath",
                        dest="method_path",
                        help="Path to method to use (kma or blastn)")
    _ = parser.add_argument("-p", "--databasePath",
                        dest="db_path",
                        help="Path to the databases",
                        default= None)
    _ = parser.add_argument("-d", "--databases",
                        help=("Databases chosen to search in - if non is "
                            "specified all is used"))
    _ = parser.add_argument("-l", "--mincov",
                        dest="min_cov",
                        help="Minimum coverage",
                        default=0.60)
    _ = parser.add_argument("-t", "--threshold",
                        dest="threshold",
                        help="Minimum hreshold for identity",
                        default=0.90)
    _ = parser.add_argument("-x", "--extended_output",
                        help=("Give extented output with allignment files, "
                            "template and query hits in fasta and a tab "
                            "seperated file with gene profile results"),
                        action="store_true")
    _ = parser.add_argument("--speciesinfo_json",
                        help=("Argument used by the cge pipeline. It takes a list"
                            " in json format consisting of taxonomy, from "
                            "domain -> species. A database is chosen based on "
                            "the taxonomy."),
                        default=None)
    _ = parser.add_argument("-q", "--quiet",
                        action="store_true")
    _ = parser.add_argument("-j", "--json",
                        dest="out_json",
                        help=("Path fo the file in the BeOne JSON format"),
                        )

    _ = parser.add_argument("--legacy",
                        action="store_true",
                        help=("Path for the file in the LEGACY JSON format"),
                        )

    _ = parser.add_argument("-v", "--version",
                        help="Show version number and exits",
                        action="version",
                        version=__version__,
                        )

    args = parser.parse_args()


    ##########################################################################
    # MAIN
    ##########################################################################
    if args.quiet:
        f = open('/dev/null', 'w')
        sys.stdout = f

    conf = Config(args)


    #####################
    # Defining variables
    min_cov = float(args.min_cov)
    threshold = float(args.threshold)
    method_path = args.method_path

    # Check if valid database is provided
    if args.db_path is None:
        sys.exit("Input Error: No database directory was provided!\n")
    elif not os.path.exists(args.db_path):
        sys.exit("Input Error: The specified database directory does not exist!\n")
    else:
        # Check existence of config file
        db_config_file = '%s/config' % (args.db_path)
        if not os.path.exists(db_config_file):
            sys.exit("Input Error: The database config file could not be found!")
        db_path = args.db_path

    # Check if valid input files are provided
    if args.infile is None:
        sys.exit("Input Error: No input file was provided!\n")
    elif not os.path.exists(args.infile[0]):
        sys.exit("Input Error: Input file does not exist!\n")
    elif len(args.infile) > 1:
        if not os.path.exists(args.infile[1]):
            sys.exit("Input Error: Input file does not exist!\n")
        infile = args.infile
    else:
        infile = args.infile

    outdir = os.path.abspath(args.outdir)
    os.makedirs(outdir, exist_ok=True)

    # Check if valid tmp directory is provided
    if args.tmp_dir:
        if not os.path.exists(args.tmp_dir):
            sys.exit("Input Error: Tmp dirctory, {}, does not exist!\n"
                    .format(args.tmp_dir))
        else:
            tmp_dir = os.path.abspath(args.tmp_dir)
    else:
        tmp_dir = outdir

    # Check if databases and config file are correct/correponds
    dbs = {}
    extensions = []
    db_description = {}
    tax_2_db = {}
    with open(db_config_file) as f:
        for i in f:
            i = i.strip()
            if i == '':
                continue
            if i[0] == '#':
                if 'extensions:' in i:
                    extensions = [
                        s.strip() for s in i.split('extensions:')[-1].split(',')]
                continue
            tmp = i.split('\t')
            if len(tmp) != 3:
                sys.exit(("Input Error: Invalid line in the database"
                        " config file!\nA proper entry requires 3 tab "
                        "separated columns!\n%s") % (i))
            db_prefix = tmp[0].strip()
            name = tmp[1].split('#')[0].strip()
            description = tmp[2]

            # Check if all db files are present
            for ext in extensions:
                db = "%s/%s.%s" % (db_path, db_prefix, ext)
                if not os.path.exists(db):
                    sys.exit(("Input Error: The database file (%s) "
                            "could not be found!") % (db))
            if db_prefix not in dbs:
                dbs[db_prefix] = []
            dbs[db_prefix].append(name)
            db_description[db_prefix] = description

            # Create database, where keys are from column 2 in config file (species
            # or other taxonomy). Values are lists of databases belonging to the
            # species or "group".
            taxdbs = tax_2_db.get(name.lower(), [])
            taxdbs.append(db_prefix)
            tax_2_db[name.lower()] = taxdbs
    if len(dbs) == 0:
        sys.exit("Input Error: No databases were found in the "
                "database config file!")

    if args.speciesinfo_json:
        databases = None
        taxonomy = tuple(json.loads(args.speciesinfo_json))
        for tax in reversed(taxonomy):
            if tax in tax_2_db:
                databases = tax_2_db[tax]
                break
        if databases is None:
            databases = databases = dbs.keys()
    elif args.databases is None:
        # Choose all available databases from the config file
        databases = dbs.keys()
    else:
        # Handle multiple databases
        args.databases = args.databases.split(',')

        # Check that the ResFinder DBs are valid
        databases = []
        for db_prefix in args.databases:
            if db_prefix in dbs:
                databases.append(db_prefix)
            else:
                sys.exit("Input Error: Provided database was not "
                        "recognised! (%s)\n" % db_prefix)

    species = set([",".join(dbs[db]) for db in databases])

    # Check file format (fasta, fastq or other format)
    file_format = get_file_format(infile)

    # Call appropriate method (kma or blastn) based on file format
    if file_format == "fastq":
        if not method_path:
            method_path = "kma"
        if which(method_path) is None:
            sys.exit("No valid path to a kma program was provided. Use the -mp "
                    "flag to provide the path.")

        # Check the number of files
        if len(infile) == 1:
            infile_1 = infile[0]
            infile_2 = None
        elif len(infile) == 2:
            infile_1 = infile[0]
            infile_2 = infile[1]
        else:
            sys.exit("Only 2 input file accepted for raw read data,\
                        if data from more runs is avaliable for the same\
                        sample, please concatinate the reads into two files")

        sample_name = os.path.basename(sorted(args.infile)[0])
        method = "kma"

        # Call KMA
        method_obj = CGEFinder.kma(infile_1, tmp_dir, databases, db_path,
                                min_cov=min_cov, threshold=threshold,
                                kma_path=method_path, sample_name=sample_name,
                                inputfile_2=infile_2, kma_mrs=0.75,
                                kma_gapopen=-5, kma_gapextend=-1,
                                kma_penalty=-3, kma_reward=1)



    elif file_format == "fasta":
        if not method_path:
            method_path = "blastn"
        if which(method_path) is None:
            sys.exit("No valid path to a blastn program was provided. Use the "
                    "-mp flag to provide the path.")

        # Assert that only one fasta file is inputted
        assert len(infile) == 1, "Only one input file accepted for assembled data"
        infile = infile[0]
        method = "blast"

        # Call BLASTn
        method_obj = Blaster(infile, databases, db_path, tmp_dir,
                            min_cov, threshold, method_path, cut_off=False)
    else:
        sys.exit("Input file must be fastq or fasta format, not " + file_format)

    results = method_obj.results
    query_aligns = method_obj.gene_align_query
    homo_aligns = method_obj.gene_align_homo
    sbjct_aligns = method_obj.gene_align_sbjct

    json_results = dict()

     #-----------------------Initializing Result object for the new JSON format--------------------#

    plasmidfinder_path= os.path.dirname(os.path.realpath(__file__))[:-2]
    plasmidfinder_results = Result.init_software_result(
        name="PlasmidFinder",
        gitdir=f"{plasmidfinder_path}/../../")

    init_result_data = {
    "provided_species": args.speciesinfo_json,
    "software_version": __version__,
    "key": f"PlasmidFinder-{__version__}",
    "run_date": time.strftime("%d.%m.%Y")}

    plasmidfinder_results.add(**init_result_data)

    plasmidfinder_results.init_database("PlasmidFinder", args.db_path)
    json_results_NEW_FORMAT= plasmidfinder_results.json_dumps()
    hits = []
    for db in results:
        contig_res = {}
        if db == 'excluded':
            continue
        db_name = str(dbs[db][0])
        if db_name not in json_results:
            json_results[db_name] = {}
        if db not in json_results[db_name]:
            json_results[db_name][db] = {}
        if results[db] == "No hit found":
            json_results[db_name][db] = "No hit found"
        else:
            for contig_id, hit in results[db].items():

                identity = float(hit["perc_ident"])
                coverage = float(hit["perc_coverage"])
                depth= hit.get("depth")
                # Skip hits below coverage
                if coverage < (min_cov * 100) or identity < (threshold * 100):
                    continue

                bit_score = identity * coverage

                if contig_id not in contig_res:
                    contig_res[contig_id] = []
                contig_res[contig_id].append([hit["query_start"], hit["query_end"],
                                            bit_score, hit])

        if not contig_res:
            json_results[db_name][db] = "No hit found"

        # Check for overlapping hits, only report the best
        for contig_id, hit_lsts in contig_res.items():

            hit_lsts.sort(key=lambda x: x[0])
            hits = [hit[3] for hit in hit_lsts]

            for hit in hits:

                if args.legacy:
                    #Write the output in the OLD JSON format
                    json_results[db_name][db].update({contig_id: {}})
                    json_results[db_name][db][contig_id] = write_old_json(contig_id, hit,json_results, db, db_name)

                else:
                    #Write the output in the BeOne JSON template format
                    plasmidfinder_results= write_new_json(contig_id, hit, plasmidfinder_results, method_obj, args )


                json_results_NEW_FORMAT= plasmidfinder_results.json_dumps()

 #-------------------------------------------OUTPUT IN OLD JSON FORMAT-----------------------------------#
    # Get run info for JSON file
    service = os.path.basename(__file__).replace(".py", "")
    date = time.strftime("%d.%m.%Y")
    my_time = time.strftime("%H:%M:%S")


    if args.legacy:
        # If the argument legacy is chosen, then proceed with the original output format
         # # Make JSON output file
        data = {service: {}}

        userinput = {"filename(s)": args.infile,
                    "method": method,
                    "file_format": file_format}
        run_info = {"date": date, "time": my_time}
        json_results=dict(sorted(json_results.items(), key=lambda x: x[0].lower()))
        data[service]["user_input"] = userinput
        data[service]["run_info"] = run_info
        data[service]["results"] = json_results

        pprint.pprint(data)

          # # Save json output
        result_file = "{}/data.json".format(outdir)
        with open(result_file, "w") as outfile:
            json.dump(data, outfile)
 #-------------------------------------------OUTPUT IN NEW JSON FORMAT-----------------------------------#
    elif args.out_json:
        #Otherwise, output the BeOne JSON format

        result_file2 = args.out_json.format(outdir)
        with open(result_file2, "w") as outfile2:
            outfile2.write(json_results_NEW_FORMAT)

        parsed = json.loads(json_results_NEW_FORMAT)
        print(json.dumps(parsed, indent=4))
    else:
        #If no output path is provided, default to BeOne as the output format, and provide output with the name
        #results_<infile name>
        current_directory = os.path.dirname(os.path.abspath(__file__))
        outdir= current_directory

        # Assuming args.infile is a list and you want the first file
        filepath = args.infile[0]
        filename = os.path.basename(filepath)           # 'test_1.fsa'
        name_without_ext = os.path.splitext(filename)[0]  # 'test_1'


        result_file2 = os.path.join(outdir, f"results_{name_without_ext}.json")
        with open(result_file2, "w") as outfile2:
            outfile2.write(json_results_NEW_FORMAT)

        parsed = json.loads(json_results_NEW_FORMAT)
        print(json.dumps(parsed, indent=4))



#-------------------------------------WRITING EXTENDED RESULTS----------------------------------------#
    # Getting and writing out the results
    header = ["Plasmid", "Identity", "Query / Template length", "Contig",
            "Position in contig", "Note", "Accession number"]

    if args.extended_output and args.legacy:
        # Define extented output
        table_filename = "{}/results_tab.tsv".format(outdir)
        query_filename = "{}/Hit_in_genome_seq.fsa".format(outdir)
        sbjct_filename = "{}/Plasmid_seqs.fsa".format(outdir)
        result_filename = "{}/results.txt".format(outdir)
        table_file = open(table_filename, "w")
        query_file = open(query_filename, "w")
        sbjct_file = open(sbjct_filename, "w")
        result_file = open(result_filename, "w")

        # Make results file
        result_file.write("{} Results\n\nOrganism(s): {}\n\n"
                        .format(service, ",".join(species)))

        # Write tsv table
        rows = [["Database"] + header]
        for species, dbs_info in json_results.items():
            for db_name, db_hits in dbs_info.items():
                result_file.write("*" * len("\t".join(header)) + "\n")
                result_file.write(db_description[db_name] + "\n")
                db_rows = []

                # Check it hits are found
                if isinstance(db_hits, str):
                    content = [''] * len(header)
                    content[int(len(header) / 2)] = db_hits
                    result_file.write(text_table(header, [content]) + "\n")
                    continue

                for gene_id, gene_info in sorted(
                        db_hits.items(),
                        key=lambda x: (x[1]['plasmid'],
                                    x[1]['accession'])):

                    vir_gene = gene_info["plasmid"]
                    identity = str(gene_info["identity"])
                    coverage = str(gene_info["coverage"])

    #               template_HSP = ("{hsp_len} / {template_len}".format(hsp_len=gene_info["HSP_length"],template_len=gene_info["template_length"]))
                    template_HSP = str(gene_info["HSP_length"]) + " / " + str(gene_info["template_length"])

                    position_in_ref = gene_info["position_in_ref"]
                    position_in_contig = gene_info["positions_in_contig"]
                    note = gene_info["note"]
                    acc = gene_info["accession"]
                    contig_name = gene_info["contig_name"]

                    # Add rows to result tables
                    db_rows.append([vir_gene, identity, template_HSP, contig_name,
                                    position_in_contig, note, acc])
                    rows.append([db_name, vir_gene, identity, template_HSP,
                                contig_name, position_in_contig, note,
                                acc])

                    # Write query fasta output
                    hit_name = gene_info["hit_id"]
                    query_seq = query_aligns[db_name][hit_name]
                    sbjct_seq = sbjct_aligns[db_name][hit_name]

                    if coverage == 100 and identity == 100:
                        match = "PERFECT MATCH"
                    else:
                        match = "WARNING"
                    qry_header = (">{}:{} ID:{}% COV:{}% Best_match:{}\n"
                                .format(vir_gene, match, identity, coverage,
                                        gene_id))
                    query_file.write(qry_header)
                    for i in range(0, len(query_seq), 60):
                        query_file.write(query_seq[i:i + 60] + "\n")

                    # Write template fasta output
                    sbj_header = ">{}\n".format(gene_id)
                    sbjct_file.write(sbj_header)
                    for i in range(0, len(sbjct_seq), 60):
                        sbjct_file.write(sbjct_seq[i:i + 60] + "\n")

                # Write db results tables in results file and table file
                result_file.write(text_table(header, db_rows) + "\n")

            result_file.write("\n")

        for row in rows:
            table_file.write("\t".join(row) + "\n")

        # Write allignment output
        result_file.write("\n\nExtended Output:\n\n")
        make_aln(result_file, json_results, query_aligns, homo_aligns,
                sbjct_aligns)

        # Close all files
        query_file.close()
        sbjct_file.close()
        table_file.close()
        result_file.close()




    if args.quiet:
        f.close()



if __name__ == "__main__":
    sys.exit(main())
