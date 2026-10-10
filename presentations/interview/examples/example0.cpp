#include <iostream>
using namespace std;

class Person{
  private:
    int age;
  public:
    Person(int);
    int happyBirthday();
};

Person::Person(int anAge){
  age = anAge;
}

int Person::happyBirthday(){
  age = age + 1;
  return age;
}

int main(){
  int anAge = 0;
  cout << "Enter the person's age: ";
  cin >> anAge;
  Person person1 (anAge);
  cout << person1.happyBirthday() << endl;
  cout << person1.happyBirthday() << endl;
  return 0;
}
