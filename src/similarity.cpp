#include"similarity.h"
#include<ctime>

typedef unsigned int uint32;
# define FILETYPE "jac"


Similarity::Similarity(std::string dirpathNew){
    dirpath=dirpathNew;

}
bool Similarity::getFileType(std::string file){
    std::string fileType;
    for(int pos=file.size()-1; pos >= 0; pos--){
        if (file[pos] == '.'){
            fileType=file.substr(pos+1, file.size()-pos);
            break;
        }
    }
    if (fileType.compare(FILETYPE) == 0){
        return true;
    }else{
        return false;
    }
}



float Similarity::getFileCFile(std::string file_1, std::string file_2, int paiLen){
    std::ifstream is1(file_1, std::ios::in);
    std::ifstream is2(file_2, std::ios::in);

    if (!is1.good()){
        std::cerr<<file_1<<" is error, please input the right file! "<<std::endl;
        exit(-1);
    }
    if (!is2.good()){
        std::cerr<<file_2<<" is error, please input the right file! "<<std::endl;
        exit(-1);
    }

    uint32 index1, index2;
    uint32 cnt1, cnt2;
    std::vector<uint32> minhash1_arr(paiLen);
    std::vector<uint32> minhash2_arr(paiLen);
    uint32 intersection = 0;
    uint32 uni = 0;

    uint intersection_arr[paiLen];
    for(int i=0; i < paiLen; i++){
       intersection_arr[i] = 0;
    }

    is1>>index1;
    is2>>index2;


    for(int i=0; i < paiLen; i++){
        is1>>minhash1_arr[i];
        is2>>minhash2_arr[i];
    }

    uni++;

    while ((!is1.eof())&&(!is2.eof())){
        while((!is1.eof())&&(!is2.eof())&&(index1 == index2)){
            for(int i=0; i < paiLen; i++){
                if (minhash1_arr[i] == minhash2_arr[i]){
                    intersection_arr[i]++;
                }
            }
            is1>>index1;
            is2>>index2;
            for(int i=0; i < paiLen; i++){
                is1>>minhash1_arr[i];
                is2>>minhash2_arr[i];
            }

            uni++;
        }
        while ((!is1.eof())&&(!is2.eof())&&(index1 > index2)){
            is2>>index2;
            for(int i=0; i < paiLen; i++){
                is2>>minhash2_arr[i];
            }

            uni++;
        }
        while((!is1.eof())&&(!is2.eof())&&(index1 < index2)){
            is1>>index1;
            for(int i=0; i < paiLen; i++){
                is1>>minhash1_arr[i];
            }

            uni++;
        }
        
    }

    float jaccard;
    for(int i=0; i < paiLen; i++){
        jaccard = (float)intersection_arr[i]/uni;
        if (jaccard > 0.999) jaccard = 1;
    }
    
    is1.close();
    is2.close();
    return jaccard;

}

bool getF2L(std::string file, std::string filelist, int paiLen, Similarity &similarity){
    
    std::ifstream list(filelist, std::ios::in);
    if (!list.good()){
        std::cerr<<filelist<<" is error! please input the right file list(including the absolute path)."<<std::endl;
        return false;
    }
    if(similarity.getFileType(file)){
        std::cerr<<"the input file is error! ! !"<<std::endl;
        return false;
    }

    // 输出文件
    std::string output=similarity.dirpath+"/jaccard.txt"; 
    std::ofstream ot(output, std::ios::out);

    std::vector<std::string> filelistArr;
    std::string suftmp;
    while (!list.eof()){
        getline(list, suftmp);
        if (suftmp == "") break;
        if (similarity.getFileType(suftmp)){
            filelistArr.push_back(suftmp);
        }
    }
    if (filelistArr.size() == 0){
        std::cerr<<"the input file is error! ! ! "<<std::endl;
        return false;
    }

    float jaccard;


    // 时间
    time_t now = time(nullptr);
    tm *curr_tm = localtime(&now);
    char timeArr[80] = {0};
    strftime(timeArr, 80, "%Y-%m-%d %H:%M:%S", curr_tm);
    std::cout<<timeArr<<"    compare："<<file<<std::endl;

    // 数据行
    ot<<'\t';
    for(int i=0; i < filelistArr.size(); i++){
        // 取出名字
        uint32 _PATH_POS = filelistArr[i].rfind('/');
        uint32 _NAME_POS = filelistArr[i].find('.');
        std::string name(filelistArr[i], _PATH_POS+1, _NAME_POS-_PATH_POS-1);
        // 行名
        ot<<'\t'<<name;
    }
    ot<<std::endl;
    // 列名
    uint32 _PATH_POS = file.rfind('/');
    uint32 _NAME_POS = file.find('.');
    std::string name(file, _PATH_POS+1, _NAME_POS-_PATH_POS-1);
    ot<< name;
    for(int i=0; i < filelistArr.size(); i++){
        jaccard=similarity.getFileCFile(file, filelistArr[i], paiLen);
        ot<<'\t'<<jaccard;
    }
    ot<<std::endl;
    ot.close();
    now=time(nullptr);
    curr_tm = localtime(&now);
    strftime(timeArr, 80, "%Y-%m-%d %H:%M:%S", curr_tm);
    std::cout<<timeArr<<"    It has finished. Output: "<<output<<std::endl;

    return 0;
}

bool getL2L(std::string filelist_1, std::string filelist_2, int paiLen, Similarity &similarity){
    std::ifstream list_1(filelist_1, std::ios::in);
    std::ifstream list_2(filelist_2, std::ios::in);
    if (!list_1.good() || !list_2.good()){
        std::cerr<<"the file list is error! please input the right file list(including the absolute path)."<<std::endl;
        return false;
    }

    std::vector<std::string> filelistArr_1;

    std::vector<std::string> filelistArr_2;
    std::string suftmp;

    if (filelist_1.compare(filelist_2) == 0){
        while (!list_1.eof()){
            getline(list_1, suftmp);
            if (suftmp == "") break;
            if (similarity.getFileType(suftmp)){
                filelistArr_1.push_back(suftmp);
            }
        }
        filelistArr_2=filelistArr_1;
    }else{
        while (!list_1.eof()){
            getline(list_1, suftmp);
            if (suftmp == "") break;
            if (similarity.getFileType(suftmp)){
                filelistArr_1.push_back(suftmp);
            }
        }

        while (!list_2.eof()){
            getline(list_2, suftmp);
            if (suftmp == "") break;
            if (similarity.getFileType(suftmp)){
                filelistArr_2.push_back(suftmp);
            }
        }
    }

    if (filelistArr_1.size() == 0 || filelistArr_2.size() == 0){
        std::cerr<<"The file list is error，please check the input! ! !"<<std::endl;
        return false;
    }

    float jaccard;

    // 输出文件
    std::string output=similarity.dirpath+"/jaccard.txt";
    std::ofstream ot(output, std::ios::out);
    // 时间
    time_t now = time(nullptr);
    tm *curr_tm = localtime(&now);
    char timeArr[80] = {0};
    strftime(timeArr, 80, "%Y-%m-%d %H:%M:%S", curr_tm);
    std::cout<<timeArr<<"    compare："<<std::endl;
    // 标题行
    // for(int i=0; i < filelistArr_1.size(); i++){
    //     ot<<"# No."<<i<<" :  "<<filelistArr_1[i]<<std::endl;
    // }

    // 取出名字
    // int listMaxLen = (filelistArr_1.size() > filelistArr_2.size()?filelistArr_1.size():filelistArr_2.size());
    
    for(int i=0; i < filelistArr_2.size(); i++){
        // 取出名字
        uint32 _PATH_POS = filelistArr_2[i].rfind('/');
        uint32 _NAME_POS = filelistArr_2[i].find('.');
        std::string name(filelistArr_2[i], _PATH_POS+1, _NAME_POS-_PATH_POS-1);
        // 行名
        ot<<'\t'<<name;
    }
    ot<<std::endl;


    for(int i=0; i < filelistArr_1.size(); i++){
        // 列名
        uint32 _PATH_POS = filelistArr_1[i].rfind('/');
        uint32 _NAME_POS = filelistArr_1[i].find('.');
        std::string name(filelistArr_1[i], _PATH_POS+1,_NAME_POS-_PATH_POS-1);
        ot<<'\t'<<name;

        for(int j=0; j < filelistArr_2.size(); j++){
            jaccard=similarity.getFileCFile(filelistArr_1[i], filelistArr_2[j], paiLen);
            ot<<'\t'<<jaccard;
        }
        ot<<std::endl;
        now = time(nullptr);
        curr_tm = localtime(&now);
        strftime(timeArr, 80, "%Y-%m-%d %H:%M:%S", curr_tm);
        std::cout<<timeArr<<"    No."<<i<<" has finished. "<<std::endl;
    }


    list_1.close();
    list_2.close();
    ot.close();
    ot<<std::endl;
    now = time(nullptr);
    curr_tm = localtime(&now);
    strftime(timeArr, 80, "%Y-%m-%d %H:%M:%S", curr_tm);
    std::cout<<timeArr<<"    It has finished, Output: "<<output<<std::endl;
    return 0;
}

bool getF2F(std::string file_1, std::string file_2, int paiLen, Similarity &similarity){
    
    std::string fileName_1; 
    std::string fileName_2;
    for(int i=file_1.size()-1; i >= 0; i--){
        if (file_1[i] == '/'){
            fileName_1=file_1.substr(i+1, file_1.size()-1);
            break;
        }
    }

    for(int i=file_2.size()-1; i >=0; i--){
        if (file_2[i] == '/'){
            fileName_2=file_2.substr(i+1, file_2.size()-i);
            break;
        }
    }

    float jaccard;
    if ((similarity.getFileType(file_1))&&(similarity.getFileType(file_2))){
        jaccard = similarity.getFileCFile(file_1, file_2, paiLen);
        std::cout<<"The Jaccard coefficient between "<<fileName_1<<" and "<<fileName_2<<" is "<<jaccard<<std::endl;
        return true;
    }else{
        std::cerr<<"[ERROR]:    The unknown ERROR has has happened. Please check the format of input file."<<std::endl;
        return false;
    }
}

// int main(){
//     std::string dirpath="/public/home/wangfang/sp/tmp/similarity";
//     Similarity similarity(dirpath);
//     std::string file_1="/data0/stu_wangfang/tmp4/kmer_20/tmpdir/farauti.minhash1.txt";
//     std::string file_2="/data0/stu_wangfang/tmp4/kmer_20/tmpdir/melas.minhash1.txt";
//     std::string list_1="/public/home/wangfang/sp/tmp/similarity/list";
//     std::string list_2="/public/home/wangfang/sp/tmp/similarity/list";
//     int paiLen=1;
//     //getF2F(file_1, file_2, paiLen, similarity);
//     // getF2L(file_1, list_2, paiLen, similarity);
//     getL2L(list_1, list_2, paiLen, similarity);

//     return 0;
// }