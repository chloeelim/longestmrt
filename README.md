# Stupid MRT: Hack&Roll 2023

![](./frontend/src/stupidsmrtlogo.svg)

Ever wanted to burn a whole day squeezed in the MRT? Well, we heard you, loud and clear! That's why we built _Stupid MRT_ just for you! (disclaimer: the logo of this app is not an attack on SMRT, but ourselves)

With _Stupid MRT_, you can not just only find the _shortest_ path between two MRT stations (because that's **so** boring, just use Google Maps for that). Instead, we're bringing you a **new**, **everlasting**, **pointless** experience.

Say hello to _Stupid MRT_'s take on a NP-hard problem, served along a side of a ~~stupidly~~ long runtime (somewhere between 30 seconds to 5 minutes). We're bring the longest path problem (by **number of** stations) to Singapore's MRT system!


![](./assets/stupid-mrt-demo.mov)

---
## Take a look beneath the hood

To calculate the longest path, we...
1. precomputed the shortest path between all stations with the Floyd-Warshall algorithm
2. used a priority queue to prioritise nodes that are **further** away from the destination node for optimisation