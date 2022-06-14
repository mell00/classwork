// ======================================================
// File Name: assignment2.cpp
// Author: Madison Ell
// Copyright: None.
// Description: This program calculates mortgage loan amount, maturity date, monthly payment (with and
// without property tax), and total payment.
// Disclaimer: If this program works obviously it's written by me. If it doesn't I don't know who wrote it.
// Revision History:
// Date             Version       ChangeID         Author        Comments
// 10-12-20          1.0                1        Madison Ell    Initial Implementation
// ======================================================

#include <cmath>
#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

void Delay (int milliseconds, std::string delay_message = "", char  delay_symbol = '.');

int main()
{
    int zip_code;
    int principal;
    int maturity_year;
    int time;
    double down_payment;
    double annual_interest_rate;
    double loan_amount;
    double monthly_interest_rate;
    double monthly_payment;
    double monthly_property_tax;
    double total_monthly_payment;
    double total_payment;
    double annual_tax_rate = 0.015;
    string address;
    cout << "Enter property zip code: ";
    cin >> zip_code;
    cout << "Enter property address: ";
    getline(cin, address);
    cout << "Enter property offer price (principal): $";
    cin >> principal;
    cout << "Enter down payment (in percentage %): ";
    cin >> down_payment;
    cout << "Enter annual interest rate (in percentage %): ";
    cin >> annual_interest_rate;
    cout << "Enter number of years financing: ";
    cin >> time;
    Delay (5000, "Mortgage calculator is processing your data ...  Please wait.");   // delay for 5000 miliseconds or five seconds as if your program is busy calculating.
    loan_amount = principal*(1-(down_payment/100));
    monthly_interest_rate = annual_interest_rate/1200;
    monthly_payment = loan_amount*(monthly_interest_rate / (1 - 1/pow(1+monthly_interest_rate, time*12)));
    monthly_property_tax = principal*((annual_tax_rate/100)/12);
    total_monthly_payment = monthly_payment + monthly_property_tax;
    total_payment = total_monthly_payment*12*time;
    maturity_year = 2020+time;

    cout << "\t\t" << "**************************************" << endl;
    cout << "\t\t\t" << "MORTGAGE CALCULATOR RESULTS" << endl;
    cout << "\t\t" << "**************************************" << endl;
    cout << "Property address: " << address << " " << zip_code << endl;
    cout << "Property offer price: " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << principal << endl;
    cout << "Down payment: " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << down_payment << endl;
    cout << "Loan amount: " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << loan_amount << endl;
    cout << "Loan maturity date: " << "\t\t\t\t\t\t\t\t\t\t" << "12/31/" << maturity_year << endl;
    cout << "Mortgage monthly payment: " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << monthly_payment << endl;
    cout << "Monthly payment (property tax included): " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << total_monthly_payment << endl;
    cout << "Total payment: " << "\t\t\t\t\t\t\t\t\t\t" << "$ " << total_payment << endl;

};

void  Delay (int  milliseconds,  std::string delay_message,  char  delay_symbol) {
                   const int millisecond_cycles = 600;

                   std::cout  << delay_message << std::flush ;
                   for (int millisecond =0 ; millisecond < milliseconds;  ++millisecond) {
                          for (int cycle=0;  cycle <= millisecond_cycles * 1000; ++cycle) {
                                if (millisecond%1000 == 0 && cycle == millisecond_cycles) { // print a symbol every second
                                      std::cout << delay_symbol << std::flush;
                                }
                           }
                   }
            }
