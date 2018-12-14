# Program to find the PageRank of the docID present in the text file passed with the in-link relationship

# Importing required libraries
import math  # Provides access to the mathematical functions
import operator  # Provides function corresponding to the intrinsic operators


class PageRank:
    in_link_rel = {}  # Dictionary representing the in-link relationship
    out_link_rel = {}  # Dictionary representing the out-link relationship
    rank_link_rel = {}  # Dictionary representing the rank associated with all the docID
    new_rank_link_rel = {}
    __url_graph_file_name = ""
    damping_factor = 0.85  # Is the PageRank damping factor, 0.85 is a typical value for consideration
    sink_nodes = []  # List of all the docID which are sink nodes(no output-link or having only one to itself)
    init_perplexity = 0  # Storing the value of the perplexity

    # Constructor of the class taking the name of the file, with graph, as input
    def __init__(self, url_graph_file_name):
        self.__url_graph_file_name = url_graph_file_name

    # Will initialize the page rank dictionary and call all the other functions required for the initialization
    def init_page_rank(self):

        self.init_in_link_rel()  # for in_link_rel
        self.init_out_link_rel()  # for out_link_rel
        self.get_sink_nodes()  # for sink_nodes

        # Initial value of the PageRank for all the pages (1/N)
        # N is the total number of pages to be ranked
        for key in self.in_link_rel:
            self.rank_link_rel[key] = 1 / (len(self.in_link_rel))

    # Assigning values to the in-link relation dictionary from the input graph
    def init_in_link_rel(self):

        with open(self.__url_graph_file_name, 'r+') as f:
            for url in f:
                url = url.split()
                if not url:
                    continue
                self.in_link_rel[url[0]] = url[1:]

    # Assigning values to the out-link relation dictionary from the in-link relation
    def init_out_link_rel(self):

        self.out_link_rel = self.in_link_rel.copy()  # Copy of the in-link relation for initialization

        # To empty all the list values for all keys
        for key in self.out_link_rel:
            self.out_link_rel[key] = []

        # Assigning the values of the dictionary as the out-link to the docID as keys
        for key in self.in_link_rel:
            for values in self.in_link_rel[key]:
                self.out_link_rel[values].append(key)

    # Appending all the docId which are sink in sink_nodes
    def get_sink_nodes(self):

        for key in self.out_link_rel:
            if self.out_link_rel[key] == []:
                self.sink_nodes.append(key)

    # Returns the value of the perplexity at the point called
    def perplexity(self):

        entropy_value = 0

        # Applying the formula to find the entropy
        for key in self.rank_link_rel:
            entropy_value = ((self.rank_link_rel[key]) * (math.log(self.rank_link_rel[key], 2))) + entropy_value

        entropy_value = - entropy_value  # Negation of the entropy value
        perplexity_value = 2 ** entropy_value  # Finding the value of perplexity "2^EntropyValue"

        return perplexity_value

    # The main function to implement the PageRank algorithm
    # Assigns and return PageRank value for all the docId
    def find_page_rank(self):

        i = 0  # Counter initialization for finding convergence

        self.init_page_rank()  # Initializing the values of all the docId

        # The loop will run till the counter is less than 4
        # The counter value will increase only when the change in the perplexity is less than 1
        # The conter value will keep on increasing only if the change is less than 1 for 4 consecutive iterations
        while i < 4:
            # Increasing the counter value only if the change in perplexity is less than 1
            if (self.perplexity() - self.init_perplexity) < 1:
                i = i + 1
            else:
                i = 0  # The value of the counter will be set to 0 if change is not less than 1, in iterations as well

            self.init_perplexity = self.perplexity()

            sink_pr = 0

            # Calculating the PageRank value of total sink nodes
            for page in self.sink_nodes:
                sink_pr = self.rank_link_rel[page] + sink_pr

            # Calculating the PageRank values of all the pages
            for page in self.rank_link_rel:
                # For damping or teleportation
                self.new_rank_link_rel[page] = (1 - self.damping_factor) / (len(self.rank_link_rel))
                # To spread the sink PageRank evenly to all pages PageRank
                self.new_rank_link_rel[page] = (((self.damping_factor * sink_pr) / (len(self.rank_link_rel)))
                                                + (self.new_rank_link_rel[page]))

                # For all the in-link pages for the page
                for in_page in self.in_link_rel[page]:
                    self.new_rank_link_rel[page] = (((self.damping_factor * self.rank_link_rel[in_page])
                                                     / (len(self.out_link_rel[in_page])))
                                                    + (self.new_rank_link_rel[page]))

            # Assigning the new Page Rank to all the pages
            for page in self.rank_link_rel:
                self.rank_link_rel[page] = self.new_rank_link_rel[page]

        # Sorting all the docID according to its PageRank value
        asc_sorted_page_rank = sorted(self.rank_link_rel.items(), key=operator.itemgetter(1))
        asc_sorted_page_rank.reverse()

        # For converting the list into string for proper representation
        for page in asc_sorted_page_rank:
            sorted_page_rank = (str(asc_sorted_page_rank)).replace("[(","(")
            sorted_page_rank = sorted_page_rank.replace(")]",")")

        print(sorted_page_rank)

        return asc_sorted_page_rank


# To create an object of the class PageRank and passing the name of the file with in-link relation graph
# The name of the file submitted is "bfs_web_graph.txt" and "dfs_web_graph.txt"
DFSPageRank = PageRank("bfs_web_graph.txt")

# Calling the main function to give the PageRank of all the docId passed as a in-link relation graph
DFSPageRank.find_page_rank()