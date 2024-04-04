#include<string>
#include<iostream>
#include<map>
#include<vector>
#include"command.h"
#include"dist.h"
#include"commanddist.h"

CommandDist::CommandDist(){
    name = "dist";
    getDefault();
}

int CommandDist::run(){
    std::string list1=argumentMap['l'];
    std::string list2=argumentMap['L'];
    std::string dirpath=argumentMap['d'];
    int32_t paiLen=1;

    Distance distance(dirpath);

    if ((list2.size() != 0) && (list1.size() != 0)){
        getL2L(list1, list2, paiLen, distance);
    }else{
        std::cerr<<"[ERROR]:    "<<"Errors in the two filelists used for comparison. please check the filelist ! "<<std::endl;
    }

    return 0;
}