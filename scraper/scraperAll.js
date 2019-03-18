const fs = require('fs');
const puppeteer = require('puppeteer');

const URL = 'https://www.museweb.net/bibliography/?by=all';

function go() {
  return new Promise(async (resolve, reject) => {
    try {
      const browser = await puppeteer.launch();
      const page = await browser.newPage();
      
      await page.goto(URL, { waitUntil: 'load' });

      const toScrape = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('.entry-content p a')).map((e) => {
          return /bib=\d/.test(e.href) ? e.href : null;
        }).filter(Boolean);
      });
      
      let data = [];
      
      for (const link of toScrape) {
        await page.goto(link, { waitUntil: 'load' });
        const paperInfo = await page.evaluate(() => {
          const rows = Array.from(document.querySelectorAll("#main > div > table > tbody > tr"));
          const abstract = rows.map((e) => e.querySelector('td').innerText === 'Abstract:' ? e : null).filter(Boolean);
          const title = rows.map((e) => e.querySelector('td').innerText === 'Title:' ? e : null).filter(Boolean);
          const author = rows.map((e) => e.querySelector('td').innerText === 'Authors:' ? e : null).filter(Boolean);
          const year = rows.map((e) => e.querySelector('td').innerText === 'Year:' ? e : null).filter(Boolean);
          const url = rows.map((e) => e.querySelector('td').innerText === 'Link:' ? e : null).filter(Boolean);
          return {
            title: title.length ? title[0].querySelector('td:nth-child(2)').innerText : null,
            author: author.length ? author[0].querySelector('td:nth-child(2)').innerText : null,
            url: url.length ? url[0].querySelector('td:nth-child(2)').innerText : null,
            year: year.length ? year[0].querySelector('td:nth-child(2)').innerText : null,
            abstract: abstract.length ? abstract[0].querySelector('td:nth-child(2)').innerText : null,
          };
        });
        data.push(paperInfo);
      }

      browser.close();
      return resolve(data);

    } catch (e) {
      return reject(e);
    }
  });
}

go()
  .then((data) => {
    fs.writeFileSync('mwALL.json', JSON.stringify(data));
  }).catch(console.error);