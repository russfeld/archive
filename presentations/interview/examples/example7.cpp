#include <iostream>
using namespace std;

class Person{
  protected:
    int age;
  public:
    void whoAmI();
};

class Student : public Person{
  public:
    void whoAmI();
};

void Person::whoAmI() {
  cout << "Parent" << endl;
}

void Student::whoAmI() {
  cout << "Student" << endl;
}

int main(){
  Student student;
  Person* person = &student;
  student.whoAmI();
  person->whoAmI();
  return 0;
}
