# A Python project for the Petri-nets models of the paper
<b>This repository contains Petri nets models of the paper implemented using the [SNAKES](https://snakes.ibisc.univ-evry.fr) package. The code creates a pn model and generates a reachability graph automaton. The automaton is written in xml and can be viewed and edited using [GOAL](http://goal.im.ntu.edu.tw/wiki/doku.php). </b>

<b>*Note: the project was implemented and tested on Python 3.7.4</b>
## Installation
<ol>
<li>
Clone the project :

```shell
git clone https://github.com/bThink-BGU/Papers-2022-BP-PN.git
```
</li>
<li>
Create a virtual environment and activate it:

```shell
cd Papers-2022-BP-PN/pn
python -m venv venv 
source venv/bin/activate
```
</li>
<li>
Update pip and install all dependencies:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```
</li>
</ol>

## Usage
### creating reachability graph automata for the Petri nets:
<ul>
<li>
Level Crossing:

```shell
python level_crossing.py
```
</li>

<li>
Dining Philosophers:

```shell
python dining_philosophers.py
```
</li>

<li>
Tic-Tac-Toe:

```shell
python tic_tac_toe.py
```
</li>
</ul>

