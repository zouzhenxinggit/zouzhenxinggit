#include "deepcopy.h"

#include <iostream>
#include <string.h>

int main(int argc, char const *argv[])
{
    DeepCopy cases1((char*)"123", strlen("123"));
    DeepCopy cases2((char*)"45678", strlen("45678"));

    return 0;
}
