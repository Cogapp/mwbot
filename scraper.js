const fs = require('fs');
const puppeteer = require('puppeteer');

const URL = 'https://www.museumsandtheweb.com/researchForum7267.html?%24Version=1&%24Path=%2F';
const OUTPUT_PATH = 'mwbib2.txt';

function run(pagesToScrape) {
  return new Promise(async (resolve, reject) => {
    try {
      if (!pagesToScrape) {
        pagesToScrape = 1;
      }

      const browser = await puppeteer.launch({
        headless: false,
      });
      
      const page = await browser.newPage();
      
      await page.goto(URL);
      
      let currentPage = 1;
      let output = [];
      
      while (currentPage <= pagesToScrape) {
        const newOutput = await page.evaluate(() => {
          const results = [];
          const items = document.querySelectorAll('.biblio-entry');
        
          items.forEach((item) => {
            const paperInfo = {
              text: item.querySelector('.biblio-title').innerText,
              link: item.querySelector('.biblio-title a').href,
              author: item.querySelector('.biblio-authors').innerText,
              year: item.querySelector('.biblio-style-apa').childNodes[2].nodeValue.trim(),
            };
            results.push(paperInfo);
          });
          
          return results;
        });
        
        output = output.concat(newOutput);
        
        if (currentPage < pagesToScrape) {
          await Promise.all([
            await page.waitForSelector('.pager-next'),
            await page.click('.pager-next'),
            await page.waitForSelector('.biblio-title'),
          ]);
        }
        currentPage += 1;
      }

      for (let index = 0; index < output.length; index++) {
        await page.goto(output[index]['link'], { waitUntil: 'load' });
        await page.click('.biblio-field-contents-url a');
        await page.waitForSelector('#main-content');
        const text = await page.evaluate(() => {
          return document.querySelector('#main-content').innerText;
        });

        output[index]['text'] = text;
      }

      browser.close();
      return resolve(data);

    } catch (e) {
      return reject(e);
    }
  });
}

run(1).then((data) => {
  fs.writeFileSync('mwbibfull.json', JSON.stringify(data));
}).catch(console.error);