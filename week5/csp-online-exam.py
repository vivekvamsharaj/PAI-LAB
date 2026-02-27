import networkx as nx
import matplotlib.pyplot as plt

# -------- Data --------
exams = ['E1','E2','E3']
exam_time = {'E1':'9AM','E2':'9AM','E3':'2PM'}
skills = {'P1':['E1','E2'],'P2':['E1','E3'],'P3':['E2','E3']}
domains = {'E1':['P1','P2'],'E2':['P1','P3'],'E3':['P2','P3']}

# -------- Backtracking --------
def backtrack(assign={}):
    if len(assign) == len(exams):
        return assign
    exam = next(e for e in exams if e not in assign)
    for p in domains[exam]:
        if exam in skills[p] and all(
            not (assign.get(e)==p and exam_time[e]==exam_time[exam])
            for e in assign):
            assign[exam] = p
            res = backtrack(assign)
            if res: return res
            assign.pop(exam)
    return None

solution = backtrack({})
print("Proctor Assignment:", solution)

# -------- Graph --------
G = nx.Graph()
G.add_nodes_from(exams + list(skills.keys()))
G.add_edges_from([(e,p) for e,p in solution.items()])

colors = ['skyblue' if n in exams else 'lightgreen' for n in G.nodes()]
nx.draw(G, with_labels=True, node_color=colors, node_size=2000)
plt.show()