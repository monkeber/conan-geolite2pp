#include "GeoLite2PP.hpp"
#include <iostream>

int main()
{
    GeoLite2PP::DB db;
    std::string json = db.lookup( "216.58.216.163" );
    std::cout << json << std::endl;

    return 0;
}
