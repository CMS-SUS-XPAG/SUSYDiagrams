#! /usr/bin/env python

################# Compiles LaTeX files with Feynman diagrams created with feynmp
import argparse
import subprocess
import os
import sys


def CheckCommand(command, message, print_file):
    with open(os.devnull, 'w') as null_file:
        status = subprocess.call(command)
        #status = subprocess.call(command, stdout=null_file)
        #status = subprocess.call(command, stdout=print_file)
        if status != 0:
            print(message)
            #PrintFile(print_file)
            sys.exit("\n\n\033[91m\033[1m==== Compilation error: "+message+". Exiting \033[0m\n\n")

def Compile(infile):
    orig_dir = os.getcwd()
    folder = os.path.dirname(infile)+'/'
    if folder == '/': folder = ""
    else: os.chdir(folder)
    infile = infile.split('/')[-1]
    base = infile.replace(".tex","")

    ### Running LaTeX first
    cmdlatex = ["latex", infile]
    CheckCommand(cmdlatex, "Failed initial compilation", "latex1.log")

    ### Creating diagram with feynmp
    feyn = "Feynman"+base+ ".mp"
    if not os.path.exists(feyn):
        sys.exit("\n\n==== \033[91m\033[1m"+feyn+
                 '\033[0m does not exist, make sure you named \033[91m\033[1mFeynman'+base
                 +'\033[0m the {fmffile} in '+folder+infile+'. Exiting \n\n')
    mpost_cmd = ["mpost", feyn] 
    CheckCommand(mpost_cmd, "Failed mpost", "mpost.log")

    ### Running LaTeX again and conversion .dvi -> .ps -> .pdf
    CheckCommand(cmdlatex, "Failed initial compilation", "latex1.log")
    dvips_cmd = ["dvips", "-o", infile.replace(".tex", ".ps"), infile.replace(".tex", ".dvi")]
    CheckCommand(dvips_cmd, "Failed dvips", "dvips.log")
    ps2pdf_cmd = ["ps2pdf", infile.replace(".tex", ".ps")]
    CheckCommand(ps2pdf_cmd, "Failed ps2pdf", "ps2pdf.log")

    ### Cleaning up
    os.system("rm "+"Feynman"+base+"*")
    os.system("rm "+base+"*.aux")
    os.system("rm "+base+"*.ps")
    os.system("rm "+base+"*.dvi")
    os.system("rm "+base+"*.log")

    #### Cropping the .pdf file
    os.system("pdfcrop --margins '10 10 10 10' "+infile.replace(".tex", ".pdf"))
    os.system("mv "+infile.replace(".tex", "-crop.pdf")+" "+infile.replace(".tex", ".pdf"))
    os.chdir(orig_dir)
    print "\n\n\033[32m\033[1m open "+folder+infile.replace(".tex", ".pdf")+"\033[0m\n\n"

def CompileAll():
    files = [f for f in os.listdir("./") if f.endswith(".tex")]
    for f in files:
        Compile(f)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compiles Feynman diagrams",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("input", default="TChiHH.tex", metavar="INPUT_FILE",
                        help="File to compile.")
    args = parser.parse_args()

    if(args.input == "all"): CompileAll()
    else: Compile(args.input)
