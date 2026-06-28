#include <iostream>
#include <fstream>
using namespace std;
#include <string>
#include "student.h"
#include <map>

void loadSampleData(vector<Student>& Students){
    Students.push_back(Student(1001, "James Carter",   "Computer Science", 3.8));
    Students.push_back(Student(1002, "Sofia Martinez", "Mathematics",      3.5));
    Students.push_back(Student(1003, "Liam Johnson",   "Computer Science", 2.9));
    Students.push_back(Student(1004, "Emma Wilson",    "Biology",          3.7));
    Students.push_back(Student(1005, "Noah Brown",     "Mathematics",      3.2));
    Students.push_back(Student(1006, "Ava Thompson",   "Physics",          3.9));
    Students.push_back(Student(1007, "Oliver Davis",   "Computer Science", 2.7));
    Students.push_back(Student(1008, "Isabella White", "Biology",          3.4));
    Students.push_back(Student(1009, "Ethan Harris",   "Physics",          3.6));
    Students.push_back(Student(1010, "Mia Clark",      "Mathematics",      3.1));
}

void displayMenu(){
cout << "\n+------------------------------------------------------+\n";
cout << "|            COLLEGE MANAGEMENT SYSTEM              |\n";
cout << "+------------------------------------------------------+\n";
cout << "| 1. Add Student                                       |\n";
cout << "| 2. View Students                                     |\n";
cout << "| 3. Search Student                                    |\n";
cout << "| 4. Delete Student                                    |\n";
cout << "| 5. Save Data                                         |\n";
cout << "| 6. View Dashboard                                       |\n";
cout << "| 7. Update Student                         |\n";
cout << "| 8. Sort Students                                  |\n";
cout << "| 9. Dean's List                                         |\n";
cout << "| 0. Exit                                              |\n";
cout << "+------------------------------------------------------+\n";
cout << "Enter your choice: ";
}

void saveToCSV(vector<Student>& Students){
    ofstream file("students.txt");

    if(!file.is_open()){
        cout << "Error opening file.";
        return;
    }
    file << "Name, ID, Major, GPA\n";

    for(int i=0; i< Students.size(); i++){
        file << Students[i].getName()  << ","
             << Students[i].getid()    << ","
             << Students[i].getMajor() << ","
             << Students[i].getGpa()   << "\n";
    }

    file.close();
    cout << "Students saved to file succesfully!";

}

bool idExists(vector<Student>& Students, int inputid){
    for(int i=0; i<Students.size(); i++){
        if(Students[i].getid() == inputid )
            return true;
    }
    return false;
}

void dashboard(int students, int avggpa, string major){
cout << "================================\n";
cout << "       DASHBOARD       \n";
cout << "================================\n";
cout << "  Total Students  : " << students << "\n";
cout << "  Average GPA     : " <<avggpa << "\n";
cout << "  Most Popular Major : " << major << "\n";
cout << "================================\n";
}

string mostPopularMajor(vector<Student>& Students){
    map<string, int> majorCount;
    string topMajor;

    for(int i=0; i<Students.size(); i++){
        majorCount[Students[i].getMajor()]++;
        int counter = 0;
        for(auto& pair : majorCount){
            if(pair.second > counter){
                counter += pair.second;
                topMajor = pair.first;
            }
        }
        
    }
    return topMajor;
}


int main(){


    vector<Student> Students;
    loadSampleData(Students);

    int answer;

do{
    displayMenu();
    cin >> answer;

    switch(answer) {

    case 1:{
        string nameInput;
        cout << "enter student name: \n";
        cin.ignore();
        getline(cin, nameInput);
    


        int idInput;
        cout << "enter student id: \n";
        cin >> idInput;
        while(idExists(Students, idInput)){
            cout << "This Id is already taken. Enter another one: ";
            cin >> idInput;
        }
        cin.ignore();

        string majorInput;
        cout << "enter student major: \n";
        getline(cin, majorInput);

        double gpaInput;
        cout << "enter student gpa: \n";
        cin >> gpaInput;

        Student s(idInput, nameInput, majorInput, gpaInput);
        Students.push_back(s);
        cout << "Student Created!" << endl;
    break;

    }

    case 2: {
        if(Students.empty())
            cout << "No Students found";
        for(int i=0; i<Students.size(); i++){
        Students[i].displayStudent();
        cout << "\n------------------\n";
        }
    break;
    }

    case 3: {
        bool found = false;
        int idSearch;

        cout << "Enter Student Id: " << endl;
        cin >> idSearch;

        for(int i=0; i<Students.size(); i++){
            if(Students[i].getid() == idSearch){
                found = true;
                Students[i].displayStudent();
            }
        }
       
       if(found == false)
            cout << "No student found \n";
        
        

        break;
    }

    case 4: {
        bool found = false;
        int idSearch;
        cout << "Enter Id: ";
        cin >> idSearch;


        for(int i=0; i<Students.size(); i++){
            if(Students[i].getid() == idSearch){
                Students.erase(Students.begin() + i);
                cout << "Student deleted succesfully";
                found = true;
            }

            if(!found)
                cout << "Student not found";
        }
    break;
    }

    case 5: 
        saveToCSV(Students);
        break;

    case 6: {
        int totalstudents = Students.size();
        double avggpa;
        for(int i=0; i<Students.size(); i++){
            avggpa += Students[i].getGpa();
        }
        avggpa = avggpa / totalstudents;
        string topMajor = mostPopularMajor(Students);
        dashboard(totalstudents, avggpa, topMajor);
        break;
    }


}
}while(answer!=0);

}
