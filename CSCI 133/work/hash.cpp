#include <iostream>
#include <boost/math/distributions/chi_squared.hpp>
#include <cstdint>
#include <iomanip>
#include <fstream>
#include <string>
#include <cmath>
#include <vector>
#include <type_traits>

using namespace std;

#define HASH_INTS = 65536;
#define BINS = 128;

unsigned char char_to_unsigned(char c) {
    return static_cast<std::make_unsigned<char>::type>(c);
}

uint16_t h;

vector<int> hashes(HASH_INTS);
int bins[BINS + 1];
vector<char> titles = ["String Length","First Character","Checksum","Remainder",
"Multiplicative"];

void locate_hashes(int k){
  for (int i = 0; i < k, ++i){
    cout << hashes.at(i) << endl;
  }
};

void bins(){
  for (int i = 0; i < BINS, ++i){
    cout << bins[i] << endl;
  }
};

void division_of_bins(string data){
  int c;
  for (int i = 0; i < BINS, ++i){
    c = 0;
    for (int j = i*512; j < (i + 1) * 512; ++j){
      c += hashes.at(j);
    }
    bins[i] = c;
  }
  c = 0;
  for (int j = BINS * 512; j < HASH_INTS; ++j)
  {
    c += hashes.at(j);
  }
  bins[BINS] = count;
};


float chi_squared_test(){
  double c2 = 0;
  double expected = 99170/HASH_INTS;
  for (int i = 0; i < HASH_INTS; ++i){
    c2 += pow(expected - hashes[i], 2)/expected;
  }
  boost::math::chi_squared c2d(HASH_INTS);
  float p = boost::math::cdf(c2d, c2);
  return p = (1 - p) * 100;
};

void output(string data){
  int p;
  division_of_bins();
  p = chi_squared_test();
  cout << data << "p-value = " << p << endl;
};


int str_len()
{
  string s;
  ifstream inStream;
  inStream.open("/usr/share/dict/words");
  if (inStream.is_open())
  {
    while (getline(inStream, s))
    {
      inStream >> s;

      uint16_t h = s.length() % HASH_INTS;

      hashes.at(h)++;
      }
      output(titles[0]);
      hashes.clear();
}};

int first_char()
{
  string s;
  ifstream inStream;
  inStream.open("/usr/share/dict/words");
  if (inStream.is_open())
  {
    while (getline(inStream, s))
    {
      inStream >> s;

      uint16_t h = s[0] % HASH_INTS;

      hashes.at(h)++;
      }
      output(titles[1]);
      hashes.clear();
};

int check_sum()
{
  string s;
  ifstream inStream;
  inStream.open("/usr/share/dict/words");
  if (inStream.is_open())
  {
    while (getline(inStream, s))
    {
      inStream >> s;

      uint16_t h = s[0];
      for (int i = 1; i<s.length(); ++i){
        h = (h+s[i]) % HASH_INTS;
      }
      hashes.at(h)++;
      }
    output(titles[2]);
    hashes.clear();
};


int rem_hash()
{
  string s;
  ifstream inStream;
  inStream.open("/usr/share/dict/words");
  if (inStream.is_open())
  {
    while (getline(inStream, s))
    {
      inStream >> s;

      uint16_t h = s[0] + 128;
      for (int i = 1; i<s.length(); ++i){
        h = (256 * h + s[i] + 128) % HASH_INTS;
      }
      hashes.at(h)++;
      }
    output(titles[3]);
    hashes.clear();
};



int mult_hash()
{
  string s;
  ifstream inStream;
  inStream.open("/usr/share/dict/words");
  if (inStream.is_open())
  {
    while (getline(inStream, s))
    {
      inStream >> s;

      double h = s[0];
      for (int i = 1; i<s.length(); ++i){
        h = fmod(A(256 * k + c),1);
      }
      h* = HASH_INTS;
      hashes.at(h)++;
      }
    output(titles[4]);
    hashes.clear();

};

int main(){
  str_len();
  first_char();
  check_sum();
  rem_hash();
  mult_hash();
}
