#include <iostream>
#include <stdio.h>
#include <fstream>
#include <bitset>
using namespace std;

void r_format(uint32_t);
void i_format(uint32_t);
void j_format(uint32_t);

int main(){
    ifstream binFile("mips-test.bin", ios::in | ios::binary);
    uint32_t currInst;
    uint32_t temp;
    long tm;
    FILE* bFile = fopen("mips-test.bin", "rb");

    for(int i = 0; i < 10; ++i)
    {
        //binFile.seekg(i * 4);
        //binFile.read((char*)&currInst, sizeof(uint32_t));
        fread((char*)&currInst, sizeof(uint32_t), 1, bFile);

        tm = ftell(bFile);

        cout << "#" << i + 1 << ":/t 0x" << hex << currInst << dec
             << endl << "ftell = " << tm << endl;

        temp = currInst >> 26;

        if(temp == 0)
        {
            cout << "R-format:";
            r_format(currInst);
        }
        else if(temp == 2 || temp == 3)
        {
            cout << "J-format";
            j_format(currInst);
        }
        else if(temp > 3)
        {
            cout << "I-format";
            i_format(currInst);
        }
        else
        {
            cout << "Invalid entry\n\n";
        }
    }
    binFile.close();
    return 0;
}

void r_format(uint32_t currInst)
{
    uint32_t temp;

    temp = (currInst >> 21) & 0x1f;
    cout << "\tRs  = " << temp;

    temp = (currInst >> 16) & 0x1f;
    cout << "\tRt = " << temp;

    temp = (currInst >> 11) & 0x1f;
    cout << "\tRd = " << temp;

    temp = (currInst >> 6) & 0x01f;
    cout << "\tSh amt = " << temp;

    temp = currInst & 0x01f;
    cout << "\tFunc = " << temp << "\n\n";

    return;
}

void i_format(uint32_t currInst)
{
    uint32_t temp;

    temp = (currInst >> 21) & 0x1f;
    cout << "\tRs = " << temp;

    temp = (currInst >> 16) & 0x1f;
    cout << "\tRt = " << temp;

    temp = currInst & 0xffff;
    cout << "\tImmediate = " << temp << "\n\n";
}

void j_format(uint32_t currInst)
{
    cout << "\tJump Target = 0x" << hex << (currInst & 0x03ffffff)
         << dec << "\n\n";
    return;
}
