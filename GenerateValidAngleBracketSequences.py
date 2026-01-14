def generateAngleBracketSequences(n):
    result = []

    def backtrack(current, open_used, close_used):
        # If we've used all pairs, store the result
        if open_used == n and close_used == n:
            result.append(current)
            return

        # Add '<' if we still have opening brackets left
        if open_used < n:
            backtrack(current + '<', open_used + 1, close_used)

        # Add '>' if it won't break validity
        if close_used < open_used:
            backtrack(current + '>', open_used, close_used + 1)

    backtrack("", 0, 0)
    return result

