# 2017 day 07

Part two was a real bitch.

In the end I created an algorithm that calculated and printed unbalanced
nodes, which I used to manually identify the lone incorrect node.

```python
$ python clusterf.py
part 1: parent found: Node(<vgzejbd>: weight=10 children=[vuoqao(159240), vwkkml(159246), kmpfxl(159240), snuewn(159240), jjgjvki(159240), fiprusz(159240)])
part 2: unbalanced node found: Node(<vgzejbd>: weight=10 children=[vuoqao(159240), vwkkml(159246), kmpfxl(159240), snuewn(159240), jjgjvki(159240), fiprusz(159240)])
part 2: unbalanced node found: Node(<vwkkml>: weight=148790 children=[hvpess(2090), nuozixg(2090), tshyvej(2090), yfxbu(2090), kiatxq(2096)])
--Return--
> /Users/bennett/src/advent-of-code/2017-day07/clusterf.py(85)<module>()->None
-> import pdb; pdb.set_trace()
(Pdb) unbalanced_nodes()
[Node(<vgzejbd>: weight=10 children=[vuoqao(159240), vwkkml(159246), kmpfxl(159240), snuewn(159240), jjgjvki(159240), fiprusz(159240)]), Node(<vwkkml>: weight=148790 children=[hvpess(2090), nuozixg(2090), tshyvej(2090), yfxbu(2090), kiatxq(2096)])]
(Pdb) nodes['kiatxq']
Node(<kiatxq>: weight=1232 children=[dispgy(288), irnjtjo(288), iqpoc(288)])
(Pdb) nodes['kiatxq'].weight = 1226
(Pdb) unbalanced_nodes()
[]
(Pdb)
```

