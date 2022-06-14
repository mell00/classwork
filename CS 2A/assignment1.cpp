//============================================================================
// File Name   : assignment1.cpp
// Author      : Madison Ell
// Copyright   : Your copyright notice
// Description :  This program displays a movie ticket stub.

// Revision History:
// Date              Version     Change ID         Author             Comment
// 09/29/20          1.0           123              Madison Ell       Initial creation, revisions
//============================================================================

#include <iostream>
#include <iomanip>
#include <string>

using namespace std;

int main ()  {
    int time_minutes = 0;
    int time_hours = 0;
    int date_month = 0;
    int date_day = 0;
    int date_year = 0;
    int theater_number = 0;
    double adult_price = 0.0;
    time_minutes = 20;
    time_hours = 3;
    date_month = 9;
    date_day = 25;
    date_year = 2020;
    theater_number = 10;
    adult_price = 12.75;
    string movie_title = "A Star is Born Encore";
    string am_or_pm = "PM";
    string movie_rating = "PG-13";
    cout << "--------------------------------------------------------------------------------------------------------------------------------\n";

     cout << "\t\t AMC Universal CityWalk\n";
     cout << "\t\t Presenting\n";
     cout << "\t\t" << movie_title << "\n";
     cout << "Show time: " << time_hours << ":" << time_minutes << " " << am_or_pm;
     cout << "\t Date: " << date_month << "/" << date_day << "/" << date_year << "\n";
     cout << "Theater: "<< theater_number;
     cout << "\t\t" << movie_rating << endl;
     cout << "Adult Admission  $" << adult_price << endl;
     cout << "Don't forget to get your free small popcorn with 4 tickets or more!!!" << endl;
     cout << "--------------------------------------------------------------------------------------------------------------------------------";
     return 0;
}
