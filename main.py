def main():
    genome = input("Enter a genome string: ")
    gene = [genome[i:i+3] for i in range(0, len(genome), 3)]
    if gene != "TGA" or "TAA" or "TAG" or "ATG":
        print(gene)
main()

