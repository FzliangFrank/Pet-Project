## A Business Proposal For Splicing Schedlule Software

Key technical point: 
- [x] graph editing schema [done]
- [ ] graph or subgraph structure
- [ ] transaction (who and when can they edit a graph) management (and make sure each edit don't interfere with one and another)
- [ ] version control features



### Transaction 
One challenge is graph is one person's tansaction made on a graph may not be compatible with the other. 

Let's say some one deleted a node in their own session interacting with the graph. This transaction has not been commited yet. What happen if someone else interacting with node at the same time?

> If the node is eveltually deleted, any connection the second person based up on would be void (because that node was eventually deleted). Or (should action of the next person overwrite it?). But either way they should not have interact with it when the first person start editing. 

The same challenge problem with any collaboration softwere. Mirosoft has encontered this problem. So is Mirror. Even Apple has the same problem. It has always been difficult. 

Because of this concept. We need to restructure of graph model. here are some key concept in this: 

- **isolation**: component of continent of a given graph can be isolated. So one person editing on one continent of graph can not interfere with one on the other graph. 

- **storage**: given space for putting deleted node, or edge component instead of deleting them. So in the event that someone has created unwanted graph this equipment will always be aviable for them. (in the very fact is they need a full managememntal QGIS system).

- **subgraph structure**: For any linked graph. In the very fact if I have this problem solved I can solve other problem? 
It is all about scalling and descaling a graph structure. 
When node count excceds 1000 `visNetwork` suffers significantly. This is where subgraph/sale cames in. This is either by: 
    - Neiborhood alghorithm;
    - Or known structure of the graph;
    - Implementation and Extension as:
        - For instance we can find out how each graph is related and compose these graph into, one node represent a community or mutiple inconnected graph (this require graph to reference one and another)
        - Secondly we want the link between each continent graph and true graph to be somewhat in syn. 
        - In each continent we can identify the last node that goes off to a different continent
- **Version Control**: This generic Structure is suited. And should be easity to implement once you have time stamp imprinted in teh node/edge link. Sheet



> [Also you know people can not always find the perfect candidate, so they have to identify what is the most important for them. Chris identified ability and interests in network modeling is. Ross identified loyatly is the most important fact for him. They both are not neccessiraly wrong.]


Let's Talk Further about Subgraph Structure