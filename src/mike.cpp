#include "command.h"
#include "commandhash.h"
#include "commandsimilarity.h"
#include "commandlist.h"
#include "commanddist.h"

// 
int main(int argc, const char ** argv)
{
    CommandList commandList("mike");

    commandList.addCommand(new Commandhash);
    commandList.addCommand(new CommandSimilarity);
    commandList.addCommand(new CommandDist);
    //const char *tmp[]={"mike", "compute", "-l", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-L", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
    //const char *tmp[]={"mike", "sketch", "-k", "21", "-l", "/data0/stu_wangfang/tmp4/kmer_20/file.list", "-d", "/data0/stu_wangfang/tmp4/kmer_20/tmpdir/tmpdir"};
    return commandList.run(argc, argv);

}