#include<string>
#include<iostream>
#include<map>
#include<vector>
#include"command.h"
#include"similarity.h"
#include"commandsimilarity.h"


CommandSimilarity::CommandSimilarity(){
    name="compute";
    getDefault();
}


int CommandSimilarity::run() {

    // 接受参数
    //std::string file1=argumentMap['f'];
    //std::string file2=argumentMap['F'];
    std::string list1=argumentMap['l'];
    std::string list2=argumentMap['L'];
    std::string dirpath=argumentMap['d'];
    int32_t paiLen=1;

    // 调用参数
    Similarity similarity(dirpath);

    if ((list2.size() != 0) && (list1.size() != 0)){
        getL2L(list1, list2, paiLen, similarity);
    }else{
        std::cerr<<"Errors in the two filelists used for comparison. please check the filelist ! "<<std::endl;
    }

    return 0;
    
}

// int main(){
//     CommandSimilarity similarity();
//     const char *tmp[]={"-l", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-L", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
//     Command *ptr = new CommandSimilarity;
//     ptr->run(6, tmp);
//     delete ptr;
//     return 0;
// }