#include <iostream>
using namespace std;
#include <string>
#include "student.h"



Student::Student()
{
        studentId = 0;
        name = "";
        major = "";
        gpa = 0.0;
}
Student::Student(int id, string nameinput, string majorinput, double gpainput){
        studentId = id;
        name = nameinput;
        major = majorinput;
        gpa = gpainput;
}
    
void Student::displayStudent() const{
        cout << "Name: " << name 
        << "\nStudent Id: " << studentId 
        << "\nMajor: " <<major 
        << "\nGpa: "<< gpa;
}

int Student::getid() const{
        return studentId;
    }

string Student::getName() const{
        return name;
    }

string Student::getMajor() const{
        return major;
    }

double Student::getGpa() const{
        return gpa;
    }





