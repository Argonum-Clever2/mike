
#ifndef __COMMAND__H__
#define __COMMAND__H__

#include <map>
#include <string>
#include <vector>
#include <set>
#include<sstream>
#include<iostream>

template <typename T>
T toNumber(std::string strNum){
    T num=0;
    std::stringstream ss;
    ss << strNum;
    ss >> num;
    return static_cast<T>(num);
}


class Command{
    
    public:

        // 参数数组初始化
        std::map<char, std::string>argumentMap;

        std::string description;
        std::string descriptionhash;
        std::string descriptionsimilarity;
        


        // 判断后面的参数是否正确，不正确就打印说明信息
        int run(int argc, const char **argv);
        // 虚函数
        virtual int run()=0;

        void addOption(std::string name);
        bool getFileBoolean(const std::string fileName);
        bool getListBoolean(const std::string fileList);
        bool getPathBoolean(const std::string dirpath);
        void printOption();
        // 直接给参数列表赋值;
        void getDefault();

        std::string name;

        
};


#endif