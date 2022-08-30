// 定义概率值，使得随机挖坑的概率有变化
#define CUSTOM_PROB {0:.4f}
// 定义最短对象长度，用于限制在较短的 list、set、dict 等对象中易被 debug 发现的问题。
#define CUSTOM_MIN_LENGTH {1:d}

#include "generateuniform.h"
#include "pyport.h"