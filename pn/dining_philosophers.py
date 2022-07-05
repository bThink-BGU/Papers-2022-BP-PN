from snakes.nets import *
from dfs_pn import *

def get_net():
    net = PetriNet('DP')
    net.add_place(Place('fork1', [1]))
    net.add_place(Place('fork2', [1]))
    net.add_place(Place('p11', [1]))
    net.add_place(Place('p12', [0]))
    net.add_place(Place('p13', [1]))
    net.add_place(Place('p14', [0]))
    net.add_place(Place('p15', [0]))
    net.add_place(Place('p16', [0]))
    net.add_place(Place('p17', [0]))
    net.add_place(Place('p18', [1]))
    net.add_place(Place('p21', [1]))
    net.add_place(Place('p22', [0]))
    net.add_place(Place('p23', [0]))
    net.add_place(Place('p24', [0]))
    net.add_place(Place('p25', [0]))
    net.add_place(Place('p26', [1]))
    net.add_place(Place('p27', [0]))
    net.add_place(Place('p28', [1]))

    net.add_transition(Transition('putRightFork1', Expression('x>=1 and y>=0 and z>=0')))
    net.add_input('p12', 'putRightFork1', Variable('x'))
    net.add_output('p12', 'putRightFork1', Expression('x-1'))
    net.add_output('p11', 'putRightFork1', Expression('y+1'))
    net.add_input('p11', 'putRightFork1', Variable('y'))
    net.add_output('fork1', 'putRightFork1', Expression('z+1'))
    net.add_input('fork1', 'putRightFork1', Variable('z'))

    net.add_transition(Transition('takeRightFork1', Expression('x>=1 and y>=1 and z>=0')))
    net.add_input('fork1', 'takeRightFork1', Variable('x'))
    net.add_output('fork1', 'takeRightFork1', Expression('x-1'))
    net.add_input('p11', 'takeRightFork1', Variable('y'))
    net.add_output('p11', 'takeRightFork1', Expression('y-1'))
    net.add_output('p14', 'takeRightFork1', Expression('z+1'))
    net.add_input('p14', 'takeRightFork1', Variable('z'))

    net.add_transition(Transition('startThinking1', Expression('x>=1 and y>=0 and z>=0 and a>=0')))
    net.add_input('p16', 'startThinking1', Variable('x'))
    net.add_output('p16', 'startThinking1', Expression('x-1'))
    net.add_output('p15', 'startThinking1', Expression('y+1'))
    net.add_input('p15', 'startThinking1', Variable('y'))
    net.add_output('p12', 'startThinking1', Expression('z+1'))
    net.add_input('p12', 'startThinking1', Variable('z'))
    net.add_output('p13', 'startThinking1', Expression('a+1'))
    net.add_input('p13', 'startThinking1', Variable('a'))

    net.add_transition(Transition('startEating1', Expression('x>=1 and y>=1 and z>=1 and a>=0')))
    net.add_input('p13', 'startEating1', Variable('x'))
    net.add_output('p13', 'startEating1', Expression('x-1'))
    net.add_input('p14', 'startEating1', Variable('y'))
    net.add_output('p14', 'startEating1', Expression('y-1'))
    net.add_input('p17', 'startEating1', Variable('z'))
    net.add_output('p17', 'startEating1', Expression('z-1'))
    net.add_output('p16', 'startEating1', Expression('a+1'))
    net.add_input('p16', 'startEating1', Variable('a'))

    net.add_transition(Transition('putLeftFork1', Expression('x>=1 and y>=0 and z>=0')))
    net.add_input('p15', 'putLeftFork1', Variable('x'))
    net.add_output('p15', 'putLeftFork1', Expression('x-1'))
    net.add_output('p18', 'putLeftFork1', Expression('y+1'))
    net.add_input('p18', 'putLeftFork1', Variable('y'))
    net.add_output('fork2', 'putLeftFork1', Expression('z+1'))
    net.add_input('fork2', 'putLeftFork1', Variable('z'))

    net.add_transition(Transition('takeLeftFork1', Expression('x>=1 and y>=1 and z>=0')))
    net.add_input('fork2', 'takeLeftFork1', Variable('x'))
    net.add_output('fork2', 'takeLeftFork1', Expression('x-1'))
    net.add_input('p18', 'takeLeftFork1', Variable('y'))
    net.add_output('p18', 'takeLeftFork1', Expression('y-1'))
    net.add_output('p17', 'takeLeftFork1', Expression('z+1'))
    net.add_input('p17', 'takeLeftFork1', Variable('z'))

    net.add_transition(Transition('takeLeftFork2', Expression('x>=1 and y>=1 and z>=0')))
    net.add_input('fork1', 'takeLeftFork2', Variable('x'))
    net.add_output('fork1', 'takeLeftFork2', Expression('x-1'))
    net.add_input('p21', 'takeLeftFork2', Variable('y'))
    net.add_output('p21', 'takeLeftFork2', Expression('y-1'))
    net.add_output('p22', 'takeLeftFork2', Expression('z+1'))
    net.add_input('p22', 'takeLeftFork2', Variable('z'))

    net.add_transition(Transition('putLeftFork2', Expression('x>=1 and y>=0 and z>=0')))
    net.add_input('p24', 'putLeftFork2', Variable('x'))
    net.add_output('p24', 'putLeftFork2', Expression('x-1'))
    net.add_output('p21', 'putLeftFork2', Expression('y+1'))
    net.add_input('p21', 'putLeftFork2', Variable('y'))
    net.add_output('fork1', 'putLeftFork2', Expression('z+1'))
    net.add_input('fork1', 'putLeftFork2', Variable('z'))

    net.add_transition(Transition('startEating2', Expression('x>=1 and y>=1 and z>=1 and a>=0')))
    net.add_input('p22', 'startEating2', Variable('x'))
    net.add_output('p22', 'startEating2', Expression('x-1'))
    net.add_input('p26', 'startEating2', Variable('y'))
    net.add_output('p26', 'startEating2', Expression('y-1'))
    net.add_input('p25', 'startEating2', Variable('z'))
    net.add_output('p25', 'startEating2', Expression('z-1'))
    net.add_output('p23', 'startEating2', Expression('a+1'))
    net.add_input('p23', 'startEating2', Variable('a'))

    net.add_transition(Transition('startThinking2', Expression('x>=1 and y>=0 and z>=0 and a>=0')))
    net.add_input('p23', 'startThinking2', Variable('x'))
    net.add_output('p23', 'startThinking2', Expression('x-1'))
    net.add_output('p24', 'startThinking2', Expression('y+1'))
    net.add_input('p24', 'startThinking2', Variable('y'))
    net.add_output('p26', 'startThinking2', Expression('z+1'))
    net.add_input('p26', 'startThinking2', Variable('z'))
    net.add_output('p27', 'startThinking2', Expression('a+1'))
    net.add_input('p27', 'startThinking2', Variable('a'))

    net.add_transition(Transition('takeRightFork2', Expression('x>=1 and y>=1 and z>=0')))
    net.add_input('fork2', 'takeRightFork2', Variable('x'))
    net.add_output('fork2', 'takeRightFork2', Expression('x-1'))
    net.add_input('p28', 'takeRightFork2', Variable('y'))
    net.add_output('p28', 'takeRightFork2', Expression('y-1'))
    net.add_output('p25', 'takeRightFork2', Expression('z+1'))
    net.add_input('p25', 'takeRightFork2', Variable('z'))

    net.add_transition(Transition('putRightFork2', Expression('x>=1 and y>=0 and z>=0')))
    net.add_input('p27', 'putRightFork2', Variable('x'))
    net.add_output('p27', 'putRightFork2', Expression('x-1'))
    net.add_output('p28', 'putRightFork2', Expression('y+1'))
    net.add_input('p28', 'putRightFork2', Variable('y'))
    net.add_output('fork2', 'putRightFork2', Expression('z+1'))
    net.add_input('fork2', 'putRightFork2', Variable('z'))

    return net

if __name__ == "__main__":
    graph, initial_state = run_dfs_pn(get_net())
    write_xml(graph, initial_state, "exports/dining_philosophers.xml")




















