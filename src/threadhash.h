#ifndef __THREADHASH__H__
#define __THREADHASH__H__

#include<string>
#include<vector>


typedef unsigned int uint32;
typedef long long int64;
typedef int int32;


static char MaskCharArr[4] = {'A', 'C', 'G', 'T'};
static uint32 MaskIntArr[32] = {1U, 2U, 4U, 8U, 16U, 32U, 64U, 128U, 256U, 512U, 1024U, 2048U, 4096U, 8192U, 16384U, 32768U, 65536U, 131072U, 262144U, 524288U, 1048576U, 2097152U, 4194304U, 8388608U, 16777216U, 33554432U, 67108864U, 134217728U, 268435456U, 536870912U, 1073741824U, 2147483648U};
static uint32 MaskArr[4] = {
    0U, //  0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000
    1U, //  0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0001
    2U, //  0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0010
    3U  //  0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0011
};


class Minhash{
    public:
       // 结构体初始化; 没有输入参数，默认以第一个构造函数开始，如果输入参数了就用第二个构造函数初始化
        struct Parameters{
            Parameters():
                kmerSize(21),
                threadCout(64),
                paiLen(1)
                {}
            
            Parameters(const Parameters &other):
                kmerSize(other.kmerSize),
                threadCout(other.threadCout),
                paiLen(other.paiLen)
                {}
            int kmerSize;
            int threadCout;
            int paiLen;
        };
        // 输入的是一个存有n个文件的文件列表
        struct MinhashListInput{
            MinhashListInput(std::string filelistNew, const std::string dirpathNew, const Minhash::Parameters & parametersNew):
                filelist(filelistNew),
                dirpath(dirpathNew),
                parameters(parametersNew)
                {}
            std::string filelist;
            std::string dirpath;
            Minhash::Parameters parameters;
        };

        struct MinhashFileInput
        {
            MinhashFileInput(std::string fileNew, const std::string dirpathNew, const Minhash::Parameters & parametersNew):
                file(fileNew),
                dirpath(dirpathNew),
                parameters(parametersNew)
                {}
            std::string file;
            std::string dirpath;
            Minhash::Parameters parameters;
        };
        
        std::vector<std::pair<int64, int64> > readPointArr;
        std::vector<std::vector<uint32> > Pai_Shuffle;
        std::vector<std::string> outputListArr;
        std::vector<std::string> fileListArr;

        int getKmerSize() const {return parameters.kmerSize;}
        int getThreadCout() const {return parameters.threadCout;}
        int getPaiLen() const {return parameters.paiLen;}

        bool getDirPath(const MinhashListInput &minhashinput);
        //bool getDirPath(const MinhashFileInput &minhashfile);

        bool getFileList(const MinhashListInput &minhashinput);
        //bool getFileList(const MinhashFileInput &minhashfile);

        bool deleteDirPath(const MinhashListInput &minhashinput);
        bool deleteDirPath(const MinhashFileInput &minhashfile);
        
        int getReadResizeArr(){readPointArr.resize(parameters.threadCout);}
        //int getOutputResizeArr(){outputListArr.resize(parameters.threadCout);}
        int get_read_point(const std::string &file, Minhash::Parameters &parameters);

        int get_pai_shuffle();
        // 错了，这里要用目标路径dirpath
        //int getOutputFile(const std::string &file, Minhash::MinhashFileInput &minhashfileinput);
        int getOutputFile(const std::string &file, Minhash::MinhashListInput &minhashlistinput);
        int clearOutputFile(Minhash &minhash);





    private:
        Parameters parameters;
};

int get_thread_onehot(const std::string file, int tid, int kmerSize, std::vector<std::vector<unsigned int> > &Pai_Shuffle, std::string output_file, long long start_point, long long volume, int Pai_len);
int get_muliti_thread_hash(const std::string file, Minhash &minhash, Minhash::Parameters &parameters);
int get_muliti_list();


#endif
