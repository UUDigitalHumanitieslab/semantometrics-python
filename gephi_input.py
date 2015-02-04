from semantometrics import Similarity

import glob
import os
import csv

def main(): 
    """Retrieves the files and creates input files for Gephi"""
    files = glob.glob('cultmach/*.txt')

    # Create Similarity objects
    s = Similarity(files)
    ps = s.pairwise_similarity()

    with open('nodes.csv', 'wb') as node_file: 
        with open('edges.csv', 'wb') as edge_file: 
            node_writer = csv.writer(node_file)
            node_writer.writerow(['Nodes', 'Id', 'Label'])

            edge_writer = csv.writer(edge_file)
            edge_writer.writerow(['Source', 'Target', 'Type', 'Id', 'Weight'])

            id_count = 0
            for i, f in enumerate(files): 
                n = os.path.basename(f)
                node_writer.writerow([n, i, n])
                for j in range(i + 1, len(files)): 
                    id_count += 1
                    cossim = round(ps[i, j], 4)
                    edge_writer.writerow([i, j, 'Undirected', id_count, cossim])

if __name__ == "__main__":
    main()