# Combined Linkage Model

<!--This project is an implementation for CLM.-->
  We implement the CLM based on KGs and recommender systems for generating more linkage data.  Linkage data is to associate items from recommender systems with entities from Freebase and Yago. 
## Directory
* [Motivations](#Motivations)
* [Datasets](#Datasets)
* [Models](#Models)
* [Usage](#Usage)
* [Licence](#Licence)
* [References](#References)


## <div id="Motivations"></div>Motivations

   
   To provide rich and structured knowledge information for recommender system items, previous methods focus on linking items of recommender systems with Knowledge Graphs (KGs) without considering the impact of linkage ratio on recommendation performance. To bridge this gap, we propose a combined linkage model (CLM) based on existing KGs for generating more linkage data.
   
## <div id="Datasets"></div>Datasets

In our implementation, we organized the linkage results by linked ID pairs, which consists of an item ID of recommender system and an entity ID of KGs. All the IDs are inner values from the original datasets. Here, we present a sample snippet of our linkage results for MovieLens 1M, in which we pair a MovieLens item ID with a Freebase entity ID.

```   

                                           1,m.0dyb1 
                                           2,m.09w353
                                           3,m.0676dr
                                           4,m.03vny7
                                           5,m.094g2z
```

And we present a sample snippet of our linkage results for MovieLens 1M, in which we pair a MovieLens item ID with a Yago entity ID.
   
```   

                                           1,http://yago-knowledge.org/resource/Toy Story
                                           2,http://yago-knowledge.org/resource/Jumanji
                                           3,http://yago-knowledge.org/resource/Grumpier Old Men
                                           4,http://yago-knowledge.org/resource/Waiting to Exhale
                                           5,http://yago-knowledge.org/resource/Father of the Bride Part II
```


We consider two popular recommender systems datasets for linkage, namely MovieLens 1M, Amazon book, which covers the two domains of movie,book respectively. For KGs, we adopt the large-scale Freebase and Yago.

We present the statistics of the linked dataset in the following table:

### Attention! MovieLens 1M and Amazon Book data need to be preprocessed. The rules of preprocessed are showed on the paper.

### Linkage Detail Statistics：
|   Dataset    | Items | Linked-Items | Linkage-ratio | 
|:------------:|:-----:|:------------:|:-------------:|
| MovieLens 1M | 3662  |     3598     |    99.33%     |
| Amazon book  | 59877 |     5564     |     9.29%     |

* `movies.dat`,`users.dat`,`ratings.dat`
  * Original MovieLens 1M data.
  * You can see /data/ml-1m/README
  
* `Books.csv`,`meta_Books.json`
  * Original Amazon book data.
  
* `movies1.txt`,`users1.txt`,`ratings1.txt`
  * Preprocessed movie data.
  
* `Books1.csv`,`Books2.csv`,`BooksMeta.json`
  * Preprocessed book data.
  
* `ml2fb.txt`,`ab2fb.txt`
  * From KB4Rec v1.0 dataset.
  
* `ml2fb2.txt`,`ab2fb2.txt`
  * Generated datasets from CLM on Freebase.

* `mlsubfb.txt`,`absubfb.txt`
  * Triples from Freebase.

* `query-result.csv`,`bookquery-result.csv`
  * All movie entities and book entities in Yago.

* `query-result1.csv`,`bookquery-result1.csv`
  * Special characters of movie entities and book entities are processed of Yago.

* `ml2yg.txt`,`ab2yg.txt`
  * Generated datasets from CLM on Yago.

* `isbn.csv`,`author.csv`
  * 570 books have ISBN and 2876 books have author name from Yago.
  
* `ab2yg1.txt`,`ab2yg2.txt`
  * Linkage number is 218 according to book title and ISBN. 
  * Linkage number is 45 according to book title and author name. 
  * Merge two datasets, the Linkage number is 219 (ab2yg.txt) with Yago.


If you want to get Freebase and Yago data, please refer to our papers.
## <div id="Models"></div>Models
* [RippleNet](https://github.com/hwwang55/RippleNet)
* [KGCN](https://github.com/hwwang55/KGCN)
* [KGAT](https://github.com/xiangwang1223/knowledge_graph_attention_network)
* [KGIN](https://github.com/huangtinglin/Knowledge_Graph_based_Intent_Network)

## <div id="Usage"></div>Usage
### By using our model, you must agree to be bound by the terms of the following [license](#Licence).


## <div id="Licence"></div>Licence

If you want to use our dataset in this project, you must agree to be bound by the terms of the following license.

```
License agreement
This dataset is made freely available to academic and non-academic entities for non-commercial purposes such as academic research, teaching, scientific publications, or personal experimentation. Permission is granted to use the data given that you agree:
1. That the dataset comes “AS IS”, without express or implied warranty. Although every effort has been made to ensure accuracy, we do not accept any responsibility for errors or omissions. 
2. That you include a reference to the our dataset in any work that makes use of the dataset. For research papers, cite our preferred publication as listed on our References; for other media cite our preferred publication as listed on our website or link to the dataset website.
3. That you do not distribute this dataset or modified versions. It is permissible to distribute derivative works in as far as they are abstract representations of this dataset (such as models trained on it or additional annotations that do not directly include any of our data) and do not allow to recover the dataset or something similar in character.
4. That you may not use the dataset or any derivative work for commercial purposes as, for example, licensing or selling the data, or using the data with a purpose to procure a commercial gain.
5. That all rights not expressly granted to you are reserved by us (Hu Jing, Universiti Teknologi Malaysia).
```

## <div id="References"></div>References

If you produce datasets using the CLM according to your own needs, please kindly cite our papers.
You can cite this dataset as below.

```


@inproceedings{
  author    = {
               
                 
              },
  title     = {}
  booktitle = {}
  pages     = {}
  year      = {},
  url       = {},
  doi       = {},
}


```

