# List
# An ordered set of values
# ['gene', 5.16]

# Sets
# A set on unordered collection with NO duplicate elements.
# Support operations like 'union', 'intersection', and 'difference'
brca = {'DNA repair', 'zinc ion binding', 'ubiquitin-protein transferase activity', 'protein ubiquitination'}
brca2 = {'Protein binding', 'H4 histone acetyltransferase activity', 'nucleoplasm', 'DNA repair', 'double-strand break repair via homologous recombination'}

print('Union')
print(brca | brca2)

print('Intersect')
print(brca & brca2)

print('Difference')
print(brca - brca2)
