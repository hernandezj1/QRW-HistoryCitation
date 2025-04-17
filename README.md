# QRW-HistoryCitation
Quantum Random Walks applied in Qiskit and the [QuantumRandomWalks Python package](https://github.com/hernandezj1/QuantumRandomWalks) which can be installed here [Pypi](https://pypi.org/project/QuantumRandomWalks/) to a Historical Citation Network

Contents of repo: 
- __Images__- folder that contains the images where the citations occur in the three books that connect the work of node 9 to 7 and 8.

- __8-node-intro:__
  
    -__8-node-trial.ipynb:__ 8 - node application for proof of concept and introductory case with all actual code
  
    - __quantum_results_starting_on_node_4_8_nodes.csv__ - simulated results of 8-node trial
  
    - __quantum_results_starting_on_node_4_8_nodes_IBM.csv__ - quantum device results of 8-node trial
 

- __citation-network:__
- 
_Note:_ This utilizes the QuantumRandomWalk package and a lot of the code has bee abstracted to keep ease of use

    - __Application_of_QRW.ipynb:__ First simulated application of a CTQW to the actual Historical network starting on node 9
  
    - __complete-citation-network.csv:__ Input file extracted from our historical citatio network, originally hosted in Gephi

    - __start_at_node9_walk.csv:__- results from citation network starting the walk at node 9
      
    - __superposition_walk.csv:__- results from citation network starting at a superposition of all nodes
  
    - __node_mapping.csv:__- keeps track of the renamed nodes from the citation network so we can make inferences from the results
  




