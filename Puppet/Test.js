const puppeteer = require('puppeteer-core');

(async () => {
    const browser = await puppeteer.launch({
        executablePath: 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        headless: false,
        slowMo: 250,
        devtools: true,
        ignoreDefaultArgs: ['--disable-extensions']
    });
    const page = await browser.newPage();
    await page.goto('http://mnl785win:8888');
    await page.screenshot({path: 'Trial_1.png'});

    await browser.close();
})();