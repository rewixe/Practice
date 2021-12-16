package com.docker.practice.student;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.Month;
import java.util.ArrayList;

@RestController
@RequestMapping("/rest/docker/student")
public class StudentResource {

    @GetMapping
    public String StudentList() {
        ArrayList<Student> students = new ArrayList();
        Student kevin = new Student(1L,"Kevin","kev@gmail.com", LocalDate.of(2000, Month.APRIL,1));
        students.add(kevin);
        return students.get(0).toString();
    }
}
