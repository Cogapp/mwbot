2. Dumb-as-fuck: we took all the words from the title and picked the most popular (expect result like "A the at museum by digital of")

```
python main.py
```

Will print mean title length, mode title length and top 20 most frequently used words, using ../data/all.json as the input

```
Mean title length: 71.41554559043348
Mode title length: [58]
Most frequently used words:
[(':', 773), ('the', 664), ('and', 534), ('of', 425), ('for', 312), ('Museum', 290), ('in', 274), (',', 261), ('to', 238), ('a', 223), ('Web', 155), ('on', 119), ('’', 114), ('A', 114), ('The', 113), ('Digital', 99), ('?', 86), ('Museums', 82), ('with', 80), ('at', 78)]
```


```
python main.py --stop
```

Same but excluding stopwords

```
Mean title length: 71.41554559043348
Mode title length: [58]
Most frequently used words:
[('Museum', 290), ('Web', 155), ('Digital', 99), ('Museums', 82), ("'s", 74), ('Art', 74), ('New', 73), ('Virtual', 69), ('Online', 67), ('Cultural', 52), ('museum', 45), ('Mobile', 44), ('Using', 43), ('Collections', 39), ('Content', 37), ('digital', 36), ('Media', 36), ('Heritage', 35), ('Design', 34), ('Experience', 34)]
```

```
python main.py --stop --normalise
```

Same but normalised

```

```