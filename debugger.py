import inspect

class Debug():
    def __init__(self) -> None:
        self.maxLenOfLogs = 10
        self.logEqualsValues = False
        self.variables = {}
        self.variables_frequences = {}
        self.oneLineValues = False
    def addVar(self, varName) -> None:
        self.variables[varName] = []
        self.variables_frequences[varName] = []
    def removeVar(self, varName) -> None:
        del self.variables[varName]
        del self.variables_frequences[varName]
    def addVariables(self, var_list):
         for var in var_list:
            self.variables[var] = []
            self.variables_frequences[var] = []
    def update(self) -> bool:
        caller_locals = inspect.currentframe().f_back.f_locals
        for key, value in self.variables.items():
            if len(value) == 0:
                value.append(caller_locals.get(key))
                self.variables_frequences[key].append(1)
            elif caller_locals.get(key) != value[-1] or self.logEqualsValues:
                value.append(caller_locals.get(key))
                self.variables_frequences[key].append(1)
            else:
                self.variables_frequences[key][-1] += 1
            while len(value) > self.maxLenOfLogs:
                value.pop(0)
        return True
    def show(self):
        for name, values in self.variables.items():
            print(f"########## {name} ##########")
            if self.oneLineValues:
                print(values)
            else:
                for nvalue in range(len(values)):
                    if not(self.logEqualsValues):
                        if self.variables_frequences[name][nvalue] != 1:
                            print(f" - {values[nvalue]}   (x{self.variables_frequences[name][nvalue]})")
                        else:
                            print(f" - {values[nvalue]}")
                    else:
                        print(f" - {values[nvalue]}")
            print()
