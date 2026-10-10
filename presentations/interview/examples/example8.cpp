#include <iostream>
using namespace std;

class Person{
  protected:
    int age;
  public:
    virtual void whoAmI();
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
	Person person;
  Student student;
  person.whoAmI();
  student.whoAmI();
  return 0;
}
