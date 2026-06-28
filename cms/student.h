#ifndef STUDENT_H
#define STUDENT_H

#include <string>
using namespace std;

class Student{
    private:
    int studentId;
    string name;
    string major;
    double gpa;
    public:
    Student();
    Student(int id, string nameinput, string majorinput, double gpainput);

    void displayStudent() const;

    int getid() const;
    string getName() const;
    string getMajor() const;
    double getGpa() const;
};


#endif