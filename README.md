# Stupid MRT: Hack&Roll 2023

:warning: Our [github page](https://github.com/chloeelim/longestmrt/deployments/activity_log?environment=github-pages) site is not yet working because we couldn't host our backend server somewhere (~~heroku student tier~~) without facing request timeouts due to the long query time
of our algorithm.

But we're working on that! In the mean time, feel free to play around with our app on your local environment!

---

![stupidsmrtlogo](https://user-images.githubusercontent.com/79991214/212520205-3dd36c6c-886c-4fea-aeba-65771fc18a8c.svg)

Ever wanted to burn a whole day squeezed in the MRT? Well, we heard you, loud and clear! That's why we built _Stupid MRT_ just for you! (disclaimer: the logo of this app is not an attack on SMRT, but ourselves)

With _Stupid MRT_, you can not just only find the _shortest_ path between two MRT stations (because that's **so** boring, just use Google Maps for that). Instead, we're bringing you a **new**, **everlasting**, **pointless** experience.

Say hello to _Stupid MRT_'s take on a NP-hard problem, served along a side of a ~~stupidly~~ long runtime (somewhere between 30 seconds to 5 minutes). We're bring the longest path problem (by **number of** stations) to Singapore's MRT system!

[https://user-images.githubusercontent.com/79991214/212520202-1654e280-35bb-4844-b3c6-fc6f61b5ca63.mov](https://user-images.githubusercontent.com/79991214/212521921-1166f4f5-3f84-4439-92f1-190edb947348.mov
)

---
## Take a look beneath the hood

To calculate the longest path, we...
1. precomputed the shortest path between all stations with the Floyd-Warshall algorithm
2. used a priority queue to prioritise nodes that are ~~**further** away from~~ closer to the destination node ~~for optimisation~~ and recalculate everything (this accident might have actually made it accurate because the other one is incredibly fast but the route seems to be cut to 40-70 stations) 
