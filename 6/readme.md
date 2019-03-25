6. Time analysis: how do these popular terms vary over time?

`python main.py --range 1997-2018 --stop`

6.1 Show some graphs

6.2 generate a title (or just some popular words) from each five-year period

`python main.py -d 1997-2001 --stop --customstop`
```
[('Virtual', 33),
('Art', 21),
('Online', 18),
('New', 17),
('Digital', 17),
('Using', 12),
('Sites', 11),
('Internet', 11),
('Design', 11),
('Information', 11),
('Building', 10),
('Site', 10),
('Collections', 10),
('Experience', 9),
('Learning', 9),
('Access', 8),
('Project', 8),
('World', 7),
('Arts', 7),
('Education', 7)]
```

`python main.py -d 2002-2006 --stop --customstop`
```
[('Virtual', 16),
('Digital', 16),
('Experience', 16),
('Online', 15),
('Site', 15),
('On-Line', 14),
('Using', 12),
('Collections', 12),
('New', 12),
('Sites', 11),
('Art', 10),
('Learning', 10),
('Content', 10),
('Educational', 9),
('Knowledge', 9),
('Media', 9),
('Project', 9),
('Cultural', 9),
('Design', 8),
('Study', 8)]
```

`python main.py -d 2007-2011 --stop --customstop `
```
[('New', 18),
('Online', 16),
('Heritage', 14),
('Cultural', 14),
('2.0', 13),
('Art', 12),
('Content', 12),
('Learning', 11),
('Community', 10),
('Social', 10),
('Mobile', 10),
('Collections', 10),
('Virtual', 9),
('Project', 9),
('Using', 9),
('On-line', 8),
('Interactive', 7),
('Access', 7),
('Technology', 7),
('Media', 7)]
```

`python main.py -d 2012-2016 --stop --customstop`
```
[('Digital', 55),
('Art', 29),
('Collections', 19),
('New', 19),
('Online', 19),
('Mobile', 18),
('Using', 17),
('Heritage', 16),
('Project', 16),
('Experience', 16),
('Visitor', 15),
('Cultural', 14),
('Design', 14),
('Open', 13),
('Learning', 13),
('Media', 13),
('Experiences', 12),
('Technology', 11),
('Social', 11),
('Data', 10)]
```

`python main.py -d 2017-2018 --stop --customstop`
```
[('technology', 6),
('digital', 5),
('cultural', 5),
('art', 4),
('understanding', 4),
('learning', 3),
('mobile', 3),
('new', 3),
('experience', 3),
('content', 3),
('audiences', 3),
('learned', 3),
('product', 3),
('Open', 3),
('information', 3),
('interpretation', 2),
('tangible', 2),
('city', 2),
('Crowdsourcing', 2),
('visitors', 2)]
```

6.3 generate a title made of ascendant words to form our end-result title for 2020