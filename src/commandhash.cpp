#include<iostream>
#include<sstream>
#include<vector>
#include"threadhash.h"
#include"commandhash.h"
#include"combine.h"
#include"command.h"


Commandhash::Commandhash(){
    name="sketch";
    getDefault();
}



int Commandhash::run(){

    // 接受参数
    //std::string file=argumentMap['f'];
    std::string list=argumentMap['l'];
    //int32_t kmerSize=toNumber<int32_t>(argumentMap['k']);
    int32_t kmerSize=21;
    int32_t threadCount=toNumber<int32_t>(argumentMap['t']);
    std::string dirpath=argumentMap['d'];
    int32_t paiLen=1;

    // std::cout<<argumentMap['f']<<std::endl;
    // std::cout<<argumentMap['k']<<std::endl;
    // std::cout<<argumentMap['t']<<std::endl;
    // std::cout<<argumentMap['l']<<std::endl;


    // 调用参数40

    Minhash::Parameters parameters;
    parameters.kmerSize=kmerSize;
    parameters.paiLen=paiLen;
    parameters.threadCout=threadCount;
    Minhash minhash;
    Combine combine;
    minhash.get_pai_shuffle();
    if (list !="") {
        if (Commandhash::getListBoolean(list)){
            Minhash::MinhashListInput minlist(list, dirpath, parameters);
            if (minhash.getDirPath(minlist)){
                minhash.getFileList(minlist);
                for(int i=0; i < minhash.fileListArr.size(); i++){
                    minhash.get_read_point(minhash.fileListArr[i], parameters);
                    minhash.getOutputFile(minhash.fileListArr[i], minlist);
                    get_muliti_thread_hash(minhash.fileListArr[i], minhash, parameters);
                    combine.getCombine(minhash.outputListArr, minhash.fileListArr[i], minlist.dirpath, parameters.threadCout);
                    minhash.clearOutputFile(minhash);

                }
            }else{
                return -1;
            }
        }else{
            return -1;
        }
    }else{
            std::cerr<<"The input filelist is error! You should input the list like: "<<std::endl;
            std::cerr<<"for example: mike sketch -l /public/home/Argonum/similarity "<<std::endl;
            return -1;
        
    }
    return 0;

}
// 文件要检查，是否输入正确 不能够-f输入文件列表，-l输入文件

// int main(){
//     Commandhash commandhash;    
//     Command *ptr = new Commandhash();
//     const char *tmp[]={"-k", "21", "-l", "/data0/stu_wangfang/tmp4/kmer_20/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
//     ptr->run(6, tmp);
//     delete ptr;
//     return 0;
// }