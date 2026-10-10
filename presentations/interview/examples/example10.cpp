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
	Person person;
  Student student;
  person.whoAmI();
  student.whoAmI();
  return 0;
}
