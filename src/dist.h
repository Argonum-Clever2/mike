#ifndef __DISTANCE__H__
#define __DISTANCE__H__

#include<iostream>
#include<fstream>
#include<string>
#include<vector>

class Distance{  
    public:
        Distance(std::string dirpathNew);
        std::string dirpath;
        bool getFileType(std::string file);
        float getFileCFile(std::string fileNew_1, std::string fileNew_2, int paiLenNew);

};


bool getL2L(std::string filelist_1, std::string filelist_2, int paiLen, Distance &distance);
bool getF2L(std::string file, std::string filelist, int paiLen, Distance &distance);
bool getF2F(std::string file_1, std::string file_2, int paiLen, Distance &distance);

#endif