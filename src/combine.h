#ifndef __COMBINE__H__
#define __COMBINE__H__

#include<string>
#include<fstream>
#include<iostream>
#include<vector>

class Combine{
    public:
        bool getCombine(std::vector<std::string> &outputListArr, std::string file, std::string dirpath, int threadCount);
};


#endif