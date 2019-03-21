3. Slightly more clever: TFIDF to remove common words (expect result like "museum digital curator dams web")

Excluding terms that appear in more than 80% of documents and fewer than 5 documents.

```
python 3/main.py data/titles.txt
            term    weight
206       museum  0.072962
356          web  0.049426
216      museums  0.038799
84       digital  0.036592
15           art  0.027618
230       online  0.026169
342      virtual  0.025941
225          new  0.023746
52   collections  0.019279
197       mobile  0.019052
69      cultural  0.018759
337        using  0.018510
168     learning  0.017439
117   experience  0.017411
79        design  0.017407
62       content  0.017378
258      project  0.017151
33      building  0.015786
284         site  0.015505
136     heritage  0.014602
```




```
python main.py data/abstracts.txt
            term    weight
278       museum  0.070219
484          web  0.051708
284      museums  0.050838
293          new  0.042850
116      digital  0.042056
313        paper  0.041506
351      project  0.038945
80       content  0.037471
31           art  0.036909
208  information  0.034666
479     visitors  0.033676
404         site  0.032591
463          use  0.031956
91      cultural  0.031583
300       online  0.030123
70   collections  0.029938
153   experience  0.029882
444   technology  0.029730
107       design  0.029641
99          data  0.029400
```