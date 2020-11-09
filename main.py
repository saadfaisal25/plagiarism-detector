import time, os
# importing all the functions from the project files
from processtxt import processTXT
from lcs import getLCSSim
from senMatch import getSenSim
from rabinKarp import getRKSim
from senMatchBinary import getBinarySim
from cosineSim import getCosineSim
from jaccard import getJaccardSim

# prints the similarity percentage for the given algorithm, as well as the runtime of the algorithm
def printSimilarity(data1, data2, func, alg):
    start = time.time()
    sim = func(data1, data2)
    end = time.time()
    print("\n{} Algorithm: ".format(alg))
    print("Percentage of similarity: {}%".format(sim))
    print("Function runtime:", end-start , '\n')

# returns a list of similarity calculations comparing the given file data with each file in the file_repo directory
def getSimilarities(data1, func):
    dirpath = "file_repo"
    # creates a variable called filenames and assigns it a list of all files in the given directory ("file_repo")
    (_, _, filenames) = next(os.walk(dirpath))

    if filenames[0] == '.gitignore':
        del filenames[0]

    sims = []
    # gets the similarity of data1 to the data of each file in filenames
    for f in filenames:
        data2 = processTXT(dirpath+'/'+f)
        # appending a list of the percentage and the filename, with the percentage first. Percentage is the first element in the list since I'm going to be sorting by percentage,
        # and Python sorts 2d lists by the first element
        sims.append( [func(data1, data2), f] )

    return sims

# basically just a menu that utilizes all the functions depending on what the user wants to do
def main():
    print(
        """
1. Check for plagiarism between 2 given files 
2. Check for plagiarism between a given file and the file repository
        """
        )

    while True:
        check = input("Enter the number for your choice (-1 to quit): ")
        if check == '-1':
            break

        elif check == '1':
            file1 = input("Enter filename 1: ")
            file2 = input("Enter filename 2: ")
            data1 = processTXT(file1)
            data2 = processTXT(file2)
            print("Files Processed!")
            
            print("""
a. Sentence Matching
b. Sentence Matching using Binary Search
c. Longest Common Subsequence
d. Rabin Karp
e. Cosine Similarity
f. Jaccard Similarity
            """)

            # depending on what algorithm the user chooses, it calls printSimilarity() and keeps looping until the user exits
            while True:
                algo = input("Enter the letter for the algorithm to use (any other input to exit): ").lower()
                if algo == 'a':
                    printSimilarity(data1, data2, getSenSim, "Sentence Matching")
                elif algo == 'b':
                    printSimilarity(data1, data2, getBinarySim, "Sentence Matching using Binary Search")
                elif algo == 'c':
                    printSimilarity(data1, data2, getLCSSim, "Longest Common Subsequence")
                elif algo == 'd':
                    printSimilarity(data1, data2, getRKSim, "Rabin Karp")
                elif algo == 'e':
                    printSimilarity(data1, data2, getCosineSim, "Cosine Similarity")
                elif algo == 'f':
                    printSimilarity(data1, data2, getJaccardSim, "Jaccard Similarity")
                else:
                    break

        elif check == '2':
            filename = input("Enter filename: ")
            data = processTXT(filename)
            print("File Processed!")
            
            print("""
a. Sentence Matching
b. Sentence Matching using Binary Search
c. Longest Common Subsequence
d. Rabin Karp
e. Cosine Similarity
f. Jaccard Similarity
            """)

            # calls getSimilarities() depending on user's algorithm selection, and keeps looping until exited
            while True:
                algo = input("Enter the letter for the algorithm to use (any other input to exit): ").lower()
                sims = 0
                start = 0
                end = 0

                if algo == 'a':
                    start = time.time()
                    sims = getSimilarities(data, getSenSim)
                    end = time.time()
                elif algo == 'b':
                    start = time.time()
                    sims = getSimilarities(data, getBinarySim)
                    end = time.time()
                elif algo == 'c':
                    start = time.time()
                    sims = getSimilarities(data, getLCSSim)
                    end = time.time()
                elif algo == 'd':
                    start = time.time()
                    sims = getSimilarities(data, getRKSim)
                    end = time.time()
                elif algo == 'e':
                    start = time.time()
                    sims = getSimilarities(data, getCosineSim)
                    end = time.time()
                elif algo == 'f':
                    start = time.time()
                    sims = getSimilarities(data, getJaccardSim)
                    end = time.time()
                else:
                    break

                # loops through the reverse of the sorted similarity percentages and prints them
                print("\nFiles in order of decreasing similarity percentage:")
                for i in sorted(sims, reverse=True):
                    print(i[1]+': '+str(i[0])+'%', end=', ')
                print("\nFunction runtime:", end-start, '\n')

        else:
            print("Please enter a valid option.")

if __name__ == "__main__":
    main()