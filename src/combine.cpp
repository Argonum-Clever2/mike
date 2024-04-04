#include<stdlib.h>
#include<stdio.h>
#include<string>
#include<sstream>
#include<vector>
#include<fstream>
#include<cstdio>
#include<iostream>
#include<chrono>
#include"threadhash.h"
#include"combine.h"


bool Combine::getCombine(std::vector<std::string> &outputListArr, std::string file, std::string dirpath, int threadCount){
    std::string outfileName;
    std::string fileName;
    const char path_delimeter='/';
    // 提出文件名
    for(int pos=file.size()-1; pos >=0; pos--){
        if (file[pos] == path_delimeter){
            fileName=file.substr(pos, file.size()-pos);
            break;
        }
    }
    // 插入输出文件的名字
    std::string name;
    const char file_delimeter = '.';
    for(int pos=fileName.size()-1; pos >= 0; pos--){
        if (fileName[pos] == file_delimeter){
            name=fileName.substr(0, pos)+".minhash.jac";
            break;
        }
    }
    

    outfileName=dirpath+name;

    std::ofstream ot(outfileName, std::ios::out);
    std::string suftmp;

    for(int i=0; i < outputListArr.size(); i++){
        std::ifstream is(outputListArr[i], std::ios::in);
        if (!is.good()){
            std::cerr<<outputListArr[i]<<" is error, please check the file!"<<std::endl;
            return false;
        }
        while(!is.eof()){
            getline(is, suftmp);
            if (suftmp[suftmp.size()-1] != '\n')
                suftmp += "\n";
            if (suftmp == "") break;
            ot<<suftmp;
        }
        is.close();
        if (!remove(outputListArr[i].c_str())==0){
            std::cout<<errno<<std::endl;
        }
    }

    ot.close();
    return 0;
}

// int main(){
//     Combine combine;
//     Minhash minhash;
//     Minhash::Parameters parameters;
//     parameters.threadCout=1;
//     //parameters.threadCout=5;

//     std::string dirpath="/public/home/wangfang/simulate/ncbi_p/fastadir/fqdir/fqdir/similarity";
//     std::string list="/public/home/wangfang/simulate/ncbi_p/fastadir/fqdir/fqdir/filelist";
//     Minhash::MinhashListInput minhashfileinput(list, dirpath, parameters);
//     minhash.getFileList(minhashfileinput);
//     for(int i=0; i < minhash.fileListArr.size(); i++){
//         minhash.getOutputFile(minhash.fileListArr[i], minhashfileinput);
//         combine.getCombine(minhash.outputListArr, minhash.fileListArr[i], minhashfileinput.dirpath, parameters.threadCout);
//         minhash.clearOutputFile(minhash);
//     }
//     return 0;
// }