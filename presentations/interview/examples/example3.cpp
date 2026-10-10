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
  Administrator admin;
	Teacher* teacher = &admin;
	Person* person = &admin;
  admin.age = 25;
  admin.title = 5;
	admin.salary = 12;
  teacher->happyBirthday();
  admin.promotion();
  cout << person->age << endl;
  cout << teacher->title << endl;
	cout << admin.salary << endl;
  return 0;
}
