#ifndef __COMMANDDIST__H__
#define __COMMANDDIST__H__

# include "command.h"
# include "dist.h"

class CommandDist : public Command
{
    public:
    CommandDist();
    virtual int run(); // override
};

#endif
