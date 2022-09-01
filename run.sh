# This file is toautomatically compile and build a modified
# version of Python Interpreter.
# before executing `run.sh`, please make sure you have cloned
# $ git clone https://github.com/YourVirtualWorld/PyGhostFace
# $ git clone https://github.com/python/cpython`
# And then, `cd PyGhostFace`.
# Please make sure `PyGhostFace` and `cpython` are located in
# the same directory.

CPYTHON_FOLDER=$(cd "$(dirname ../cpython/LICENSE)"; pwd)
echo ${CPYTHON_FOLDER}

# change cpython
cd pyghostface
python3 change_cpython.py \
    --cpython_path ${CPYTHON_FOLDER} \
    --skip_exception \
    --CUSTOM_PROB 0.03 \
    --CUSTOM_MIN_LENGTH 12 \
    --pydict_contains \
    --pydict_size \
    --pyset_contains \
    --pyset_size \
    --pylist_contains \
    --pylist_size

# compile cpython
cd ../../cpython
./comfigure --enable-optimizations
make
make test
sudo make install
