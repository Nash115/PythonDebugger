import inspect

class Debug():
    def __init__(self) -> None:
        self.maxLenOfLogs = 10
        self.logEqualsValues = True
        self.variables = {}
        self.oneLineValues = False
    def addVar(self, varName) -> None:
        self.variables[varName] = []
    def removeVar(self, varName) -> None:
        del self.variables[varName]
    def addVariables(self, var_list):
         for var in var_list:
             self.variables[var] = []
    def update(self) -> bool:
        caller_locals = inspect.currentframe().f_back.f_locals
        for key, value in self.variables.items():
            if len(value) == 0:
                value.append(caller_locals.get(key))
            elif caller_locals.get(key) != value[-1] or self.logEqualsValues:
                value.append(caller_locals.get(key))
            while len(value) > self.maxLenOfLogs:
                value.pop(0)
        return True
    def show(self):
        for name, values in self.variables.items():
            print(f"########## {name} ##########")
            if self.oneLineValues:
                print(values)
            else:
                for value in values:
                    print(f" - {value}")
            print()
