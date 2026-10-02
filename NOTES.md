# 1. Les classes principales

Je te propose de commencer avec ces 7 classes :
* Zone
* Connection
* Drone
* Graph
* Path
* Simulation
* Scheduler


### A- Zone

Représente un hub de la carte.
```
Zone
├── name
├── x
├── y
├── zone_type
├── color
└── max_drones
```

zone_type pourrait être :
* normal
* blocked
* restricted
* priority

### B- Connection

Représente une liaison entre deux zones.
```
Connection
├── zone_a
├── zone_b
└── max_link_capacity
```
Elle est bidirectionnelle.
Donc :
```
A ───── B
```
permet :
```
A → B
B → A
```
avec la même capacité.

### C- Drone

Représente un drone pendant la simulation.

Il faudra notamment mémoriser :
```
Drone
├── id
├── current_zone
├── state
├── destination
└── remaining_turns
```
Par exemple :
```
D1
current_zone = bottleneck1
state = AT_ZONE
```
ou pendant un déplacement restricted :
```
D1
state = IN_TRANSIT
destination = overflow1
remaining_turns = 1
```

### D- Graph

C'est notre représentation du réseau.
```
Graph
├── zones
├── connections
└── adjacency
```
Par exemple :
```
start
 ├── dist_gate1
 ├── dist_gate2
 └── dist_gate3
```
Le Graph doit savoir répondre à des questions comme :

- Quels sont les voisins de maze_correct ?
- Quelle connexion relie A et B ?
- Cette zone existe-t-elle ?

Mais Graph ne doit pas décider du chemin optimal.

### E- Path

Un chemin complet :
```
start
 → dist_gate1
 → maze_correct
 → bottleneck1
 → bottleneck2
 → priority_hub
 → ...
 → goal
```
Il peut contenir des informations calculées :
```
Path
├── zones
├── total_cost
└── ...
```
L'idée importante :

    Path représente une route, pas son calendrier.

Donc un même Path peut être utilisé avec différents timings.

### F- Simulation

Elle représente l'état global :
```
Simulation
├── graph
├── drones
├── current_turn
└── ...
```
Elle fait évoluer la simulation :
```
turn 1
turn 2
turn 3
...
```

### G- Scheduler

C'est lui qui décide quoi faire à chaque tour.

Conceptuellement :
```
Scheduler
        │
        ├── D1 → zone A
        ├── D2 → zone B
        ├── D3 → WAIT
        └── D4 → zone C
```