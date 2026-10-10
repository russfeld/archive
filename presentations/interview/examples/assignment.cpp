#include <iostream>
using namespace std;

class Vehicle{
  protected:
    double taxRate;
  public:
    Vehicle();
    virtual double taxValue() = 0;
    virtual void vehicleType();
};

Vehicle::Vehicle(){
  taxRate = 36.7;
}

void Vehicle::vehicleType(){
  cout << "Vehicle" << endl;
}

class Car : public Vehicle{
  protected:
    int wheels;
    int doors;
  public:
    void setWheels(int);
    int getWheels();
    void setDoors(int);
    int getDoors();
    virtual double taxValue();
    virtual void vehicleType();
};

void Car::setWheels(int aWheels){
  wheels = aWheels;
}

int Car::getWheels(){
  return wheels;
}

void Car::setDoors(int aDoors){
  doors = aDoors;
}

int Car::getDoors(){
  return doors;
}

double Car::taxValue(){
  return (wheels + doors) * taxRate;
}

void Car::vehicleType(){
  cout << "Car" << endl;
}

class Truck : public Car{
  private:
    double cargoSize;
  public:
    void setCargo(double);
    double getCargo();
    virtual double taxValue();
    virtual void vehicleType();
};

void Truck::setCargo(double aCargo){
  cargoSize = aCargo;
}

double Truck::getCargo(){
  return cargoSize;
}

double Truck::taxValue(){
  return (wheels + doors) * taxRate + cargoSize;
}

void Truck::vehicleType(){
  cout << "Truck" << endl;
}

class Motorcycle : public Vehicle{
  private:
    int speed;
  protected:
    int wheels;
  public:
    void setWheels(int);
    int getWheels();
    void setSpeed(int);
    int getSpeed();
    virtual double taxValue();
    virtual void vehicleType();
};

void Motorcycle::setWheels(int aWheels){
  wheels = aWheels;
}

int Motorcycle::getWheels(){
  return wheels;
}

void Motorcycle::setSpeed(int aSpeed){
  speed = aSpeed;
}

int Motorcycle::getSpeed(){
  return speed;
}

double Motorcycle::taxValue(){
  return (wheels * taxRate) + speed;
}

void Motorcycle::vehicleType(){
  cout << "Motorcycle" << endl;
}

class Scooter : public Motorcycle{
  private:
    int baskets;
  public:
    void setBaskets(int);
    int getBaskets();
    virtual double taxValue();
    virtual void vehicleType();
};

void Scooter::setBaskets(int aBaskets){
  baskets = aBaskets;
}

int Scooter::getBaskets(){
  return baskets;
}

double Scooter::taxValue(){
  return (wheels * taxRate) - (10 * baskets);
}

void Scooter::vehicleType(){
  cout << "Scooter" << endl;
}

int main(){
  char input;
  Vehicle* vehicle;
  Car car;
  Truck truck;
  Motorcycle motorcycle;
  Scooter scooter;
  int tempInt;
  double tempDouble;
  cout << "Choose a vehicle type - [c]ar, [t]ruck, [m]otorcycle, or [s]cooter: ";
  cin >> input;
  switch(input){
    case 'c':
      cout << "Enter a number of wheels: ";
      cin >> tempInt;
      car.setWheels(tempInt);
      cout << "Enter a number of doors: ";
      cin >> tempInt;
      car.setDoors(tempInt);
      vehicle = &car;
      break;
    case 't':
      cout << "Enter a number of wheels: ";
      cin >> tempInt;
      truck.setWheels(tempInt);
      cout << "Enter a number of doors: ";
      cin >> tempInt;
      truck.setDoors(tempInt);
      cout << "Enter a cargo size: ";
      cin >> tempDouble;
      truck.setCargo(tempDouble);
      vehicle = &truck;
      break;
    case 'm':
      cout << "Enter a number of wheels: ";
      cin >> tempInt;
      motorcycle.setWheels(tempInt);
      cout << "Enter a top speed: ";
      cin >> tempInt;
      motorcycle.setSpeed(tempInt);
      vehicle = &motorcycle;
      break;
    case 's':
      cout << "Enter a number of wheels: ";
      cin >> tempInt;
      scooter.setWheels(tempInt);
      cout << "Enter a number of baskets: ";
      cin >> tempInt;
      scooter.setBaskets(tempInt);
      vehicle = &scooter;
      break;
    default:
      cout << "Error!" << endl;
      return 1;
  }
  vehicle->vehicleType();
  cout << "Tax Value: " << vehicle->taxValue() << endl;
  return 0;
}
