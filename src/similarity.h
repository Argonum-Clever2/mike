#ifndef __SIMILARITY__H__
#define __SIMILARITY__H__

#include<iostream>
#include<fstream>
#include<string>
#include<vector>

class Similarity{  
    public:
        Similarity(std::string dirpathNew);
        std::string dirpath;
        bool getFileType(std::string file);
        float getFileCFile(std::string fileNew_1, std::string fileNew_2, int paiLenNew);

};


bool getL2L(std::string filelist_1, std::string filelist_2, int paiLen, Similarity &similarity);
bool getF2L(std::string file, std::string filelist, int paiLen, Similarity &similarity);
bool getF2F(std::string file_1, std::string file_2, int paiLen, Similarity &similarity);

#endif