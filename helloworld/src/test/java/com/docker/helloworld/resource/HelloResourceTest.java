package com.docker.helloworld.resource;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HelloResourceTest {
    @Test
    void hello() {
        HelloResource hc = new HelloResource();
        String out = hc.hello();
        assertEquals("Hello", out);
    }
}