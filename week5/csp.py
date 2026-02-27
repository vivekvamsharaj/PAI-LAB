import networkx as nx
import matplotlib.pyplot as plt


class CSP:
    def __init__(self, vars, domains, constraints):
        self.vars = vars
        self.domains = domains
        self.constraints = constraints

    def valid(self, var, val, assign):
        return all(c(var, val, assign) for c in self.constraints.get(var, []))

    def backtrack(self, assign={}):
        if len(assign) == len(self.vars):
            return assign
        var = next(v for v in self.vars if v not in assign)
        for val in self.domains[var]:
            if self.valid(var, val, assign):
                assign[var] = val
                result = self.backtrack(assign)
                if result:
                    return result
                assign.pop(var)
        return None


vars = ['A','B','C']
domains = {v:[1,2,3] for v in vars}
constraints = {
    'A':[lambda v,val,a: 'B' not in a or a['B']!=val,
         lambda v,val,a: 'C' not in a or a['C']!=val],
    'B':[lambda v,val,a: 'A' not in a or a['A']!=val,
         lambda v,val,a: 'C' not in a or a['C']!=val],
    'C':[lambda v,val,a: 'A' not in a or a['A']!=val,
         lambda v,val,a: 'B' not in a or a['B']!=val]
}


csp = CSP(vars, domains, constraints)
sol = csp.backtrack({})
print("Solution:", sol)


G = nx.Graph()
G.add_edges_from([('A','B'),('A','C'),('B','C')])

colors = {1:'red',2:'green',3:'blue'}
nx.draw(G, with_labels=True,
        node_color=[colors[sol[n]] for n in G.nodes()],
        node_size=2000)
plt.show()