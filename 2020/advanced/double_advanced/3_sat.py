def evaluate3sat(args, statements):
    def propToArg(s): return not args[int(s[1])] if s[0] == "~" else args[int(s[0])]

    def statementTo3Sat(statement):
        if len(statement) < 2:
            return propToArg(statement[0])
        else:
            if statement[1] == "&":
                return propToArg(statement[0]) and statementTo3Sat(statement[2:])
            else:
                assert(statement[1] == "|")
                return propToArg(statement[0]) or statementTo3Sat(statement[2:])
    
    return statementTo3Sat(statements[0]) and evaluate3sat(args, statements[1:]) if len(statements) >= 1 else True

def solve3sat(allStatements):
    def getNumArgs(statements):
        def propToNum(p): return int(p[-1])

        if len(statements) < 1:
            return 0
        thisMax = max(propToNum(statements[0][0]), propToNum(statements[0][2]), propToNum(statements[0][4]))
        return max(thisMax, getNumArgs(statements[1:]))

    totalArgs = getNumArgs(allStatements) + 1

    def solve3SatHelper(args = []):
        if len(args) == totalArgs:
            return args if evaluate3sat(args, allStatements) else None
        else:
            res1 = solve3SatHelper(args + [True])
            return solve3SatHelper(args + [False]) if res1 == None else res1

    return solve3SatHelper()
