var config = {
    mode: "fixed_servers",
    rules: {
      singleProxy: {
        scheme: "http",
        host: "proxy-server.scraperapi.com",
        port: parseInt("8001")
      },
    bypassList: [""]
    }
  };
chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
function callbackFn(details) {
    return {
        authCredentials: {
            username: "http",
            password: "//scraperapi"
        }
    };
}
chrome.webRequest.onAuthRequired.addListener(
        callbackFn,
        {urls: ["<all_urls>"]},
        ['blocking']
);