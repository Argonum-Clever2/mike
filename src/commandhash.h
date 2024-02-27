#ifndef __COMMANDSKETCH__H__
#define __COMMANDSKETCH__H__

#include "command.h"



class Commandhash: public Command
{
public:

    Commandhash();

    virtual int run();// override
};



#endif