#include <iostream>
using namespace std;

class Person{
  protected:
    int age;
  public:
    virtual void whoAmI() = 0;
};

class Student : public Person{
  public:
    void whoAmI();
};

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
