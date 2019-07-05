# MuseWeb paper generator

_A series of experiments to generate an increasingly-convincing paper tile and abstract for the MuseWeb conference (formerly Museums and the Web)._

Techniques include data-mining twenty years of previous papers (output in [the /data folder](data), as spidered by code in [the /scraper folder](scraper)) using techniques susch as natural-language processing (NLP), term-frequency-inverse document frequenct (TF-IDF), Markov chains, and the mightly GPT-2.

This was created for a [lightning talk at MuseWeb 2019](https://mw19.mwconf.org/proposal/bot-to-the-future-using-machine-learning-to-develop-the-ultimate-mw-paper/), and you can read all about the project in [this blog post](https://medium.com/@tristan_roddis/bot-to-the-future-3a22e66b2b01) or [see a video of Tristan presenting the findings at the conference](https://vimeo.com/328666025#t=3m40s), accompanied by the [talk slides](https://docs.google.com/presentation/d/1DHKLS2Jd69D7iuuKrNJ1uFV3fb12xiHB9tD8xyxkcQY/edit?usp=sharing). 

There is also the [graphical interface](https://cogapplabs.github.io/mwbot/) featured in the talk that you can try out yourself to see how common certain words are over MuseWeb's illustrious history.

If you want to try any of the Python code for yourself, first do a ...

`pip install -r requirements.txt`

... from the top-level of this repo. Then look in the numbered directories to find instructions for generating content for each step of the presentation.
