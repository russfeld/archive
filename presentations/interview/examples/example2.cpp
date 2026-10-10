#include <iostream>
using namespace std;

class Person{
	public:
		int age;
		void happyBirthday();
};

class Student : public Person{
	public:
		int major;
		void changeMajor();
};

class Teacher: public Person{
	public:
		int title;
		void promotion();
};

class Administrator: public Teacher{
	public:
		int salary;
		void promotion();
};

void Person::happyBirthday() {
	age = age + 1;
}

void Student::changeMajor() {
	major = major + 1;
}

void Teacher::promotion() {
	title = title + 1;
}

void Administrator::promotion() {
	title = title + 1;
	salary = salary + 1;
}

int main(){
  Student student;
	Person* person = &student;
  student.age = 42;
  student.major = 2;
  student.happyBirthday();
  student.changeMajor();
  cout << student.age << endl;
	cout << person->age << endl;
  cout << student.major << endl;
  return 0;
}
