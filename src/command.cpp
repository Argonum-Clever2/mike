#include <iostream>
#include <sys/ioctl.h>
#include <sstream>
#include <fstream>
#include<cstring>
#include<sys/stat.h>

#include "command.h"
#include<map>

using std::cout;
using std::cerr;
using std::endl;
using std::string;
using std::exception;
using std::vector;
using std::pair;

#define FILESIZE 1048576


void Command::getDefault(){
    //    {"f", ""}, {"l", ""}, {"k", "21"}, {"t", "5"}, {"d", ""}, {"F", ""}, {"L", ""}
    //argumentMap['f']="";
    argumentMap['l']="";
    //argumentMap['k']="21";
    argumentMap['t']="10";
    argumentMap['d']="";
    //argumentMap['F']="";
    argumentMap['L']="";
}

bool Command::getFileBoolean(const std::string fileName){
    struct stat statbuf;
    stat(fileName.c_str(), &statbuf);
    size_t filesize = statbuf.st_size;
    if (filesize < FILESIZE){
        cerr<<"the file size is tool small, please input the file(>1Mb)."<<endl;
        return false;
    }

    return true;
}

bool Command::getListBoolean(const std::string fileList){
    struct stat statbuf;
    stat(fileList.c_str(), &statbuf);
    size_t filesize = statbuf.st_size;
    if (filesize > FILESIZE){
        cerr<<"the file list is too large, please input the file list(<1Mb)."<<endl;
        return false;
    }
    return true;
}

void Command::printOption(){
    cout<<"mike sketch"<<endl;
    cout<<"Options: "<<endl<<endl;
    //cout<<"-f <file>                 sketch file."<<endl<<endl;
    cout<<"-l <fileList>             the file including a list of files."<<endl<<endl;
    cout<<"-t <int>                  total number of threads (default: 10)"<<endl<<endl;
    cout<<"-d <absolute path>        the path of sketch file."<<endl<<endl;
    cout<<"mike compute"<<endl;
    cout<<"Options: "<<endl<<endl;
    //cout<<"-f <sketched file>          sketched file."<<endl<<endl;
    cout<<"-l <sketched fileList>      the file including a list of sketched files"<<endl<<endl;
    //cout<<"-F <sketched file>          sketched file."<<endl<<endl;
    cout<<"-L <sketched fileList>      the file including a list of sketched files"<<endl<<endl;
    cout<<"-d <absolute path>          the path of the Jaccard coefficietn file."<<endl<<endl;
    cout<<endl<<"mike dist"<<endl;
    cout<<endl<<"Option:"<<endl<<endl;
    cout<<"-l <filelist>             the file including a list of sketched files."<<endl<<endl;
    cout<<"-L <filelist>             the file including a list of sketched files."<<endl<<endl;             
    cout<<"-d <absolute path>        the path of the evolutionary distance file."<<endl<<endl;
    // cout<<endl<<"mike draw"<<endl;
    // cout<<endl<<"Option:"<<endl<<endl;
    // cout<<"-f <filelist>             the file including a list of sketched files."<<endl<<endl;
    // cout<<"-L <filelist>             the file including a list of sketched files."<<endl<<endl;             
    // cout<<"-d <absolute path>        the path of the evolutionary distance file."<<endl<<endl;
    cout<<"**************************************ATTENTION**************************************"<<endl;
    cout<<"                      all files should include the absolute path! ! !                "<<endl;
    cout<<"filelist is the file that include the all files you want to sketch or dist or compute "<<endl;
    cout<<"*************************************************************************************"<<endl<<endl;

    cout <<"EXAMPLE: we input the fastq file, SRR1_R1.fastq, SRR1_R2.fastq, and want to construct the phylogenetic tree. the step is below:" <<endl<<endl;
    cout<<"python kmc.py -f SRR1_R1.fastq SRR1_R2.fastq -d /home/Argonum "<<endl;
    cout<<"mike sketch -t 20 -l /home/Argonum/filelist -d /home/Argonum "<<endl;
    cout<<"mike dist -l /home/Argonum/filelist1 -L /home/Argonum/filelist2 -d /home/Argonum "<<endl;
    cout<<"Rscript draw.r -f /home/Argonum/dist.txt -o /home/Argonum/dist.nwk"<<endl;

}

int Command::run(int argc, const char **argv){

    if (argc == 0){
        printOption();
        return -1;
    }
    if (argc&2==1){
        printOption();
        cout<<"the input Option is lack, please check it."<<endl;
        return -1;
    }
    if (argc ==1 && strcmp(argv[0], "--help") == 0){
        printOption();
        return -1;
    }
    if (argc == 1 && strcmp(argv[0], "-h") == 0){
        printOption();
        return -1;
    }
    for(int i=0; i < argc; i++){
        if ( argv[i][0] == '-' && argv[i][1] != 0){
            if (argumentMap.find((argv[i][1])) == argumentMap.end()){
                printOption();
            }else{
                string str(argv[i+1]);
                argumentMap.at(argv[i][1]) = str;
                i++;
            }
        }else{
            printOption();
            return -1;
        }
    }
    cout<<"<<<<<<<<<<<<<<"<<endl;
    return run();

}




