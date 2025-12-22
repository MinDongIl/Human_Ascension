chrome.declarativeNetRequest.onRuleMatchedDebug?.addListener((info) => {
    console.log("차단됨: ", info);
});

// 이 부분은 사실 Manifest V3에서 declarativeNetRequest의 action type을 "redirect"로 바꿔야 더 깔끔함
// 일단 차단은 됐으니, 사용자가 차단된 페이지를 보려 할 때 아예 욕설 페이지로 보내기