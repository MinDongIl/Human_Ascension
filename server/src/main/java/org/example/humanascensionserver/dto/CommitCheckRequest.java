package org.example.humanascensionserver.dto;

public record CommitCheckRequest(
        String username,     // 깃허브 아이디
        boolean hasActivity  // 커밋 했냐? (true/false)
) {}
