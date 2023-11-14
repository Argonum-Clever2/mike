#include<string>
#include<cstring>
#include "version.h"
#include<iostream>
#include"commandlist.h"

#include "commandhash.h"
#include "commandsimilarity.h"

using std::cout;
using std::endl;
using std::string;


CommandList::CommandList(string nameNew){
    name=nameNew;
}

CommandList::~CommandList(){
    for(std::map<string, Command *>::iterator i=commands.begin(); i != commands.end(); i++){
        delete i->second;
    }
}



void CommandList::printUsage(){
    cout<<endl<<"mike version 1.0 "<<endl;
    cout<<endl<<"Usage:"<<endl<<endl;
    cout<<"mike <command> [options] [arguments...]"<<endl<<endl;
    cout<<"command:"<<endl<<endl;
    //cout<<"kmc                       call the KMC software to process the sequence file."<<endl<<endl;
    cout<<"sketch                    Process a list of genome-skims"<<endl<<endl;
    cout<<"compute                   compute pairwise Jaccard coefficient for a processed a list of genome-skims"<<endl<<endl;
    cout<<"dist                      compute pairwise the evolutionary distancece for a processed a list of genome-skims"<<endl<<endl;
    cout<<"draw                      draw the phylogenetic tree.(use ape of R package)"<<endl<<endl;
    cout<<"for example: "<<endl<<endl;
    cout<<"mike sketch -l /public/home/Argonum/filelist -d /public/home/Argonum/similarity -t 10"<<endl;
    cout<<"mike compute -l /public/home/Argonum/similarity/filelist -L /public/home/Argonum/similarity/filelist -d /public/home/Argonum/"<<endl;
    cout<<"mike draw -f dist.txt -o tree.nwk"<<endl;
}


void CommandList::addCommand(Command *command){
    commands[command->name] = command;
}


int CommandList::run(int argc, const char ** argv){
    if (argc >1 && strcmp(argv[1], "--version") == 0){
        cout<< version <<endl;
        return -1;
    }
    if (argc > 1 && strcmp(argv[1], "--help") == 0){
        printUsage();
        return -1;
    }
    if (argc < 2 || commands.find(argv[1]) == commands.end()){
        printUsage();
        return -1;
    }

    return commands.at(argv[1]) -> run(argc-2, argv+2);
}

// int main(){

//     //const char *tmp[]={"mike", "compute", "-l", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-L", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
//     const char *tmp[]={"mike", "sketch", "-k", "21", "-l", "/data0/stu_wangfang/tmp4/kmer_20/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
//     std::string name="mike";
//     CommandList commandList("mike");
//     commandList.addCommand(new Commandhash);
//     commandList.addCommand(new CommandSimilarity());
//     commandList.run(8, tmp);

//     return 0;
// }