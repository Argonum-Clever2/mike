#ifndef __COMMANDSIMILARITY__H__
#define __COMMANDSIMILARITY__H__

#include "command.h"
#include "similarity.h"



class CommandSimilarity : public Command
{
public:
    
    CommandSimilarity();
    
    virtual int run(); // override
};


#endif