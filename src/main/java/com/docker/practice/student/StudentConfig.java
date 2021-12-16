package com.docker.practice.student;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;
import java.time.Month;

@Configuration
public class StudentConfig {

    @Bean
    CommandLineRunner commandLineRunner(
            StudentRepository repository) {
        return args -> {
            Student kevin = new Student(1L,"Kevin","kev@gmail.com", LocalDate.of(2000, Month.APRIL,1));
            Student john = new Student(1L,"John","john@gmail.com", LocalDate.of(2001, Month.MARCH,14));
            repository.save(john);
            repository.save(kevin);
        };
    }
}
