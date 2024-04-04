#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<stddef.h>
#include <stdarg.h>
#include <sys/types.h>
#include <sys/stat.h>
#include<sys/time.h>
#include <fcntl.h>
#include <unistd.h>
#include<ctype.h>
#include <assert.h>
#include <stdarg.h>
#include <string.h>
#include <errno.h>
#include <dirent.h>
#include <getopt.h>
#include <limits.h>
#include<sys/sysinfo.h>
#include<time.h>

#include <cstdlib>
#include <cstdarg>
#include<cstdio>
#include <thread>
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <chrono>
#include<functional>
#include<algorithm>
#include<map>
#include<sys/time.h>
#include<condition_variable>
#include<mutex>
#include<deque> 
#include<ctime>
#include"threadhash.h"
using namespace std;

# define ALPHAT_COUNT 4
# define SUFFIX_LEN 131072
# define SUFFIX_MAX 4194304
# define PAI_LEN 33
# define PART_CNT 4
# define MASK_CHAR_LEN 4
# define SEED 1
# define PATH_DELIMITER '/'


//输入目标文件的绝对路径，如果存在则返回true，如果不存在则创建，否则的话则返回false；
bool Minhash::getDirPath(const MinhashListInput &minhashinput){
    std::string folder_builder;
    std::string suftmp;
    std::string dirpath;
    if (minhashinput.dirpath[minhashinput.dirpath.size()-1] == '/'){
        dirpath=minhashinput.dirpath.substr(0, minhashinput.dirpath.size()-1);
    }else{
        dirpath=minhashinput.dirpath;
    }

    suftmp.reserve(dirpath.size());
    for(auto it=dirpath.begin(); it != dirpath.end(); ++it){
        const char c = *it;
        suftmp.push_back(c);
        if (c == PATH_DELIMITER || it == dirpath.end()-1){
            folder_builder.append(suftmp);
            if (access(folder_builder.c_str(), F_OK)){
                if (!(mkdir(folder_builder.c_str(), 0755))){
                    cerr<<"The folder doesn't exist，"<<dirpath<<", successfully created。 "<<endl;
                    return true;
                }else{
                    cerr<<dirpath<<", was not created successfully, please check the input！ "<<endl;
                    return false;
                }
            }
            suftmp.clear();
        }
    }
    return true;
}

// bool Minhash::getDirPath(const MinhashFileInput &minhashinput){
//     std::string folder_builder;
//     std::string suftmp;
//     std::string dirpath;
//     if (minhashinput.dirpath[minhashinput.dirpath.size()-1] == '/'){
//         dirpath=minhashinput.dirpath.substr(0, minhashinput.dirpath.size()-1);
//     }else{
//         dirpath=minhashinput.dirpath;
//     }

//     suftmp.reserve(dirpath.size());
//     for(auto it=dirpath.begin(); it != dirpath.end(); ++it){
//         const char c = *it;
//         suftmp.push_back(c);
//         if (c == PATH_DELIMITER || it == dirpath.end()-1){
//             folder_builder.append(suftmp);
//             if (access(folder_builder.c_str(), F_OK)){
//                 if (!(mkdir(folder_builder.c_str(), 0755))){
//                     cerr<<dirpath<<", 文件夹创建成功。 "<<endl;
//                     return true;
//                 }else{
//                     cerr<<dirpath<<", 文件夹创建不成功，请检查输入！"<<endl;
//                     return false;
//                 }
//             }
//             suftmp.clear();
//         }
//     }
//     return true;
// }


// 如果文件列表存在，则输入文件列表数组；如果文件列表不存在，则退出并报错
bool Minhash::getFileList(const MinhashListInput &minhashinput){
    ifstream list(minhashinput.filelist, ios::in);
    if (!list.good()){
        cerr<<"No such "<<minhashinput.filelist<<" please check the input!"<<endl;
        return false;
    }


    std::string suftmp;
    while (!list.eof()){
        std::getline(list, suftmp);
        if (suftmp == "") break;
        fileListArr.push_back(suftmp);
    }
    list.close();
    return true;
}

// 输入文件(包含绝对路径，如果文件不存在，则退出并且返回false)
// bool Minhash::getFileList(const MinhashFileInput &minhashfile){
//     ifstream is(minhashfile.file);
//     if (!is.good()){
//         cerr<<"No such "<<minhashfile.file<<" please check the input!"<<endl;
//         return false;
//     }
//     fileListArr.push_back(minhashfile.file);
//     is.close();
//     return true;
// }

// 输入文件，并且根据线程分成对应的部分，然后返回存储位点的vector
int Minhash::get_read_point(const std::string &file, Minhash::Parameters &parameters){
    Minhash::getReadResizeArr();
    ifstream is(file, ios::in);
    if(!is.good()){
        cerr<<"No such "<<file<<", please check the input!"<<endl;
        exit(-1);
    }

    is.seekg(0, is.end);
    int64 length = is.tellg();
    is.clear();
    is.seekg(0, is.beg);

    int64 avg = length / parameters.threadCout;

    Minhash::readPointArr[0].first = 0;
    int64 begin = Minhash::readPointArr[0].first;

    unsigned int prefix = 0;
    unsigned int prefix_pre = 0;

    // 按照前缀分组
    //std::cout<<parameters.threadCout<<endl;
    for(int i=0; i < parameters.threadCout-1; i++){
        prefix_pre = 0;
        is.seekg(avg, is.cur);
        int64 pos = is.tellg();
        string suftmp;
        std::getline(is, suftmp);
        std::getline(is, suftmp);


        int half_length = parameters.kmerSize/2;

        for(int i=0; i < half_length; i++){
            if ((suftmp[i] == 'A')){
                prefix_pre = ((prefix_pre <<2) | MaskArr[0]);
                //continue;
            }else if (suftmp[i] == 'C'){
                prefix_pre = ((prefix_pre << 2 ) | MaskArr[1]);
                //prefix |= MaskArr[1] << (2*(i));
            }else if (suftmp[i] == 'G'){
                prefix_pre = ((prefix_pre << 2 ) | MaskArr[2]);
                //prefix |= MaskArr[2] << (2*(i));
            }else if (suftmp[i] == 'T'){
                prefix_pre = ((prefix_pre << 2) | MaskArr[3]);
                //prefix |= MaskArr[3] << (2*(i));
            }
        }

        while(1){
            prefix = 0;
            std::getline(is, suftmp);
            for(int i=0; i < half_length; i++){
                if ((suftmp[i] == 'A')){
                    prefix = ((prefix <<2) | MaskArr[0]);
                    //continue;
                }else if (suftmp[i] == 'C'){
                    prefix = ((prefix << 2 ) | MaskArr[1]);
                    //prefix |= MaskArr[1] << (2*(i));
                }else if (suftmp[i] == 'G'){
                    prefix = ((prefix << 2 ) | MaskArr[2]);
                    //prefix |= MaskArr[2] << (2*(i));
                }else if (suftmp[i] == 'T'){
                    prefix = ((prefix << 2) | MaskArr[3]);
                    //prefix |= MaskArr[3] << (2*(i));
                }
            }
            if (prefix != prefix_pre){
                break;
            }
        }

        pos = is.tellg();
        Minhash::readPointArr[i].second = pos - begin;
        //std::cout<<"第"<<i<<"部分的字节长度为"<<readPointArr[i].second<<endl;

        begin = pos;
        Minhash::readPointArr[i+1].first = begin;
        
    }

    Minhash::readPointArr[parameters.threadCout-1].second = length - Minhash::readPointArr[parameters.threadCout-1].first;
    //std::cout<<"第"<<parameters.threadCout-1<<"部分的字节长度为"<<readPointArr[parameters.threadCout-1].second<<endl;

    is.close();
    return 0;
}

int Minhash::get_pai_shuffle(){
    int paiLen = Minhash::getPaiLen();
    vector<uint32> Shuffle(SUFFIX_MAX);
    for(int i=0; i < SUFFIX_MAX; i++){
        Shuffle[i] = i+1;
    }
    
    for(int i=0; i < paiLen; i++){
        srand(unsigned(SEED));
        random_shuffle(Shuffle.begin(), Shuffle.end());
        Minhash::Pai_Shuffle.push_back(Shuffle);
    }
}

int Minhash::getOutputFile(const std::string &file, Minhash::MinhashListInput &minhashlistinput){
    std::string suftmp;
    std::string fileName;
    std::string fileNameNew;
    const char delimeter = '.';
    // 把文件名取出来
    for(int pos=file.size()-1; pos>=0; pos--){
        if (file[pos] == PATH_DELIMITER){
            suftmp = file.substr(pos, file.size()-pos);
            break;
        }
    }
    // 把去掉后缀的文件名取出来
    for(int pos=suftmp.size()-1; pos>=0; pos--){
        if (suftmp[pos] == delimeter){
            fileName = suftmp.substr(0, pos);
            break;
        }
    }

    // 文件名
    for(int i=0; i < minhashlistinput.parameters.threadCout; i++){
        fileNameNew = minhashlistinput.dirpath+fileName+delimeter+to_string(i)+".txt";
        Minhash::outputListArr.push_back(fileNameNew);
        cout<<fileNameNew<<endl;
    }
    return 0;
}

// int Minhash::getOutputFile(const std::string &file, Minhash::MinhashFileInput &minhashfileinput){
//     std::string suftmp;
//     std::string fileName;
//     std::string fileNameNew;
//     const char delimeter = '.';
//     // 把文件名取出来
//     for(int pos=file.size()-1; pos>=0; pos--){
//         if (file[pos] == PATH_DELIMITER){
//             suftmp = file.substr(pos, file.size()-pos);
//             break;
//         }
//     }
//     // 把去掉后缀的文件名取出来
//     for(int pos=suftmp.size()-1; pos>=0; pos--){
//         if (suftmp[pos] == delimeter){
//             fileName = suftmp.substr(0, pos);
//             break;
//         }
//     }

//     // 文件名
//     for(int i=0; i < minhashfileinput.parameters.threadCout; i++){
//         fileNameNew = minhashfileinput.dirpath+fileName+delimeter+to_string(i)+".txt";
//         Minhash::outputListArr.push_back(fileNameNew);
//         cout<<fileNameNew<<endl;
//     }
//     return 0;
// }

int Minhash::clearOutputFile(Minhash &minhash){
    minhash.outputListArr.clear();
    return 0;
}




int get_thread_onehot(const std::string file, int tid, int kmerSize, std::vector<std::vector<unsigned int> > &Pai_Shuffle, std::string output_file, long long start_point, long long volume, int Pai_len){
    ifstream is(file, ios::in);
    if (!is.good()){
        cerr<<"the file is error! the procedure can't read this file"<<endl;
        exit(1);
    }
    string suftmp;
    vector<vector<unsigned int> > kmer_vector;
    //MaskIntArr MASKintarr;
    //vector<MaskIntArr>kmer_vector;
    vector<unsigned int> minhash_arr(Pai_len+1); 
    vector<unsigned int> suffix_arr(SUFFIX_LEN);
    vector<unsigned int> tmp_suffix_arr(SUFFIX_LEN);
    vector<unsigned int> tmp_minhash_arr(Pai_len+1);



    unsigned int prefix = 0U;
    unsigned int prefix_pre = 0U;
    unsigned int suffix = 0U;
    unsigned int minhash = 0U;
    int flag = -1;
    int pos = 0;
    const int len = 32;

    int half_length = kmerSize/2;



    is.seekg(start_point, ios::beg);
    getline(is, suftmp);

    // 给prefix_pre初始化, 同时给minhash_arr的第一个初始化
    for(int i=0; i < half_length; i++){
        if ((suftmp[i] == 'A')){
            prefix_pre = ((prefix_pre <<2) | MaskArr[0]);
            //continue;
        }else if (suftmp[i] == 'C'){
            prefix_pre = ((prefix_pre << 2 ) | MaskArr[1]);
            //prefix |= MaskArr[1] << (2*(i));
        }else if (suftmp[i] == 'G'){
            prefix_pre = ((prefix_pre << 2 ) | MaskArr[2]);
            //prefix |= MaskArr[2] << (2*(i));
        }else if (suftmp[i] == 'T'){
            prefix_pre = ((prefix_pre << 2) | MaskArr[3]);
            //prefix |= MaskArr[3] << (2*(i));
        }
    }
    minhash_arr[0] = prefix_pre;



    //int tmp_cnt = 0;

    while (volume > 0){
        
        if (suftmp == "") break;
        prefix = 0U;
        suffix = 0U;
        for(int i=0; i < half_length; i++){
            if ((suftmp[i] == 'A') && (prefix != 0)){
                prefix = ((prefix <<2) | MaskArr[0]);
                //continue;
            }else if (suftmp[i] == 'C'){
                prefix = ((prefix << 2 ) | MaskArr[1]);
                //prefix |= MaskArr[1] << (2*(i));
            }else if (suftmp[i] == 'G'){
                prefix = ((prefix << 2 ) | MaskArr[2]);
                //prefix |= MaskArr[2] << (2*(i));
            }else if (suftmp[i] == 'T'){
                prefix = ((prefix << 2) | MaskArr[3]);
                //prefix |= MaskArr[3] << (2*(i));
            }
        }

        for (int j=half_length; j < kmerSize; j++){
            if ((suftmp[j] == 'A') && (suffix != 0)) {
                suffix = ((suffix << 2) | MaskArr[0]);
                //continue;
            }else if (suftmp[j] == 'C'){
                suffix = ((suffix << 2) | MaskArr[1]);
                //suffix |= MaskArr[1] << (2*(j-half_length));
            }else if (suftmp[j] == 'G'){
                suffix = ((suffix << 2) | MaskArr[2]);
                //suffix |= MaskArr[2] << (2*(j-half_length));
            }else if (suftmp[j] == 'T'){
                suffix = ((suffix << 2) | MaskArr[3]);
                //suffix |= MaskArr[3] << (2*(j-half_length));
            }
        }

        // 根据前缀进行分组
        if (prefix == prefix_pre){
            // suffix index: suffix >> 5
            // suffix position:  suffix&(32-1)
            // 根据后缀, 对suffix_arr相应的位置进行赋值,one-hot向量
            //suffix_arr[(suffix >> 5)] = (suffix_arr[(suffix >> 5)] | mask_int_arr[suffix&(32-1)]);
            for(int m=0; m < Pai_len; m++){
                if (minhash_arr[m+1] == 0){
                    minhash_arr[m+1] = Pai_Shuffle[m][suffix];
                }else{
                    if (minhash_arr[m+1] > Pai_Shuffle[m][suffix]){
                        minhash_arr[m+1] = Pai_Shuffle[m][suffix];
                    }
                }
            }
        }else{
            kmer_vector.push_back(minhash_arr);
            minhash_arr.assign(tmp_minhash_arr.begin(), tmp_minhash_arr.end());

            // 因为前缀变了以后，还有一个后缀没处理，这个时候还要重复处理一下；
            prefix_pre = prefix;
            minhash_arr[0] = prefix_pre;
            for(int m=0; m < Pai_len; m++){
                if (minhash_arr[m+1] == 0){
                    minhash_arr[m+1] = Pai_Shuffle[m][suffix];
                }else{
                    if (minhash_arr[m+1] > Pai_Shuffle[m][suffix]){
                        minhash_arr[m+1] = Pai_Shuffle[m][suffix];
                    }
                }
            }
        }

        getline(is, suftmp);
        volume -= suftmp.size()+1;
    }
    
    cout<<"<<<<<<<<<<<<<<<<<<<<<<<<"<<" thread "<<tid<<" has finished， quit。"<<">>>>>>>>>>>>>>>>>>>>>>>>>"<<endl;
    

    // 输出文件
    ofstream ot(output_file, ios::out );
    if (!ot.good()){ 
        cerr<<"the file is error!"<<endl;
        exit(-1);
    }
    for(int i=0; i < kmer_vector.size(); i++){
        for(int j=0; j < kmer_vector[i].size(); j++){
            ot<<kmer_vector[i][j]<<"\t";
        }
        ot<<endl;
    }
    ot.close();


    is.clear();
    is.close();
    // 返回值；
    return 0;
}

int get_muliti_thread_hash(const std::string file, Minhash &minhash, Minhash::Parameters &parameters){
    std::vector<std::thread> vec_thread;
    for(int i=0; i < parameters.threadCout; i++){
        std::thread th(get_thread_onehot, file, i, parameters.kmerSize, ref(minhash.Pai_Shuffle), minhash.outputListArr[i], minhash.readPointArr[i].first, minhash.readPointArr[i].second, parameters.paiLen);
        vec_thread.push_back(std::move(th));
    }
    for(auto &th:vec_thread)
        th.join();
    
    return 0;
}


// int main(){

//     Minhash::Parameters parameters;
//     parameters.threadCout = 5;
//     parameters.kmerSize=21;
//     parameters.paiLen=1;
//     std::cout<<parameters.kmerSize<<'\t'<<parameters.threadCout<<'\t'<<parameters.paiLen<<endl;
//     std::string list="./filelist";
//     std::string dirpath="./similarity";

//     Minhash minhash;
//     Minhash::MinhashListInput minhashlistinput(list, dirpath, parameters);
//     if (minhash.getDirPath(minhashlistinput)){

//         minhash.get_pai_shuffle();
//         minhash.getFileList(minhashlistinput);
//         for(int i=0; i < minhash.fileListArr.size(); i++){
//             minhash.get_read_point(minhash.fileListArr[i], parameters);
//             minhash.getOutputFile(minhash.fileListArr[i], minhashlistinput);
//             get_muliti_thread_hash(minhash.fileListArr[i], minhash, parameters);
//             minhash.clearOutputFile(minhash);
//         }
//     }else{
//         cerr<<"The program has happend unknown error! ! ! please check the input! ! !"<<endl;
//     }

//      return 0;

// }
