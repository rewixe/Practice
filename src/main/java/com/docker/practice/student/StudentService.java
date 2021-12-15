package com.docker.practice.student;

import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;

@Service
public class StudentService {

    @GetMapping
    public String StudentList() {
        ArrayList<Student> students = new ArrayList();
        Student kevin = new Student(1L,"Kevin","kev@gmail.com", LocalDate.of(2000, Month.APRIL,1), 21);
        students.add(kevin);
        return students.get(0).toString();
    }
}
