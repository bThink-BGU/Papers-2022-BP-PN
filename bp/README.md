# A BP project for paper.
This folder contains a BP project for generating automaton and all possible paths for BP the BP and translated PN models of the paper.

* *Note: the project requires Java 11 and above and Maven*

## Running the code:
## Installation
<ol>
<li>
Clone the project :

```shell
git clone https://github.com/bThink-BGU/Papers-2022-BP-PN.git
```
</li>
<li>
Compile the code:

```shell
cd Papers-2022-BP-PN/bp
mvn compile
```
</li>
</ol>

## Usage
*IMPORTANT: The program requires a lot of RAM. The exact amount of RAM can* be configured using the [MAVEN_OPTS](https://maven.apache.org/configure.html) environment variable (demonstrated below).

### Run parameters
There are code samples for each of the following paper examples: 
* TicTacToe
* DiningPhilosophers
* LevelCrossing

Each example has two type of models - BP and (translated) PN.


Optional parameters for the Level Crossing example:
* *--num-of-tracks \<arg\>* - number of desired tracks.
* *--no-paths* - do not generate the csv file (see below).
* *--no-helper* - remove helper events for the level-crossing example.
* *--with-faults* - add faults for the level-crossing example.

### Executing the code
```shell
export MAVEN_OPTS="-Xms4g -Xmx8g"
mvn exec:java -D"exec.args"="--example <TicTacToe|DiningPhilosophers|LevelCrossing> --model <BP|PN> --num-of-tracks [number of tracks] [additional params]"
```

### Output
The code creates a folder named "exports" that includes the following files for the requested model:
* A dot file that contains the resulted automaton in [Graphviz](https://graphviz.org/) format.
* A gff file that contains the resulted automaton in [GOAL](http://goal.im.ntu.edu.tw/wiki/doku.php) format.
* A zip file with a csv file in it, that includes a list of all possible execution paths.