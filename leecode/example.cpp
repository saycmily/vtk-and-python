std::stringstream x(lineStr); // string数据流化
std::string str;
struct world_cities city;
std::getline(x, str, ','); // 用逗号隔开
city.name = str;