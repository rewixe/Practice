package com.docker.helloworld.resource;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class HelloResourceTest {
    @Test
    void hello() {
        com.docker.helloworld.resource.HelloResource hc = new com.docker.helloworld.resource.HelloResource();
        String out = hc.hello();
        assertEquals("Hello", out);
    }
}