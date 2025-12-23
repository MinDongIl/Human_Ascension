package org.example.humanascensionserver;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.jdbc.autoconfigure.DataSourceAutoConfiguration;

// (exclude = {DataSourceAutoConfiguration.class}) 이거 넣어서 DB 연결 일단 무시
@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class})
public class HumanAscensionServerApplication {
    public static void main(String[] args) {
        SpringApplication.run(HumanAscensionServerApplication.class, args);
    }
}
