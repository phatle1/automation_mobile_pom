var wd = require('wd');
   var assert = require('assert');
   var asserters = wd.asserters;

   desiredCaps = {
     'browserstack.user' : 'phatle_afrz7u',
     'browserstack.key' : 'zj4zjb2ZMjDn9nzzezPv',
     'build' : 'Node Android',
     'name': 'single_test',
     'device' : 'Samsung Galaxy S10',
     'os_version' : '9.0',
     'interactiveDebugging' : true,
     'browserstack.debug' : true,
     'app' : 'bs://11866145de1c11a6dedbef7ada3cb72fd810f93c', // replace <app_url> with the app URL received in the terminal
   };
   driver = wd.promiseRemote("https://hub-cloud.browserstack.com/wd/hub");

   driver
     .init(desiredCaps)
     .then(function () {
       return driver.waitForElementByAccessibilityId('Search Wikipedia', asserters.isDisplayed && asserters.isEnabled, 30000);
     })
     .then(function (searchElement) {
       return searchElement.click();
     })
     .then(function () {
       return driver.waitForElementById('org.wikipedia.alpha:id/search_src_text', asserters.isDisplayed && asserters.isEnabled, 30000);
     })
     .then(function (searchInput) {
       return searchInput.sendKeys("BrowserStack");
     })
     .then(function () {
       return driver.elementsByClassName('android.widget.TextView'); // Add a breakpoint here
     })
     .then(function (search_results) {
       assert(search_results.length > 0);
     })
     .fin(function() { return driver.quit(); })
     .done();