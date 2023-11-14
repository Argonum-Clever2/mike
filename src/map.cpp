#include <iostream>
#include "threadpool.h"
#include <math.h>
#include <string>

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
#include<getopt.h>
#include<sys/sysinfo.h>
#include<time.h>
#include<chrono>

#include<mutex>
#include<future>
#include<cstdarg>
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

# define SUFTMP_ARR_LEN 256
# define K 21
# define ALPHAT_COUNT 4
# define SUFFIX_SCALE 2
# define VECTOR_LEN 524288
# define BRANCH_LEN 32
# define PREFIX_MAX 1048575
# define SUFFIX_LEN 131072
# define SUFFIX_MAX 4194304
# define MASK_CHAR_LEN 4
# define SEED 1


using namespace std;



int get_pai_Ranking(vector<unsigned int> &Shuffle, vector<vector<unsigned int> > &Pai_Shuffle, int Pai_len){
    
    for (int i=0; i < Pai_len; i++){
        srand(unsigned(SEED));
        random_shuffle(Shuffle.begin(), Shuffle.end());
        Pai_Shuffle.push_back(Shuffle);
    }
    return 0;
}



int main(){

    int part_cnt = 64;
    int Pai_len = 1;

    map<unsigned int, unsigned int> ShuffleMap;
    vector<map<unsigned int, unsigned int>> ShuffleMap_Arr(Pai_len);

    vector<vector<unsigned int> > Pai_Shuffle;
    vector<unsigned int> Shuffle(SUFFIX_MAX);
    for(int i=0; i < SUFFIX_MAX; i++){
        Shuffle[i] = i+1;
    }
    get_pai_Ranking(Shuffle, Pai_Shuffle, Pai_len);

    for(int i=0; i < Pai_Shuffle.size(); i++){
        for(int j=0; j < SUFFIX_MAX; j++){
            ShuffleMap_Arr[i].insert(pair<unsigned int, unsigned int>(Pai_Shuffle[i][j], j));
        }
    }

    string filename="/data0/stu_wangfang/mink/shuffle.txt";
    // //ofstream ot(filename, ios::out);




    ofstream ot(filename, ios::out | ios::binary);

    for(int i=0; i < Pai_len; i++){
        for(int j=0; j < Pai_Shuffle[i].size(); j++){
            ot.write((char*)&(Pai_Shuffle[i][j]), sizeof(Pai_Shuffle[i][j]));
        }
    }



    ifstream is(filename, ios::in | ios::binary);
    vector<unsigned int> tmp(SUFFIX_MAX);
    vector<vector<unsigned int>> tmp_arr(Pai_len);
    vector<map<unsigned int, unsigned int>> buffer_arr(Pai_len);

    // for(int i=0; i < Pai_len; i++){
    //     tmp_arr[i].resize(SUFFIX_MAX);
    //     for(int j=0; j < SUFFIX_MAX; j++){
    //         is>>tmp_arr[i][j];
    //     }
    //     cout<<"<<<<"<<i<<">>>>>"<<endl;
        
    // }
    unsigned int value;
    
    for(int i=0; i < Pai_len; i++){
        unsigned int pos = 0;
        for(int j=0; j < Pai_Shuffle[i].size(); j++){
            is.read((char*)&value, sizeof(value));
            buffer_arr[i].insert(pair<unsigned int, unsigned int>(value, pos++));
        }
    }
    is.close();


    return 0;
}