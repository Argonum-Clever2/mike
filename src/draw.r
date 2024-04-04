#install.packages("codetools_0.2-19.tar.gz", repos=NULL, type = "source")

# install.packages("glue_1.3.0.tar.gz", repos=NULL, type = "source")
# install.packages("stringi_1.2.2.tar.gz", repos=NULL, type = "source")
# install.packages("magrittr_1.5.tar.gz", repos=NULL, type = "source")
# install.packages("stringr_1.3.1.tar.gz", repos=NULL, type = "source")

#install.packages("Rcpp_1.0.11.tar.gz", repos=NULL, type = "source", lib="lib")
#install.packages("RInside_0.2.15.tar.gz", repos=NULL, type = "source", lib="lib")
#install.packages("getopt_1.20.2.tar.gz", repos=NULL, type = "source")
#install.packages("optparse_1.6.0.tar.gz", repos=NULL, type = "source")

#install.packages("digest_0.6.19.tar.gz", repos=NULL, type = "source")
#install.packages("ape_5.7-1.tar.gz", repos=NULL, type = "source")

#install.packages("jsonlite_1.6.tar.gz", repos=NULL, type = "source")


library(ape)
library(Rcpp)
library(optparse)
option_list <- list(
  make_option(c("-f", "--file"), type = "character", default = NULL, help = "Input file path"),
  make_option(c("-o", "--output"), type = "character", default = NULL, help = "Output file path")
)

opt_parser <- OptionParser(option_list = option_list)

tryCatch({
    opt <- parse_args(opt_parser)
    if (is.null(opt$file) || is.null(opt$output)){
        stop("[ERROR]:    Missing required options. ")
    }
    inputfile <- opt$file
    outputfile <- opt$output

}, error = function(e) {
    cat("[ERROR]:    ", conditionMessage(e), "\n")
    cat(getOption("usage"), "\n")
})





tree <- read.csv(inputfile, sep='\t', header = TRUE, row.names = 1)

dist <- as.dist(as.matrix(tree))
tree <- bionj(dist)
write.tree(tree, outputfile)
lines <- readLines(outputfile)


sourceCpp(code="
    #include <string>
    #include <Rcpp.h>

    using namespace std;
    using namespace Rcpp;

    // [[Rcpp::export]]

    string getTree(string &suftmp){
        char tmp;
        string tree;
        for (int i=0; i < suftmp.size(); i++){
            if (suftmp[i] == ':'){
                i++;
                while ((suftmp[i] != ',') && (suftmp[i] != ')') && (suftmp[i] != ';')){
                    i++;
                }
                tree += suftmp[i];
            }else{
                tree += suftmp[i];
            }
        }
        return tree;
    }

    StringVector StringVector_type(StringVector x){
        return x;
    }


")

tmp <- vector("character")
tmp[1] = getTree(lines[1])
writeLines(tmp[1], outputfile)
