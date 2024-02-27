#ifndef __COMMANDLIST__H__
#define __COMMANDLIST__H__

#include"command.h"
#include <map>

class CommandList{
    std::map<std::string, Command *> commands;
    public:
        CommandList(std::string nameNew);
        ~CommandList();

        void addCommand(Command * command);
        void printUsage();
        int run(int argc, const char **argv);

    private:
        std::string name;
};

#endif
