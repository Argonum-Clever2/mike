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
    cout<<"mike sketch"<<endl<<endl;
    cout<<"Options: "<<endl<<endl;
    //cout<<"-f <file>                 sketch file."<<endl<<endl;
    cout<<"-l <fileList>             a list of files."<<endl<<endl;
    cout<<"-t <int>                  total number of threads (default: 10)"<<endl<<endl;
    cout<<"-d <absolute path>        the path of sketch file."<<endl<<endl;
    cout<<"mike compute"<<endl<<endl;
    cout<<"Options: "<<endl<<endl;
    //cout<<"-f <sketched file>          sketched file."<<endl<<endl;
    cout<<"-l <sketched fileList>      a list of sketched files"<<endl<<endl;
    //cout<<"-F <sketched file>          sketched file."<<endl<<endl;
    cout<<"-L <sketched fileList>      a list of sketched files"<<endl<<endl;
    cout<<"-d <absolute path>     the path of the Jaccard coefficietn file."<<endl<<endl;
    cout<<endl<<"mike dist"<<endl<<endl;
    cout<<endl<<"Option:"<<endl<<endl;
    cout<<"-l <filelist>             a list of sketched files."<<endl<<endl;
    cout<<"-L <filelist>             a list of sketched files."<<endl<<endl;             
    cout<<"-d <absolute path>        the path of the evolutionary distance file."<<endl<<endl;
    cout<<endl<<"mike draw"<<endl<<endl;
    cout<<endl<<"Option:"<<endl<<endl;
    cout<<"-f <filelist>             a list of sketched files."<<endl<<endl;
    cout<<"-L <filelist>             a list of sketched files."<<endl<<endl;             
    cout<<"-d <absolute path>        the path of the evolutionary distance file."<<endl<<endl;

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




