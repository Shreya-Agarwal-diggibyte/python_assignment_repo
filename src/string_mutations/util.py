def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    string=string[:position]+character+string[position+1:]
    return string
