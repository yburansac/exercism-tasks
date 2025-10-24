def to_rna(dna_strand):

    complements = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U'}

    rna = [ complements[tide] for tide in dna_strand]
    return "".join(rna)

    
