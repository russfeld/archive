#include <iostream>
using namespace std;

class Person{
	protected:
		int age;
		void happyBirthday();
};

class Student : public Person{
	public:
		int major;
		void setAge(int);
		int getAge();
		void getOlder();
		void changeMajor();
};

void Person::happyBirthday() {
	age = age + 1;
}

void Student::setAge(int anAge) {
	age = anAge;
}

int Student::getAge() {
	return age;
}

void Student::getOlder() {
	happyBirthday();
}
void
Student::changeMajor() {
	major = major + 1;
}

int main(){
	Student student;
  student.age = 42;
  student.major = 2;
  student.happyBirthday();
  student.changeMajor();
  cout << student.age << endl;
  cout << student.major << endl;
  return 0;
}
