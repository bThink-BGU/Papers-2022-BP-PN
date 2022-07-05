from snakes.nets import *
from xml.etree.ElementTree import Element, SubElement, tostring

visited = []

def dfs_pn(g, state, depth, graph):
    global visited
    g.goto(state)
    if depth > 0:
        l = list(g.successors())
        if state not in visited:
            visited.append(state)
            graph[state] = []
            for s in l:
                graph[state].append((s[1].name, s[0]))
                dfs_pn(g, s[0], depth - 1, graph)


def run_dfs_pn(net, depth=1000):
    g = StateGraph(net)
    graph = {}
    initial_state = g.current()
    dfs_pn(g, g.current(), depth, graph)
    return graph, initial_state

def write_xml(g, initial_state, file_name):
    item = Element("Structure")
    item.set("label-on", "Transition")
    item.set("type", "FiniteStateAutomaton")
    child = SubElement(item, "Alphabet")
    child.set("type", "Classical")
    transition_set = set()
    for v in g.values():
        for t, s2 in v:
            transition_set.add(t)
    for t in transition_set:
        grandson = SubElement(child, "Symbol")
        grandson.text = t
    child = SubElement(item, "StateSet")
    for k in g.keys():
        grandson = SubElement(child, "State")
        grandson.set("sid", str(k))
    child = SubElement(item, "InitialStateSet")
    grandson = SubElement(child, "StateID")
    grandson.text = str(initial_state)
    child = SubElement(item, "TransitionSet")
    child.set("complete", "false")
    counter = 0
    for s1, v in g.items():
        for t, s2 in v:
            grandson = SubElement(child, "Transition")
            grandson.set("tid", str(counter))
            grandson2 = SubElement(grandson, "From")
            grandson2.text = str(s1)
            grandson2 = SubElement(grandson, "To")
            grandson2.text = str(s2)
            grandson2 = SubElement(grandson, "Label")
            grandson2.text = t
            counter += 1
    child = SubElement(item, "Acc")
    child.set("type", "Buchi")
    for k in g.keys():
        grandson = SubElement(child, "StateID")
        grandson.text = str(k)
    with open(file_name, "wb") as f:
        f.write(tostring(item))

