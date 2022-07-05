from snakes.nets import *
from dfs_pn import *

def get_net(n=1):
    net = PetriNet('LC')
    net.add_place(Place('p1', [0]))
    net.add_place(Place('p2', [n]))#n
    net.add_place(Place('p3', [0]))
    net.add_place(Place('p4', [0]))
    net.add_place(Place('p5', [0]))
    net.add_place(Place('p6', [n]))#n
    net.add_place(Place('p7', [1]))
    net.add_place(Place('p8', [0]))
    net.add_place(Place('p9', [0]))

    for i in range(n):
        net.add_place(Place('p1' + str(i), [1]))
        net.add_place(Place('p2' + str(i), [0]))
        net.add_place(Place('p3' + str(i), [0]))
    
        net.add_transition(Transition('Approaching' + str(i), Expression('x>=1 and y>=0 and z>=0')))
        
        net.add_input('p1' + str(i), 'Approaching' + str(i), Variable('x'))
        net.add_output('p1' + str(i), 'Approaching' + str(i), Expression('x-1'))
        net.add_output('p2' + str(i), 'Approaching' + str(i), Expression('y+1'))
        net.add_input('p2' + str(i), 'Approaching' + str(i), Variable('y'))
        net.add_output('p1', 'Approaching' + str(i), Expression('z+1'))
        net.add_input('p1', 'Approaching' + str(i), Variable('z'))

        net.add_transition(Transition('Entering' + str(i), Expression('x>=1 and y>=1 and z>=0')))

        net.add_input('p2' + str(i), 'Entering' + str(i), Variable('x'))
        net.add_output('p2' + str(i), 'Entering' + str(i), Expression('x-1'))
        net.add_input('p9', 'Entering' + str(i), Variable('y'))
        net.add_output('p9', 'Entering' + str(i), Expression('y'))
        net.add_output('p3' + str(i), 'Entering' + str(i), Expression('z+1'))
        net.add_input('p3' + str(i), 'Entering' + str(i), Variable('z'))

        net.add_transition(Transition('Leaving' + str(i), Expression('x>=1 and y>=1 and z>=0 and a>=0')))

        net.add_input('p3' + str(i), 'Leaving' + str(i), Variable('x'))
        net.add_output('p3' + str(i), 'Leaving' + str(i), Expression('x-1'))
        net.add_input('p9', 'Leaving' + str(i), Variable('y'))
        net.add_output('p9', 'Leaving' + str(i), Expression('y-1'))
        net.add_output('p1' + str(i), 'Leaving' + str(i), Expression('z+1'))
        net.add_input('p1' + str(i), 'Leaving' + str(i), Variable('z'))
        net.add_output('p4', 'Leaving' + str(i), Expression('a+1'))
        net.add_input('p4', 'Leaving' + str(i), Variable('a'))

    
    net.add_transition(Transition('ClosingRequest', Expression('x>=1 and y>=1 and z>=1 and a>=0 and b>=0')))

    net.add_input('p1', 'ClosingRequest', Variable('x'))
    net.add_output('p1', 'ClosingRequest', Expression('x-1'))
    net.add_input('p2', 'ClosingRequest', Variable('y'))
    net.add_output('p2', 'ClosingRequest', Expression('y-1'))
    net.add_input('p6', 'ClosingRequest', Variable('z'))
    net.add_output('p6', 'ClosingRequest', Expression('z-1'))
    net.add_output('p3', 'ClosingRequest', Expression('a+1'))
    net.add_input('p3', 'ClosingRequest', Variable('a'))
    net.add_output('p5', 'ClosingRequest', Expression('b+1'))
    net.add_input('p5', 'ClosingRequest', Variable('b'))


    net.add_transition(Transition('OpeningRequest', Expression('x>=1 and y>=1 and z>=0 and a>=0')))

    net.add_input('p3', 'OpeningRequest', Variable('x'))
    net.add_output('p3', 'OpeningRequest', Expression('x-1'))
    net.add_input('p4', 'OpeningRequest', Variable('y'))
    net.add_output('p4', 'OpeningRequest', Expression('y-1'))
    net.add_output('p2', 'OpeningRequest', Expression('z+1'))
    net.add_input('p2', 'OpeningRequest', Variable('z'))
    net.add_output('p6', 'OpeningRequest', Expression('a+1'))
    net.add_input('p6', 'OpeningRequest', Variable('a'))
    

    net.add_transition(Transition('KeepDown', Expression('x>=1 and y>=1 and z>=0')))

    net.add_input('p5', 'KeepDown', Variable('x'))
    net.add_output('p5', 'KeepDown', Expression('x-1'))
    net.add_input('p8', 'KeepDown', Variable('y'))
    net.add_output('p8', 'KeepDown', Expression('y'))
    net.add_output('p9', 'KeepDown', Expression('z+1'))
    net.add_input('p9', 'KeepDown', Variable('z'))

    net.add_transition(Transition('Lower', Expression('x>=1 and y>=1 and z>=0 and a>=0')))

    net.add_input('p5', 'Lower', Variable('x'))
    net.add_output('p5', 'Lower', Expression('x-1'))
    net.add_input('p7', 'Lower', Variable('y'))
    net.add_output('p7', 'Lower', Expression('y-1'))
    net.add_output('p9', 'Lower', Expression('z+1'))
    net.add_input('p9', 'Lower', Variable('z'))
    net.add_output('p8', 'Lower', Expression('a+1'))
    net.add_input('p8', 'Lower', Variable('a'))

    net.add_transition(Transition('Raise', Expression('x>=' + str(n) + ' and y>=1 and z>=0')))

    net.add_input('p6', 'Raise', Variable('x'))#n
    net.add_output('p6', 'Raise', Expression('x'))#n
    net.add_input('p8', 'Raise', Variable('y'))
    net.add_output('p8', 'Raise', Expression('y-1'))
    net.add_output('p7', 'Raise', Expression('z+1'))
    net.add_input('p7', 'Raise', Variable('z'))

    return net

if __name__ == "__main__":
    graph, initial_state = run_dfs_pn(get_net())
    write_xml(graph, initial_state, "exports/level_crossing.xml")