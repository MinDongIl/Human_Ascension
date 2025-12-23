package org.example.humanascensionserver.controller;

import org.example.humanascensionserver.dto.CommitCheckRequest;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@Slf4j
@RestController
@RequestMapping("/api/v1/monitor")
public class MonitorController {

    @PostMapping("/commit-check")
    public ResponseEntity<Map<String, Object>> reportCommit(@RequestBody CommitCheckRequest request) {

        log.info("생존 신고 들어옴 - ID: {}, 생존여부: {}", request.username(), request.hasActivity());

        if (request.hasActivity()) {
            log.info("[인증 성공] {}, 오늘은 인간이네", request.username());
            return ResponseEntity.ok(Map.of("message", "생존 확인. 내일도 이렇게 살아라."));
        } else {
            log.error("[폐기물 감지] {}님, 오늘 커밋 0회. 아 수금 달달하다 병신새끼 ㅋㅋ", request.username());
            // 202 Accepted: 접수는 했는데 넌 좀 맞아야겠다.
            return ResponseEntity.accepted().body(Map.of("message", "너 이 새끼 오늘 뒤졌다."));
        }
    }
}
